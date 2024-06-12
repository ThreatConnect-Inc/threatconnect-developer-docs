Retrieve Playbook Executions
----------------------------

Retrieve All Playbook Executions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Playbook executions in your Organization:

**Request**

.. code::

    GET /v3/playbook/executions

**Response**

.. code:: json

    {
        "data": [
            {
                "id": 95,
                "playbookId": 13122,
                "playbookXid": "GiTVUWaN",
                "completedTime": "2024-04-04T21:39:42Z",
                "logLevel": "DEBUG",
                "status": "Completed",
                "queueTime": "2024-04-04T21:39:31Z",
                "startTime": "2024-04-04T21:39:31Z"
            },
            {
                "id": 94,
                "playbookId": 14000,
                "playbookXid": "etUM6cLX",
                "logLevel": "TRACE",
                "status": "Failed",
                "queueTime": "2024-02-21T14:22:32Z",
                "startTime": "2024-02-21T14:22:32Z"
            },
            {...}
        ],
        "countFailure": 25,
        "status": "Success",
        "countSuccess": 70
    }

.. note::

    The ``countFailure`` and ``countSuccess`` fields provide the total number of failed and successful Playbook executions, respectively, included in the API response.

Retrieve Playbook Executions Completed During a Specific Time Range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following request demonstrates how to use TQL to filter Playbook executions based on when they were completed. In the following example, the API request will retrieve data only for Playbook executions completed within the last hour:

**Request (Decoded URL)**

.. code::

    GET /v3/playbook/executions?tql=completedTime > "NOW() - 1 HOUR"

**Request (Encoded URL)**

.. code::

    GET /v3/playbook/executions?tql=completedTime%20%3E%20%22NOW()%20-%201%20HOUR%22

Retrieve Executions for a Specific Playbook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following requests demonstrate how to use TQL to filter Playbook executions by the corresponding Playbook's XID and ID number. For instructions on obtaining a Playbook's XID and ID number, see `Playbooks Overview <https://docs.threatconnect.com/en/latest/rest_api/v3/playbooks/playbooks.html>`_.

Filter Executions by XID
""""""""""""""""""""""""

In the following example, the API request will retrieve data only for executions of the Playbook whose XID is **GiTVUWaN**:

**Request (Decoded URL)**

.. code::

    GET /v3/playbook/executions?tql=playbookXid = "GiTVUWaN"

**Request (Encoded URL)**

.. code::

    GET /v3/playbook/executions?tql=playbookXid%20%3D%20%22GiTVUWaN%22

Filter Executions by ID Number
""""""""""""""""""""""""""""""

In the following example, the API request will retrieve data only for executions of the Playbook whose ID number is **12345**:

**Request (Decoded URL)**

.. code::

    GET /v3/playbook/executions?tql=playbookId = 12345

**Request (Encoded URL)**

.. code::

    GET /v3/playbook/executions?tql=playbookId%20%3D%2012345