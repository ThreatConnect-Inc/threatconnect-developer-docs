Update Victim Attributes
------------------------

The basic format for updating a Victim Attribute is:

.. code::

    PUT /v3/victimAttributes/{victimAttributeId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request for the ``victimAttributes`` object.

For example, the following query will update the value of the Victim Attribute with ID 1 and make it the default Attribute of its type:

.. code::

    PUT /v3/victimAttributes/1
    {
        "default": true,
        "value": "Based on additional analysis, it was determined that this victim’s social media, bank, and email accounts were hacked as the result of a phishing attack."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 1,
            "type": "Additional Analysis and Context",
            "value": "Based on additional analysis, it was determined that this victim’s bank account was hacked.",
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
            "default": true
        },
        "message": "Updated",
        "status": "Success"
    }
