Basic Get ANC Endpoints
============================================

.. include:: <isonum.txt>

This sample gets all endpoints with a Cisco Adaptive Network Control (ANC) policy applied to them.

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
``sample/basic/basic_anc_get_endpoints_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_get_endpoints_example.py

If information can be retrieved successfully for the endpoint, the output
should appear similar to the following:

    .. code-block:: json

        {
            "endpoints": [
                {
                    "macAddress": "00:11:22:33:44:55",
                    "policyName": "ANC_Shut"
                }                
            ]
        }

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
                # Invoke 'get endpoints'
                resp_dict = client.anc.get_endpoints()

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.get_endpoints`
method.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to retrieve the endpoints.