Update Adversaries
^^^^^^^^^^^^^^^^^^

The example below demonstrates how to update an Adversary Resource in
the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,20-21

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Adversaries object
    adversaries = tc.adversaries()

    owner = 'Example Community'

    # create an Adversary with an updated name
    adversary = adversaries.add('Updated Adversary', owner)
    # set the ID of the new Adversary to the ID of the existing Adversary you want to update
    adversary.set_id(123456)

    # you can update the Adversary metadata as described here: https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-metadata

    try:
        # update the Adversary
        adversary.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
