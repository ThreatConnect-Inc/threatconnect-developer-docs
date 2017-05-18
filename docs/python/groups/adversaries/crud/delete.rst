Delete Adversaries
^^^^^^^^^^^^^^^^^^

The example below demonstrates how to delete an Adversary Resource in
the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 11-14,17-18

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Adversaries object
    adversaries = tc.adversaries()

    owner = 'Example Community'
    # create an empty Adversary
    adversary = adversaries.add('', owner)
    # set the ID of the new Adversary to the ID of the Adversary you would like to delete
    adversary.set_id(123456)

    try:
        # delete the Adversary
        adversary.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.
