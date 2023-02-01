Create Indicator Attributes
---------------------------

The following example illustrates the basic format for creating an Indicator Attribute:

.. code::

    POST /v3/indicatorAttributes
    {
        "indicatorId": 12345,
        "type": "Attribute type goes here",
        "value": "Attribute value goes here"
    }

For example, the following request will create an Attribute and add it to the Indicator whose ID is 20:

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
            "dateAdded": "2021-11-09T13:32:37Z",
            "type": "Additional Analysis and Context",
            "value": " Host used by hacker conglomerate traced to Iran.",
            "source": "Phase of Intrusion",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "lastModified": "2021-11-09T13:32:37Z",
            "pinned": false,
            "default": false
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``indicatorAttributes`` object.

.. hint::
    Indicator Attributes can also be created and added to an Indicator when creating the Indicator. See the “Create Indicators” section of `Indicators <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_ for more information.