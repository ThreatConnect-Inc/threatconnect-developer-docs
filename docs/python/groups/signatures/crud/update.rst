Update Signatures
^^^^^^^^^^^^^^^^^

The example below demonstrates how to update a Signature Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,20-21

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Signatures object
    signatures = tc.signatures()

    owner = 'Example Community'

    # create a Signature with an updated name
    signature = signatures.add('Updated Signature', owner)
    # set the ID of the new Signature to the ID of the existing Signature you want to update
    signature.set_id(123456)

    # you can update the Signature metadata as described here: https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-metadata

    try:
        # update the Signature
        signature.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
