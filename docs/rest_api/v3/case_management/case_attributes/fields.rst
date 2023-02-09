Available Fields
----------------

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, for the ``/v3/caseAttributes`` endpoint:

.. code::

    OPTIONS /v3/caseAttributes

.. hint::
    To include read-only fields in the response, append the ``?show=readonly`` query parameter to the OPTIONS request.

.. note::
    The API response for the ``OPTIONS /v3/caseAttributes`` request will include the ``default``, ``pinned``, and ``securityLabels`` fields. However, these fields do not apply to Case Attributes and should not be used in POST or PUT requests to the ``/v3/caseAttributes`` endpoint.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/caseAttributes`` endpoint.

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - caseId
     - The ID of the Case to which the Attribute is added
     - Integer
     - TRUE
     - FALSE
   * - source
     - The Attribute's source
     - String
     - FALSE
     - TRUE
   * - type [1]_
     - The Attribute's type
     - String
     - TRUE
     - FALSE
   * - value
     - The Attribute's value
     - String
     - TRUE
     - TRUE

.. [1] Attribute Types for Cases must first be created at the System- or Organization-level before you can add Attributes to a Case, as detailed in the `Creating Custom Attribute Types <https://knowledge.threatconnect.com/docs/creating-custom-attribute-types>`_ knowledge base article. To retrieve a list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_ and determine whether an Attribute Type applies to Cases, send the following request and then review the ``attributeTypeMappings`` field included in the response: ``GET /v3/attributeTypes?fields=mapping``.

.. attention::
    If you try to add an Attribute to a Case when the Attribute Type's **Max Allowed** limit for Cases has been reached, the API will return a **400 - Bad Request** error.