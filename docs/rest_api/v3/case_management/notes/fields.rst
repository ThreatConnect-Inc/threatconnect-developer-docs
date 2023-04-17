Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/notes`` endpoint:

.. code::

    OPTIONS /v3/notes

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/notes`` endpoint.

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - artifactId
     - The ID of the Artifact to which the Note will be applied
     - Integer
     - FALSE
     - FALSE
   * - caseId
     - The ID of the Case to which the Note will be applied
     - Integer
     - TRUE [1]_ [2]_
     - FALSE
   * - caseXid
     - The XID of the Case to which the Note will be applied
     - String
     - TRUE [1]_ [2]_
     - FALSE
   * - taskId
     - The ID of the Task to which the Note will be applied
     - Integer
     - FALSE
     - FALSE
   * - taskXid
     - The XID of the Task to which the Note will be applied
     - String
     - FALSE
     - FALSE
   * - text
     - The contents of the Note
     - String
     - TRUE
     - TRUE
   * - workflowEventId
     - The ID of the Workflow Event to which the Note will be applied
     - Integer
     - FALSE
     - FALSE

.. [1] When adding a Note to a Case, you must include either the ``caseId`` or ``caseXid`` field in the body of the POST request. Only one needs to be included in the body of the POST request, but both can be included, if desired.

.. [2] When adding a Note to an Artifact or Task, you **do not** need to include the ``caseId`` or ``caseXid`` field in the body of the POST request.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/notes`` endpoint:

.. code::

    OPTIONS /v3/notes/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/notes`` endpoint:

.. code::

    OPTIONS /v3/notes/tql