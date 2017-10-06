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
from dxlciscopxgridclient.callbacks import AncDeletePolicyCallback

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

    class MyAncDeletePolicyCallback(AncDeletePolicyCallback):
        def on_delete_policy(self, delete_dict):
            print("on_delete_policy\n" +
                  MessageUtils.dict_to_json(delete_dict, pretty_print=True))

    # Attach callback for 'delete policy' events
    client.anc.add_delete_policy_callback(MyAncDeletePolicyCallback())

    # Wait forever
    print("Waiting for delete policy events...")
    while True:
        time.sleep(60)
