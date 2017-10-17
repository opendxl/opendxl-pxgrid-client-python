Basic Retrieve All ANC Policies Example
=======================================

.. include:: <isonum.txt>

This sample retrieves information for all Cisco Adaptive Network Control (ANC)
policies via DXL and Cisco pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).
* One or more ANC policies have been configured. The policies could be created
  by logging into the Cisco Identity Services Engine (ISE) web interface and
  performing the following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, click on the **Add** button.
    * On the **List** |rarr| **New** screen, enter ``quarantine_policy`` in the
      **name** field, select ``QUARANTINE`` in the **Action** field, and press
      the **Submit** button.
    * Back on the **List** screen, click on the **Add** button again.
    * On the **List** |rarr| **New** screen, enter ``shutdown_policy`` in the
      **name** field, select ``SHUT_DOWN`` in the **Action** field, and press
      the **Submit** button.

Running
*******

To run this sample execute the
``sample/basic/basic_anc_retrieve_all_policies_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_retrieve_all_policies_example.py

If policy information can be retrieved successfully, the output should appear
similar to the following:

    .. code-block:: json

        {
            "ancStatus": "success",
            "ancpolicy": [
                {
                    "action": [
                        "ShutDown"
                    ],
                    "name": "shutdown_policy"
                },
                {
                    "action": [
                        "Quarantine"
                    ],
                    "name": "quarantine_policy"
                }
            ]
        }

The received results are displayed.

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            # Invoke 'retrieve all policies' method on service
            resp_dict = client.anc.retrieve_all_policies()

            # Print out the response (convert dictionary to JSON for pretty
            # printing)
            print("Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.retrieve_all_policies`
method is invoked.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to retrieve policy information.
