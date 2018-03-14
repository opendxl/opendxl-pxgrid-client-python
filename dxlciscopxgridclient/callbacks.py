from __future__ import absolute_import
from dxlbootstrap.util import MessageUtils
from dxlclient.callbacks import EventCallback


class AncApplyEndpointPolicyCallback(EventCallback):
    """
    Callback wrapper which invokes the :meth:`on_apply_endpoint_policy` method
    when an apply endpoint policy event is received.
    """
    def on_event(self, event):
        """
        Method invoked when an apply endpoint policy event occurs. Derived
        classes can implement the :meth:`on_apply_endpoint_policy` method
        instead of this method in order to process the event payload as a
        `dict`.

        :param dxlclient.message.Event event: Message received for the event
            notification
        """
        self.on_apply_endpoint_policy(MessageUtils.json_payload_to_dict(event))

    def on_apply_endpoint_policy(self, apply_dict):
        """
        Method invoked when an apply endpoint policy event occurs.

        :param dict apply_dict: Payload for the event notification. For
            example, the value for an event sent on application of an endpoint
            policy should look similar to this:

            .. code-block:: json

                {
                    "ipAddress": "192.168.1.1",
                    "policyName": "quarantine_policy"
                }
        """
        pass


class AncClearEndpointPolicyCallback(EventCallback):
    """
    Callback wrapper which invokes the :meth:`on_clear_endpoint_policy` method
    when a clear endpoint policy event is received.
    """
    def on_event(self, event):
        """
        Method invoked when a clear endpoint policy event occurs. Derived
        classes can implement the :meth:`on_clear_endpoint_policy` method
        instead of this method in order to process the event payload as a
        `dict`.

        :param dxlclient.message.Event event: Message received for the event
            notification
        """
        self.on_clear_endpoint_policy(MessageUtils.json_payload_to_dict(event))

    def on_clear_endpoint_policy(self, clear_dict):
        """
        Method invoked when a clear endpoint policy event occurs.

        :param dict clear_dict: Payload for the event notification. For
            example, the value for an event sent on clearing of an endpoint
            policy should look similar to this:

            .. code-block:: json

                {
                    "ipAddress": "192.168.1.1"
                }
        """
        pass


class AncCreatePolicyCallback(EventCallback):
    """
    Callback wrapper which invokes the :meth:`on_create_policy` method when a
    clear policy event is received.
    """
    def on_event(self, event):
        """
        Method invoked when an create policy event occurs. Derived classes can
        implement the :meth:`on_create_policy` method instead of this method in
        order to process the event payload as a `dict`.

        :param dxlclient.message.Event event: Message received for the event
            notification
        """
        self.on_create_policy(MessageUtils.json_payload_to_dict(event))

    def on_create_policy(self, create_dict):
        """
        Method invoked when a create policy event occurs.

        :param dict create_dict: Payload for the event notification. For
            example, the value for an event sent on creation of a policy should
            look similar to this:

            .. code-block:: json

                {
                    "action": [ "Quarantine" ],
                    "name": "test_policy"
                }
        """
        pass


class AncUpdatePolicyCallback(EventCallback):
    """
    Callback wrapper which invokes the :meth:`on_update_policy` method
    when an update policy event is received.
    """
    def on_event(self, event):
        """
        Method invoked when a update policy event occurs. Derived classes can
        implement the :meth:`on_update_policy` method instead of this method in
        order to process the event payload as a `dict`.

        :param dxlclient.message.Event event: Message received for the event
            notification
        """
        self.on_update_policy(MessageUtils.json_payload_to_dict(event))

    def on_update_policy(self, update_dict):
        """
        Method invoked when an update policy event occurs.

        :param dict update_dict: Payload for the event notification. For
            example, the value for an event sent on update of a policy should
            look similar to this:

            .. code-block:: json

                {
                    "action": [ "Quarantine" ],
                    "name": "test_policy"
                }
        """
        pass


class AncDeletePolicyCallback(EventCallback):
    """
    Callback wrapper which invokes the :meth:`on_delete_policy` method
    when a delete policy event is received.
    """
    def on_event(self, event):
        """
        Method invoked when a delete policy event occurs. Derived classes can
        implement the :meth:`on_delete_policy` method instead of this method in
        order to process the event payload as a `dict`.

        :param dxlclient.message.Event event: Message received for the event
            notification
        """
        self.on_delete_policy(MessageUtils.json_payload_to_dict(event))

    def on_delete_policy(self, delete_dict):
        """
        Method invoked when an delete policy event occurs.

        :param dict delete_dict: Payload for the event notification. For
            example, the value for an event sent on deletion of a policy should
            look similar to this:

            .. code-block:: json

                {
                    "action": [ "Quarantine" ],
                    "name": "test_policy"
                }
        """
        pass


class IdentitySessionCallback(EventCallback):
    """
    Callback wrapper which invokes the :meth:`on_session` method
    when a session event is received.
    """
    def on_event(self, event):
        """
        Method invoked when a session event occurs. Derived classes can
        implement the :meth:`on_session` method instead of this method in order
        to process the event payload as a `dict`.

        :param dxlclient.message.Event event: Message received for the event
            notification
        """
        self.on_session(MessageUtils.json_payload_to_dict(event))

    def on_session(self, session_dict):
        """
        Method invoked when an session event occurs.

        :param dict session_dict: Payload for the event notification. For
            example, the value for an event sent on start of a session should
            look similar to this:

            .. code-block:: json

                {
                    "IdentitySourceFirstPort": "0",
                    "IdentitySourcePortEnd": "0",
                    "IdentitySourcePortStart": "0",
                    "MDMEndpoint": {},
                    "RADIUSAttrs": [ {
                        "attrName": "Acct-Session-Id",
                        "attrValue": "123"
                    } ],
                    "assessedPostureEvent": [ {} ],
                    "attribute": [ {
                        "name": "Authorization_Profiles",
                        "type": "string",
                        "value": "1234"
                    } ],
                    "endpointCheckResult": "none",
                    "endpointProfile": "Microsoft-Device",
                    "gid": "24703",
                    "interface": {
                        "deviceAttachPt": {
                            "deviceMgmtIntfID": {
                                "ipAddress": "192.168.1.1"
                            }
                        },
                        "ipIntfID": [
                            { "ipAddress": "192.168.1.1" }
                        ],
                        "macAddress": [ "00:11:22:33:44:55" ]
                    },
                    "lastUpdateTime": "2017-09-21T22:43:38.006Z",
                    "providers": [ "None" ],
                    "state": "Started",
                    "user": { "name": "root" }
                }

            The value for the event sent on disconnection of a session should
            look similar to the above, except with the "state" element set to
            "Disconnected", rather than "Started".
        """
        pass
