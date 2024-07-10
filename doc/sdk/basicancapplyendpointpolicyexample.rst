Basic Apply ANC Endpoint Policy Example
======================================================

.. include:: <isonum.txt>

This sample applies a Cisco Adaptive Network Control (ANC) policy to an
endpoint via DXL and Cisco pxGrid. The sample identifies the endpoint by its
MAC address, NAS IP address and other parameters.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).
* An ANC policy named ``ANC_Shut`` has been configured. The policy
  could be created by logging into the Cisco Identity Services Engine (ISE) web
  interface and performing the following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, click on the **Add** button.
    * On the **List** |rarr| **New** screen, enter ``ANC_Shut`` in the
      **name** field, select ``SHUT_DOWN`` in the **Action** field, and press
      the **Submit** button.

Configuration
*************

Update the following lines in the sample:

    .. code-block:: python

        MAC_ADDRESS = "<INSERT_MAC_HERE>"
        NAS_IP_ADDRESS = "<INSERT_NAS_IP_HERE>"
        SESSION_ID = "<INSERT_SESSIONID_HERE>"
        NAS_PORT_ID = None # "<OPTIONAL INSERT HERE>"
        IP_ADDRESS = None # "<OPTIONAL INSERT HERE>"
        USERNAME = None # "<OPTIONAL INSERT HERE>"

Note that the last 3 lines are optional parameters.

Running
*******

To run this sample execute the
``sample/basic/basic_anc_apply_endpoint_policy.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_apply_endpoint_policy.py

If the policy can be applied successfully, the output should appear similar to
the following:

    .. code-block:: json
      
        {
            "macAddress": "00:11:22:33:44:55",
            "operationId": "cise.psarchlab.com:149",
            "policyName": "ANC_Shut",
            "status": "SUCCESS"
        }

The received results are displayed.

If the ``ANC_Shut`` has already been associated with the endpoint
before the example is run, output similar to the
following should appear:

    .. parsed-literal::

        Error: mac address is already associated with this policy error associated with mac 00:11:22:33:44:55 (0)

If the ``ANC_Shut`` has not been defined before the example is run, output similar to the following should appear:

    .. parsed-literal::

        Error: Policy is not configured error associated with mac 00:11:22:33:44:55 (0)

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        MAC_ADDRESS = "<INSERT_MAC_HERE>"
        NAS_IP_ADDRESS = "<INSERT_NAS_IP_HERE>"
        SESSION_ID = "<INSERT_SESSIONID_HERE>"
        NAS_PORT_ID = "<OPTIONAL INSERT HERE>"
        IP_ADDRESS = "<OPTIONAL INSERT HERE>"
        USERNAME = "<OPTIONAL INSERT HERE>"

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            try:
                # Invoke 'retrieve policy by name' method on service
                resp_dict = client.anc.apply_endpoint_policy("ANC_Shut", MAC_ADDRESS, NAS_IP_ADDRESS, NAS_PORT_ID, IP_ADDRESS, USERNAME)

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.apply_endpoint_policy`
method is invoked with the endpoint information for which to apply the
``ANC_Shut``.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to apply the ``ANC_Shut``
to the endpoint.
