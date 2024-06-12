Retrieve Job Executions
-----------------------

Retrieve All Job Executions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Job executions in your Organization:

**Request**

.. code::

    GET /v3/job/executions

**Response**

.. code:: json

    {
        "data": [
            {
                "id": 95,
                "jobId": 174,
                "completedTime": "2024-04-04T21:39:42Z",
                "exitMessage": "Successfully Added Attribute(s).\n",
                "queueTime": "2024-04-04T21:39:41Z",
                "serverName": "tc-job",
                "startTime": "2024-04-04T21:39:41Z",
                "status": "Completed"
            },
            {
                "id": 94,
                "jobId": 100,
                "exitMessage": "Failed for status (404)\n",
                "failedTime": "2024-05-02T17:36:40Z",
                "queueTime": "2024-05-02T17:36:38Z",
                "serverName": "tc-job",
                "startTime": "2024-05-02T17:36:38Z",
                "status": "Failed"
            },
            {...}
        ],
        "countFailure": 3,
        "status": "Success",
        "countSuccess": 92
    }

.. note::

    The ``countFailure`` and ``countSuccess`` fields provide the total number of failed and successful Job executions, respectively, included in the API response.

Retrieve Job Executions Completed During a Specific Time Range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following request demonstrates how to use TQL to filter Job executions based on when they were completed. In this example, the API request will retrieve data only for Job executions completed within the last hour:

**Request (Decoded URL)**

.. code::

    GET /v3/job/executions?tql=completedTime > "NOW() - 1 HOUR"

**Request (Encoded URL)**

.. code::

    GET /v3/job/executions?tql=completedTime%20%3E%20%22NOW()%20-%201%20HOUR%22

Retrieve Executions for a Specific Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following request demonstrates how to use TQL to filter Job executions by the corresponding Job's ID number. For instructions on obtaining a Job's ID number, see `Jobs Overview <https://docs.threatconnect.com/en/latest/rest_api/v3/jobs/jobs.html>`_.

In this example, the API request will retrieve data only for executions of the Job whose ID number is **12345**:

**Request (Decoded URL)**

.. code::

    GET /v3/job/executions?tql=jobId = 12345

**Request (Encoded URL)**

.. code::

    GET /v3/job/executions?tql=jobId%20%3D%2012345