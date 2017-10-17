Basic pxGrid Session Notification Example
=========================================

.. include:: <isonum.txt>

This sample registers and outputs messages received for Cisco Identity Services
Engine (ISE) ``session`` notifications via DXL and Cisco pxGrid.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to receive
  ``DXL Cisco pxGrid Notifications`` (see :doc:`pxgridauth`).
* ``Session Notifications`` from pxGrid have been enabled (see
  :doc:`pxgridnotifications`).

Running
*******

To run this sample execute the
``sample/basic/basic_identity_session_notification_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_identity_session_notification_example.py

After the example starts up, the initial output should appear similar to the
following:

    .. parsed-literal::

        Waiting for session events...

To generate a session notification, create a session for an endpoint on the
Cisco Identity Services Engine (ISE) server. If you do not have access to an
IEEE 802.1x environment, you can use the Cisco RADIUS Simulator (see the
`pxGrid ISE testing guide <https://developer.cisco.com/site/pxgrid/documents/config-and-test/ise-2-0/#radius-simulator-1755>`_
for more details).

For example, you could run the following RADIUS simulator commands in a separate
terminal command window to startup a new session for a simulated endpoint:

    .. parsed-literal::

        java -cp RadiusSimulator.jar -DUSERNAME=iseuser -DPASSWORD=isepass -DFRAMED_IP_ADDRESS=192.168.1.1 -DFRAMED_IP_MASK=255.255.255.0 -DCALLING_STATION_ID=00:11:22:33:44:55 -DAUDIT_SESSION_ID=1234 RadiusAuthentication 192.168.1.2
        java -cp RadiusSimulator.jar -DUSERNAME=iseuser -DPASSWORD=isepass -DFRAMED_IP_ADDRESS=192.168.1.1 -DFRAMED_IP_MASK=255.255.255.0 -DCALLING_STATION_ID=00:11:22:33:44:55 -DAUDIT_SESSION_ID=1234 RadiusAccountingStart 192.168.1.2

These commands would establish a session for the endpoint ``192.168.1.1`` on
the ISE server ``192.168.1.2``.

A message similar to the following should appear in the output of the
notification example after the session has been started:

    .. code-block:: json

        {
            "IdentitySourceFirstPort": "0",
            "IdentitySourcePortEnd": "0",
            "IdentitySourcePortStart": "0",
            "MDMEndpoint": {},
            "RADIUSAttrs": [
                {
                    "attrName": "Acct-Session-Id",
                    "attrValue": "123"
                }
            ],
            "assessedPostureEvent": [
                {}
            ],
            "attribute": [
                {
                    "name": "Authorization_Profiles",
                    "type": "string",
                    "value": "1234"
                }
            ],
            "endpointCheckResult": "none",
            "endpointProfile": "Microsoft-Device",
            "gid": "24703",
            "interface": {
                "deviceAttachPt": {
                    "deviceMgmtIntfID": {
                        "ipAddress": "192.168.1.1"
                    }
                },
                "ipIntfID": [
                    {
                        "ipAddress": "192.168.1.1"
                    }
                ],
                "macAddress": [
                    "00:11:22:33:44:55"
                ]
            },
            "lastUpdateTime": "2017-09-21T22:43:38.006Z",
            "providers": [
                "None"
            ],
            "state": "Started",
            "user": {
                "name": "root"
            }
        }

You could run the following RADIUS simulator command in a separate terminal
command window to disconnect the simulated endpoint's session:

    .. parsed-literal::

        java -cp RadiusSimulator.jar -DUSERNAME=iseuser -DPASSWORD=isepass -DFRAMED_IP_ADDRESS=192.168.1.1 -DFRAMED_IP_MASK=255.255.255.0 -DCALLING_STATION_ID=00:11:22:33:44:55 -DAUDIT_SESSION_ID=1234 RadiusAccountingStop 192.168.1.2

A message similar to the following should appear in the output of the
notification example after the session has been disconnected:

    .. code-block:: json

        {
            "IdentitySourceFirstPort": "0",
            "IdentitySourcePortEnd": "0",
            "IdentitySourcePortStart": "0",
            "MDMEndpoint": {},
            "RADIUSAttrs": [
                {
                    "attrName": "Acct-Session-Id",
                    "attrValue": "123"
                }
            ],
            "assessedPostureEvent": [
                {}
            ],
            "attribute": [
                {
                    "name": "Authorization_Profiles",
                    "type": "string",
                    "value": "1234"
                }
            ],
            "endpointCheckResult": "none",
            "endpointProfile": "Microsoft-Device",
            "gid": "24703",
            "interface": {
                "deviceAttachPt": {
                    "deviceMgmtIntfID": {
                        "ipAddress": "192.168.1.1"
                    }
                },
                "ipIntfID": [
                    {
                        "ipAddress": "192.168.1.1"
                    }
                ],
                "macAddress": [
                    "00:11:22:33:44:55"
                ]
            },
            "lastUpdateTime": "2017-09-21T22:43:44.833Z",
            "providers": [
                "None"
            ],
            "state": "Disconnected",
            "user": {
                "name": "root"
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

            class MyIdentitySessionCallback(IdentitySessionCallback):
                def on_session(self, session_dict):
                    print("on_session\n" +
                          MessageUtils.dict_to_json(session_dict, pretty_print=True))

            # Attach callback for session events
            client.identity.add_session_callback(MyIdentitySessionCallback())

            # Wait forever
            print("Waiting for session events...")
            while True:
                time.sleep(60)


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the
:meth:`dxlciscopxgridclient.client.IdentityClientCategory.add_session_callback`
method is invoked to register a callback for session event notifications.

When a session event occurs, the ``on_session`` method in the
``MyIdentitySessionCallback`` class is invoked. The ``session_dict`` parameter
passed into the callback, a dictionary (``dict``) which contains the content of
the event notification, is displayed.
