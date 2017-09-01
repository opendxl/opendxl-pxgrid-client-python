from dxlbootstrap.util import MessageUtils
from dxlclient.callbacks import EventCallback


class AncApplyEndpointPolicyCallback(EventCallback):

    def on_event(self, event):
        self.on_apply_endpoint_policy(MessageUtils.json_payload_to_dict(event))

    def on_apply_endpoint_policy(self, apply_dict):
        pass


class AncClearEndpointPolicyCallback(EventCallback):

    def on_event(self, event):
        self.on_clear_endpoint_policy(MessageUtils.json_payload_to_dict(event))

    def on_clear_endpoint_policy(self, clear_dict):
        pass


class AncCreatePolicyCallback(EventCallback):

    def on_event(self, event):
        self.on_create_policy(MessageUtils.json_payload_to_dict(event))

    def on_create_policy(self, create_dict):
        pass


class AncUpdatePolicyCallback(EventCallback):

    def on_event(self, event):
        self.on_update_policy(MessageUtils.json_payload_to_dict(event))

    def on_update_policy(self, update_dict):
        pass


class AncDeletePolicyCallback(EventCallback):

    def on_event(self, event):
        self.on_delete_policy(MessageUtils.json_payload_to_dict(event))

    def on_delete_policy(self, delete_dict):
        pass


class IdentitySessionCallback(EventCallback):

    def on_event(self, event):
        self.on_session(MessageUtils.json_payload_to_dict(event))

    def on_session(self, session_dict):
        pass
