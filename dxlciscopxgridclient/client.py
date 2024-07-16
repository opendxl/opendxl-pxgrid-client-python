from __future__ import absolute_import
from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client

#: The DXL topic for making queries to pxGrid services
_PXGRID_SERVICE_PREFIX = "/mcafee/service/pxgrid/"
#: The DXL topic for events received from pxGrid services
_PXGRID_EVENT_PREFIX = "/mcafee/event/pxgrid/"

#: The IP address parameter
_PARAM_IP = "ipAddress"
#: The MAC address parameter
_PARAM_MAC = "macAddress"
#: The NAS IP address parameter
_PARAM_NAS_IP = "nasIpAddress"
#: The policy name parameter
_PARAM_POLICY_NAME = "policyName"
#: The param policy name parameter when its the only parameter
_PARAM_POLICY_NAME_2 = "name"
#: The mitigation action parameter
_PARAM_ACTION = "actions"
_PARAM_OPERATION_ID = "operationId"


class CiscoPxGridClient(Client):
    """
    The "Cisco pxGrid DXL Client Library" client wrapper class.
    """

    def __init__(self, dxl_client):
        """
        Constructor parameters:

        :param dxl_client: The DXL client to use for communication with the
            fabric
        """
        super(CiscoPxGridClient, self).__init__(dxl_client)
        self._anc_client_category = AncClientCategory(self)
        self._identity_client_category = IdentityClientCategory(self)

    @property
    def anc(self):
        """
        Retrieves a client object for use in interacting with Cisco Adaptive
        Network Control (ANC) functionality via pxGrid.

        :return: The ANC instance.
        :rtype: AncClientCategory
        """
        return self._anc_client_category

    @property
    def identity(self):
        """
        Retrieves a client object for use in interacting with identity services
        in Cisco pxGrid.

        :return: The identity client instance.
        :rtype: IdentityClientCategory
        """
        return self._identity_client_category


class _BaseClientCategory(object):
    """
    The base client service class for using Cisco pxGrid.
    """
    def __init__(self, pxgrid_client):
        """
        Constructor parameters:

        :param CiscoPxGridClient pxgrid_client: The pxGrid client object.
        """
        self._pxgrid_client = pxgrid_client


class IdentityClientCategory(_BaseClientCategory):
    """
    A client class for interacting with identity services in Cisco pxGrid.
    """

    #: The DXL topic for making queries to pxGrid identity services
    _IDENTITY_EVENT_PREFIX = _PXGRID_EVENT_PREFIX + "identity/"
    #: The DXL topic for making queries to pxGrid session endpoint
    _IDENTITY_EVENT_SESSION = _IDENTITY_EVENT_PREFIX + "session"

    def add_session_callback(self, callback):
        """
        Register an object to called back upon when a session event is
        received.

        :param dxlciscopxgridclient.callbacks.IdentitySessionCallback callback:
            The callback to register.
        """
        self._pxgrid_client._dxl_client.add_event_callback(
            self._IDENTITY_EVENT_SESSION, callback)

class AncClientCategory(_BaseClientCategory):
    """
    A client class for interacting with Cisco Adaptive Network Control (ANC)
    functionality via pxGrid.
    """

    #: The base DXL topic for making queries to the Cisco ANC
    _ANC_PREFIX = _PXGRID_SERVICE_PREFIX + "anc/"

    ### POLICY API ENDPOINTS
    #: The DXL topic for making queries to the ANC "retrieve all policies"
    _ANC_RETRIEVE_ALL_POLICIES = _ANC_PREFIX + "retrieveallpolicies"
    #: The DXL topic for making queries to the ANC "retrieve policy by name"
    _ANC_RETRIEVE_POLICY_BY_NAME = _ANC_PREFIX + "retrievepolicybyname"
    #: The DXL topic for creating policies
    _ANC_CREATE_POLICY = _ANC_PREFIX + "createpolicy"
    #: The DXL topic for deleting policies by name
    _ANC_DELETE_POLICY_BY_NAME = _ANC_PREFIX + "deletepolicybyname"

    ### ENDPOINT API ENDPOINTS
    #: The DXL topic for making queries to the ANC "get endpoints"
    _ANC_GET_ENDPOINTS = _ANC_PREFIX + "getendpoints"
    #: The DXL topic for making queries to the anc "get endpoint policies"
    _ANC_GET_ENDPOINT_POLICIES = _ANC_PREFIX + "getendpointpolicies"
    #: The DXL topic for making queries to the ANC "get endpoint by mac"
    _ANC_GET_ENDPOINT_BY_MAC = _ANC_PREFIX + "getendpointbymacaddress"
    #: The DXL topic for making queries to the ANC "get endpoint by nas ip address"
    _ANC_GET_ENDPOINT_BY_NAS_IP = _ANC_PREFIX + "getendpointbynasipaddress"
    #: The DXL topic for making queries to the ANC "apply endpoint policy by ip"
    _ANC_APPLY_ENDPOINT_POLICY_BY_IP = _ANC_PREFIX + "applyendpointpolicybyip"
    #: The DXL topic for making queries to the ANC "apply endpoint policy by mac" endpoint
    _ANC_APPLY_ENDPOINT_POLICY_BY_MAC = _ANC_PREFIX + "applyendpointpolicybymac"
    #: The DXL topic for making queries to the ANC "clear endpoint policy by mac" endpoint
    _ANC_CLEAR_ENDPOINT_POLICY_BY_MAC = _ANC_PREFIX + "clearendpointpolicybymac"
    #: The DXL topic for making queries to the ANC "apply endpoint policy"
    _ANC_APPLY_ENDPOINT_POLICY = _ANC_PREFIX + "applyendpointpolicy"
    #: The DXL topic for making queries to the ANC "clear endpoint policy"
    _ANC_CLEAR_ENDPOINT_POLICY = _ANC_PREFIX + "clearendpointpolicy"
    #: The DXL topic for making queries to the ANC "get operation status"
    _ANC_GET_OPERATION_STATUS = _ANC_PREFIX + "getoperationstatus"

    #: The base DXL topic for receiving events from the Cisco ANC
    _ANC_EVENT_PREFIX = _PXGRID_EVENT_PREFIX + "anc/"
    #: The DXL topic for receiving ANC "status" events
    _ANC_EVENT_STATUS = _ANC_EVENT_PREFIX + "status"

    ### REQUESTS
    def retrieve_all_policies(self):
        """
        Retrieve information for all ANC policies.

        :return: The policy information, which should look similar to this:

            .. code-block:: json

                {
                    "ancStatus": "success",
                    "ancpolicy": [
                        {
                            "action": [
                                "ShutDown"
                            ],
                            "name": "shutdown_policy"
                        },
                        {
                            "action": [
                                "Quarantine"
                            ],
                            "name": "quarantine_policy"
                        }
                    ]
                }
        :rtype: dict
        """
        request = Request(self._ANC_RETRIEVE_ALL_POLICIES)
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def retrieve_policy_by_name(self, policy_name):
        """
        Retrieve information for an ANC policy by name.

        :param str policy_name: Name of the policy.
        :return: The policy information, which should look similar to this:

            .. code-block:: json

                {
                    "ancStatus": "success",
                    "ancpolicy": [
                        {
                            "action": [
                                "Quarantine"
                            ],
                            "name": "quarantine_policy"
                        }
                    ]
                }
        :rtype: dict
        :raises Exception: If the policy name has not been defined.
        """
        request = Request(self._ANC_RETRIEVE_POLICY_BY_NAME)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_POLICY_NAME_2: policy_name})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def create_policy(self, name: str, actions: list):
        """
        Creates a policy object

        :param str name: name of the policy
        :param: str list actions: list of actions of the policy
        :return: the created policy object

        :rtype: dict
        """
        request = Request(self._ANC_CREATE_POLICY)
        MessageUtils.dict_to_json_payload(
            request,
            {
                _PARAM_POLICY_NAME_2: name,
                _PARAM_ACTION: actions
            }
        )
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def delete_policy_by_name(self, name):
        """
        Deletes a policy object with the name provided

        :param str name: name of the policy to be deleted
        :return: {"200": "no content"} if successful, {"204": "no content"} otherwise
        """
        request = Request(self._ANC_DELETE_POLICY_BY_NAME)
        MessageUtils.dict_to_json_payload(
            request, {_PARAM_POLICY_NAME_2: name}
        )
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def get_endpoints(self):
        """
        Gets all endpoints with policies applied

        :return: {"endpoints" : list[str]}
        """
        request = Request(self._ANC_GET_ENDPOINTS)
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def get_endpoint_policies(self):
        """
        Gets all endpoints with policies applied using both MAC address and NAS IP address

        :return: {"endpoints" : list[str]}
        """
        request = Request(self._ANC_GET_ENDPOINT_POLICIES)
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def get_endpoint_by_mac(self, mac_address):
        """
        Get information for an endpoint by its MAC address.

        :param str mac_address: MAC address of the endpoint.
        :return: The endpoint information, which should look similar to this:

            .. code-block:: json

                {
                    "macAddress": "00:11:22:33:44:55",
                    "policyName": "ANC_Shut"
                }

            or no content if macAddress not found or has no policies
        :rtype: dict
        :raises Exception: If no policy has been associated with the endpoint.
        """
        request = Request(self._ANC_GET_ENDPOINT_BY_MAC)
        MessageUtils.dict_to_json_payload(request, {_PARAM_MAC: mac_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def get_endpoint_by_nas_ip_address(self, mac_address: str, nas_ip_address: str):
        """
        Get endpoint with MAC address and NAS IP Address If endpoint does not exist,
        no content is returned

        :param str mac_address: MAC address of endpoint
        :param str nas_ip_address: nas_ip_address of endpoint
        :return: The endpoint information
        :rtype: dict
        """
        request = Request(self._ANC_GET_ENDPOINT_BY_NAS_IP)
        MessageUtils.dict_to_json_payload(request, {
            _PARAM_MAC: mac_address,
            _PARAM_NAS_IP: nas_ip_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def apply_endpoint_policy_by_ip(self, ip_address, policy_name):
        """
        Apply a policy to an endpoint by its IP address.

        :param str ip_address: IP address of the endpoint.
        :param str policy_name: Name of the policy to apply.
        :return: Results of the attempt to apply the endpoint policy.
        :rtype: dict
        """
        request = Request(self._ANC_APPLY_ENDPOINT_POLICY_BY_IP)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_IP: ip_address, _PARAM_POLICY_NAME: policy_name}
        )
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def apply_endpoint_policy_by_mac(self, mac_address, policy_name):
        """
        Apply a policy to an endpoint by its MAC address.

        :param str mac_address: MAC address of the endpoint.
        :param str policy_name: Name of the policy to apply.
        :return: Results of the attempt to apply the endpoint policy. On a
            successful application, the results should look similar to this:

            .. code-block:: json

                {
                    "macAddress": "00:11:22:33:44:55",
                    "operationId": "cise.psarchlab.com:123",
                    "policyName": "ANC_Shut",
                    "status": "SUCCESS"
                }

        :rtype: dict
        """
        request = Request(self._ANC_APPLY_ENDPOINT_POLICY_BY_MAC)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_MAC: mac_address,
             _PARAM_POLICY_NAME: policy_name})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def clear_endpoint_policy_by_mac(self, mac_address):
        """
        Clear the policy for an endpoint by its MAC address.

        :param str mac_address: MAC address of the endpoint.
        :return: Results of the attempt to clear the endpoint policy. On a
            successful clear attempt, the results should look similar to this:

            .. code-block:: json

                {
                    "macAddress": "00:11:22:33:44:55",
                    "operationId": "cise.psarchlab.com:123",
                    "policyName": "ANC_Shut",
                    "status": "SUCCESS"
                }

        :rtype: dict
        """
        request = Request(self._ANC_CLEAR_ENDPOINT_POLICY_BY_MAC)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_MAC: mac_address}
        )
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def apply_endpoint_policy(self, policy: str, mac_address: str, nas_ip_address: str,
                              session_id: str, nas_port_id: str, ip_address: str, username: str):
        """
        Apply a policy to the endpoint using MAC Address, NAS IP Address and other parameters
        If endpoint does not have an existing policy applied, the return status will be FAILURE
        with reason "mac address is not associated with a policy".

        :param str policy: policy name
        :param str mac_address: MAC address of endpoint
        :param str nas_ip_address: NAS Ip address of endpoint
        :param str session_id (optional): id of session
        :param str nas_port_id (optional): port of NAS
        :param str ip_address (optional): ip address of endpoint
        :param str username (optional): username

        :return: status object
        :rtype: dict
        """
        request = Request(self._ANC_APPLY_ENDPOINT_POLICY)
        MessageUtils.dict_to_json_payload(
            request,
            {
                'policy': policy,
                _PARAM_MAC: mac_address,
                _PARAM_NAS_IP: nas_ip_address,
                'sessionId': session_id if session_id is not None else None,
                'nasPortId': nas_port_id if nas_port_id is not None else None,
                _PARAM_IP: ip_address if ip_address is not None else None,
                'userName': username if username is not None else None
            }
        )
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def clear_endpoint_policy(self, mac_address: str, nas_ip_address: str):
        """
        Clear endpoint policy by MAC address and NAS IP address

        :param str mac_address: MAC address of endpoint
        :param str nas_ip_address: NAS IP address of endpoint
        :return: staus object
        :rtype: dict
        """
        request = Request(self._ANC_CLEAR_ENDPOINT_POLICY)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_MAC: mac_address, _PARAM_NAS_IP: nas_ip_address})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    def get_operation_status(self, operation_id: str):
        """
        If operation does not exist, HTTP status "204 No content" will be returned.

        :param str operationId: id of operation
        :return: status object
        :rtype: dict
        """
        request = Request(self._ANC_GET_OPERATION_STATUS)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_OPERATION_ID: operation_id})
        return MessageUtils.json_payload_to_dict(self._pxgrid_client._dxl_sync_request(request))

    ### NOTIFICATIONS
    def add_anc_status_callback(self, callback):
        """
        Register an object to called back upon when an ANC event is received.

        :param dxlciscopxgridclient.callbacks.AncCallback callback:
            The callback to register.
        """
        self._pxgrid_client._dxl_client.add_event_callback(self._ANC_EVENT_STATUS, callback)
