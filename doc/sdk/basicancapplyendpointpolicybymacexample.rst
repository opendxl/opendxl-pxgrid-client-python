Basic Apply ANC Endpoint Policy by MAC Address Example
======================================================

.. include:: <isonum.txt>

This sample applies a Cisco Adaptive Network Control (ANC) policy to an
endpoint via DXL and Cisco pxGrid. The sample identifies the endpoint by its
MAC address.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The DXL fabric to which the client will connect has been bridged to Cisco
  pxGrid.
* The Python client has been authorized to perform ``DXL Cisco pxGrid Queries``
  (see :doc:`pxgridauth`).
* An ANC policy named ``quarantine_policy`` has been configured. The policy
  could be created by logging into the Cisco Identity Services Engine (ISE) web
  interface and performing the following steps:

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

        HOST_MAC = "<SPECIFY_MAC_ADDRESS>"

To specify the MAC address of an endpoint for which to apply the
``quarantine_policy``. For example:

    .. code-block:: python

        HOST_MAC = "00:11:22:33:44:55"

Running
*******

To run this sample execute the
``sample/basic/basic_anc_apply_endpoint_policy_by_mac_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_anc_apply_endpoint_policy_by_mac_example.py

If the policy can be applied successfully, the output should appear similar to
the following:

    .. code-block:: json

        {
            "ancStatus": "success"
        }

The received results are displayed.

If the ``quarantine_policy`` has already been associated with the endpoint
before the example is run, an ``Exception`` is raised and output similar to the
following should appear:

    .. parsed-literal::

        Error: mac address is already associated with this policy error associated with mac 00:11:22:33:44:55 (0)

If the ``quarantine_policy`` has not been defined before the example is run, an
``Exception`` is raised and output similar to the following should appear:

    .. parsed-literal::

        Error: Policy is not configured error associated with mac 00:11:22:33:44:55 (0)

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # MAC address of the endpoint for which to get information
        HOST_MAC = "<SPECIFY_MAC_ADDRESS>"

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = CiscoPxGridClient(dxl_client)

            try:
                # Invoke 'get endpoint by MAC' method on service
                resp_dict = client.anc.get_endpoint_by_mac(HOST_MAC)

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print("Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
            except Exception as ex:
                # An exception should be raised if a policy has not already been
                # associated with the endpoint.
                print(str(ex))


Once a connection is established to the DXL fabric, a
:class:`dxlciscopxgridclient.client.CiscoPxGridClient` instance is created which
will be used to integrate with Cisco pxGrid.

Next, the :meth:`dxlciscopxgridclient.client.AncClientCategory.apply_endpoint_policy_by_mac`
method is invoked with the MAC address of the endpoint for which to apply the
``quarantine_policy``.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to apply the ``quarantine_policy``
to the endpoint.
