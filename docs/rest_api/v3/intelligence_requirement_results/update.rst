Update Intelligence Requirement Results
---------------------------------------

There are three actions you can perform when working with results for an IR:

* Archive (or unarchive) the result
* Associate the result to the IR object
* Mark the result as a false result (i.e., false positive)

.. attention::
    A result cannot have more than one of the following fields set to ``true`` at a given time: ``archived``, ``associated``, and ``falsePositive``. Attempting to set more than two of these fields to ``true`` for a result will return an error.

Archive a Result
^^^^^^^^^^^^^^^^

Send a request in the following format to archive a specific result.

**Example Request**

.. code::

    PUT /v3/intelRequirements/results/{resultId}
    Content-Type: application/json

    {
        "archived": true
    }

For example, the following request will archive the result whose ID is 10.

**Request**

.. code::

    PUT /v3/intelRequirements/results/10
    Content-Type: application/json

    {
        "archived": true
    }

**Response**

.. code:: json

    {
        "data": {
            "id": 10,
            "matchedDate": "2023-09-20T15:49:56Z",
            "name": "C0010",
            "itemType": "campaign",
            "internal": false,
            "falsePositive": false,
            "associated": false,
            "archived": true,
            "archivedDate": "2023-09-20T15:56:49Z"
        },
        "message": "Updated",
        "status": "Success"
    }

.. hint::
    To unarchive an archived result, assign the ``archived`` field a value of ``false`` in the request body of the PUT request.

Associate a Result
^^^^^^^^^^^^^^^^^^

Send a request in the following format to associate a specific result to its IR.

**Example Request**

.. code::

    PUT /v3/intelRequirements/results/{resultId}
    Content-Type: application/json

    {
        "associated": true
    }

For example, the following request will associate the result whose ID is 11 to its IR.

**Request**

.. code::

    PUT /v3/intelRequirements/results/11
    Content-Type: application/json

    {
        "associated": true
    }

**Response**

.. code:: json

    {
        "data": {
            "id": 11,
            "matchedDate": "2023-09-19T14:56:19Z",
            "name": "http://3.145.115.94/zambos_caldo_de_p.txt",
            "ownerId": 76,
            "ownerName": "abuse.ch URLHaus",
            "itemId": 1098,
            "itemType": "url",
            "internal": true,
            "falsePositive": false,
            "associated": true,
            "archived": false,
            "score": 1166
        },
        "message": "Updated",
        "status": "Success"
    }

.. attention::
    When the ``associated`` field is set to ``true`` for a result, you cannot update the field's value to ``false`` manually. Instead, you must dissociate the result from its IR, which will update the ``associated`` field's value to ``false`` automatically.

.. note::
    When you associate a global result that does not exist in one of your ThreatConnect owners to an IR, a copy of the result will be created in your Organization and then associated to the IR.

Mark a Result as a False Result
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to mark a result as a false result for the IR to which it corresponds.

**Example Request**

.. code::

    PUT /v3/intelRequirements/results/{resultId}
    Content-Type: application/json

    {
        "falsePositive": true
    }

For example, the following request will mark the result whose ID is 12 as a false result for the IR to which it corresponds.

**Request**

.. code::

    PUT /v3/intelRequirements/results/12
    Content-Type: application/json
    
    {
        "falsePositive": true
    }

**Response**

.. code:: json

    {
        "data": {
            "id": 12,
            "matchedDate": "2023-09-19T14:56:19Z",
            "name": "UNC2021",
            "ownerId": 197,
            "ownerName": "Mandiant Advantage Threat Intelligence",
            "itemId": 4855856,
            "itemType": "intrusion set",
            "internal": true,
            "falsePositive": true,
            "associated": false,
            "archived": false,
            "score": 1157
        },
        "message": "Updated",
        "status": "Success"
    }