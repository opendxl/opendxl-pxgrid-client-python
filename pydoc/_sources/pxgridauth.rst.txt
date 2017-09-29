Authorize Client to Use Cisco pxGrid via DXL
============================================

By default, systems other than the McAfee ePolicy Orchestrator (ePO) server are
not allowed to access Cisco pxGrid over DXL. In order to allow the pxGrid
examples to work, the authorization restrictions for the "DXL Cisco pxGrid
Queries" (for the examples which send queries) and "DXL Cisco pxGrid
Notifications" (for the examples which receive notifications) topic groups
must be modified to include the Certificate Authority (CA) and/or certificate
used by the client executing the examples.

Please see the `Authorization Overview <https://opendxl.github.io/opendxl-client-python/pydoc/topicauthoverview.html>`_
section in the OpenDXL Python client documentation for more information on DXL
Topic Authorization.

The following steps walk through the process of allowing a DXL client to send
messages on the DXL Topics ``/mcafee/service/pxgrid/#`` which are
associated with the DXL Topic Authorization Group ``DXL Cisco pxGrid Queries``:

1. Navigate to **Server Settings** and select the **DXL Topic Authorization**
   setting on the left navigation bar.

    .. image:: enablepxgridauth1.png

2. Click the **Edit** button in the lower right corner (as shown in the image above)

    .. image:: enablepxgridauth2.png

3. Select the check box next to the DXL Topic Authorization Group
   ``DXL Cisco pxGrid Queries`` (as shown in the image above)

    .. image:: enablepxgridauth3.png

4. Click the **Actions** button and select **Restrict Send Certificates** to
   select certificates allowed to send messages to the topics associated with
   the ``DXL Cisco pxGrid Queries`` authorization group (as shown in the image
   above)

    .. image:: enablepxgridauth4.png

5. Select the check box next to any certificate to indicate that only DXL
   Clients with the selected certs or child certs (or tags separately
   specified) will be allowed to send DXL messages on topics associated with
   the ``DXL Cisco pxGrid Queries`` authorization group

    .. image:: enablepxgridauth5.png

6. Click the **OK** button in the lower right corner (as shown in the image above)

    .. image:: enablepxgridauth6.png

7. Click the **Save** button in the lower right corner (as shown in the image above)

    .. image:: enablepxgridauth7.png

The steps for enabling a DXL client to receive messages on the DXL Topics
``/mcafee/event/pxgrid/#`` are very similar to the steps above. The only
differences are:

* The ``DXL Cisco pxGrid Notifications`` group should be selected instead of
  the ``DXL Cisco pxGrid Queries`` group.
* The ``Restrict Receive Certificates`` action should be selected instead of
  the ``Restrict Send Certificates`` action.

.. image:: enablepxgridauth8.png

Once receive permission has been granted for the
``DXL Cisco pxGrid Notifications`` group and send permission has been granted
for the ``DXL Cisco pxGrid Queries`` group, a "Certificate" link should appear
for each cell (as shown in the image above).

The DXL Topic Authorization information will propagate to the DXL brokers. This
process can take several minutes to complete.
