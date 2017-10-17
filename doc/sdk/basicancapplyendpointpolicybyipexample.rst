Basic Apply ANC Endpoint Policy by IP Address Example
=====================================================

.. include:: <isonum.txt>

This sample applies a Cisco Adaptive Network Control (ANC) policy to an
endpoint via DXL and Cisco pxGrid. The sample identifies the endpoint by its IP
address.

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
* An ANC policy named ``quarantine_policy`` has been configured. The policy
  could be created by logging into the ISE web interface and performing the
  following steps:

    * Navigate to **Operations** |rarr| **Adaptive Network Control** |rarr|
      **Policy List**.
    * On the **List** screen, click on the **Add** button.
    * On the **List** |rarr| **New** screen, enter ``quarantine_policy`` in the
      **name** field, select ``QUARANTINE`` in the **Action** field, and press
      the **Submit** button.

Configuration
*************

Update the following line in the sample:

    .. code-block:: python

        HOST_IP = "<SPECIFY_IP_ADDRESS>"

To specify the IP address of an endpoint for which to apply the
``quarantine_policy``. For example:

    .. code-block:: python

        HOST_IP = "192.168.1.1"

Running
*******

To run this sample execute the
``sample/basic/basic_anc_apply_endpoint_policy_by_ip_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_apply_endpoint_policy_by_ip_example.py

If the policy can be applied successfully, the output should appear similar to
the following:

    .. code-block:: json

        {
            "ancStatus": "success"
        }

The received results are displayed.

If the ``quarantine_policy`` has already been associated with the endpoint
before the example is run, an ``Exception`` should be raised and output similar
to the following should appear:

    .. parsed-literal::

        Error: mac address is already associated with this policy error associated with ip 192.168.1.1 (0)

If the ``quarantine_policy`` has not been defined before the example is run, an
``Exception`` should be raised and output similar to the following should
appear:

    .. parsed-literal::

        Error: Policy is not configured error associated with ip 192.168.1.1 (0)

If no session has been established for an endpoint which corresponds to the IP
address, an ``Exception`` should be raised and output similar to the following
should appear:

    .. parsed-literal::

        Error: Session lookup failure error associated with ip 192.168.1.1 (0)

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # IP address of the endpoint for which to apply the policy
        HOST_IP = "<SPECIFY_IP_ADDRESS>"

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            try:
                # Invoke 'apply endpoint policy by IP' method on service
                resp_dict = client.anc.apply_endpoint_policy_by_ip(HOST_IP,
                                                                   "quarantine_policy")

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                # An exception should be raised if the 'quarantine_policy' has already
                # been applied to the endpoint, the 'quarantine_policy' has not been
                # created, or if no session has been established for the endpoint.
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to communicate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.apply_endpoint_policy_by_ip`
method is invoked with the IP address of the endpoint for which to apply the
``quarantine_policy``.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to apply the ``quarantine_policy``
to the endpoint.
