import os
import sys
import time

from dxlbootstrap.util import MessageUtils
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxlciscopxgridclient.client import CiscoPxGridClient
from dxlciscopxgridclient.callbacks import \
    AncApplyEndpointPolicyCallback, AncClearEndpointPolicyCallback, \
    AncCreatePolicyCallback, AncUpdatePolicyCallback, AncDeletePolicyCallback

# Import common logging and configuration
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# Create the client
with DxlClient(config) as dxl_client:

    # Connect to the fabric
    dxl_client.connect()

    logger.info("Connected to DXL fabric.")

    # Create client wrapper
    client = CiscoPxGridClient(dxl_client)

    class MyAncApplyEndpointPolicyCallback(AncApplyEndpointPolicyCallback):
        def on_apply_endpoint_policy(self, apply_dict):
            print "on_apply_endpoint_policy\n" + \
                  MessageUtils.dict_to_json(apply_dict, pretty_print=True)

    class MyAncClearEndpointPolicyCallback(AncClearEndpointPolicyCallback):
        def on_clear_endpoint_policy(self, clear_dict):
            print "on_clear_endpoint_policy\n" + \
                  MessageUtils.dict_to_json(clear_dict, pretty_print=True)

    class MyAncCreatePolicyCallback(AncCreatePolicyCallback):
        def on_create_policy(self, create_dict):
            print "on_create_policy\n" + \
                  MessageUtils.dict_to_json(create_dict, pretty_print=True)

    class MyAncUpdatePolicyCallback(AncUpdatePolicyCallback):
        def on_update_policy(self, update_dict):
            print "on_update_policy\n" + \
                  MessageUtils.dict_to_json(update_dict, pretty_print=True)

    class MyAncDeletePolicyCallback(AncDeletePolicyCallback):
        def on_delete_policy(self, delete_dict):
            print "on_delete_policy\n" + \
                  MessageUtils.dict_to_json(delete_dict, pretty_print=True)

    #
    # Attach handlers
    #

    client.anc.add_apply_endpoint_policy_callback(MyAncApplyEndpointPolicyCallback())
    client.anc.add_clear_endpoint_policy_callback(MyAncClearEndpointPolicyCallback())
    client.anc.add_create_policy_callback(MyAncCreatePolicyCallback())
    client.anc.add_update_policy_callback(MyAncUpdatePolicyCallback())
    client.anc.add_delete_policy_callback(MyAncDeletePolicyCallback())

    #
    # client.anc.clear_endpoint_policy_by_ip
    #

    print '###: client.anc.clear_endpoint_policy_by_ip("10.84.200.48")'
    try:
        resp_dict = client.anc.clear_endpoint_policy_by_ip("10.84.200.48")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    #
    # client.anc.apply_endpoint_policy_by_ip
    #

    # print '###: client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "quarantine_policy")'
    # try:
    #     resp_dict = client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "quarantine_policy")
    #     print "Response:\n{0}".format(
    #         MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    # except Exception as ex:
    #     print str(ex)

    time.sleep(60 * 60)


