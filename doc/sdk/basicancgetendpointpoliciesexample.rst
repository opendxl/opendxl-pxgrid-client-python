Basic Get ANC Endpoint Policies
============================================

.. include:: <isonum.txt>

This is used to get endpoints with policies applied using both MAC address and NAS IP address.
An empty json structure must be sent as the request. If no endpoint policy is found, endpoints will have an empty array.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).

Running
*******

To run this sample execute the
``sample/basic/basic_anc_get_endpoint_policies_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_get_endpoint_policies_example.py

If information can be retrieved successfully for the endpoint, the output
should appear similar to the following:

    .. code-block:: json

        {
            "endpoints": []
        }

where the `endpoints` list is empty if no endpoints have policies.

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            try:
                # Invoke 'get endpoint policies'
                resp_dict = client.anc.get_endpoint_policies()

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.get_endpoint_policies`
method.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to retrieve the endpoints.
