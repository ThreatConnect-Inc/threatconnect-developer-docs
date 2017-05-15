Delete Victims
--------------

The example below demonstrates how to delete a Victim Resource from the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-13,15-16,19-20

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    owner = 'Example Community'

    # create an empty Victim object
    victim = victims.add('', owner)

    # set the id of the empty Victim object to the id of an existing Victim to delete
    victim.set_id(123456)

    try:
        # delete the Victim
        victim.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.
