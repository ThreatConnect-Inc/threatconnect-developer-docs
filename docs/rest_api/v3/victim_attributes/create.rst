Create Victim Attributes
------------------------

The following example illustrates the basic format for creating a Victim Attribute:

.. code::

    POST /v3/victimAttributes
    {
        "victimId": 12345,
        "type": "Attribute type goes here",
        "value": "Attribute value goes here"
    }

For example, the following request will create an Attribute and add it to the Victim whose ID is 2:

.. code::

    POST /v3/victimAttributes
    {
        "victimId": 2,
        "source": "Phase of Intrusion",
        "type": "Additional Analysis and Context",
        "value": "Based on additional analysis, it was determined that this victim's bank account was hacked."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 10,
            "dateAdded": "2021-11-09T15:43:06Z",
            "type": "Additional Analysis and Context",
            "value": "Based on additional analysis, it was determined that this victim's bank account was hacked.",
            "source": "Phase of Intrusion",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "lastModified": "2021-11-09T15:43:06Z",
            "pinned": false,
            "default": false
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request to the ``/v3/victimAttributes`` endpoint.

.. hint::
    Victim Attributes can also be created and added to a Victim when creating the Victim. See the “Create Victims” section of `Victims <https://docs.threatconnect.com/en/latest/rest_api/v3/victims/victims.html>`_ for more information.