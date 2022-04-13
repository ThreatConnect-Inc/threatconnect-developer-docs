Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/workflowTemplates`` endpoint, including each field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/workflowTemplates

.. hint::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request for the ``workflowTemplates`` object.

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
     - The Attribute Type to include in the Workflow Template
     - Config Attribute Object
     - FALSE
     - TRUE
     - [{"attributeTypeId": 3}]
   * - description
     - The description of the Workflow Template
     - String
     - FALSE
     - TRUE
     - "Template for phishing investigations."
   * - name
     - The name of the Workflow Template
     - String
     - True
     - TRUE
     - "Phishing Workflow Template"
   * - version
     - The version of the Workflow Template
     - Integer
     - FALSE
     - TRUE
     - 1, 2, 3

.. note::
    Alist of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_ and their corresponding ID can be retrieved with the following query:
    
    ``GET /v3/attributeTypes``