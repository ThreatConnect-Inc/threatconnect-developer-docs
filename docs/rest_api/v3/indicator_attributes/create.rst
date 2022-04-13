Create Indicator Attributes
---------------------------

The basic format for creating an Indicator Attribute is:

.. code::

    POST /v3/indicatorAttributes
    {
        "indicatorId": 12345,
        "type": "Attribute type goes here",
        "value": "Attribute value goes here"
    }

For example, the following query will create an Attribute and add it to the Indicator with ID 20:

.. code::

    POST /v3/indicatorAttributes
    {
        "indicatorId": 20,
        "source": "Phase of Intrusion",
        "type": "Additional Analysis and Context",
        "value": "Host used by hacker conglomerate traced to Iran."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 10,
            "type": "Additional Analysis and Context",
            "value": "Host used by hacker conglomerate traced to Iran.",
            "source": "Phase of Intrusion",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "role": "Api User"
            },
            "dateAdded": "2021-11-09T13:32:37Z",
            "lastModified": "2021-11-09T13:32:37Z",
            "default": false
        },
        "message": "Created",
        "status": "Success"
    }


Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``indicatorAttributes`` object.

.. hint::
    Indicator Attributes can also be created when creating an Indicator. See the “Create Indicators” section of `Indicators <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_ for more information.