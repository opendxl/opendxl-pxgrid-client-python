from __future__ import absolute_import
from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client

#: The DXL topic for making queries to pxGrid services
_PXGRID_SERVICE_PREFIX = "/mcafee/service/pxgrid/"
#: The DXL topic for events received from pxGrid services
_PXGRID_EVENT_PREFIX = "/mcafee/event/pxgrid/"

#: The IP address parameter
_PARAM_IP = "ip"
#: The MAC address parameter
_PARAM_MAC = "mac"
#: The policy name parameter
_PARAM_POLICY_NAME = "policyName"
#: The mitigation action parameter
_PARAM_ACTION = "action"


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
        self._eps_client_category = EpsClientCategory(self)
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
    def eps(self):
        """
        Retrieves a client object for use in interacting with Cisco Endpoint
        Protection Service (EPS) functionality via pxGrid.

        :return: The EPS instance.
        :rtype: EpsClientCategory
        """
        return self._eps_client_category

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


class EpsClientCategory(_BaseClientCategory):
    """
    A client class for interacting with Cisco Endpoint Protection Service (EPS)
    functionality via pxGrid.
    """

    #: The base DXL topic for making queries to the Cisco EPS
    _EPS_PREFIX = _PXGRID_SERVICE_PREFIX + "eps/"
    #: The DXL topic for making queries to the EPS
    #: "send mitigation action by ip" endpoint
    _EPS_SEND_MITIGATION_ACTION_BY_IP = _EPS_PREFIX + \
        "sendmitigationactionbyip"
    #: The DXL topic for making queries to the EPS
    #: "send mitigation action by mac" endpoint
    _EPS_SEND_MITIGATION_ACTION_BY_MAC = _EPS_PREFIX + \
        "sendmitigationactionbymac"

    def send_mitigation_action_by_ip(self, ip_address, action):
        """
        Send an EPS mitigation action for an endpoint IP address.

        :param str ip_address: IP address of the endpoint for which the action
            should be performed.
        :param dxlciscopxgridclient.constants.EpsAction action: The action to
            perform.
        :return: Results of the attempt to send the action. The results for a
            successful send should look similar to this:

            .. code-block:: json

                {
                    "gid": "150",
                    "macInterface": "00:11:22:33:44:55",
                    "mitigationStatus": "complete"
                }
        :rtype: dict
        :raises Exception: If no session has been established for an endpoint
            which corresponds to the IP address.
        """
        request = Request(self._EPS_SEND_MITIGATION_ACTION_BY_IP)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_IP: ip_address,
             _PARAM_ACTION: action, "foo": "bar"})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def send_mitigation_action_by_mac(self, mac_address, action):
        """
        Send an EPS mitigation action for an endpoint MAC address.

        :param str mac_address: MAC address of the endpoint for which the
            action should be performed.
        :param dxlciscopxgridclient.constants.EpsAction action: The action to
            perform.
        :return: Results of the attempt to send the action. The results for a
            successful send should look similar to this:

            .. code-block:: json

                {
                    "gid": "150",
                    "macInterface": "00:11:22:33:44:55",
                    "mitigationStatus": "complete"
                }
        :rtype: dict
        """
        request = Request(self._EPS_SEND_MITIGATION_ACTION_BY_MAC)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_MAC: mac_address,
             _PARAM_ACTION: action})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))


class AncClientCategory(_BaseClientCategory):
    """
    A client class for interacting with Cisco Adaptive Network Control (ANC)
    functionality via pxGrid.
    """

    #: The base DXL topic for making queries to the Cisco ANC
    _ANC_PREFIX = _PXGRID_SERVICE_PREFIX + "anc/"
    #: The DXL topic for making queries to the ANC "get endpoint by ip"
    #: endpoint
    _ANC_GET_ENDPOINT_BY_IP = _ANC_PREFIX + "getendpointbyip"
    #: The DXL topic for making queries to the ANC "get endpoint by mac"
    #: endpoint
    _ANC_GET_ENDPOINT_BY_MAC = _ANC_PREFIX + "getendpointbymac"
    #: The DXL topic for making queries to the ANC "retrieve all policies"
    #: endpoint
    _ANC_RETRIEVE_ALL_POLICIES = _ANC_PREFIX + "retrieveallpolicies"
    #: The DXL topic for making queries to the ANC "retrieve policy by name"
    #: endpoint
    _ANC_RETRIEVE_POLICY_BY_NAME = _ANC_PREFIX + "retrievepolicybyname"
    #: The DXL topic for making queries to the ANC
    #: "apply endpoint policy by ip" endpoint
    _ANC_APPLY_ENDPOINT_POLICY_BY_IP = _ANC_PREFIX + "applyendpointpolicybyip"
    #: The DXL topic for making queries to the ANC
    #: "apply endpoint policy by mac" endpoint
    _ANC_APPLY_ENDPOINT_POLICY_BY_MAC = _ANC_PREFIX + \
        "applyendpointpolicybymac"
    #: The DXL topic for making queries to the ANC
    #: "clear endpoint policy by ip" endpoint
    _ANC_CLEAR_ENDPOINT_POLICY_BY_IP = _ANC_PREFIX + "clearendpointpolicybyip"
    #: The DXL topic for making queries to the ANC
    #: "clear endpoint policy by mac" endpoint
    _ANC_CLEAR_ENDPOINT_POLICY_BY_MAC = _ANC_PREFIX + \
        "clearendpointpolicybymac"

    #: The base DXL topic for receiving events from the Cisco ANC
    _ANC_EVENT_PREFIX = _PXGRID_EVENT_PREFIX + "anc/"
    #: The DXL topic for receiving ANC "apply endpoint policy" events
    _ANC_EVENT_APPLY_ENDPOINT_POLICY = _ANC_EVENT_PREFIX + \
        "applyendpointpolicy"
    #: The DXL topic for receiving ANC "clear endpoint policy" events
    _ANC_EVENT_CLEAR_ENDPOINT_POLICY = _ANC_EVENT_PREFIX + \
        "clearendpointpolicy"
    #: The DXL topic for receiving ANC "create policy" events
    _ANC_EVENT_CREATE_POLICY = _ANC_EVENT_PREFIX + "createpolicy"
    #: The DXL topic for receiving ANC "update policy" events
    _ANC_EVENT_UPDATE_POLICY = _ANC_EVENT_PREFIX + "updatepolicy"
    #: The DXL topic for receiving ANC "delete policy" events
    _ANC_EVENT_DELETE_POLICY = _ANC_EVENT_PREFIX + "deletepolicy"

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
            {_PARAM_POLICY_NAME: policy_name})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def get_endpoint_by_ip(self, ip_address):
        """
        Get information for an endpoint by its IP address.

        :param str ip_address: IP address of the endpoint.
        :return: The endpoint information, which should look similar to this:

            .. code-block:: json

                    {
                        "ancEndpoint": [
                            {
                                "macAddress": "00:11:22:33:44:55",
                                "policyName": "quarantine_policy"
                            }
                        ],
                        "ancStatus": "success"
                    }
        :rtype: dict
        :raises Exception: If no policy has been associated with the endpoint
            or if no session has been defined for an endpoint which corresponds
            to the IP address.
        """
        request = Request(self._ANC_GET_ENDPOINT_BY_IP)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_IP: ip_address})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def get_endpoint_by_mac(self, mac_address):
        """
        Get information for an endpoint by its MAC address.

        :param str mac_address: MAC address of the endpoint.
        :return: The endpoint information, which should look similar to this:

            .. code-block:: json

                {
                    "ancEndpoint": [
                        {
                            "macAddress": "00:11:22:33:44:55",
                            "policyName": "quarantine_policy"
                        }
                    ],
                    "ancStatus": "success"
                }
        :rtype: dict
        :raises Exception: If no policy has been associated with the endpoint.
        """
        request = Request(self._ANC_GET_ENDPOINT_BY_MAC)
        MessageUtils.dict_to_json_payload(request, {
            _PARAM_MAC: mac_address})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def clear_endpoint_policy_by_ip(self, ip_address):
        """
        Clear the policy for an endpoint by its IP address.

        :param str ip_address: IP address of the endpoint.
        :return: Results of the attempt to clear the endpoint policy. On a
            successful clear attempt, the results should look similar to this:

            .. code-block:: json

                {
                    "ancStatus": "success"
                }
        :rtype: dict
        :raises Exception: If no policy has been associated with the endpoint.
        """
        request = Request(self._ANC_CLEAR_ENDPOINT_POLICY_BY_IP)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_IP: ip_address})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def clear_endpoint_policy_by_mac(self, mac_address):
        """
        Clear the policy for an endpoint by its MAC address.

        :param str mac_address: MAC address of the endpoint.
        :return: Results of the attempt to clear the endpoint policy. On a
            successful clear attempt, the results should look similar to this:

            .. code-block:: json

                {
                    "ancStatus": "success"
                }
        :rtype: dict
        :raises Exception: If no policy has been associated with the endpoint.
        """
        request = Request(self._ANC_CLEAR_ENDPOINT_POLICY_BY_MAC)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_MAC: mac_address})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def apply_endpoint_policy_by_ip(self, ip_address, policy_name):
        """
        Apply a policy to an endpoint by its IP address.

        :param str ip_address: IP address of the endpoint.
        :param str policy_name: Name of the policy to apply.
        :return: Results of the attempt to apply the endpoint policy. On a
            successful application, the results should look similar to this:

            .. code-block:: json

                {
                    "ancStatus": "success"
                }
        :rtype: dict
        :raises Exception: If the supplied policy name has already been
            applied to the endpoint, the policy name has not been defined, or
            if no session has been defined for an endpoint which corresponds to
            the IP address.
        """
        request = Request(self._ANC_APPLY_ENDPOINT_POLICY_BY_IP)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_IP: ip_address,
             _PARAM_POLICY_NAME: policy_name})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def apply_endpoint_policy_by_mac(self, mac_address, policy_name):
        """
        Apply a policy to an endpoint by its MAC address.

        :param str mac_address: MAC address of the endpoint.
        :param str policy_name: Name of the policy to apply.
        :return: Results of the attempt to apply the endpoint policy. On a
            successful application, the results should look similar to this:

            .. code-block:: json

                {
                    "ancStatus": "success"
                }
        :rtype: dict
        :raises Exception: If the supplied policy name has already been
            applied to the endpoint or the policy name has not been defined.
        """
        request = Request(self._ANC_APPLY_ENDPOINT_POLICY_BY_MAC)
        MessageUtils.dict_to_json_payload(
            request,
            {_PARAM_MAC: mac_address,
             _PARAM_POLICY_NAME: policy_name})
        return MessageUtils.json_payload_to_dict(
            self._pxgrid_client._dxl_sync_request(request))

    def add_apply_endpoint_policy_callback(self, callback):
        """
        Register an object to called back upon when an ANC
        "apply endpoint policy" event is received.

        :param dxlciscopxgridclient.callbacks.AncApplyEndpointPolicyCallback callback:
            The callback to register.
        """
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_APPLY_ENDPOINT_POLICY, callback)

    def add_clear_endpoint_policy_callback(self, callback):
        """
        Register an object to called back upon when an ANC
        "clear endpoint policy" event is received.

        :param dxlciscopxgridclient.callbacks.AncClearEndpointPolicyCallback callback:
            The callback to register.
        """
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_CLEAR_ENDPOINT_POLICY, callback)

    def add_create_policy_callback(self, callback):
        """
        Register an object to called back upon when an ANC
        "create endpoint policy" event is received.

        :param dxlciscopxgridclient.callbacks.AncCreatePolicyCallback callback:
            The callback to register.
        """
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_CREATE_POLICY, callback)

    def add_update_policy_callback(self, callback):
        """
        Register an object to called back upon when an ANC
        "update endpoint policy" event is received.

        :param dxlciscopxgridclient.callbacks.AncUpdatePolicyCallback callback:
            The callback to register.
        """
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_UPDATE_POLICY, callback)

    def add_delete_policy_callback(self, callback):
        """
        Register an object to called back upon when an ANC
        "delete endpoint policy" event is received.

        :param dxlciscopxgridclient.callbacks.AncDeletePolicyCallback callback:
            The callback to register.
        """
        self._pxgrid_client._dxl_client.add_event_callback(
            self._ANC_EVENT_DELETE_POLICY, callback)
