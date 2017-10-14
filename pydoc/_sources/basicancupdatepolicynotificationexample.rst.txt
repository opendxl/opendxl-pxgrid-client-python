Basic Update ANC Policy Notification Example
============================================

.. include:: <isonum.txt>

This sample registers and outputs messages received for Cisco Adaptive
Network Control (ANC) ``update policy`` notifications via DXL and Cisco pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to receive
  ``DXL Cisco pxGrid Notifications`` (see :doc:`pxgridauth`).
* ANC ``Update Policy`` notifications from pxGrid have been enabled (see
  :doc:`pxgridnotifications`).
* An ANC policy has been configured. The policy could be created by logging
  into the Cisco Identity Services Engine (ISE) web interface and performing
  the following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, click on the **Add** button.
    * On the **List** |rarr| **New** screen, enter ``test_policy`` in the
      **name** field, select ``QUARANTINE`` in the **Action** field, and press
      the **Submit** button.

Running
*******

To run this sample execute the
``sample/basic/basic_anc_update_policy_notification_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_update_policy_notification_example.py

After the example starts up, the initial output should appear similar to the
following:

    .. parsed-literal::

        Waiting for update policy events...

To generate an ``update policy`` notification, update an ANC policy on the
server. The policy could be updated by logging into the ISE web interface and
performing the following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, check the box next to the policy name -- for
      example: ``test_policy`` -- and press the **Edit** button.
    * On the **List** |rarr| **policy** screen, change the value in the
      **Action** field. For example, if the current value were ``QUARANTINE``,
      the value could be changed to ``PORT_BOUNCE``. Press the **Save**
      button to commit the change.

A message similar to the following should appear in the output of the
notification example:

    .. code-block:: json

        {
            "newPolicy": {
                "action": [
                    "PortBounce"
                ],
                "name": "test_policy"
            },
            "oldPolicy": {
                "action": [
                    "Quarantine"
                ],
                "name": "test_policy"
            }
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

            class MyAncUpdatePolicyCallback(AncUpdatePolicyCallback):
                def on_update_policy(self, update_dict):
                    print("on_update_policy\n" +
                          MessageUtils.dict_to_json(update_dict, pretty_print=True))

            # Attach callback for 'update policy' events
            client.anc.add_update_policy_callback(MyAncUpdatePolicyCallback())

            # Wait forever
            print("Waiting for update policy events...")
            while True:
                time.sleep(60)


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to integrate with Cisco pxGrid.

Next, the
:meth:`dxlciscopxgridclient.client.AncClientCategory.add_update_policy_callback`
method is invoked to register a callback for ``update policy`` event
notifications.

When an ``update policy`` event occurs, the ``on_update_policy`` method in the
``MyAncUpdatePolicyCallback`` class is invoked. The ``update_dict`` parameter
passed into the callback, a dictionary (``dict``) which contains the content of
the event notification, is displayed.
