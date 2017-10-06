Basic Clear ANC Endpoint Policy by IP Address Example
=====================================================

This sample clears a Cisco Adaptive Network Control (ANC) policy from an
endpoint via DXL and Cisco pxGrid. The sample identifies the endpoint by its IP
address.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).
* Run through the steps in the :doc:`basicancapplyendpointpolicybyipexample`
  to apply a policy to an endpoint. A run of this example can then clear the
  policy.

Configuration
*************

Update the following line in the sample:

    .. code-block:: python

        HOST_IP = "<SPECIFY_IP_ADDRESS>"

To specify the IP address of a endpoint for which to clear the policy. For
example:

    .. code-block:: python

        HOST_IP = "192.168.1.1"

Running
*******

To run this sample execute the
``sample/basic/basic_anc_clear_endpoint_policy_by_ip_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_clear_endpoint_policy_by_ip_example.py

If the policy can be cleared successfully, the output should appear similar to
the following:

    .. code-block:: json

        {
            "ancStatus": "success"
        }

The received results are displayed.

If no policy has already been associated with the endpoint before the example
is run, an ``Exception`` is raised and output similar to the following should
appear:

    .. parsed-literal::

        Error: mac address is already associated with this policy error associated with ip 192.168.1.1 (0)

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # IP address of the endpoint for which to clear the policy
        HOST_IP = "<SPECIFY_IP_ADDRESS>"

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            try:
                # Invoke 'clear endpoint policy by IP' method on service
                resp_dict = client.anc.clear_endpoint_policy_by_ip(HOST_IP)

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                # An exception should be raised if a policy has not already been
                # associated with the endpoint.
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to invoke remote commands via Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.clear_endpoint_policy_by_ip`
method is invoked with the IP address of the endpoint for which to clear the
policy.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to clear the policy from the endpoint.
