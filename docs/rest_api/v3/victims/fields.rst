Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/victims`` endpoint, including the field’s name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/victims

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``victims`` object.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example value(s)
   * - assets
     - A list of Victim Assets corresponding to the Victim
     - `Victim Asset Object <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html>`_
     - FALSE
     - TRUE
     - {"data": [{"id": 12345}]}, {"data": [{"phone": "0123456789", "type": "Phone"}]}
   * - associatedGroups
     - A list of Groups associated to the Victim
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - {"data": [{"id": 12345}]}, {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - attributes
     - A list of Attributes corresponding to the Victim
     - `Victim Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_attributes/victim_attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Attribute Type", "value": "Attribute Value", "source": "Attribute Source"]}}
   * - description
     - The Victim's description
     - String
     - FALSE
     - TRUE
     - "This Victim's bank account was hacked."
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
   * - ownerName
     - The name of the Organization, Community, or Source to which the Victim belongs 
     - String
     - FALSE
     - FALSE
     - "Demo Community"
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
   * - type
     - The type of Victim being created. The only valid value is "Victim"
     - String
     - TRUE
     - FALSE
     - "Victim"
   * - workLocation
     - The Victim's work location
     - String
     - FALSE
     - TRUE
     - "Washington, D.C."

.. note::
    The following Victim Asset types can be added to a Victim via the ``assets`` field:

    - ``EmailAddress``
    - ``NetworkAccount``
    - ``Phone``
    - ``SocialNetwork``
    - ``WebSite``

.. note::
    A list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_ can be retrieved with the following query:
    
    ``GET /v3/attributeTypes``