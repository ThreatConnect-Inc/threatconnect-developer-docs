Update Incidents
^^^^^^^^^^^^^^^^

The example below demonstrates how to update an Incident Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,20-21

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Incidents object
    incidents = tc.incidents()

    owner = 'Example Community'

    # create an Incident with an updated name
    incident = incidents.add('Updated Incident', owner)
    # set the ID of the new Incident to the ID of the existing Incident you want to update
    incident.set_id(123456)

    # you can update the Incident metadata as described here: https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-metadata

    try:
        # update the Incident
        incident.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
