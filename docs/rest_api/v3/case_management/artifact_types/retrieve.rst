Retrieve Artifact Types
-----------------------

Retrieve All Artifact Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Artifact types:

.. code::

    GET /v3/artifactTypes

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Email Address",
                "description": "A name that identifies an electronic post office box on a network where Electronic-Mail (e-mail) can be sent.",
                "dataType": "String",
                "intelType": "indicator-EmailAddress",
                "derivedLink": true
            },
            {
                "id": 2,
                "name": "Host",
                "description": "A hostname. A host is any hardware device that has the capability of permitting access to a network via a user interface, specialized software, network address, protocol stack, or any other means.",
                "dataType": "String",
                "intelType": "indicator-Host",
                "derivedLink": true
            }, 
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Artifact Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Artifact type:

.. code::

    GET /v3/artifactTypes/{artifactTypeId}

For example, the following request will retrieve data for the Artifact type whose ID is 3:

.. code::

    GET /v3/artifactTypes/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "URL",
            "description": "A uniform resource locator, or URL, is a short string containing an address which refers to an object in the web. URLs are a subset of URIs.",
            "dataType": "String",
            "intelType": "indicator-URL",
            "derivedLink": true
        },
        "status": "Success"
    }