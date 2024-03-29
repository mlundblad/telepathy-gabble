"""
Some handy constants for other tests to share and enjoy.
"""

from dbus import PROPERTIES_IFACE

CM = "org.freedesktop.Telepathy.ConnectionManager"

HT_NONE = 0
HT_CONTACT = 1
HT_ROOM = 2
HT_LIST = 3
HT_GROUP = 4

CHANNEL = "org.freedesktop.Telepathy.Channel"

CHANNEL_IFACE_CALL_STATE = CHANNEL + ".Interface.CallState"
CHANNEL_IFACE_CHAT_STATE = CHANNEL + '.Interface.ChatState'
CHANNEL_IFACE_DESTROYABLE = CHANNEL + ".Interface.Destroyable"
CHANNEL_IFACE_DTMF = CHANNEL + ".Interface.DTMF"
CHANNEL_IFACE_GROUP = CHANNEL + ".Interface.Group"
CHANNEL_IFACE_HOLD = CHANNEL + ".Interface.Hold"
CHANNEL_IFACE_MEDIA_SIGNALLING = CHANNEL + ".Interface.MediaSignalling"
CHANNEL_IFACE_MESSAGES = CHANNEL + ".Interface.Messages"
CHANNEL_IFACE_PASSWORD = CHANNEL + ".Interface.Password"
CHANNEL_IFACE_TUBE = CHANNEL + ".Interface.Tube"
CHANNEL_IFACE_SASL_AUTH = CHANNEL + ".Interface.SASLAuthentication"
CHANNEL_IFACE_CONFERENCE = CHANNEL + '.Interface.Conference'
CHANNEL_IFACE_ROOM = CHANNEL + '.Interface.Room2'
CHANNEL_IFACE_ROOM_CONFIG = CHANNEL + '.Interface.RoomConfig1'
CHANNEL_IFACE_SUBJECT = CHANNEL + '.Interface.Subject2'
CHANNEL_IFACE_FILE_TRANSFER_METADATA = CHANNEL + '.Interface.FileTransfer.Metadata'

CHANNEL_TYPE_CALL = CHANNEL + ".Type.Call1"
CHANNEL_TYPE_CONTACT_LIST = CHANNEL + ".Type.ContactList"
CHANNEL_TYPE_CONTACT_SEARCH = CHANNEL + ".Type.ContactSearch"
CHANNEL_TYPE_TEXT = CHANNEL + ".Type.Text"
CHANNEL_TYPE_TUBES = CHANNEL + ".Type.Tubes"
CHANNEL_TYPE_STREAM_TUBE = CHANNEL + ".Type.StreamTube"
CHANNEL_TYPE_DBUS_TUBE = CHANNEL + ".Type.DBusTube"
CHANNEL_TYPE_STREAMED_MEDIA = CHANNEL + ".Type.StreamedMedia"
CHANNEL_TYPE_TEXT = CHANNEL + ".Type.Text"
CHANNEL_TYPE_FILE_TRANSFER = CHANNEL + ".Type.FileTransfer"
CHANNEL_TYPE_SERVER_AUTHENTICATION = \
    CHANNEL + ".Type.ServerAuthentication"
CHANNEL_TYPE_SERVER_TLS_CONNECTION = \
    CHANNEL + ".Type.ServerTLSConnection"

TP_AWKWARD_PROPERTIES = "org.freedesktop.Telepathy.Properties"
PROPERTY_FLAG_READ = 1
PROPERTY_FLAG_WRITE = 2
PROPERTY_FLAGS_RW = PROPERTY_FLAG_READ | PROPERTY_FLAG_WRITE

CHANNEL_TYPE = CHANNEL + '.ChannelType'
TARGET_HANDLE_TYPE = CHANNEL + '.TargetHandleType'
TARGET_HANDLE = CHANNEL + '.TargetHandle'
TARGET_ID = CHANNEL + '.TargetID'
REQUESTED = CHANNEL + '.Requested'
INITIATOR_HANDLE = CHANNEL + '.InitiatorHandle'
INITIATOR_ID = CHANNEL + '.InitiatorID'
INTERFACES = CHANNEL + '.Interfaces'

INITIAL_AUDIO = CHANNEL_TYPE_STREAMED_MEDIA + '.InitialAudio'
INITIAL_VIDEO = CHANNEL_TYPE_STREAMED_MEDIA + '.InitialVideo'
IMMUTABLE_STREAMS = CHANNEL_TYPE_STREAMED_MEDIA + '.ImmutableStreams'

CALL_INITIAL_AUDIO = CHANNEL_TYPE_CALL + '.InitialAudio'
CALL_INITIAL_AUDIO_NAME = CHANNEL_TYPE_CALL + '.InitialAudioName'
CALL_INITIAL_VIDEO = CHANNEL_TYPE_CALL + '.InitialVideo'
CALL_INITIAL_VIDEO_NAME = CHANNEL_TYPE_CALL + '.InitialVideoName'
CALL_MUTABLE_CONTENTS = CHANNEL_TYPE_CALL + '.MutableContents'

CALL_CONTENT = 'org.freedesktop.Telepathy.Call1.Content'
CALL_CONTENT_IFACE_MEDIA = \
    'org.freedesktop.Telepathy.Call1.Content.Interface.Media'
CALL_CONTENT_IFACE_DTMF = \
    'org.freedesktop.Telepathy.Call1.Content.Interface.DTMF'

CALL_CONTENT_MEDIADESCRIPTION = \
    'org.freedesktop.Telepathy.Call1.Content.MediaDescription'

CALL_STREAM = 'org.freedesktop.Telepathy.Call1.Stream'
CALL_STREAM_IFACE_MEDIA = \
    'org.freedesktop.Telepathy.Call1.Stream.Interface.Media'

CALL_STREAM_ENDPOINT = 'org.freedesktop.Telepathy.Call1.Stream.Endpoint'

CALL_MEDIA_TYPE_AUDIO = 0
CALL_MEDIA_TYPE_VIDEO = 1

CALL_CONTENT_PACKETIZATION_RTP = 0
CALL_CONTENT_PACKETIZATION_RAW = 1
CALL_CONTENT_PACKETIZATION_MSN_WEBCAM = 2

CALL_STREAM_TRANSPORT_UNKNOWN = 0
CALL_STREAM_TRANSPORT_RAW_UDP = 1
CALL_STREAM_TRANSPORT_ICE = 2
CALL_STREAM_TRANSPORT_GTALK_P2P = 3
CALL_STREAM_TRANSPORT_WLM_2009 = 4
CALL_STREAM_TRANSPORT_SHM = 5
CALL_STREAM_TRANSPORT_MULTICAST = 6

#for streamed media
CALL_STATE_RINGING = 1
CALL_STATE_HELD = 4

CALL_STATE_UNKNOWN = 0,
CALL_STATE_PENDING_INITIATOR = 1
CALL_STATE_INITIALISING = 2
CALL_STATE_INITIALISED = 3
CALL_STATE_ACCEPTED = 4
CALL_STATE_ACTIVE = 5
CALL_STATE_ENDED = 6

CALL_FLAG_LOCALLY_HELD = 1
CALL_FLAG_LOCALLY_RINGING = 2
CALL_FLAG_LOCALLY_QUEUED = 4
CALL_FLAG_FORWARDED = 8
CALL_FLAG_CLEARING = 16

CALL_MEMBER_FLAG_RINGING = 1
CALL_MEMBER_FLAG_HELD = 2

CALL_DISPOSITION_NONE = 0
CALL_DISPOSITION_INITIAL = 1

CALL_SENDING_STATE_NONE = 0
CALL_SENDING_STATE_PENDING_SEND = 1
CALL_SENDING_STATE_SENDING = 2
CALL_SENDING_STATE_PENDING_STOP_SENDING = 3

CALL_STREAM_FLOW_STATE_STOPPED = 0
CALL_STREAM_FLOW_STATE_PENDING_START = 1
CALL_STREAM_FLOW_STATE_PENDING_STOP = 2
CALL_STREAM_FLOW_STATE_STARTED = 3

CALL_STREAM_ENDPOINT_STATE_CONNECTING = 0
CALL_STREAM_ENDPOINT_STATE_PROVISIONALLY_CONNECTED = 1
CALL_STREAM_ENDPOINT_STATE_FULLY_CONNECTED = 2
CALL_STREAM_ENDPOINT_STATE_EXHAUSTED_CANDIDATES = 3
CALL_STREAM_ENDPOINT_STATE_FAILED = 4

CALL_STREAM_CANDIDATE_TYPE_HOST = 1
CALL_STREAM_CANDIDATE_TYPE_SERVER_REFLEXIVE = 2
CALL_STREAM_CANDIDATE_TYPE_RELAY = 4

CALL_STATE_CHANGE_REASON_UNKNOWN = 0
CALL_STATE_CHANGE_REASON_PROGRESS_MADE = 1
CALL_STATE_CHANGE_REASON_USER_REQUESTED = 2
CALL_STATE_CHANGE_REASON_FORWARDED = 3
CALL_STATE_CHANGE_REASON_REJECTED = 4
CALL_STATE_CHANGE_REASON_NO_ANSWER = 5
CALL_STATE_CHANGE_REASON_INVALID_CONTACT = 6
CALL_STATE_CHANGE_REASON_PERMISSION_DENIED = 7
CALL_STATE_CHANGE_REASON_BUSY = 8
CALL_STATE_CHANGE_REASON_INTERNAL_ERROR = 9
CALL_STATE_CHANGE_REASON_SERVICE_ERROR = 10
CALL_STATE_CHANGE_REASON_NETWORK_ERROR = 11
CALL_STATE_CHANGE_REASON_MEDIA_ERROR = 12
CALL_STATE_CHANGE_REASON_CONNECTIVITY_ERROR = 13

CALL_STREAM_COMPONENT_UNKNOWN = 0
CALL_STREAM_COMPONENT_DATA = 1
CALL_STREAM_COMPONENT_CONTROL = 2

SUBSCRIPTION_STATE_UNKNOWN = 0
SUBSCRIPTION_STATE_NO = 1
SUBSCRIPTION_STATE_REMOVED_REMOTELY = 2
SUBSCRIPTION_STATE_ASK = 3
SUBSCRIPTION_STATE_YES = 4

CONTACT_LIST_STATE_NONE = 0
CONTACT_LIST_STATE_WAITING = 1
CONTACT_LIST_STATE_FAILURE = 2
CONTACT_LIST_STATE_SUCCESS = 3

CONN = "org.freedesktop.Telepathy.Connection"
CONN_IFACE_AVATARS = CONN + '.Interface.Avatars'
CONN_IFACE_ALIASING = CONN + '.Interface.Aliasing'
CONN_IFACE_CAPS = CONN + '.Interface.Capabilities'
CONN_IFACE_CONTACTS = CONN + '.Interface.Contacts'
CONN_IFACE_CONTACT_CAPS = CONN + '.Interface.ContactCapabilities'
CONN_IFACE_CONTACT_INFO = CONN + ".Interface.ContactInfo"
CONN_IFACE_PRESENCE = CONN + '.Interface.Presence'
CONN_IFACE_SIMPLE_PRESENCE = CONN + '.Interface.SimplePresence'
CONN_IFACE_REQUESTS = CONN + '.Interface.Requests'
CONN_IFACE_LOCATION = CONN + '.Interface.Location'
CONN_IFACE_GABBLE_DECLOAK = CONN + '.Interface.Gabble.Decloak'
CONN_IFACE_MAIL_NOTIFICATION = CONN + '.Interface.MailNotification'
CONN_IFACE_CONTACT_LIST = CONN + '.Interface.ContactList'
CONN_IFACE_CONTACT_GROUPS = CONN + '.Interface.ContactGroups'
CONN_IFACE_CLIENT_TYPES = CONN + '.Interface.ClientTypes'
CONN_IFACE_POWER_SAVING = CONN + '.Interface.PowerSaving'
CONN_IFACE_CONTACT_BLOCKING = CONN + '.Interface.ContactBlocking'
CONN_IFACE_ADDRESSING = CONN + '.Interface.Addressing1'

ATTR_CONTACT_CAPABILITIES = CONN_IFACE_CONTACT_CAPS + '/capabilities'

STREAM_HANDLER = 'org.freedesktop.Telepathy.Media.StreamHandler'

ERROR = 'org.freedesktop.Telepathy.Error'
INVALID_ARGUMENT = ERROR + '.InvalidArgument'
NOT_IMPLEMENTED = ERROR + '.NotImplemented'
NOT_AVAILABLE = ERROR + '.NotAvailable'
PERMISSION_DENIED = ERROR + '.PermissionDenied'
OFFLINE = ERROR + '.Offline'
NOT_CAPABLE = ERROR + '.NotCapable'
CONNECTION_REFUSED = ERROR + '.ConnectionRefused'
CONNECTION_FAILED = ERROR + '.ConnectionFailed'
CONNECTION_LOST = ERROR + '.ConnectionLost'
CANCELLED = ERROR + '.Cancelled'
DISCONNECTED = ERROR + '.Disconnected'
REGISTRATION_EXISTS = ERROR + '.RegistrationExists'
AUTHENTICATION_FAILED = ERROR + '.AuthenticationFailed'
CONNECTION_REPLACED = ERROR + '.ConnectionReplaced'
ALREADY_CONNECTED = ERROR + '.AlreadyConnected'
NETWORK_ERROR = ERROR + '.NetworkError'
NOT_YET = ERROR + '.NotYet'
INVALID_HANDLE = ERROR + '.InvalidHandle'
CERT_UNTRUSTED = ERROR + '.Cert.Untrusted'
SERVICE_BUSY = ERROR + '.ServiceBusy'
SERVICE_CONFUSED = ERROR + '.ServiceConfused'

BANNED = ERROR + '.Channel.Banned'

UNKNOWN_METHOD = 'org.freedesktop.DBus.Error.UnknownMethod'

TUBE_PARAMETERS = CHANNEL_IFACE_TUBE + '.Parameters'
TUBE_STATE = CHANNEL_IFACE_TUBE + '.State'
STREAM_TUBE_SERVICE = CHANNEL_TYPE_STREAM_TUBE + '.Service'
DBUS_TUBE_SERVICE_NAME = CHANNEL_TYPE_DBUS_TUBE + '.ServiceName'
DBUS_TUBE_DBUS_NAMES = CHANNEL_TYPE_DBUS_TUBE + '.DBusNames'
DBUS_TUBE_SUPPORTED_ACCESS_CONTROLS = CHANNEL_TYPE_DBUS_TUBE + '.SupportedAccessControls'
STREAM_TUBE_SUPPORTED_SOCKET_TYPES = CHANNEL_TYPE_STREAM_TUBE + '.SupportedSocketTypes'

CONFERENCE_INITIAL_CHANNELS = CHANNEL_IFACE_CONFERENCE + '.InitialChannels'
CONFERENCE_INITIAL_INVITEE_HANDLES = CHANNEL_IFACE_CONFERENCE + '.InitialInviteeHandles'
CONFERENCE_INITIAL_INVITEE_IDS = CHANNEL_IFACE_CONFERENCE + '.InitialInviteeIDs'

CONTACT_SEARCH_ASK = CHANNEL_TYPE_CONTACT_SEARCH + '.AvailableSearchKeys'
CONTACT_SEARCH_SERVER = CHANNEL_TYPE_CONTACT_SEARCH + '.Server'
CONTACT_SEARCH_STATE = CHANNEL_TYPE_CONTACT_SEARCH + '.SearchState'

SEARCH_NOT_STARTED = 0
SEARCH_IN_PROGRESS = 1
SEARCH_MORE_AVAILABLE = 2
SEARCH_COMPLETED = 3
SEARCH_FAILED = 4

TUBE_CHANNEL_STATE_LOCAL_PENDING = 0
TUBE_CHANNEL_STATE_REMOTE_PENDING = 1
TUBE_CHANNEL_STATE_OPEN = 2
TUBE_CHANNEL_STATE_NOT_OFFERED = 3

MEDIA_STREAM_TYPE_AUDIO = 0
MEDIA_STREAM_TYPE_VIDEO = 1

MEDIA_STREAM_BASE_PROTO_UDP = 0
MEDIA_STREAM_BASE_PROTO_TCP = 1

MEDIA_STREAM_TRANSPORT_TYPE_LOCAL = 0
MEDIA_STREAM_TRANSPORT_TYPE_DERIVED = 1
MEDIA_STREAM_TRANSPORT_TYPE_RELAY = 2

SOCKET_ADDRESS_TYPE_UNIX = 0
SOCKET_ADDRESS_TYPE_ABSTRACT_UNIX = 1
SOCKET_ADDRESS_TYPE_IPV4 = 2
SOCKET_ADDRESS_TYPE_IPV6 = 3

SOCKET_ACCESS_CONTROL_LOCALHOST = 0
SOCKET_ACCESS_CONTROL_PORT = 1
SOCKET_ACCESS_CONTROL_NETMASK = 2
SOCKET_ACCESS_CONTROL_CREDENTIALS = 3

TUBE_STATE_LOCAL_PENDING = 0
TUBE_STATE_REMOTE_PENDING = 1
TUBE_STATE_OPEN = 2
TUBE_STATE_NOT_OFFERED = 3

TUBE_TYPE_DBUS = 0
TUBE_TYPE_STREAM = 1

MEDIA_STREAM_DIRECTION_NONE = 0
MEDIA_STREAM_DIRECTION_SEND = 1
MEDIA_STREAM_DIRECTION_RECEIVE = 2
MEDIA_STREAM_DIRECTION_BIDIRECTIONAL = 3

MEDIA_STREAM_PENDING_LOCAL_SEND = 1
MEDIA_STREAM_PENDING_REMOTE_SEND = 2

MEDIA_STREAM_TYPE_AUDIO = 0
MEDIA_STREAM_TYPE_VIDEO = 1

MEDIA_STREAM_STATE_DISCONNECTED = 0
MEDIA_STREAM_STATE_CONNECTING = 1
MEDIA_STREAM_STATE_CONNECTED = 2

MEDIA_STREAM_DIRECTION_NONE = 0
MEDIA_STREAM_DIRECTION_SEND = 1
MEDIA_STREAM_DIRECTION_RECEIVE = 2
MEDIA_STREAM_DIRECTION_BIDIRECTIONAL = 3

FT_STATE_NONE = 0
FT_STATE_PENDING = 1
FT_STATE_ACCEPTED = 2
FT_STATE_OPEN = 3
FT_STATE_COMPLETED = 4
FT_STATE_CANCELLED = 5

FT_STATE_CHANGE_REASON_NONE = 0
FT_STATE_CHANGE_REASON_REQUESTED = 1
FT_STATE_CHANGE_REASON_LOCAL_STOPPED = 2
FT_STATE_CHANGE_REASON_REMOTE_STOPPED = 3
FT_STATE_CHANGE_REASON_LOCAL_ERROR = 4
FT_STATE_CHANGE_REASON_REMOTE_ERROR = 5

FILE_HASH_TYPE_NONE = 0
FILE_HASH_TYPE_MD5 = 1
FILE_HASH_TYPE_SHA1 = 2
FILE_HASH_TYPE_SHA256 = 3

FT_STATE = CHANNEL_TYPE_FILE_TRANSFER + '.State'
FT_CONTENT_TYPE = CHANNEL_TYPE_FILE_TRANSFER + '.ContentType'
FT_FILENAME = CHANNEL_TYPE_FILE_TRANSFER + '.Filename'
FT_SIZE = CHANNEL_TYPE_FILE_TRANSFER + '.Size'
FT_CONTENT_HASH_TYPE = CHANNEL_TYPE_FILE_TRANSFER + '.ContentHashType'
FT_CONTENT_HASH = CHANNEL_TYPE_FILE_TRANSFER + '.ContentHash'
FT_DESCRIPTION = CHANNEL_TYPE_FILE_TRANSFER + '.Description'
FT_DATE = CHANNEL_TYPE_FILE_TRANSFER + '.Date'
FT_AVAILABLE_SOCKET_TYPES = CHANNEL_TYPE_FILE_TRANSFER + '.AvailableSocketTypes'
FT_TRANSFERRED_BYTES = CHANNEL_TYPE_FILE_TRANSFER + '.TransferredBytes'
FT_INITIAL_OFFSET = CHANNEL_TYPE_FILE_TRANSFER + '.InitialOffset'
FT_FILE_COLLECTION = CHANNEL_TYPE_FILE_TRANSFER + '.FUTURE.FileCollection'
FT_URI = CHANNEL_TYPE_FILE_TRANSFER + '.URI'
FT_SERVICE_NAME = CHANNEL_IFACE_FILE_TRANSFER_METADATA + '.ServiceName'
FT_METADATA = CHANNEL_IFACE_FILE_TRANSFER_METADATA + '.Metadata'

GF_CAN_ADD = 1
GF_CAN_REMOVE = 2
GF_CAN_RESCIND = 4
GF_MESSAGE_ADD = 8
GF_MESSAGE_REMOVE = 16
GF_MESSAGE_ACCEPT = 32
GF_MESSAGE_REJECT = 64
GF_MESSAGE_RESCIND = 128
GF_CHANNEL_SPECIFIC_HANDLES = 256
GF_ONLY_ONE_GROUP = 512
GF_HANDLE_OWNERS_NOT_AVAILABLE = 1024
GF_PROPERTIES = 2048
GF_MEMBERS_CHANGED_DETAILED = 4096

GC_REASON_NONE = 0
GC_REASON_OFFLINE = 1
GC_REASON_KICKED = 2
GC_REASON_BUSY = 3
GC_REASON_INVITED = 4
GC_REASON_BANNED = 5
GC_REASON_ERROR = 6
GC_REASON_INVALID_CONTACT = 7
GC_REASON_NO_ANSWER = 8
GC_REASON_RENAMED = 9
GC_REASON_PERMISSION_DENIED = 10
GC_REASON_SEPARATED = 11

HS_UNHELD = 0
HS_HELD = 1
HS_PENDING_HOLD = 2
HS_PENDING_UNHOLD = 3

HSR_NONE = 0
HSR_REQUESTED = 1
HSR_RESOURCE_NOT_AVAILABLE = 2

CONN_STATUS_CONNECTED = 0
CONN_STATUS_CONNECTING = 1
CONN_STATUS_DISCONNECTED = 2

CSR_NONE_SPECIFIED = 0
CSR_REQUESTED = 1
CSR_NETWORK_ERROR = 2
CSR_AUTHENTICATION_FAILED = 3
CSR_ENCRYPTION_ERROR = 4
CSR_NAME_IN_USE = 5
CSR_CERT_NOT_PROVIDED = 6
CSR_CERT_UNTRUSTED = 7
CSR_CERT_EXPIRED = 8
CSR_CERT_NOT_ACTIVATED = 9
CSR_CERT_HOSTNAME_MISMATCH = 10
CSR_CERT_FINGERPRINT_MISMATCH = 11
CSR_CERT_SELF_SIGNED = 12
CSR_CERT_OTHER_ERROR = 13

BUDDY_INFO = 'org.laptop.Telepathy.BuddyInfo'
ACTIVITY_PROPERTIES = 'org.laptop.Telepathy.ActivityProperties'

CHAT_STATE_GONE = 0
CHAT_STATE_INACTIVE = 1
CHAT_STATE_ACTIVE = 2
CHAT_STATE_PAUSED = 3
CHAT_STATE_COMPOSING = 4

# Channel_Media_Capabilities
MEDIA_CAP_AUDIO = 1
MEDIA_CAP_VIDEO = 2
MEDIA_CAP_STUN = 4
MEDIA_CAP_GTALKP2P = 8
MEDIA_CAP_ICEUDP = 16
MEDIA_CAP_IMMUTABLE_STREAMS = 32

CLIENT = 'org.freedesktop.Telepathy.Client'

PRESENCE_OFFLINE = 1
PRESENCE_AVAILABLE = 2
PRESENCE_AWAY = 3
PRESENCE_EXTENDED_AWAY = 4
PRESENCE_HIDDEN = 5
PRESENCE_BUSY = 6
PRESENCE_UNKNOWN = 7
PRESENCE_ERROR = 8

CONTACT_INFO_FLAG_CAN_SET = 1
CONTACT_INFO_FLAG_PUSH = 2
CONTACT_INFO_FIELD_FLAG_PARAMETERS_EXACT = 1
CONTACT_INFO_FIELD_FLAG_OVERWRITTEN_BY_NICKNAME = 2

# Channel_Interface_SaslAuthentication
SASL_STATUS_NOT_STARTED = 0
SASL_STATUS_IN_PROGRESS = 1
SASL_STATUS_SERVER_SUCCEEDED = 2
SASL_STATUS_CLIENT_ACCEPTED = 3
SASL_STATUS_SUCCEEDED = 4
SASL_STATUS_SERVER_FAILED = 5
SASL_STATUS_CLIENT_FAILED = 6

SASL_ABORT_REASON_INVALID_CHALLENGE = 0
SASL_ABORT_REASON_USER_ABORT = 1

AUTH_METHOD = CHANNEL_TYPE_SERVER_AUTHENTICATION + ".AuthenticationMethod"
SASL_AVAILABLE_MECHANISMS = CHANNEL_IFACE_SASL_AUTH + ".AvailableMechanisms"
SASL_STATUS = CHANNEL_IFACE_SASL_AUTH + ".SASLStatus"
SASL_ERROR = CHANNEL_IFACE_SASL_AUTH + ".SASLError"
SASL_ERROR_DETAILS = CHANNEL_IFACE_SASL_AUTH + ".SASLErrorDetails"
SASL_CONTEXT = CHANNEL_IFACE_SASL_AUTH + ".SASLContext"
SASL_AUTHORIZATION_IDENTITY = CHANNEL_IFACE_SASL_AUTH + ".AuthorizationIdentity"
SASL_DEFAULT_REALM = CHANNEL_IFACE_SASL_AUTH + ".DefaultRealm"
SASL_DEFAULT_USERNAME = CHANNEL_IFACE_SASL_AUTH + ".DefaultUsername"

# Channel_Type_ServerTLSConnection
TLS_CERT_PATH = CHANNEL_TYPE_SERVER_TLS_CONNECTION + ".ServerCertificate"
TLS_HOSTNAME = CHANNEL_TYPE_SERVER_TLS_CONNECTION + ".Hostname"
TLS_REFERENCE_IDENTITIES = \
    CHANNEL_TYPE_SERVER_TLS_CONNECTION + ".ReferenceIdentities"

# Connection.Interface.Location

LOCATION_FEATURE_CAN_SET = 1

# Channel.Type.Text

MT_NORMAL = 0
MT_ACTION = 1
MT_NOTICE = 2
MT_AUTO_REPLY = 3
MT_DELIVERY_REPORT = 4

PROTOCOL = 'org.freedesktop.Telepathy.Protocol'
PROTOCOL_IFACE_PRESENCES = PROTOCOL + '.Interface.Presence'
PROTOCOL_IFACE_ADDRESSING = PROTOCOL + '.Interface.Addressing'

PARAM_REQUIRED = 1
PARAM_REGISTER = 2
PARAM_HAS_DEFAULT = 4
PARAM_SECRET = 8
PARAM_DBUS_PROPERTY = 16

AUTHENTICATION = 'org.freedesktop.Telepathy.Authentication'
AUTH_TLS_CERT = AUTHENTICATION + ".TLSCertificate"

TLS_CERT_STATE_PENDING = 0
TLS_CERT_STATE_ACCEPTED = 1
TLS_CERT_STATE_REJECTED = 2

TLS_REJECT_REASON_UNKNOWN = 0
TLS_REJECT_REASON_UNTRUSTED = 1

# Channel.Interface.Messages

MESSAGE_PART_SUPPORT_FLAGS = CHANNEL_IFACE_MESSAGES + '.MessagePartSupportFlags'
DELIVERY_REPORTING_SUPPORT = CHANNEL_IFACE_MESSAGES + '.DeliveryReportingSupport'
SUPPORTED_CONTENT_TYPES = CHANNEL_IFACE_MESSAGES + '.SupportedContentTypes'

MSG_SENDING_FLAGS_REPORT_DELIVERY = 1
MSG_SENDING_FLAGS_REPORT_READ = 2
MSG_SENDING_FLAGS_REPORT_DELETED = 4

DELIVERY_REPORTING_SUPPORT_FLAGS_RECEIVE_FAILURES = 1
DELIVERY_REPORTING_SUPPORT_FLAGS_RECEIVE_SUCCESSES = 2
DELIVERY_REPORTING_SUPPORT_FLAGS_RECEIVE_READ = 4
DELIVERY_REPORTING_SUPPORT_FLAGS_RECEIVE_DELETED = 8

DELIVERY_STATUS_UNKNOWN = 0
DELIVERY_STATUS_DELIVERED = 1
DELIVERY_STATUS_TEMPORARILY_FAILED = 2
DELIVERY_STATUS_PERMANENTLY_FAILED = 3
DELIVERY_STATUS_ACCEPTED = 4
DELIVERY_STATUS_READ = 5
DELIVERY_STATUS_DELETED = 6

MEDIA_STREAM_ERROR_UNKNOWN = 0
MEDIA_STREAM_ERROR_EOS = 1
MEDIA_STREAM_ERROR_CODEC_NEGOTIATION_FAILED = 2
MEDIA_STREAM_ERROR_CONNECTION_FAILED = 3
MEDIA_STREAM_ERROR_NETWORK_ERROR = 4
MEDIA_STREAM_ERROR_NO_CODECS = 5
MEDIA_STREAM_ERROR_INVALID_CM_BEHAVIOR = 6
MEDIA_STREAM_ERROR_MEDIA_ERROR = 7

PASSWORD_FLAG_PROVIDE = 8

# Channel.Interface.Room
ROOM_NAME = CHANNEL_IFACE_ROOM + '.RoomName'
ROOM_SERVER = CHANNEL_IFACE_ROOM + '.Server'

# Channel.Interface.Subject
SUBJECT = CHANNEL_IFACE_ROOM + '.Subject'
SUBJECT_PRESENT = 1
SUBJECT_CAN_SET = 2
