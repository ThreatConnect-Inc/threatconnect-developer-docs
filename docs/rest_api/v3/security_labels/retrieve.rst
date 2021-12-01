Retrieve Security Labels
------------------------

Retrieve All Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Security Labels, use the following query:

.. code::

    GET /v3/securityLabels/

JSON Response:

.. code:: json

    {
        "data": [{
            "id": 1,
            "name": "TLP:WHITE",
            "description": "This security label is used for information that carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release.",
            "color": "FFFFFF",
            "owner": "System",
            "dateAdded": "2016-08-31T00:00:00Z"
        }, {
            "id": 2,
            "name": "TLP:GREEN",
            "description": "This security label is used for information that is useful for the awareness of all participating organizations as well as with peers within the broader community or sector.",
            "color": "33FF00",
            "owner": "System",
            "dateAdded": "2016-08-31T00:00:00Z"
        }, {
            "id": 3,
            "name": "TLP:AMBER",
            "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
            "color": "FFC000",
            "owner": "System",
            "dateAdded": "2016-08-31T00:00:00Z"
        }, {
            "id": 4,
            "name": "TLP:RED",
            "description": "This security label is used for information that cannot be effectively acted upon by additional parties, and could lead to impacts on a party"s privacy, reputation, or operations if misused.",
            "color": "FF0033",
            "owner": "System",
            "dateAdded": "2016-08-31T00:00:00Z"
        }],
        "status": "Success"
    }

Retrieve a Single Security Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Security Label, use a query in the following format:

.. code::

    GET /v3/securityLabel/{securityLabelId}

For example, the following query will return information about the Security Label with ID 2:

.. code::

    GET /v3/securityLabels/2

JSON Response:

.. code:: json

    {
        "data": {
            "id": 2,
            "name": "TLP:GREEN",
            "description": "This security label is used for information that is useful for the awareness of all participating organizations as well as with peers within the broader community or sector.",
            "color": "33FF00",
            "owner": "System",
            "dateAdded": "2016-08-31T00:00:00Z"
        },
        "status": "Success"
    }

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
