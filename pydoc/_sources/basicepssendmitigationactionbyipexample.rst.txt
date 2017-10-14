Basic Send EPS Mitigation Action by IP Address Example
======================================================

.. include:: <isonum.txt>

This sample sends a Cisco Endpoint Protection Service (EPS) mitigation action
for an endpoint via DXL and Cisco pxGrid. The sample identifies the endpoint by
its IP address.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).
* A session has been established with the Cisco Identity Services Engine (ISE)
  server for an endpoint. The endpoint's IP address will be used when running
  this example. For an example on creating a simulated session for testing, see
  the Cisco RADIUS Simulator command examples in
  :doc:`basicidentitysessionnotificationexample`.

Configuration
*************

Update the following line in the sample:

    .. code-block:: python

        HOST_IP = "<SPECIFY_IP_ADDRESS>"

To specify the IP address of an endpoint for which to send the mitigation
action. For example:

    .. code-block:: python

        HOST_IP = "192.168.1.1"

Running
*******

To run this sample execute the
``sample/basic/basic_eps_send_mitigation_action_by_ip_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_eps_send_mitigation_action_by_ip_example.py

If the action can be sent successfully, the output should appear similar to
the following:

    .. code-block:: json

        {
            "gid": "150",
            "macInterface": "00:11:22:33:44:55",
            "mitigationStatus": "complete"
        }

The received results are displayed.

If no session has been established for an endpoint which corresponds to the IP
address, an ``Exception`` should be raised and output similar to the following
should appear:

    .. parsed-literal::

        Error: Session lookup failure (0)

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # IP address of the endpoint for which to send the mitigation action
        HOST_IP = "<SPECIFY_IP_ADDRESS>"

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            try:
                # Invoke 'send mitigation action by IP' method on service
                resp_dict = client.eps.send_mitigation_action_by_ip(
                    HOST_IP,
                    EpsAction.QUARANTINE)

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                # An exception should be raised if no session exists for the endpoint.
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to integrate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.EpsClientCategory.send_mitigation_action_by_ip`
method is invoked with the IP address of the endpoint and a mitigation action,
:const:`dxlciscopxgridclient.constants.EpsAction.QUARANTINE`.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to send the mitigation action.
