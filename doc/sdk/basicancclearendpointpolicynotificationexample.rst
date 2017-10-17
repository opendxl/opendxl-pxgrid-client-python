Basic Clear ANC Endpoint Policy Notification Example
====================================================

.. include:: <isonum.txt>

This sample registers and outputs messages received for Cisco Adaptive
Network Control (ANC) ``clear endpoint policy`` notifications via DXL and Cisco
pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to receive
  ``DXL Cisco pxGrid Notifications`` (see :doc:`pxgridauth`).
* ANC ``Clear Endpoint Policy`` notifications from pxGrid have been enabled
  (see :doc:`pxgridnotifications`).

Running
*******

To run this sample execute the
``sample/basic/basic_anc_clear_endpoint_policy_notification_example.py`` script
as follows:

    .. parsed-literal::

        python sample/basic/basic_anc_clear_endpoint_policy_notification_example.py

After the example starts up, the initial output should appear similar to the
following:

    .. parsed-literal::

        Waiting for clear policy events...

To generate a ``clear endpoint policy by IP address`` notification, run through
the steps in the :doc:`basicancclearendpointpolicybyipexample` in a separate
terminal command window. Assuming that a policy is successfully cleared, the following
message should appear in the output of the notification example:

    .. code-block:: json

        {
            "ipAddress": "192.168.1.1"
        }

To generate a ``clear endpoint policy by MAC address`` notification, run
through the steps in the :doc:`basicancclearendpointpolicybymacexample` in a
separate terminal command window. Assuming that a policy is successfully cleared, the
following message should appear in the output of the notification example:

    .. code-block:: json

        {
            "macAddress": "00:11:22:33:44:55"
        }

Note that if the ``clear endpoint policy`` calls encounter any errors -- for
example, due to no policy already having been applied -- no corresponding event
notification will be generated.

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

            class MyAncClearEndpointPolicyCallback(AncClearEndpointPolicyCallback):
                def on_clear_endpoint_policy(self, clear_dict):
                    print("on_clear_endpoint_policy\n" +
                          MessageUtils.dict_to_json(clear_dict, pretty_print=True))

            # Attach callback for 'clear policy' events
            client.anc.add_clear_endpoint_policy_callback(
                MyAncClearEndpointPolicyCallback())

            # Wait forever
            print("Waiting for clear policy events...")
            while True:
                time.sleep(60)


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.add_clear_endpoint_policy_callback`
method is invoked to register a callback for clear policy event notifications.

When a ``clear endpoint policy`` event occurs, the ``on_clear_endpoint_policy``
method in the ``MyAncClearEndpointPolicyCallback`` class is invoked. The
``clear_dict`` parameter passed into the callback, a dictionary (``dict``)
which contains the content of the event notification, is displayed.
