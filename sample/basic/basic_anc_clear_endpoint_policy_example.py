from __future__ import absolute_import
from __future__ import print_function
import os
import sys

from dxlbootstrap.util import MessageUtils
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxlciscopxgridclient.client import CiscoPxGridClient

# Import common logging and configuration
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# MAC address of the endpoint for which to clear the policy
HOST_MAC = "<INSERT_MAC_HERE>"
NAS_IP_ADDRESS = "<INSERT_IP_HERE>"

# Create the client
with DxlClient(config) as dxl_client:

    # Connect to the fabric
    dxl_client.connect()

    logger.info("Connected to DXL fabric.")

    # Create client wrapper
    client = CiscoPxGridClient(dxl_client)

    try:
        # Invoke 'clear endpoint policy by MAC' method on service
        resp_dict = client.anc.clear_endpoint_policy(HOST_MAC, NAS_IP_ADDRESS)

        # Print out the response (convert dictionary to JSON for pretty
        # printing)
        print("Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
    except Exception as ex:
        # An exception would be raised if a policy has not already been
        # associated with the endpoint.
        print(str(ex))
