Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/tags`` endpoint, including the field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/tags

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``tags`` object.

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - description
     - The Tag's description
     - String
     - FALSE
     - TRUE
   * - name
     - The Tag's name
     - String
     - TRUE
     - TRUE
   * - owner
     - The Organization, Community, or Source to which the Tag belongs
     - String
     - FALSE
     - FALSE