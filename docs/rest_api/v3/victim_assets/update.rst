Update Victim Assets
--------------------

The basic format for updating a Victim Asset is:

.. code::

    PUT /v3/victimAssets/{victimAssetId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request for the ``victimAssets`` object.

.. note::
    When updating a Victim, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedGroups``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.

For example, the following query will complete the following actions for a Victim Asset with ID 3:

- Associate the ``Bad Incident`` Group to the Victim Asset
- Update the website associated with the Victim Asset.

.. code::

    PUT /v3/victimAssets/3
    {
        "associatedGroups": {"data": [{"name": "Bad Incident", "type": "Incident"}]},
        "website": "hackerwebsite.com"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "WebSite",
            "victimId": 2
            "website": "hackerwebsite.com"
        },
        "message": "Updated",
        "status": "Success"
    }
