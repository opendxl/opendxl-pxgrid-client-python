from __future__ import absolute_import
import base64
import json
from dxlbootstrap.util import MessageUtils
from dxlclient.callbacks import EventCallback

class CallbackHelper:
    @staticmethod
    def append_base64_decoded_content(event_dict):
        if 'content' in event_dict:
            content = event_dict['content']
            event_dict['content_base64'] = content
            if isinstance(content, str):
                try:
                    decoded_content = base64.b64decode(content).decode('utf-8')
                    event_dict['content'] = json.loads(decoded_content)
                except (TypeError, base64.binascii.Error):
                    pass
        return event_dict

class AncStatusCallback(EventCallback):
    """
    Callback wrapper which is invoked on all ANC notifications
    """
    def on_event(self, event):
        """
        Method invoked when a status notification event occurs. Derived classes can
        implement the :meth:`on_session_notification` method instead of this method in order
        to process the event payload as a `dict`.

        :param dxlclient.message.Event event: Message received for the event
            notification
        """
        event_dict = MessageUtils.json_payload_to_dict(event)
        self._on_status_notification(CallbackHelper.append_base64_decoded_content(event_dict))

    def _on_status_notification(self, status_dict):
        """
        Method invoked when a status notification event occurs.

        :param dict status_dict: Payload for the event notification.
            Example status_dict look similar to this:

            {
                "command": "MESSAGE",
                "content" : {
                    "operationId":"cise.psarchlab.com:219",
                    "macAddress":"02:B5:47:E2:0E:73",
                    "status":"SUCCESS"
                },
                "content_base64": "eyJvcGVyYXRpb25JZCI6ImNpc2UucHNhcmNobGFiLmNvbToxMDYiLCJtYW\
                            NBZGRyZXNzIjoiMDI6QjU6NDc6RTI6MEU6NzMiLCJzdGF0dXMiOiJTVUNDR\
                            VNTIiwicG9saWN5TmFtZSI6IkFOQ19TaHV0In0=",
                "headers": {
                    "content-length": "116",
                    "destination": "/topic/com.cisco.ise.config.anc.status",
                    "message-id": "106527",
                    "subscription": "1"
                }
            }

            where the content is the base64 encoded content of the event. The content
            after being decoded and json.loads()-ed will be similar to this format:

            {
                "macAddress": "00:11:22:33:44:55",
                "operationId": "cise.psarchlab.com:104",
                "policyName": "ANC_Shut",
                "status": "SUCCESS"
            }

            PolicyName is not required for all events and just a status and endpoint
            identifier can be present.
            https://github.com/cisco-pxgrid/pxgrid-rest-ws/wiki/ANC-configuration#objects
            for more information

        See the example _on_status_notification() handler in
        basic_anc_status_notification_example.py
        for a simple handler that decodes and json.loads().
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
        event_dict = MessageUtils.json_payload_to_dict(event)
        self.on_session(CallbackHelper.append_base64_decoded_content(event_dict))

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
