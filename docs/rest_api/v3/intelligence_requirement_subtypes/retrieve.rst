Retrieve Intelligence Requirement Subtypes
------------------------------------------

Retrieve All Intelligence Requirement Subtypes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all IR subtypes.

**Request**

.. code::

    GET /v3/intelRequirements/subtypes

**Response**

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Intelligence Requirement (IR)",
                "description": "Threats of overall concern to an organization (e.g., cyber threats, fraud, geopolitical/physical threats)"
            },
            {
                "id": 2,
                "name": "Priority Intelligence Requirement (PIR)",
                "description": "Threat actor motives; tactics, techniques, and procedures (TTPs); targets; impacts; or attributions in association with IRs"
            },
            {
                "id": 3,
                "name": "Specific Intelligence Requirement (SIR)",
                "description": "Facts associated with threat activity, such as indicators of compromise (IOCs)"
            },
            {
                "id": 4,
                "name": "Request for Information (RFI)",
                "description": "One-off requests for information related to topics of interest to particular stakeholders"
            },
            {
                "id": 5,
                "name": "Research Requirement (RR)",
                "description": "A topic or area of investigation that is of interest to an individual or group and does not merit a full intelligence requirement, but does require tracking of relevant information"
            }
        ],
        "count": 5,
        "status": "Success"
    }

Retrieve a Specific Intelligence Requirement Subtype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific IR subtype.

**Example Request**

.. code::

    GET /v3/intelRequirements/subtypes/{subtypeId}

For example, the following request will retrieve data for the IR subtype whose ID is 2.

**Request**

.. code::

    GET /v3/intelRequirements/subtypes/2

**Response**

.. code:: json

    {
        "data": {
            "id": 2,
            "name": "Priority Intelligence Requirement (PIR)",
            "description": "Threat actor motives; tactics, techniques, and procedures (TTPs); targets; impacts; or attributions in association with IRs"
        },
        "status": "Success"
    }