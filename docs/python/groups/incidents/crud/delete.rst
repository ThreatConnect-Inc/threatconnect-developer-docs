Delete Incidents
^^^^^^^^^^^^^^^^

The example below demonstrates how to delete an Incident Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Incidents object
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
