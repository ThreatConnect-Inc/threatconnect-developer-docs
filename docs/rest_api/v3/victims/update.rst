Update Victims
--------------

The following example illustrates the basic format for updating a Victim:

.. code::

    PUT /v3/victims/{victimId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }

For example, the following request will perform the following actions for the Victim whose ID is 2:

- Add a **WebSite** Victim Asset to the Victim
- Update the Victim's name
- Replace any Security Labels applied to the Victim with the **TLP: RED** Security Label

.. hint::
    To include the ``assets`` and ``securityLabels`` fields in the API response, append ``?fields=assets&fields=securityLabels`` to the end of the request URL.

.. code::

    PUT /v3/victims/2
    Content-Type: application/json
    
    {
        "assets": {
            "data": [
                {
                    "website": "evilll.com",
                    "type": "WebSite"
                }
            ]
        },
        "name": "Jane Doe",
        "securityLabels": {
            "data": [
                {
                    "name": "TLP:RED"
                }
            ],
            "mode": "replace"
        }
    }


JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2",
            "name": "Jane Doe",
            "org": "Company ABC",
            "suborg": "HR Department",
            "workLocation": "Washington, D.C.",
            "nationality": "American"
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/victims`` endpoint.

.. hint::
    When updating a Victim, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedGroups``
    - ``attributes``
    - ``securityLabels``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.