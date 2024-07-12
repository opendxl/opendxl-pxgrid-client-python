Basic Create Policy Example
======================================================

This sample creates a Cisco Adaptive Network Control (ANC) policy.

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
``sample/basic/basic_anc_create_policy_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_create_policy_example.py

If the policy can be created successfully, the output should appear similar to
the following:

    .. code-block:: json

        {
            "actions": [
                "SHUT_DOWN"
            ],
            "name": "ANC_Shut_2"
        }

The received results are displayed.

If the policy already exists:

    .. parsed-literal::

        Error: 500 (0)

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
                # Invoke 'create policy'
                resp_dict = client.anc.create_policy("ANC_Shut_2",["SHUT_DOWN"])

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.create_policy`
method is invoked with the policy name and list of actions to perform.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the created policy.
