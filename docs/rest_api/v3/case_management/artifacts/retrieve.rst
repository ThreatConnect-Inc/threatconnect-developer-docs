Retrieve Artifacts
------------------

Retrieve All Artifacts
^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Artifacts:

.. code::

    GET /v3/artifacts

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "summary": "badguy@bad.com",
                "type": "Email Address",
                "intelType": "indicator-EmailAddress",
                "dateAdded": "2021-04-22T19:24:06Z",
                "derivedLink": true,
                "hashCode": "a/mHEtrRoPrG9csrdltEY73kdKHihi2jow40V3WFYrU="
            },
            {
                "id": 2,
                "summary": "123.456.78.90",
                "type": "IP Address",
                "intelType": "indicator-Address",
                "source": "johnsmith",
                "dateAdded": "2021-03-08T13:24:38Z",
                "derivedLink": true,
                "hashCode": "cbdb4defdbb9433683a9daa0764c58a45bddd729"
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Artifact
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Artifact:

.. code::

    GET /v3/artifacts/{artifactId}

For example, the following request will retrieve data for the Artifact whose ID is 3:

.. code::

    GET /v3/artifacts/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "summary": "URGENT - APPROVAL IS REQUIRED!!!",
            "type": "Email Subject",
            "fieldName": "helloSubject",
            "intelType": "indicator-Email Subject",
            "source": "patjones",
            "dateAdded": "2021-03-15T10:16:40Z",
            "derivedLink": true,
            "hashCode": "fec31a1f2937c37b110d467cf78c03d820954596"
        },
        "status": "Success"
    }