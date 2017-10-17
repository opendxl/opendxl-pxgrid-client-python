Basic Create ANC Policy Notification Example
============================================

.. include:: <isonum.txt>

This sample registers and outputs messages received for Cisco Adaptive
Network Control (ANC) ``create policy`` notifications via DXL and Cisco pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to receive
  ``DXL Cisco pxGrid Notifications`` (see :doc:`pxgridauth`).
* ANC ``Create Policy`` notifications from pxGrid have been enabled (see
  :doc:`pxgridnotifications`).

Running
*******

To run this sample execute the
``sample/basic/basic_anc_create_policy_notification_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_create_policy_notification_example.py

After the example starts up, the initial output should appear similar to the
following:

    .. parsed-literal::

        Waiting for create policy events...

To generate a ``create policy`` notification, create an ANC policy on the
Cisco Identity Services Engine (ISE) server. The policy could be created by
logging into the ISE web interface and performing the following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, click on the **Add** button.
    * On the **List** |rarr| **New** screen, enter ``quarantine_policy`` in the
      **name** field, select ``QUARANTINE`` in the **Action** field, and press
      the **Submit** button.

A message similar to the following should appear in the output of the
notification example:

    .. code-block:: json

        {
            "action": [
                "Quarantine"
            ],
            "name": "quarantine_policy"
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

            class MyAncCreatePolicyCallback(AncCreatePolicyCallback):
                def on_create_policy(self, create_dict):
                    print("on_create_policy\n" +
                          MessageUtils.dict_to_json(create_dict, pretty_print=True))

            # Attach callback for 'create policy' events
            client.anc.add_create_policy_callback(MyAncCreatePolicyCallback())

            # Wait forever
            print("Waiting for create policy events...")
            while True:
                time.sleep(60)


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the
:meth:`dxlciscopxgridclient.client.AncClientCategory.add_create_policy_callback`
method is invoked to register a callback for ``create policy`` event
notifications.

When a ``create policy`` event occurs, the ``on_create_policy`` method in the
``MyAncCreatePolicyCallback`` class is invoked. The ``create_dict`` parameter
passed into the callback, a dictionary (``dict``) which contains the content of
the event notification, is displayed.
