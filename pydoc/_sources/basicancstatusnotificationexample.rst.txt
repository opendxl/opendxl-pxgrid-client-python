Basic pxGrid ANC Status Notification Example
============================================

.. include:: <isonum.txt>

This sample registers and outputs messages received for Cisco Identity Services
Engine (ISE) ``ANC Status`` notifications via DXL and Cisco pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to receive
  ``DXL Cisco pxGrid Notifications`` (see :doc:`pxgridauth`).
* ``ANC Status Notifications`` from pxGrid have been enabled (see
  :doc:`pxgridnotifications`).

Running
*******

To run this sample execute the
``sample/basic/basic_anc_status_notification_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_status_notification_example.py

After the example starts up, the initial output should appear similar to the
following:

    .. parsed-literal::

        Waiting for anc status events...

To generate a status notification, navigate to Adaptive Network Control in ISE,
and create a new Endpoint Assignment.

Output would be similar to:

    .. code-block:: json

        {
            "command": "MESSAGE",
            "content": {
                "macAddress": "00:11:22:33:44:55",
                "operationId": "cise.psarchlab.com:144",
                "policyName": "ANC_Shut",
                "status": "SUCCESS"
            },
            "headers": {
                "content-length": "116",
                "destination": "/topic/com.cisco.ise.config.anc.status",
                "message-id": "112331",
                "subscription": "1"
            }
        }


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

            class MyAncNotificationCallback(AncStatusCallback):
                def _on_status_notification(self, apply_dict):
                    if 'content' in apply_dict:
                        content = apply_dict['content']
                        if isinstance(content, str):
                            try:
                                decoded_content = base64.b64decode(content).decode('utf-8')
                                apply_dict['content'] = json.loads(decoded_content)
                            except (TypeError, base64.binascii.Error) as e:
                                print(f"Error decoding content: {e}")
                        else:
                            print("Content is not a string, cannot decode.")
                    print("anc_status_notification\n" +
                        MessageUtils.dict_to_json(apply_dict, pretty_print=True) + '\n')

            # Attach callback for 'apply policy' events
            client.anc.add_anc_status_callback(
                MyAncNotificationCallback())


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the
:meth:`dxlciscopxgridclient.client.AncClientCategory.add_anc_status_callback`
method is invoked to register a callback for ANC status event notifications.

When an ANC status event occurs, the ``_on_status_notification`` method in the
``MyAncNotificationCallback`` class is invoked. The ``status_dict`` parameter
passed into the callback, a dictionary (``dict``) which contains the content of
the event notification, is displayed after having its content decoded from base64.
