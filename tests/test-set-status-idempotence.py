
"""
Test that redundant calls to SetPresence don't cause anything to happen.
"""

from twisted.internet import glib2reactor
glib2reactor.install()

import dbus

from gabbletest import go, conn_iface

def expect_connected(event, data):
    if event[0] != 'dbus-signal':
        return False

    if event[2] != 'StatusChanged':
        return False

    if event[3] != [0, 1]:
        return False

    presence = dbus.Interface(data['conn'],
        'org.freedesktop.Telepathy.Connection.Interface.Presence')

    # Set presence to away. This should cause PresenceUpdate to be emitted,
    # and a new <presence> stanza to be sent to the server.
    presence.SetStatus({'away':{'message': 'gone'}})
    return True

def expect_presence_update1(event, data):
    if event[0] != 'dbus-signal':
        return False

    if event[2] != 'PresenceUpdate':
        return False

    if event[3] != [{1L: (0L, {u'away': {u'message': u'gone'}})}]:
        return False

    return True

def expect_presence_stanza1(event, data):
    if event[0] != 'stream-presence':
        return False

    presence = dbus.Interface(data['conn'],
        'org.freedesktop.Telepathy.Connection.Interface.Presence')

    children = list(event[1].elements())
    assert children[0].name == 'show'
    assert str(children[0]) == 'away'
    assert children[1].name == 'status'
    assert str(children[1]) == 'gone'

    # Set presence a second time. Since this call is redundant, there should
    # be no PresenceUpdate or <presence> sent to the server.
    presence.SetStatus({'away':{'message': 'gone'}})

    # Set presence a third time. This call is not redundant, and should
    # generate a signal/message.
    presence.SetStatus({'available':{'message': 'yo'}})

    return True

def expect_presence_update2(event, data):
    if event[0] != 'dbus-signal':
        return False

    if event[2] != 'PresenceUpdate':
        return False

    if event[3] != [{1L: (0L, {u'available': {u'message': u'yo'}})}]:
        return False

    return True

def expect_presence_stanza2(event, data):
    if event[0] != 'stream-presence':
        return False

    children = list(event[1].elements())
    assert children[0].name == 'status'
    assert str(children[0]) == 'yo'

    conn_iface(data['conn']).Disconnect()
    return True

def expect_disconnected(event, data):
    if event[0] != 'dbus-signal':
        return False

    if event[2] != 'StatusChanged':
        return False

    if event[3] != [2, 1]:
        return False

    return True

if __name__ == '__main__':
    go()

