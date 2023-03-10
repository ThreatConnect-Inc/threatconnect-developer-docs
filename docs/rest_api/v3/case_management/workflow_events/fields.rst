Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/workflowEvents`` endpoint:

.. code::

    OPTIONS /v3/workflowEvents

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/workflowEvents`` endpoint.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - caseId
     - The ID of the Case that contains the Workflow Event
     - Integer
     - TRUE [1]_
     - FALSE
     - 1, 2, 3
   * - caseXid
     - The XID of the Case that contains the Workflow Event
     - String
     - TRUE [1]_
     - FALSE
     - "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"
   * - eventDate
     - The date and time when the Workflow Event took place
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T12:30:00Z"
   * - notes
     - A list of Notes added to the Workflow Event
     - `Note Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/notes/notes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"text": "Additional information about this Workflow Event"}]}
   * - summary
     - The Workflow Event's summary
     - String
     - TRUE
     - TRUE
     - "Notes about Case uploaded to SOC team shared drive"

.. [1] When adding an Workflow Event to a Case, you must include either the ``caseId`` or ``caseXid`` field in the body of the POST request. Only one needs to be included in the body of the POST request, but both can be included, if desired.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/workflowEvents`` endpoint:

.. code::

    OPTIONS /v3/workflowEvents/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/workflowEvents`` endpoint:

.. code::

    OPTIONS /v3/workflowEvents/tql