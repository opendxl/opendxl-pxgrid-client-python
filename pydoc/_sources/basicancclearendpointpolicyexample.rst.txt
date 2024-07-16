Basic Clear ANC Endpoint Policy Example
======================================================

This sample clears a Cisco Adaptive Network Control (ANC) policy from an
endpoint via DXL and Cisco pxGrid. The sample identifies the endpoint by its
MAC address and NAS IP address.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).
* Run through the steps in the :doc:`basicancapplyendpointpolicyexample`
  to apply a policy to an endpoint. A run of this example can then clear the
  policy.

Configuration
*************

Update the following line in the sample:

    .. code-block:: python

        HOST_MAC = "<SPECIFY_MAC_ADDRESS>"
        NAS_IP_ADDRESS = "<SPECIFY_NASIP_ADDRESS>"

To specify the MAC address and NAS IP addresss of an endpoint for which to clear the policy. For
example:

    .. code-block:: python

        HOST_MAC = "00:11:22:33:44:55"
        NAS_IP_ADDRESS = "192.168.1.1"

Running
*******

To run this sample execute the
``sample/basic/basic_anc_clear_endpoint_policy_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_clear_endpoint_policy_example.py

If the policy can be cleared successfully, the output should appear similar to
the following:

    .. code-block:: json

        {
            "ancStatus": "success"
        }

The received results are displayed.

If no policy has been associated with the endpoint before the example is run, output similar to the following should appear:

    .. parsed-literal::

        Error: mac address is not associated with a policy error associated with mac 00:11:22:33:44:55 (0)

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # MAC and NAS IP address of the endpoint for which to clear the policy
        HOST_MAC = "<SPECIFY_MAC_ADDRESS>"
        NAS_IP_ADDRESS = "<SPECIFY_NASIP_HERE>"

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
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.clear_endpoint_policy`
method is invoked with the MAC address and NAS IP address of the endpoint for which to clear the
policy.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to clear the policy from the endpoint.
