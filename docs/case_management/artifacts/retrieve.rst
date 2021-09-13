Retrieve Artifacts
------------------

Retrieve All Artifacts
^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Artifacts, use the following query:

.. code::

    GET /v3/artifacts/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "summary": "badguy@bad.com",
        "type": "Email Address",
        "fieldName": "helloRecipient",
        "intelType": "indicator-EmailAddress",
        "source": "11112222333344445555",
        "dateAdded": "2021-04-22T19:24:06Z",
        "derivedLink": "True",
        "hashCode": "2e7d3603331dea4ec9a14442c0a409dcfc3f69e7"
      }, {
        "id": 2,
        "summary": "123.456.78.90",
        "type": "IP Address",
        "intelType": "indicator-Address",
        "source": "johnsmith",
        "dateAdded": "2021-03-08T13:24:38Z",
        "derivedLink": "True",
        "hashCode": "cbdb4defdbb9433683a9daa0764c58a45bddd729"
      }],
      "count": 2,
      "status": "Success"
    }

Retrieve a Single Artifact
^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Artifact, use a query in the following format:

.. code::

    GET /v3/artifacts/{artifactID}

For example, the following query will return information about the Artifact with ID 3:

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
        "derivedLink": "True",
        "hashCode": "fec31a1f2937c37b110d467cf78c03d820954596"
      },
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned Artifact, refer to the `Request Additional Fields for Returned Objects <..additional_fields.html>`__ section in this documentation.

Filter Results
^^^^^^^^^^^^^^

To filter returned Artifacts using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <..filter_results.html>`__ section in this documentation.
