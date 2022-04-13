Create Victim Attributes
------------------------

The basic format for creating a Victim Attribute is:

.. code::

    POST /v3/victimAttributes
    {
        "victimId": 12345,
        "type": "Attribute type goes here",
        "value": "Attribute value goes here"
    }

For example, the following query will create an Attribute and add it to the Victim with ID 2:

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
            "id": 1,
            "type": "Additional Analysis and Context",
            "value": "Based on additional analysis, it was determined that this victim's bank account was hacked.",
            "source": "Phase of Intrusion",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "role": "Api User"
            },
            "dateAdded": "2021-11-09T15:43:06Z",
            "lastModified": "2021-11-09T15:43:06Z",
            "default": false
        },
        "message": "Created",
        "status": "Success"
    }


Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``victimAttributes`` object.

.. hint::
    Victim Attributes can also be created when creating a Victim. See the “Create Victims” section of `Victims <https://docs.threatconnect.com/en/latest/rest_api/v3/victims/victims.html>`_ for more information.