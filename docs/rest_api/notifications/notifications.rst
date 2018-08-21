Notifications
==============

Notifications are a great way for users to follow updates on certain items, such as Indicators, Groups, or Contributes. Click the **Bell** icon on the navigation bar to utilize the Notification feature. The red bubble by the icon will include the number of “Push” Notifications that are available for viewing, which are Notifications that may warrant immediate attention. This documentation will detail how to create Notifications via the API.

Creating a Notification
-------------------------

To create a Notification, use a query in the following format:

.. code::

    POST /v2/notifications

Required Name/Value Pairs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If any of the following required name/value pairs are not included in the request, it will fail and be returned with a Bad Request (400) response.

**notificationType**: Free-form text value limited to 50 characters. Values larger than 50 characters are truncated at 50. If the type does not exist, it will be saved for the API user’s organization. Users in the organization will be able to set notification preferences for this type after it is saved. The only value that cannot be used is “System” in any variation of case, as this is a reserved notification type for “system” push notifications.

**priority**: LOW|MEDIUM|HIGH

**message**: Message in free-form text that can contain Markdown, limited to 64k in MySQL and 2G in SAP HANA.

**recipients**: A comma-separated list of usernames that will receive the message. The usernames must be in the same organization as the API user sending the message. This parameter is required if the optional “isOrganization” parameter is not provided, or if it is set to “false.”

Optional Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

JSON Response:

.. code-block:: json

    {
      "message":"Integration Completed!  No errors",
      "notificationType":"API",
      "recipients":"user@user.com",
      "isOrganization":"false",
      "priority":"HIGH
     }      
