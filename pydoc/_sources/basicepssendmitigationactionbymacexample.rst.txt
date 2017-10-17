Basic Send EPS Mitigation Action by MAC Address Example
=======================================================

.. include:: <isonum.txt>

This sample sends a Cisco Endpoint Protection Service (EPS) mitigation action
for an endpoint via DXL and Cisco pxGrid. The sample identifies the endpoint by
its MAC address.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).

Configuration
*************

Update the following line in the sample:

    .. code-block:: python

        HOST_MAC = "<SPECIFY_MAC_ADDRESS>"

To specify the IP address of an endpoint for which to send the mitigation
action. For example:

    .. code-block:: python

        HOST_MAC = "00:11:22:33:44:55"

Running
*******

To run this sample execute the
``sample/basic/basic_eps_send_mitigation_action_by_mac_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_eps_send_mitigation_action_by_mac_example.py

If the action can be sent successfully, the output should appear similar to
the following:

    .. code-block:: json

        {
            "gid": "150",
            "macInterface": "00:11:22:33:44:55",
            "mitigationStatus": "complete"
        }

The received results are displayed.

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # MAC address of the endpoint for which to send the mitigation action
        HOST_MAC = "<SPECIFY_MAC_ADDRESS>"

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            # Invoke 'send mitigation action by MAC' method on service
            resp_dict = client.eps.send_mitigation_action_by_mac(
                HOST_MAC,
                EpsAction.QUARANTINE)

            # Print out the response (convert dictionary to JSON for pretty
            # printing)
            print("Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.EpsClientCategory.send_mitigation_action_by_mac`
method is invoked with the MAC address of the endpoint and a mitigation action,
:const:`dxlciscopxgridclient.constants.EpsAction.QUARANTINE`.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to send the mitigation action.
