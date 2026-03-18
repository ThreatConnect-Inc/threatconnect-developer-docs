Notifications
=============

Notifications allow users to track changes made to Groups, Indicators, Intelligence Requirements, Tags, Victims, and other items. Users can view notifications in the ThreatConnect user interface by clicking the **bell** icon on the top navigation bar.

The v2 API allows you to create and send notifications to users in your Organization or members of a specific Community or Source.

.. note::
   - Notifications sent to a Community or Source will be delivered to only non-Banned members in the Community or Source.
   - Notifications will not be sent to API users.

Endpoint: ``{baseUrl}/api/v2/notifications``

Create Notifications
--------------------

.. code:: http

   POST /v2/notifications

Create and send a notification.

Requirements
^^^^^^^^^^^^

-  To create and send notifications to users in an Organization, your API user account must have an Organization role or Organization Administrator.
-  To create and send notifications to members of a Community or Source, your API user account must have a Community role of Commenter, Contributor, Editor, or Director for that Community or Source.

Request Body Schema
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 40 20 20
   :header-rows: 1

   * - Field
     - Description
     - Data Type
     - Required
   * - ``message``
     - | The contents of the notification. Supports Markdown.
       | 
       | Maximum size: 64 KB
     - String
     - **Required**
   * - ``notificationType``
     - | The notification's type. If the type is new, it will be registered to the recipient's Organization and can be used when updating notification settings.
       | 
       | Maximum length: 50 characters
       |
       | **Note**: "System" (case-insensitive) is reserved and cannot be used.
     - String
     - **Required**
   * - ``priority``
     - | The notification's priority.
       | 
       | Acceptable values (case-insensitive): **low**, **medium**, **high**
     - Enum
     - **Required**
   * - ``recipients``
     - A comma-separated list of usernames in your Organization that will receive the notification. This field is required if ``ownerId`` is omitted, or if ``isOrganization`` is **false** or omitted.
     - Enum
     - **Conditional**
   * - ``isOrganization``
     - | If **true**, the notification will be sent to all non-API users in your Organization.
       | 
       | Default value: **false**
     - Boolean
     - Optional
   * - ``ownerId``
     - The unique ID of the owner whose users or members will receive the notification.
     - Integer
     - Optional


Example Request
^^^^^^^^^^^^^^^

.. note::
   In addition to the required ``Content-Type`` header, you must include the required authentication headers for the method you are using to `authenticate your API request <https://threatconnect.readme.io/reference/getting-started-1#authentication>`__.

**Request**

.. code:: http

   POST /v2/notifications
   Content-Type: application/json

   {
       "message": "Test message created using the `v2 API`.",
       "notificationType": "API",
       "recipients": "jsmith",
       "isOrganization": false,
       "priority": "High"
   }

**Response**

.. code:: json

   {
       "status": "Success"
   }