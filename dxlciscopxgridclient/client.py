from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client


class CiscoPxGridClient(Client):
    """
    The "Cisco pxGrid DXL Client Library" client wrapper class.
    """

    _PXGRID_SERVICE_PREFIX = "/mcafee/service/pxgrid/"
    _PXGRID_EVENT_PREFIX = "/mcafee/event/pxgrid/"
    _PARAM_IP = "ip"
    _PARAM_MAC = "mac"
    _PARAM_POLICY_NAME = "policyName"
    _PARAM_ACTION = "action"

    def __init__(self, dxl_client):
        """
        Constructor parameters:

        :param dxl_client: The DXL client to use for communication with the fabric
        """
        super(CiscoPxGridClient, self).__init__(dxl_client)
        self._anc_client_category = AncClientCategory(self)
        self._eps_client_category = EpsClientCategory(self)
        self._identity_client_category = IdentityClientCategory(self)

    @property
    def anc(self):
        return self._anc_client_category

    @property
    def eps(self):
        return self._eps_client_category

    @property
    def identity(self):
        return self._identity_client_category


class _BaseClientCategory(object):

    def __init__(self, pxgrid_client):
        self._pxgrid_client = pxgrid_client


class IdentityClientCategory(_BaseClientCategory):

    _IDENTITY_EVENT_PREFIX = CiscoPxGridClient._PXGRID_EVENT_PREFIX + "identity/"
    _IDENTITY_EVENT_SESSION = _IDENTITY_EVENT_PREFIX + "session"

    def add_session_callback(self, callback):
        self._pxgrid_client._dxl_client.add_event_callback(
            self._IDENTITY_EVENT_SESSION, callback)


class EpsClientCategory(_BaseClientCategory):

    _EPS_PREFIX = CiscoPxGridClient._PXGRID_SERVICE_PREFIX + "eps/"
    _EPS_GET_MITIGATION_ACTION_STATUS_BY_IP = _EPS_PREFIX + "getmitigationactionstatusbyip"
    _EPS_GET_MITIGATION_ACTION_STATUS_BY_MAC = _EPS_PREFIX + "getmitigationactionstatusbymac"
    _EPS_SEND_MITIGATION_ACTION_BY_IP = _EPS_PREFIX + "sendmitigationactionbyip"
    _EPS_SEND_MITIGATION_ACTION_BY_MAC = _EPS_PREFIX + "sendmitigationactionbymac"

    def __init__(self, pxgrid_client):
        super(EpsClientCategory, self).__init__(pxgrid_client)

    def get_mitigation_action_status_by_ip(self, ip_address):
        request = Request(self._EPS_GET_MITIGATION_ACTION_STATUS_BY_IP)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_IP: ip_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def send_mitigation_action_by_ip(self, ip_address, action):
        request = Request(self._EPS_SEND_MITIGATION_ACTION_BY_IP)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_IP: ip_address,
                                                    CiscoPxGridClient._PARAM_ACTION: action, "foo": "bar"})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def get_mitigation_action_status_by_mac(self, mac_address):
        request = Request(self._EPS_GET_MITIGATION_ACTION_STATUS_BY_MAC)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_MAC: mac_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def send_mitigation_action_by_mac(self, mac_address, action):
        request = Request(self._EPS_SEND_MITIGATION_ACTION_BY_MAC)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_MAC: mac_address,
                                                    CiscoPxGridClient._PARAM_ACTION: action})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))


class AncClientCategory(_BaseClientCategory):

    _ANC_PREFIX = CiscoPxGridClient._PXGRID_SERVICE_PREFIX + "anc/"
    _ANC_GET_ENDPOINT_BY_IP = _ANC_PREFIX + "getendpointbyip"
    _ANC_GET_ENDPOINT_BY_MAC = _ANC_PREFIX + "getendpointbymac"
    _ANC_RETRIEVE_ALL_POLICIES = _ANC_PREFIX + "retrieveallpolicies"
    _ANC_RETRIEVE_POLICY_BY_NAME = _ANC_PREFIX + "retrievepolicybyname"
    _ANC_APPLY_ENDPOINT_POLICY_BY_IP = _ANC_PREFIX + "applyendpointpolicybyip"
    _ANC_APPLY_ENDPOINT_POLICY_BY_MAC = _ANC_PREFIX + "applyendpointpolicybymac"
    _ANC_CLEAR_ENDPOINT_POLICY_BY_IP = _ANC_PREFIX + "clearendpointpolicybyip"
    _ANC_CLEAR_ENDPOINT_POLICY_BY_MAC = _ANC_PREFIX + "clearendpointpolicybymac"

    _ANC_EVENT_PREFIX = CiscoPxGridClient._PXGRID_EVENT_PREFIX + "anc/"
    _ANC_EVENT_APPLY_ENDPOINT_POLICY = _ANC_EVENT_PREFIX + "applyendpointpolicy"
    _ANC_EVENT_CLEAR_ENDPOINT_POLICY = _ANC_EVENT_PREFIX + "clearendpointpolicy"
    _ANC_EVENT_CREATE_POLICY = _ANC_EVENT_PREFIX + "createpolicy"
    _ANC_EVENT_UPDATE_POLICY = _ANC_EVENT_PREFIX + "updatepolicy"
    _ANC_EVENT_DELETE_POLICY = _ANC_EVENT_PREFIX + "deletepolicy"

    def __init__(self, pxgrid_client):
        super(AncClientCategory, self).__init__(pxgrid_client)

    def retrieve_all_policies(self):
        request = Request(self._ANC_RETRIEVE_ALL_POLICIES)
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def retrieve_policy_by_name(self, policy_name):
        request = Request(self._ANC_RETRIEVE_POLICY_BY_NAME)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_POLICY_NAME: policy_name})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def get_endpoint_by_ip(self, ip_address):
        request = Request(self._ANC_GET_ENDPOINT_BY_IP)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_IP: ip_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def get_endpoint_by_mac(self, mac_address):
        request = Request(self._ANC_GET_ENDPOINT_BY_MAC)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_MAC: mac_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def clear_endpoint_policy_by_ip(self, ip_address):
        request = Request(self._ANC_CLEAR_ENDPOINT_POLICY_BY_IP)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_IP: ip_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def apply_endpoint_policy_by_ip(self, ip_address, policy_name):
        request = Request(self._ANC_APPLY_ENDPOINT_POLICY_BY_IP)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_IP: ip_address,
                                                    CiscoPxGridClient._PARAM_POLICY_NAME: policy_name})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def clear_endpoint_policy_by_mac(self, mac_address):
        request = Request(self._ANC_CLEAR_ENDPOINT_POLICY_BY_MAC)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_MAC: mac_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def apply_endpoint_policy_by_mac(self, mac_address, policy_name):
        request = Request(self._ANC_APPLY_ENDPOINT_POLICY_BY_MAC)
        MessageUtils.dict_to_json_payload(request, {CiscoPxGridClient._PARAM_MAC: mac_address,
                                                    CiscoPxGridClient._PARAM_POLICY_NAME: policy_name})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def add_apply_endpoint_policy_callback(self, callback):
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_APPLY_ENDPOINT_POLICY, callback)

    def add_clear_endpoint_policy_callback(self, callback):
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_CLEAR_ENDPOINT_POLICY, callback)

    def add_create_policy_callback(self, callback):
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_CREATE_POLICY, callback)

    def add_update_policy_callback(self, callback):
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_UPDATE_POLICY, callback)

    def add_delete_policy_callback(self, callback):
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_DELETE_POLICY, callback)
