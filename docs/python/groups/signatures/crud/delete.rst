Delete Signatures
^^^^^^^^^^^^^^^^^

The example below demonstrates how to delete a Signature Resource in the
ThreatConnect platform.

.. code-block:: python
    :emphasize-lines: 11-14,17-18

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Signatures object
    signatures = tc.signatures()

    owner = 'Example Community'
    # create an empty Signature
    signature = signatures.add('', owner)
    # set the ID of the new Signature to the ID of the Signature you would like to delete
    signature.set_id(123456)

    try:
        # delete the Signature
        signature.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate a Signatures container object.                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signature = signatures.add('', owner)``    | Add a Resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signature.set_id(20)``                     | Set the ID of the Signature to the **EXISTING** Signature ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signature.delete()``                       | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+
