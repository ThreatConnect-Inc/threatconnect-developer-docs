Retrieve Security Labels
------------------------

Retrieve All Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Security Labels:

.. code::

    GET /v3/securityLabels

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "TLP:WHITE",
                "description": "This security label is used for information that carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release.",
                "color": "FFFFFF",
                "owner": "System",
                "dateAdded": "2016-08-31T00:00:00Z"
            },
            {
                "id": 2,
                "name": "TLP:GREEN",
                "description": "This security label is used for information that is useful for the awareness of all participating organizations as well as with peers within the broader community or sector.",
                "color": "33FF00",
                "owner": "System",
                "dateAdded": "2016-08-31T00:00:00Z"
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Security Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Security Label:

.. code::

    GET /v3/securityLabel/{securityLabelId}

For example, the following request will retrieve data for the Security Label whose ID is 3:

.. code::

    GET /v3/securityLabels/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "TLP:AMBER",
            "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved. Information with this label can be shared with members of an organization and its clients.",
            "color": "FFC000",
            "owner": "System",
            "dateAdded": "2016-08-31T00:00:00Z"
        },
        "status": "Success"
    }