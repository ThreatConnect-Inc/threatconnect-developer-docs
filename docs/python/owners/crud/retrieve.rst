Retrieve Owners
---------------

The example below demonstrates how to retrieve Owners from the ThreatConnect platform:

.. code-block:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Owners object
    owners = tc.owners()

    try:
        # retrieve the Owners
        owners.retrieve()
    except RunTimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Owners
    for owner in owners:
        print(owner.id)
        print(owner.name)
        print(owner.type)

**Code Highlights**

+---------------------------------------------+---------------------------------------------------------------------+
| Snippet                                     | Description                                                         |
+=============================================+=====================================================================+
| ``tc = ThreatConnect(api_access_id, ap...`` | Instantiate an instance of the ThreatConnect Class.                 |
+---------------------------------------------+---------------------------------------------------------------------+
| ``owners = tc.owners()``                    | Create an Owner's container object.                                 |
+---------------------------------------------+---------------------------------------------------------------------+
| ``owners.retrieve()``                       | Trigger an API request to retrieve Owners.                          |
+---------------------------------------------+---------------------------------------------------------------------+
| ``for owner in owners:``                    | Iterate through Owner's generator.                                  |
+---------------------------------------------+---------------------------------------------------------------------+
| ``print(owner.id)``                         | Display the **'id'** property of the Owner.                         |
+---------------------------------------------+---------------------------------------------------------------------+
