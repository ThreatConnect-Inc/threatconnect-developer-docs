Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/workflowTemplates`` endpoint:
.. code::

    OPTIONS /v3/workflowTemplates

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/workflowTemplates`` endpoint.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - configAttribute
     - A list of Attribute Types to include in the Workflow Template [1]_
     - Config Attribute Object
     - FALSE
     - TRUE
     - [{"attributeTypeId": 271}]
   * - description
     - The description of the Workflow Template
     - String
     - FALSE
     - TRUE
     - "Workflow for phishing investigations."
   * - name
     - The name of the Workflow Template
     - String
     - True
     - TRUE
     - "Phishing Investigation Workflow"
   * - version
     - The version of the Workflow Template
     - Integer
     - FALSE
     - TRUE
     - 1, 2, 3

.. [1] To retrieve a list of available Attribute Types that apply to Cases, send the following request: ``GET /v3/attributeTypes?tql=associatedType EQ "Case"``. Note that you will need to encode the request URL before sending the request.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/workflowTemplates`` endpoint:

.. code::

    OPTIONS /v3/workflowTemplates/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/workflowTemplates`` endpoint:

.. code::

    OPTIONS /v3/workflowTemplates/tql