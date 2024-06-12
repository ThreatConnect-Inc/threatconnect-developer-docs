Schemas
-------

Response Body
^^^^^^^^^^^^^

The default response returned from a successful GET request to the ``/v3/playbook/executions`` endpoint includes one or more objects with the following fields:

* ``id``: <*Integer*> The Playbook execution's ID number.
* ``playbookId``: <*Integer*> The ID number of the Playbook that was executed.
* ``playbookXid``: <*String*> The XID of the Playbook that was executed.
* ``completedTime``: <*DateTime*> The date and time when the Playbook execution completed.
* ``logLevel``: <*String*> The log level used during the Playbook execution.
* ``status``: <*String*> The Playbook execution's status.
* ``queueTime``: <*DateTime*> The date and time when the Playbook execution was queued.
* ``startTime``: <*DateTime*> The date and time when the Playbook execution started.

**Example**

.. code:: json

    {
        "id": <int>,
        "playbookId": <int>,
        "playbookXid": "<string>",
        "completedTime": "<datetime>",
        "logLevel": "<string>",
        "status": "<string>",
        "queueTime": "<datetime>",
        "startTime": "<datetime>"
    }