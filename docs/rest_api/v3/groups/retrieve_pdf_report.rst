Retrieve a PDF Report for a Group
---------------------------------

Send a request in the following format to retrieve a PDF report for a Group:

**Example Request (Group ID)

.. code::

    GET /v3/groups/{groupId}/pdf

**Example Request (Group XID)

.. code::

    GET /v3/groups/{groupXid}/pdf?owner={ownerName}

You can retrieve PDF reports for the following Group types:

- Adversary
- Attack Pattern
- Campaign
- Course of Action
- Event
- Incident
- Intrusion Set
- Malware
- Report
- Tactic
- Threat
- Tool
- Vulnerability