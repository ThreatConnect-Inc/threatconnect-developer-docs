Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/victimAttributes`` endpoint, including each field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/victimAttributes

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``victimAttributes`` object.

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - default
     - A flag indicating whether an Attribute is the default Attribute of its type within the object (this field applies to certain Attribute and data types only)
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
   * - victimId
     - The ID of the Victim associated with the Attribute
     - Integer
     - TRUE
     - FALSE

.. note::
    When setting the ``type`` field, you must enter a valid Attribute Type that applies to Victims. To retrieve a list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_, use the following query:
    
    ``GET /v3/attributeTypes``