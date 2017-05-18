Create Incidents
^^^^^^^^^^^^^^^^

The example below demonstrates how to create an Incident Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,25-26

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Incidents object
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

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

**Supported Properties**

+-----------------+--------------------+------------+
| Property Name   | Method             | Required   |
+=================+====================+============+
| event\_date     | set\_event\_date   | True       |
+-----------------+--------------------+------------+
