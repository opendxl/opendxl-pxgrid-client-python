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

# Create the client
with DxlClient(config) as dxl_client:

    # Connect to the fabric
    dxl_client.connect()

    logger.info("Connected to DXL fabric.")

    # Create client wrapper
    client = CiscoPxGridClient(dxl_client)

    #
    # client.anc.get_endpoint_by_ip
    #

    print '###: client.anc.get_endpoint_by_ip("10.84.200.48")'
    try:
        resp_dict = client.anc.get_endpoint_by_ip("10.84.200.48")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.get_endpoint_by_ip("10.84.200.foo")'
    try:
        resp_dict = client.anc.get_endpoint_by_ip("10.84.200.foo")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.get_endpoint_by_ip(None)'
    try:
        resp_dict = client.anc.get_endpoint_by_ip(None)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    #
    # client.anc.get_endpoint_by_mac
    #

    print '###: client.anc.get_endpoint_by_mac("BA:BE:BA:BE:11:11")'
    try:
        resp_dict = client.anc.get_endpoint_by_mac("BA:BE:BA:BE:11:11")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.get_endpoint_by_mac("sdfsdf")'
    try:
        resp_dict = client.anc.get_endpoint_by_mac("sdfsdf")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.get_endpoint_by_mac(None)'
    try:
        resp_dict = client.anc.get_endpoint_by_mac(None)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    #
    # client.anc.retrieve_all_policies
    #

    print '###: client.anc.retrieve_all_policies()'
    try:
        resp_dict = client.anc.retrieve_all_policies()
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    #
    # client.anc.retrieve_policy_by_name
    #

    print '###: client.anc.retrieve_policy_by_name("quarantine_policy")'
    try:
        resp_dict = client.anc.retrieve_policy_by_name("quarantine_policy")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.retrieve_policy_by_name("sdfsdf")'
    try:
        resp_dict = client.anc.retrieve_policy_by_name("sdfsdf")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.retrieve_policy_by_name(None)'
    try:
        resp_dict = client.anc.retrieve_policy_by_name(None)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

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

    print '###: client.anc.clear_endpoint_policy_by_ip("sdfsdfsdf")'
    try:
        resp_dict = client.anc.clear_endpoint_policy_by_ip("sdfsdfsdf")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.clear_endpoint_policy_by_ip(None)'
    try:
        resp_dict = client.anc.clear_endpoint_policy_by_ip(None)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    #
    # client.anc.apply_endpoint_policy_by_ip
    #

    print '###: client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "quarantine_policy")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "quarantine_policy")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "quarantine_policy")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "quarantine_policy")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "sdfsdf")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_ip("10.84.200.48", "sdfsdf")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_ip(None, None)'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_ip(None, None)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_ip(None, "quarantine_policy")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_ip(None, "quarantine_policy")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    #
    # client.anc.clear_endpoint_policy_by_mac
    #

    print '###: client.anc.clear_endpoint_policy_by_mac("BA:BE:BA:BE:11:11")'
    try:
        resp_dict = client.anc.clear_endpoint_policy_by_mac("BA:BE:BA:BE:11:11")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.clear_endpoint_policy_by_mac("sdfsdfsdf")'
    try:
        resp_dict = client.anc.clear_endpoint_policy_by_mac("sdfsdfsdf")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.clear_endpoint_policy_by_mac(None)'
    try:
        resp_dict = client.anc.clear_endpoint_policy_by_mac(None)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    #
    # client.anc.apply_endpoint_policy_by_mac
    #

    print '###: client.anc.apply_endpoint_policy_by_mac("BA:BE:BA:BE:11:11", "quarantine_policy")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_mac("BA:BE:BA:BE:11:11", "quarantine_policy")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_mac("BA:BE:BA:BE:11:11", "quarantine_policy")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_mac("BA:BE:BA:BE:11:11", "quarantine_policy")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_mac("BA:BE:BA:BE:11:12", "sdfsdf")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_mac("BA:BE:BA:BE:11:12", "sdfsdf")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_mac(None, None)'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_mac(None, None)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

    print '###: client.anc.apply_endpoint_policy_by_mac(None, "quarantine_policy")'
    try:
        resp_dict = client.anc.apply_endpoint_policy_by_mac(None, "quarantine_policy")
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))
    except Exception as ex:
        print str(ex)

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


