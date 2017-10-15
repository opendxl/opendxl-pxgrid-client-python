Basic Get ANC Endpoint by IP Address Example
============================================

.. include:: <isonum.txt>

This sample gets information for a Cisco Adaptive Network Control (ANC)
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
  to apply a policy to an endpoint. A run of this example can then get policy
  information for the endpoint.

Configuration
*************

Update the following line in the sample:

    .. code-block:: python

        HOST_IP = "<SPECIFY_IP_ADDRESS>"

To specify the IP address of an endpoint for which to get information. For
example:

    .. code-block:: python

        HOST_IP = "192.168.1.1"

Running
*******

To run this sample execute the
``sample/basic/basic_anc_get_endpoint_by_ip_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_get_endpoint_by_ip_example.py

If information can be retrieved successfully for the endpoint, the output
should appear similar to the following:

    .. code-block:: json

        {
            "ancEndpoint": [
                {
                    "macAddress": "00:11:22:33:44:55",
                    "policyName": "quarantine_policy"
                }
            ],
            "ancStatus": "success"
        }

The received results are displayed.

If no policy has already been associated with the endpoint but an active
session exists for the endpoint before the example is run, an ``Exception``
should be raised and output similar to the following should appear:

    .. parsed-literal::

        Error: No policy applied to specified IP (0)

If no session has been established for an endpoint which corresponds to the IP
address, an ``Exception`` should be raised and output similar to the following
should appear:

    .. parsed-literal::

        Error: No active session found for this IP address (0)

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # IP address of the endpoint for which to get information
        HOST_IP = "<SPECIFY_IP_ADDRESS>"

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            try:
                # Invoke 'get endpoint by IP' method on service
                resp_dict = client.anc.get_endpoint_by_ip(HOST_IP)

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
will be used to integrate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.get_endpoint_by_ip`
method is invoked with the IP address of the endpoint for which to retrieve
information.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to retrieve the endpoint information.
