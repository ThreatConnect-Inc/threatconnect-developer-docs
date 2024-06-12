Retrieve Jobs
-------------

Retrieve All Jobs
^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Jobs in your Organization:

**Request**

.. code::

    GET /v3/jobs

**Response**

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "name": "QRadar",
                "displayName": "QRadar Integration",
                "programName": "TC - QRadar Extract v2.2",
                "programVersion": "2.2.22",
                "active": true
            },
            {
                "id": 9,
                "name": "Import from MISP",
                "displayName": "MISP-Import",
                "programName": "TC - MISP Import v1.0",
                "programVersion": "1.0.34",
                "active": false
            },
            {...}
        ],
        "status": "Success"
    }

.. hint::

    To include details about a Job's most recent execution in the API response, append ``?fields=lastExecution`` to the end of the request URL.

Retrieve a Specific Job
^^^^^^^^^^^^^^^^^^^^^^^

The following requests demonstrate how to use TQL to retrieve data for a specific Job.

Filter by ID Number
"""""""""""""""""""

In the following example, the API request will retrieve data only for the Job whose ID number is **12345**:

**Request (Decoded URL)**

.. code::

    GET /v3/jobs?tql=id = 12345

**Request (Encoded URL)**

.. code::

    GET /v3/jobs?tql=id%20%3D%2012345

Filter by Name
""""""""""""""

In the following example, the API request will retrieve data only for the Job whose name is **Test Job**:

**Request (Decoded URL)**

.. code::

    GET /v3/jobs?tql=name = "Test Job"

**Request (Encoded URL)**

.. code::

    GET /v3/jobs?tql=name%20%3D%20%22Test%20Job%22