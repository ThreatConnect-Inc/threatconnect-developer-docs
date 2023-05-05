Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/victims`` endpoint:

.. code::

    OPTIONS /v3/victims

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/victims`` endpoint.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - assets [1]_
     - A list of Victim Assets added to the Victim
     - `Victim Asset Object <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"phone": "0123456789", "type": "Phone"}]}
   * - associatedGroups
     - A list of Groups associated to the Victim
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - attributes [2]_
     - A list of Attributes added to the Victim
     - `Victim Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_attributes/victim_attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Attribute Type", "value": "Attribute Value", "source": "Attribute Source"}]}
   * - name
     - The Victim's name
     - String
     - TRUE
     - TRUE
     - "Bob Loblaw"
   * - nationality
     - The Victim's nationality
     - String
     - FALSE
     - TRUE
     - "American"
   * - org
     - The Victim's organization
     - String
     - FALSE
     - TRUE
     - "Company ABC"
   * - ownerId [3]_
     - The ID of the `owner <https://docs.threatconnect.com/en/latest/rest_api/v3/owners/owners.html>`_ to which the Victim belongs
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3,...100
   * - ownerName [3]_
     - The name of the owner to which the Victim belongs
     - String
     - FALSE
     - FALSE
     - "American"
   * - securityLabels
     - A list of Security Labels applied to the Victim
     - `Security Label Object <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "TLP:AMBER"}]}
   * - suborg
     - The Victim's suborganization
     - String
     - FALSE
     - TRUE
     - "HR Department"
   * - tags
     - A list of Tags applied to the Victim
     - `Tag Object <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "Targeted Attack"}]}
   * - workLocation
     - The Victim's work location
     - String
     - FALSE
     - TRUE
     - "Washington, D.C."

.. [1] The following Victim Asset types can be added to a Victim via the ``assets`` field:

    - ``EmailAddress``
    - ``NetworkAccount``
    - ``Phone``
    - ``SocialNetwork``
    - ``WebSite``

.. [2] To retrieve a list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_, send the following request: ``GET /v3/attributeTypes``.

.. [3] By default, Victims will be created in the Organization in which your API user account resides. To create a Victim in a Community or Source, include the ``ownerId`` or ``ownerName`` field in your request. Alternatively, Alternatively, use the ``owner`` query parameter to `specify the owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ in which to create the Victim.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/victims`` endpoint:

.. code::

    OPTIONS /v3/victims/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/victims`` endpoint:

.. code::

    OPTIONS /v3/victims/tql