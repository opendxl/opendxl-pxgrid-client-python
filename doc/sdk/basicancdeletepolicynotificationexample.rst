Basic Delete ANC Policy Notification Example
============================================

.. include:: <isonum.txt>

This sample registers and outputs messages received for Cisco Adaptive
Network Control (ANC) ``delete policy`` notifications via DXL and Cisco pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to receive
  ``DXL Cisco pxGrid Notifications`` (see :doc:`pxgridauth`).
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
``sample/basic/basic_anc_delete_policy_notification_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_delete_policy_notification_example.py

After the example starts up, the initial output should appear similar to the
following:

    .. parsed-literal::

        Waiting for delete policy events...

To generate a ``delete policy`` notification, delete an ANC policy on the
server. The policy could be deleted by logging into the ISE web interface and
performing the following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, check the box next to the policy name -- for
      example: ``test_policy`` -- and press the **Trash** drop down.
    * Press the **Selected** item in the **Trash** drop down to delete the
      policy.

A message similar to the following should appear in the output of the
notification example:

    .. code-block:: json

        {
            "action": [
                "Quarantine"
            ],
            "name": "test_policy"
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

            class MyAncDeletePolicyCallback(AncDeletePolicyCallback):
                def on_delete_policy(self, delete_dict):
                    print("on_delete_policy\n" +
                          MessageUtils.dict_to_json(delete_dict, pretty_print=True))

            # Attach callback for 'delete policy' events
            client.anc.add_delete_policy_callback(MyAncDeletePolicyCallback())

            # Wait forever
            print("Waiting for delete policy events...")
            while True:
                time.sleep(60)


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to invoke remote commands via Cisco pxGrid.

Next, the
:meth:`dxlciscopxgridclient.client.AncClientCategory.add_delete_policy_callback`
method is invoked to register a callback for ``delete policy`` event
notifications.

When an ``delete policy`` event occurs, the ``on_delete_policy`` method in the
``MyAncDeletePolicyCallback`` class is invoked. The ``delete_dict`` parameter
passed into the callback, a dictionary (``dict``) which contains the content of
the event notification, is displayed.
