Retrieve Workflow Events
------------------------

Retrieve All Workflow Events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Workflow Events, use the following query:

.. code::

    GET /v3/workflowEvents/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "eventDate": "2021-03-05T14:48:44Z",
        "dateAdded": "2021-03-05T14:48:44Z",
        "summary": "Case created",
        "systemGenerated": True,
        "link": "https://app.threatconnect.com/api/v3/cases/1"
      }, {
        "id": 2,
        "eventDate": "2021-03-05T14:49:24Z",
        "dateAdded": "2021-03-05T14:49:24Z",
        "summary": "Added a note",
        "systemGenerated": True,
        "link": "https://app.threatconnect.com/api/v3/notes/1"
      }],
      "count": 2,
      "status": "Success"
    }

Retrieve a Single Workflow Event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Workflow Event, use a query in the following format:

.. code::

    GET /v3/workflowEvents/{workflowEventID}

For example, the following query will return information about the Workflow Event with ID 1:

.. code::

    GET /v3/workflowEvent/1

JSON Response:

.. code:: json

    {
      "data": {
        "id": 1,
        "eventDate": "2021-03-05T14:48:44Z",
        "dateAdded": "2021-03-05T14:48:44Z",
        "summary": "Case created",
        "systemGenerated": True,
        "link": "https://app.threatconnect.com/api/v3/cases/1"
      },
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned Workflow Event, refer to the `Request Additional Fields for Returned Objects <../additional_fields.html>`__ section in this documentation.

Filter Results
^^^^^^^^^^^^^^

To filter returned Workflow Events using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../filter_results.html>`__ section in this documentation.
