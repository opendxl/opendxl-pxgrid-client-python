import os
import sys

from dxlbootstrap.util import MessageUtils
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxlciscopxgridclient.client import CiscoPxGridClient
from dxlciscopxgridclient.constants import EpsAction

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

    #
    # client.eps.get_mitigation_action_status_by_ip
    #

    print '###: client.eps.get_mitigation_action_status_by_ip("10.84.200.48")'
    try:
        resp_dict = client.eps.get_mitigation_action_status_by_ip("10.84.200.48")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.eps.send_mitigation_action_by_ip("10.84.200.48")'
    try:
        resp_dict = client.eps.send_mitigation_action_by_ip("10.84.200.48", EpsAction.QUARANTINE)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.eps.get_mitigation_action_status_by_mac("BA:BE:BA:BE:11:11")'
    try:
        resp_dict = client.eps.get_mitigation_action_status_by_mac("BA:BE:BA:BE:11:11")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.eps.send_mitigation_action_by_mac("BA:BE:BA:BE:11:11")'
    try:
        resp_dict = client.eps.send_mitigation_action_by_mac("BA:BE:BA:BE:11:11", EpsAction.QUARANTINE)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)




