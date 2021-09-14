Retrieve Artifact Types
-----------------------

Retrieve All Artifact Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Artifact types, use the following query:

.. code::

    GET /v3/artifactTypes/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "name": "Email Address",
        "description": "A name that identifies an electronic post office box on a network where Electronic-Mail (e-mail) can be sent.",
        "dataType": "String",
        "intelType": "indicator-EmailAddress",
        "derivedLink": "True"
      }, {
        "id": 2,
        "name": "Host",
        "description": "A hostname. A host is any hardware device that has the capability of permitting access to a network via a user interface, specialized software, network address, protocol stack, or any other means.",
        "dataType": "String",
        "intelType": "indicator-Host",
        "derivedLink": "True"
      }, {...},
         {...}
      ],
      "count": 75,
      "status": "Success"
    }

Retrieve a Single Artifact Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Artifact type, use a query in the following format:

.. code::

    GET /v3/artifactTypes/{artifactTypeID}

For example, the following query will return information about the Artifact type with ID 3:

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
        "derivedLink": "True"
      },
      "status": "Success"
    }

Filter Results
^^^^^^^^^^^^^^

To filter returned Artifact types using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../filter_results.html>`__ section in this documentation.
