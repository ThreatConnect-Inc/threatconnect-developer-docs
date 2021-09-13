v3 REST API
===========

Case Management
---------------

Case Management and the Workflow feature in ThreatConnect allow users to combine manual and automated operations to define consistent and standardized processes for their security teams, including, but not limited to:

•	Malware analysis
•	Phishing triage
•	Alert triage
•	Intel requirement development
•	Escalation procedures
•	Breach SOP

Workflow in ThreatConnect supports the concept of Case Management, which gives users the capability to investigate and track information security threats and incidents by:

•	Minimizing the time it takes to match a case to historical data 
•	Minimizing the time it takes to assess scope 
•	Minimize the time it takes to assess impact 
•	Maximizing the amount of information that can be turned into actionable intelligence for later use

Components of Case Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    artifacts/artifacts
    artifact_types/artifact_types
    cases/cases
    notes/notes
    tasks/tasks
    workflow_events/workflow_events
    workflow_templates/workflow_templates
    
.. note:: To add, edit, and delete Case Management data, the API user’s Organization role must be set to **Organization Administrator**.

Attribute Types
---------------

.. toctree::
    :maxdepth: 1

    attribute_types/attribute_types


Methods
-------

.. toctree::
    :maxdepth: 1

    additional_fields
    bulk_delete
    filter_results
    users_list

Additional information about each method and how they relate to v3 API is available in the `API Versioning <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#api-versioning>`__ section in this documentation.
