Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/caseAttributes`` endpoint, including the field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/caseAttributes

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``caseAttributes`` object.

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - caseId
     - The ID of the Case associated to the Attribute
     - Integer
     - TRUE
     - FALSE
   * - default
     - A flag indicating whether an Attribute is the default Attribute of its type within the object. This field applies on to certain Attribute and data types
     - Boolean
     - FALSE
     - TRUE
   * - source
     - The Attribute's source
     - String
     - FALSE
     - TRUE
   * - type
     - The Attribute's type
     - String
     - TRUE
     - FALSE
   * - value
     - The Attribute's value
     - String
     - TRUE
     - TRUE

.. note::
    Attribute Types for Cases must first be created in the System or Organization in which a Case resides before they can be added to the Case. See the `Creating Custom Attribute Types <https://training.threatconnect.com/learn/article/creating-custom-attributes-kb-article>`__ knowledge base article for more information.

.. warning::
    Trying to add an Attribute to a Case when the Case Attribute Type's **Max Allowed** limit has been reached will result in an error.