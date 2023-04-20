Update Victim Assets
--------------------

The following example illustrates the basic format for updating a Victim Asset:

.. code::

    PUT /v3/victimAssets/{victimAssetId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following request will perform the following actions for the Victim Asset whose ID is 3:

- Create an Incident Group named **Bad Incident** and associate it to the Victim Asset
- Update the website associated with the Victim Asset

.. hint::
    To include the ``associatedGroups`` field in the API response, append ``?fields=groups`` to the end of the request URL.

.. code::

    PUT /v3/victimAssets/3
    {
        "associatedGroups": {
            "data": [
                {
                    "name": "Bad Incident",
                    "type": "Incident"
                }
            ]
        },
        "website": "hackerwebsite.com"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "WebSite",
            "victimId": 2,
            "website": "hackerwebsite.com",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2"
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/victimAssets`` endpoint.

.. hint::
    When updating a Victim Asset, you can use the ``mode`` field within the ``associatedGroups`` field to associate Groups to and dissociate them from the Victim Asset. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.