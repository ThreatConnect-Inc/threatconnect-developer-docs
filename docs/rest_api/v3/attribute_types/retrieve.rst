Retrieve Attribute Types
------------------------

Retrieve All Attribute Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Attribute Types:

.. code::

    GET /v3/attributeTypes

JSON Response:

.. code:: json

    {
        "next": "https://app.threatconnect.com/api/v3/attributeTypes?resultStart=100&resultLimit=100",
        "data": [
            {
                "id": 1,
                "name": "Course of Action Taken",
                "description": "Describe the Course of Action Taken.",
                "maxSize": 500,
                "allowMarkdown": true,
                "errorMessage": "Please enter a valid Course of Action."
            },
            {
                "id": 2,
                "name": "Infrastructure Ownership",
                "description": "Select ownership details of the Infrastructure (IP Address, Domain Name, URL, etc) used in an Adversary operation.",
                "maxSize": 19,
                "allowMarkdown": false,
                "errorMessage": "Please enter valid infrastructure ownership details: Adversary Owned, Adversary Leased, Adversary Subverted",
                "validationRule": {
                    "id": 12,
                    "name": "Adversary Ownership",
                    "text": "Adversary Owned;Adversary Leased;Adversary Subverted;Unknown;",
                    "type": "SelectOne",
                    "description": "Infrastructure Ownership Types",
                    "version": "1"
                }
            },
            {...}
        ],
        "count": 214,
        "status": "Success"
    }


Retrieve a Specific Attribute Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Attribute Type:

.. code::

    GET /v3/attributeTypes/{attributeTypeId}

For example, the following request will retrieve data for the Attribute Type whose ID is 3:

.. code::

    GET /v3/attributeTypes/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "TTP Description: Malware/Tool Information",
            "description": "Malware and hackertools usage characteristics: backdoor, self-propagating, rootkit, pass-the-hash, keylogger, Other.",
            "maxSize": 500,
            "allowMarkdown": true,
            "errorMessage": "Please enter a valid TTP Description: Malware/Tool Information."
        },
        "status": "Success"
    }