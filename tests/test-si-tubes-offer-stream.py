"""Test 1-1 tubes support."""

import base64
import errno
import os

import dbus
from dbus.connection import Connection
from dbus.lowlevel import SignalMessage

# must come before the twisted imports due to side-effects
from gabbletest import go, make_result_iq
from servicetest import call_async, lazy, match, tp_name_prefix

from twisted.internet.protocol import Factory, Protocol
from twisted.words.protocols.jabber.client import IQ
from twisted.words.xish import domish, xpath
from twisted.internet import reactor

NS_TUBES = 'http://telepathy.freedesktop.org/xmpp/tubes'
NS_SI = 'http://jabber.org/protocol/si'
NS_FEATURE_NEG = 'http://jabber.org/protocol/feature-neg'
NS_SI_TUBES = 'http://telepathy.freedesktop.org/xmpp/si/profile/tubes'
NS_SI_TUBES_OLD = 'http://jabber.org/protocol/si/profile/tubes'
NS_IBB = 'http://jabber.org/protocol/ibb'
NS_X_DATA = 'jabber:x:data'


class Echo(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

def set_up_echo():
    factory = Factory()
    factory.protocol = Echo
    try:
        os.remove(os.getcwd() + '/stream')
    except OSError, e:
        if e.errno != errno.ENOENT:
            raise
    reactor.listenUNIX(os.getcwd() + '/stream', factory)


@match('dbus-signal', signal='StatusChanged', args=[0, 1])
def expect_connected(event, data):

    set_up_echo()

    return True

@match('stream-iq', query_ns='jabber:iq:roster')
def expect_roster_iq(event, data):
    event.stanza['type'] = 'result'

    item = event.query.addElement('item')
    item['jid'] = 'bob@localhost'
    item['subscription'] = 'both'

    data['stream'].send(event.stanza)

    presence = domish.Element(('jabber:client', 'presence'))
    presence['from'] = 'alice@localhost/Alice'
    presence['to'] = 'test@localhost/Resource'
    c = presence.addElement('c')
    c['xmlns'] = 'http://jabber.org/protocol/caps'
    c['node'] = 'http://example.com/ICantBelieveItsNotTelepathy'
    c['ver'] = '1.2.3'
    data['stream'].send(presence)

    presence = domish.Element(('jabber:client', 'presence'))
    presence['from'] = 'bob@localhost/Bob'
    presence['to'] = 'test@localhost/Resource'
    c = presence.addElement('c')
    c['xmlns'] = 'http://jabber.org/protocol/caps'
    c['node'] = 'http://example.com/ICantBelieveItsNotTelepathy'
    c['ver'] = '1.2.3'
    data['stream'].send(presence)

    return True

@match('stream-iq', iq_type='get',
    query_ns='http://jabber.org/protocol/disco#info',
    to='bob@localhost/Bob')
def expect_caps_disco(event, data):
    event.stanza['type'] = 'result'
    assert event.query['node'] == \
        'http://example.com/ICantBelieveItsNotTelepathy#1.2.3'
    feature = event.query.addElement('feature')
    feature['var'] = NS_SI_TUBES
    feature = event.query.addElement('feature')
    feature['var'] = NS_SI_TUBES_OLD

    data['stream'].send(event.stanza)

    call_async(data['test'], data['conn_iface'], 'RequestHandles', 1,
        ['bob@localhost'])
    return True

@match('dbus-return', method='RequestHandles')
def expect_request_handles_return(event, data):
    data['bob_handle'] = event.value[0][0]

    call_async(data['test'], data['conn_iface'], 'RequestChannel',
        tp_name_prefix + '.Channel.Type.Tubes', 1, data['bob_handle'], True)

    return True

sample_parameters = dbus.Dictionary({
    's': 'hello',
    'ay': dbus.ByteArray('hello'),
    'u': dbus.UInt32(123),
    'i': dbus.Int32(-123),
    }, signature='sv')

@match('dbus-return', method='RequestChannel')
def expect_request_channel_return(event, data):
    bus = data['conn']._bus
    data['tubes_chan'] = bus.get_object(
        data['conn'].bus_name, event.value[0])
    data['tubes_iface'] = dbus.Interface(data['tubes_chan'],
        tp_name_prefix + '.Channel.Type.Tubes')

    data['self_handle'] = data['conn_iface'].GetSelfHandle()

    call_async(data['test'], data['tubes_iface'], 'OfferStreamUnixTube',
        'echo', os.getcwd() + '/stream', sample_parameters)

    return True

@match('stream-iq', iq_type='set', to='bob@localhost/Bob')
def expect_stream_initiation(event, data):

    iq = event.stanza
    si_nodes = xpath.queryForNodes('/iq/si', iq)
    if si_nodes is None:
        return False

    assert len(si_nodes) == 1
    si = si_nodes[0]
    assert si['profile'] == NS_SI_TUBES_OLD # FIXME: shouldn't be _OLD
    data['stream_id'] = si['id']

    feature = xpath.queryForNodes('/si/feature', si)[0]
    x = xpath.queryForNodes('/feature/x', feature)[0]
    assert x['type'] == 'form'
    field = xpath.queryForNodes('/x/field', x)[0]
    assert field['var'] == 'stream-method'
    assert field['type'] == 'list-single'
    value = xpath.queryForNodes('/field/option/value', field)[0]
    assert str(value) == NS_IBB

    tube = xpath.queryForNodes('/si/tube', si)[0]
    assert tube['initiator'] == 'test@localhost'
    assert tube['service'] == 'echo'
    # FIXME: tube['id'] has rubbish in it
    assert tube['offering'] == 'true'
    assert tube['type'] == 'stream'
    data['tube_id'] = long(tube['id'])

    params = {}
    parameter_nodes = xpath.queryForNodes('/tube/parameters/parameter', tube)
    for node in parameter_nodes:
        assert node['name'] not in params
        params[node['name']] = (node['type'], str(node))
    assert params == {'ay': ('bytes', 'aGVsbG8='),
                      's': ('str', 'hello'),
                      'i': ('int', '-123'),
                      'u': ('uint', '123'),
                     }

    result = IQ(data['stream'], 'result')
    result['id'] = iq['id']
    result['from'] = iq['to']
    result['to'] = 'test@localhost/Resource'
    res_si = result.addElement((NS_SI, 'si'))
    res_feature = res_si.addElement((NS_FEATURE_NEG, 'feature'))
    res_x = res_feature.addElement((NS_X_DATA, 'x'))
    res_x['type'] = 'submit'
    res_field = res_x.addElement((None, 'field'))
    res_field['var'] = 'stream-method'
    res_value = res_field.addElement((None, 'value'))
    res_value.addContent(NS_IBB)

    data['stream'].send(result)

    return True

@match('stream-iq', iq_type='set', to='bob@localhost/Bob')
def expect_ibb_open(event, data):
    iq = event.stanza
    open = xpath.queryForNodes('/iq/open', iq)[0]
    assert open.uri == NS_IBB
    assert open['sid'] == data['stream_id']

    result = IQ(data['stream'], 'result')
    result['id'] = iq['id']
    result['from'] = iq['to']
    result['to'] = 'test@localhost/Resource'

    data['stream'].send(result)

    return True

@match('dbus-signal', signal='TubeStateChanged')
def expect_tube_open(event, data):
    assert event.args[0] == data['tube_id']
    assert event.args[1] == 2       # OPEN

    call_async(data['test'], data['tubes_iface'], 'ListTubes',
        byte_arrays=True)

    return True

@match('dbus-return', method='ListTubes')
def expect_list_tubes_return(event, data):
    assert event.value[0] == [(
        data['tube_id'],
        data['self_handle'],
        1,      # Unix stream
        'echo',
        sample_parameters,
        2,      # OPEN
        )]

    # FIXME: if we use an unknown JID here, everything fails
    # (the code uses lookup where it should use ensure)

    # The CM is the server, so fake a client wanting to talk to it
    iq = IQ(data['stream'], 'set')
    iq['to'] = 'test@localhost/Resource'
    iq['from'] = 'bob@localhost/Bob'
    si = iq.addElement((NS_SI, 'si'))
    si['id'] = 'alpha'
    si['profile'] = NS_SI_TUBES_OLD
    feature = si.addElement((NS_FEATURE_NEG, 'feature'))
    x = feature.addElement((NS_X_DATA, 'x'))
    x['type'] = 'form'
    field = x.addElement((None, 'field'))
    field['var'] = 'stream-method'
    field['type'] = 'list-single'
    option = field.addElement((None, 'option'))
    value = option.addElement((None, 'value'))
    value.addContent(NS_IBB)

    tube = si.addElement((NS_SI_TUBES_OLD, 'tube'))
    tube['id'] = str(data['tube_id'])
    tube['offering'] = 'false'

    data['stream'].send(iq)

    return True

@match('stream-iq', iq_type='result')
def expect_stream_initiation_ok(event, data):
    return True

@match('dbus-signal', signal='StreamUnixSocketNewConnection')
def expect_new_connection(event, data):
    assert event.args[0] == data['tube_id']
    assert event.args[1] == data['bob_handle']

    # have the fake client open the stream
    iq = IQ(data['stream'], 'set')
    iq['to'] = 'test@localhost/Resource'
    iq['from'] = 'bob@localhost/Bob'
    open = iq.addElement((NS_IBB, 'open'))
    open['sid'] = 'alpha'
    open['block-size'] = '4096'
    data['stream'].send(iq)
    return True

@match('stream-iq', iq_type='result')
def expect_ibb_open_ok(event, data):

    # have the fake client send us some data
    message = domish.Element(('jabber:client', 'message'))
    message['to'] = 'test@localhost/Resource'
    message['from'] = 'bob@localhost/Bob'
    data_node = message.addElement((NS_IBB, 'data'))
    data_node['sid'] = 'alpha'
    data_node['seq'] = '0'
    data_node.addContent(base64.b64encode('hello, world'))
    data['stream'].send(message)
    return True

@match('stream-message')
def expect_echo(event, data):
    message = event.stanza

    assert message['to'] == 'bob@localhost/Bob'
    data_nodes = xpath.queryForNodes('/message/data[@xmlns="%s"]' % NS_IBB,
        message)
    assert data_nodes is not None
    assert len(data_nodes) == 1
    ibb_data = data_nodes[0]
    assert ibb_data['sid'] == 'alpha'
    binary = base64.b64decode(str(ibb_data))
    assert binary == 'hello, world'

    # OK, we're done
    data['conn_iface'].Disconnect()
    return True

@match('dbus-signal', signal='StatusChanged', args=[2, 1])
def expect_disconnected(event, data):
    return True

if __name__ == '__main__':
    go()
