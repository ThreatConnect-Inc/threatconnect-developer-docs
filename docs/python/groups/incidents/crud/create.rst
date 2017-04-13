Create Incidents
^^^^^^^^^^^^^^^^

The example below demonstrates how to create an Incident Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,23-24

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate an Incidents container
    incidents = tc.incidents()

    owner = 'Example Community'
    # create a new Incident in 'Example Community' with the name: 'New Incident'
    incident = incidents.add('New Incident', owner)
    # set the event date for the Incident
    incident.set_event_date('2017-03-21T00:00:00Z')  # REQUIRED

    # add a description attribute
    incident.add_attribute('Description', 'Description Example')
    # add a tag
    incident.add_tag('Example')
    # add a security label
    incident.set_security_label('TLP Green')

    try:
        # create the Incident
        incident.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

Supported Properties

+-----------------+--------------------+------------+
| Property Name   | Method             | Required   |
+=================+====================+============+
| event\_date     | set\_event\_date   | True       |
+-----------------+--------------------+------------+

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident = incidents.add('New Incident')`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.set_event_date('2017-03-21T0...`` | **(REQUIRED)** Set event date of Incident.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.add_attribute('Description' ...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.add_tag('EXAMPLE')``              | Add a Tag to the Incident.                                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.set_security_label('TLP Green')`` | Add a Security Label to the Incident.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
