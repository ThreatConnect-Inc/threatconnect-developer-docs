Schemas
-------

Response Body
^^^^^^^^^^^^^

The default response returned from a successful GET request to the ``/v3/playbooks`` endpoint includes one or more objects with the following fields:

* ``id``: <*Integer*> The Playbook's ID number.
* ``groupXid``: <*String*> The Playbook's XID.
* ``name``: <*String*> The Playbook's name.
* ``description``: <*String*> The Playbook's description. This field is included in the response body only if a description has been provided for the Playbook.
* ``webLink``: <*String*> The Playbook's URL. This URL includes the Playbook's ID number.
* ``groupWebLink``: <*String*> The Playbook's URL. This URL Includes the Playbook's XID.
* ``version``: <*String*> The Playbook's current version number.
* ``comment``: <*String*> The comment associated with the Playbook's current version number.
* ``lastInteractiveSession``: <*String*> The XID associated with the most recent interactive session for the Playbook. This field is included in the response body only if the Playbook has been used in **Interactive Mode**.
* ``type``: <*String*> The Playbook's type. Possible values include **Playbook** (for standard Playbooks), **Component** (for Playbook Components), and **Workflow** (for Workflow Playbooks).
* ``triggerType``: <*String*> The type of Trigger that the Playbook uses. This field is included in the response body only if a Trigger has been added to the Playbook.
* ``endpoint``: <*String*> The endpoint for the Playbook's Trigger. This field is included in the response body only for Playbooks that use a Mailbox or WebHook Trigger.
* ``active``: <*Boolean*> Specifies whether the Playbook is active.
* ``basicAuthEnabled``: <*Boolean*> Specifies whether basic authentication is turned on for the Playbook's Trigger.
* ``logLevel``: <*String*> The Playbook's log level.
* ``updated``: <*DateTime*> The date and time when the Playbook was last updated.
* ``labels``: <*String Array*> The label(s) applied to the Playbook. This field is included in the response body only if one or more labels have been applied to the Playbook.
* ``priority``: <*Integer*> The Playbook's priority. Possible values include **3** (for Low), **6** (for Medium, which is the default priority), and **7** (for High).
* ``scheduleCronFormat``: <*String*> The schedule of the Playbook's Timer Trigger defined as a cron expression. This field is included in the response body only for Playbooks that use a Timer Trigger.
* ``status``: <*String*> The Playbook's status.
* ``zoom``: <*Float*> The current zoom level for the Playbook in the Playbook Designer.
* ``panX``: <*Float*> The number of units that the Playbook has been moved horizontally in the Playbook Designer.
* ``panY``: <*Float*> The number of units that the Playbook has been moved vertically in the Playbook Designer.
* ``roiDollarsPerHour``: <*Integer*> The dollars per hour that will be saved with each execution of the Playbook.
* ``roiMinutes``: <*Integer*> The amount of an analyst's time, in minutes, that will be saved with each execution of the Playbook.
* ``apiUser``: <*String*> The name of the user under which the Playbook will execute.
* ``enableNotifications``: <*Boolean*> Specifies whether failure notifications are turned on for the Playbook.
* ``notifyEmailList``: <*String*> The email address(es) to which failure notifications will be sent. This field is included in the response body only if failure notifications are turned on for the Playbook and one or more email addresses to which notifications will be sent have been specified.
* ``notifyIncludeLogFiles``: <*Boolean*> Specifies whether to include log files in the failure notifications.
* ``notifyEmailCount``: <*Integer*> The number of failure notifications that have been sent for the Playbook.
* ``ownerName``: <*String*> The Organization in which the Playbook exists.

**Example**

.. code:: json

    {
        "id": <int>,
        "groupXid": "<string>",
        "name": "<string>",
        "description": "<string>",
        "webLink": "<string>",
        "groupWebLink": "<string>",
        "version": "<string>",
        "comment": "<string>",
        "lastInteractiveSession": "<string>",
        "type": "<string>",
        "triggerType": "<string>",
        "active": <boolean>,
        "basicAuthEnabled": <boolean>,
        "logLevel": "<string>",
        "updated": "<datetime>",
        "labels": [
            "<string>"
        ],
        "priority": <int>,
        "status": "<string>",
        "zoom": <float>,
        "panX": <float>,
        "panY": <float>,
        "roiDollarsPerHour": <int>,
        "roiMinutes": <int>,
        "apiUser": "<string>",
        "enableNotifications": <boolean>,
        "notifyEmailList": "<string>",
        "notifyIncludeLogFiles": <boolean>,
        "notifyEmailCount": <int>,
        "ownerName": "<string>"
    }