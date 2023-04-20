Create Victim Assets
--------------------

The following example illustrates the basic format for creating a Victim Asset:

.. code::

    POST /v3/victimAssets
    {
        "type": "Victim Asset type goes here",
        "victimId": 12345
        //additional fields for the selected Victim Asset type
    }

For example, the following request will create a Phone Victim Asset and add it to the Victim with ID 2:

.. code::

    POST /v3/victimAssets
    {
        "phone": "0123456789",
        "type": "Phone",
        "victimId": 2
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 4,
            "type": "Phone",
            "victimId": 2,
            "phone": "0123456789",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request to the ``/v3/victimAssets`` endpoint.