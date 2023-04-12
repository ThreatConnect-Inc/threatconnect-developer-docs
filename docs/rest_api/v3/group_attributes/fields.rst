Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/groupAttributes`` endpoint:

.. code::

    OPTIONS /v3/groupAttributes

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/groupAttributes`` endpoint.

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - default
     - Indicates whether the Attribute is the default Attribute of its type for the Group to which it is added (this field applies to certain Attribute and data types only)
     - Boolean
     - FALSE
     - TRUE
   * - groupId
     - The ID of the Group to which the Attribute is added
     - Integer
     - TRUE
     - FALSE
   * - pinned
     - Indicates whether the Attribute is to be displayed as a Pinned Attribute on the **Details** screen for the Group to which the Attribute is added
     - Boolean
     - FALSE
     - TRUE
   * - securityLabels
     - A list of Security Labels applied to the Attribute
     - `Security Label Object <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_
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

.. [1] When setting the ``type`` field, you must enter a valid Attribute Type that applies to the type of Group to which the Attribute is being added. To retrieve a list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_, send the following request: ``GET /v3/attributeTypes``.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/groupAttributes`` endpoint:

.. code::

    OPTIONS /v3/groupAttributes/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/groupAttributes`` endpoint:

.. code::

    OPTIONS /v3/groupAttributes/tql