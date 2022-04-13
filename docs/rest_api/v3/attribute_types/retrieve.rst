Retrieve Attribute Types
------------------------

Retrieve All Attribute Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Attribute Types, use the following query:

.. code::

    GET /v3/attributeTypes

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Course of Action Taken",
                "description": "Describe the Course of Action Taken.",
                "maxSize": 500,
                "allowMarkdown": true,
                "errorMessage": "Please enter a valid Course of Action.",
                "systemRequired": false
            },
            {
                "id": 2,
                "name": "Infrastructure Ownership",
                "description": "Select ownership details of the Infrastructure (IP Address, Domain Name, URL, etc) used in an Adversary operation.",
                "maxSize": 19,
                "allowMarkdown": false,
                "errorMessage": "Please enter valid infrastructure ownership details: Adversary Owned, Adversary Leased, Adversary Subverted",
                "systemRequired": false,
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
        "status": "Success"
    }


Retrieve a Single Attribute Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Attribute Type, use a query in the following format:

.. code::

    GET /v3/attributeTypes/{attributeTypeId}

For example, the following query will return information about the Attribute Type with ID 3:

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
            "errorMessage": "Please enter a valid TTP Description: Malware/Tool Information.",
            "systemRequired": false
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
