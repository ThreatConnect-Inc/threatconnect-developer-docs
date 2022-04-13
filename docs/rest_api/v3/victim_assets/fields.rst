Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/victimAssets`` endpoint, including the field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/victimAssets

.. hint::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``victimAssets`` object.

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
     - TRUE*
     - TRUE
     - "@johnsmith"
   * - address
     - The email address associated with a **Email Address** Victim Asset
     - String
     - TRUE*
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
     - TRUE*
     - TRUE
     - "0123456789"
   * - socialNetwork
     - The type of **Social Account** Victim Asset
     - String
     - FALSE
     - TRUE
     - "Twitter"
   * - type
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
     - TRUE*
     - TRUE
     - "``http://examplesite.com``"

Available values for the ``type`` field include:

- ``EmailAddress``
- ``NetworkAccount``
- ``Phone``
- ``SocialNetwork``
- ``WebSite``

.. note::
  \*This field is required if creating a Victim Asset that matches the type listed in the **Description** column.

.. hint::
    To **associate an existing Group** to a Victim Asset, use the Group's ID when setting the ``associatedGroups`` field (e.g., {``"data": [{"id": 12345}]}``).