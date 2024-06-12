Schemas
-------

Response Body
^^^^^^^^^^^^^

The default response returned from a successful GET request to the ``/v3/job/executions`` endpoint includes one or more objects with the following fields:

* ``id``: <*Integer*> The Job execution's ID number.
* ``jobId``: <*Integer*> The ID number of the Job that was executed.
* ``completedTime``: <*DateTime*> The date and time when the Job execution completed. If the Job execution failed, the API response will include a ``failedTime`` field that provides the date and time when the execution failed instead of the ``completedTime`` field.
* ``exitMessage``: <*String*> The Job execution's exit message.
* ``queueTime``: <*DateTime*> The date and time when the Job execution was queued.
* ``serverName``: <*String*> The name of the server on which the Job was executed.
* ``startTime``: <*DateTime*> The date and time when the Job execution started.
* ``status``: <*String*> The Job execution's status.


**Example**

.. code:: json

    {
        "id": <int>,
        "jobId": <int>,
        "completedTime": "<datetime>",
        "exitMessage": "<string>",
        "queueTime": "<datetime>",
        "serverName": "<string>",
        "startTime": "<datetime>",
        "status": "<string>"
    }