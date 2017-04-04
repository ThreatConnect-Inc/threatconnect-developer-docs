Retrieve Victims
----------------

Retrieving a Single Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to retrieve a Victim Resource from the ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()

    # set a filter to retrieve the victim with the id: 123456
    filter1 = victims.add_filter()
    filter1.add_id(123456)

    try:
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for victim in victims:
        print(obj.id)
        print(obj.name)
        print(obj.nationality)
        print(obj.org)
        print(obj.suborg)
        print(obj.work_location)
        print(obj.weblink)

Retrieving Multiple Victims
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to retrieve multiple Victim Resources from the ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()
    owner = 'Example Community'

    filter1 = victims.add_filter()
    filter1.add_owner(owner)
    filter1.add_adversary_id(531)

    try:
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for victim in victims:
        print(obj.id)
        print(obj.name)
        print(obj.nationality)
        print(obj.org)
        print(obj.suborg)
        print(obj.work_location)
        print(obj.weblink)

This example will demonstrate how to retrieve Victims while applying
filters. In this example two filters will be added, one for the Owner
and another for an Adversary ID. The result set returned from this
example would contain any Victim in the "Example Community" Owner that
has associations with the Adversary having the supplied ID.

**Code Highlights**

+----------------------------------------------+----------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                            |
+==============================================+========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                  |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                                                |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1 = victims.add_filter()``           | Add a filter object to the Victims container object (support multiple filter objects). |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1.add_adversary_id(531)``            | Add API filter to retrieve Victims associated with the given Adversary.                |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``victims.retrieve()``                       | Trigger the API request and retrieve the Victims intelligence data.                    |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``for victim in victims:``                   | Iterate over the Victims container object generator.                                   |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``print(victim.id)``                         | Display the **id** property of the Victim object.                                      |
+----------------------------------------------+----------------------------------------------------------------------------------------+
