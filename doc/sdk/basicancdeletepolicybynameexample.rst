Basic Delete Policy By Name Example
======================================================

This sample creates a Cisco Adaptive Network Control (ANC) policy.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).
* A policy has been created and is to be deleted (see :doc:`basicanccreatepolicyexample`)

Running
*******

To run this sample execute the
``sample/basic/basic_anc_delete_policy_by_name.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_delete_policy_by_name.py

Output if the delete was successful should be:

    .. code-block:: json

        {
            "200": "no content"
        }

Otherwise:

    .. code-block:: json

        {
            "204": "no content"
        }

which indicates that the policy was not found and therefore not deleted.

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
                # Invoke 'delete policy by name' method on service
                resp_dict = client.anc.delete_policy_by_name("ANC_Shut_2")

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.delete_policy_by_name`
method is invoked with the MAC address of the endpoint for which to clear the
policy.

The final step is to display the contents of the returned dictionary (``dict``)
which contains 204 - no content.
