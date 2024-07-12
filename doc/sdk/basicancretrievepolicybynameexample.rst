Basic Retrieve ANC Policy by Name Example
=========================================

.. include:: <isonum.txt>

This sample retrieves information for a named Cisco Adaptive Network
Control (ANC) policy via DXL and Cisco pxGrid.

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

Running
*******

To run this sample execute the
``sample/basic/basic_anc_retrieve_policy_by_name_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_retrieve_policy_by_name_example.py

If policy information can be retrieved successfully, the output should appear
similar to the following:

    .. code-block:: json

        {
            "actions": [
                "SHUT_DOWN"
            ],
            "name": "ANC_Shut"
        }

The received results are displayed.

If the ``ANC_Shut`` has not been defined before the example is run, output similar to the following should
appear:

    .. code-block:: json

        {
            "204": "no content"
        }

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

            try:
                # Invoke 'retrieve policy by name' method on service
                resp_dict = client.anc.retrieve_policy_by_name("ANC_Shut")

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                # An exception should be raised if the 'ANC_Shut' has not
                # already been created.
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.retrieve_policy_by_name`
method is invoked with the name of the policy for which to retrieve information.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to retrieve policy information.
