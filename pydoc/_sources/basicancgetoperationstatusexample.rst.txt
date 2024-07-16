Basic Get ANC Operation Status
============================================

.. include:: <isonum.txt>

This sample gets the status of a Cisco Adaptive Network Control (ANC) operation.

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
``sample/basic/basic_anc_get_operation_status.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_get_operation_status.py

If information can be retrieved successfully for the operation, the output
should appear similar to the following:

    .. code-block::
    
        {
          status object
        }

Otherwise, this will be the result indicating that the operating with the corresponding ID was not found:

  .. code-block:: json
    
        {
            "204": "no content"
        }

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            print("Connected to DXL fabric.", flush=True)

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            # Invoke 'get operation status'
            resp_dict = client.anc.get_operation_status("1")

            # Print out the response (convert dictionary to JSON for pretty
            # printing)
            print("Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.get_operation_status`
method.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to retrieve the operation status.
