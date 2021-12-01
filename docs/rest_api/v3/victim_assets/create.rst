Create Victim Assets
--------------------

The basic format for creating a Victim Asset is:

.. code::

    POST /v3/victimAssets/
    {
        "type": "Victim Asset type goes here",
        "victimId": 12345
        //additional fields for the selected Victim Asset type
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can included in the body of a POST request for the ``victimAssets`` object.

For example, the following query will create a Phone Victim Asset and add it to the Victim with ID 2:

.. code::

    POST /v3/victimAssets/
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
            "phone": "0123456789"
        },
        "message": "Created",
        "status": "Success"
    }