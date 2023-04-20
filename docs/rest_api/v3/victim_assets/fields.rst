Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including the field's name, description, and accepted data type that can be included in the body of a POST or PUT request to the ``/v3/victimAssets`` endpoint:

.. code::

    OPTIONS /v3/victimAssets

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/victimAssets`` endpoint.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - accountName
     - The account name associated with a **Network Account** or **Social Network** Victim Asset
     - String
     - TRUE [1]_
     - TRUE
     - "@johnsmith"
   * - address
     - The email address associated with an **Email Address** Victim Asset
     - String
     - TRUE [1]_
     - TRUE
     - "jsmith@companyabc.com"
   * - addressType
     - The type of **Email Address** Victim Asset
     - String
     - FALSE
     - TRUE
     - "Corporate email"
   * - associatedGroups
     - A list of Groups associated to the Victim Asset
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - networkType
     - The type of **Network Account** Victim Asset
     - String
     - FALSE
     - TRUE
     - "Company network"
   * - phone
     - The phone number associated with a **Phone** Victim Asset
     - String
     - TRUE [1]_
     - TRUE
     - "0123456789"
   * - socialNetwork
     - The type of **Social Account** Victim Asset
     - String
     - FALSE
     - TRUE
     - "Twitter"
   * - type [2]_
     - The type of Victim Asset being created
     - String
     - TRUE
     - FALSE
     - "Demo Community"
   * - securityLabels
     - A list of Security Labels applied to the Victim
     - String
     - FALSE
     - TRUE
     - "EmailAddress", "NetworkAccount", "Phone", "SocialNetwork", or "WebSite"
   * - victimId
     - The ID of the Victim to which the Victim Asset should be added
     - Integer
     - TRUE
     - FALSE
     - 1, 2, 3
   * - website
     - The website address associated with a **Website** Victim Asset
     - String
     - TRUE [1]_
     - TRUE
     - "``http://examplesite.com``"

.. [1] This field is required only if creating a Victim Asset that matches the type listed in the **Description** column.

.. [2] The following are accepted values for the ``type`` field:

    - ``EmailAddress``
    - ``NetworkAccount``
    - ``Phone``
    - ``SocialNetwork``
    - ``WebSite``

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/victimAssets`` endpoint:

.. code::

    OPTIONS /v3/victimAssets/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/victimAssets`` endpoint:

.. code::

    OPTIONS /v3/victimAssets/tql