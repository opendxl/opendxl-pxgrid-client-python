Basic Apply ANC Endpoint Policy Notification Example
====================================================

.. include:: <isonum.txt>

This sample registers and outputs messages received for Cisco Adaptive
Network Control (ANC) ``apply endpoint policy`` notifications via DXL and Cisco
pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to receive
  ``DXL Cisco pxGrid Notifications`` (see :doc:`pxgridauth`).
* ANC ``Apply Endpoint Policy`` notifications from pxGrid have been enabled
  (see :doc:`pxgridnotifications`).
* An ANC policy named ``quarantine_policy`` has been configured.  The policy
  could be created by logging into the Cisco Identity Services Engine (ISE) web
  interface and performing the following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, click on the **Add** button.
    * On the **List** |rarr| **New** screen, enter ``quarantine_policy`` in the
      **name** field, select ``QUARANTINE`` in the **Action** field, and press
      the **Submit** button.

Running
*******

To run this sample execute the
``sample/basic/basic_anc_apply_endpoint_policy_notification_example.py`` script
as follows:

    .. parsed-literal::

        python sample/basic/basic_anc_apply_endpoint_policy_notification_example.py

After the example starts up, the initial output should appear similar to the
following:

    .. parsed-literal::

        Waiting for apply policy events...

To generate an ``apply endpoint policy by IP address`` notification, run
through the steps in the :doc:`basicancapplyendpointpolicybyipexample` in a
separate terminal command window. Assuming that the policy is successfully
applied, the following message should appear in the output of the notification
example:

    .. code-block:: json

        {
            "ipAddress": "192.168.1.1",
            "policyName": "quarantine_policy"
        }

To generate an ``apply endpoint policy by MAC address`` notification, run
through the steps in the :doc:`basicancapplyendpointpolicybymacexample` in a
separate terminal command window. Assuming that the policy is successfully applied, the
following message should appear in the output of the notification example:

    .. code-block:: json

        {
            "macAddress": "00:11:22:33:44:55",
            "policyName": "quarantine_policy"
        }

Note that if the ``apply endpoint policy`` calls encounter any errors -- for
example, due to the policy not existing or the policy already having been
applied -- no corresponding event notification will be generated.

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

            class MyAncApplyEndpointPolicyCallback(AncApplyEndpointPolicyCallback):
                def on_apply_endpoint_policy(self, apply_dict):
                    print("on_apply_endpoint_policy\n" +
                          MessageUtils.dict_to_json(apply_dict, pretty_print=True))

            # Attach callback for 'apply policy' events
            client.anc.add_apply_endpoint_policy_callback(
                MyAncApplyEndpointPolicyCallback())

            # Wait forever
            print("Waiting for apply policy events...")
            while True:
                time.sleep(60)


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to integrate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.add_apply_endpoint_policy_callback`
method is invoked to register a callback for apply policy event notifications.

When an ``apply endpoint policy`` event occurs, the ``on_apply_endpoint_policy``
method in the ``MyAncApplyEndpointPolicyCallback`` class is invoked. The
``apply_dict`` parameter passed into the callback, a dictionary (``dict``)
which contains the content of the event notification, is displayed.
