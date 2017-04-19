Delete Incidents
^^^^^^^^^^^^^^^^

The example below demonstrates how to delete an Incident Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,15-16

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Incidents container
    incidents = tc.incidents()

    owner = 'Example Community'
    # create an empty Incident
    incident = incidents.add('', owner)
    # set the ID of the new Incident to the ID of the Incident you would like to delete
    incident.set_id(123456)

    try:
        # delete the Incident
        incident.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------+
| Snippet                                      | Description                                                           |
+==============================================+=======================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                            |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incident = incidents.add('', owner)``      | Add a Resource object setting the name and Owner.                     |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incident.set_id(20)``                      | Set the ID of the Incident to the **EXISTING** Incident ID to delete. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incident.delete()``                        | Trigger API calls to write all added, deleted, or modified data.      |
+----------------------------------------------+-----------------------------------------------------------------------+
