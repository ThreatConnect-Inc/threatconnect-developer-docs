Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/tags`` endpoint:

.. code::

    OPTIONS /v3/tags

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/tags`` endpoint.

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

.. note::
  In addition to the fields listed in the preceding table, you can include the ``securityCoverage`` field in the body of a PUT request when updating an ATT&CK® Tag. See the `"Assign Security Coverage to ATT&CK Tags" <#id3>`_ section for further instruction.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/tags`` endpoint:

.. code::

    OPTIONS /v3/tags/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/tags`` endpoint:

.. code::

    OPTIONS /v3/tags/tql