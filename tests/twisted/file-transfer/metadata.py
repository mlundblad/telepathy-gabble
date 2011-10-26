# The 'normal' cases are tested with test-receive-file.py and test-send-file-provide-immediately.py
# This file tests some corner cases
import dbus

from file_transfer_helper import exec_file_transfer_test, ReceiveFileTest, SendFileTest
from servicetest import assertEquals, call_async

import constants as cs

class SendFileNoMetadata(SendFileTest):
    # this is basically the equivalent of calling CreateChannel
    # without these two properties
    service_name = ''
    metadata = {}

class ReceiveFileNoMetadata(SendFileTest):
    service_name = ''
    metadata = {}

class SendFileBadProps(SendFileTest):
    metadata = {'FORM_TYPE': 'this shouldnt be allowed'}

    def request_ft_channel(self):
        requests_iface = dbus.Interface(self.conn, cs.CONN_IFACE_REQUESTS)

        request = { cs.CHANNEL_TYPE: cs.CHANNEL_TYPE_FILE_TRANSFER,
            cs.TARGET_HANDLE_TYPE: cs.HT_CONTACT,
            cs.TARGET_HANDLE: self.handle,
            cs.FT_CONTENT_TYPE: self.file.content_type,
            cs.FT_FILENAME: self.file.name,
            cs.FT_SIZE: self.file.size,
            cs.FT_CONTENT_HASH_TYPE: self.file.hash_type,
            cs.FT_CONTENT_HASH: self.file.hash,
            cs.FT_DESCRIPTION: self.file.description,
            cs.FT_DATE:  self.file.date,
            cs.FT_INITIAL_OFFSET: 0,
            cs.FT_SERVICE_NAME: self.service_name,
            cs.FT_METADATA: dbus.Dictionary(self.metadata, signature='ss')}

        call_async(self.q, requests_iface, 'CreateChannel', request)

        # FORM_TYPE is not allowed, soz
        self.q.expect('dbus-error', method='CreateChannel', name=cs.INVALID_ARGUMENT)

        return True

if __name__ == '__main__':
    exec_file_transfer_test(SendFileNoMetadata, True)
    exec_file_transfer_test(ReceiveFileNoMetadata, True)
    exec_file_transfer_test(SendFileBadProps, True)
