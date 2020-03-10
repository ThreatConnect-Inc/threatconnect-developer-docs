Case Management
===============

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
-----------------------------

Case
^^^^

A case contains all required elements of a notable event in a logical structure. It is used to build an incident or capture key evidence to enable the security team to decide if a case should be escalated.

Endpoint: /api/v3/cases

Workflow Template
^^^^^^^^^^^^^^^^^

Workflow starts with the creation of Workflow templates, which are processes users define for their team. A user, for example, might create one template for phishing analysis, one for alert triage, and maybe several different ones for handling breaches. By codifying these processes in a template, users can reduce the risk of missing critical steps or artifacts during an investigation, because processes and procedures that are stored externally can be captured in ThreatConnect and tied back to threat intel.

Endpoint: /api/v3/workflowTemplates

Task
^^^^

A task is an individual unit of work that a user must perform to complete a case. Tasks can be manual (a user performs them) or automated (a Playbook performs them).

Endpoint: /api/v3/tasks

Artifact
^^^^^^^^

An artifact is used in a case to collect key evidence to support the Workflow. Not all artifacts are significant and some can be loosely correlated to Threat Intelligence. Examples of artifacts include domains, email addresses, log files, email, PCAP, screen shots, SIEM event files, and malware documents.

Endpoint: /api/v3/artifacts

Note
^^^^

A note is the primary mechanism to capture the progress of a case in human-readable form. Notes enable a security team to journal key data findings in unstructured form.

Endpoint: /api/v3/notes

Methods
^^^^^^^

For an explanation of methods and how they relate to v3 Api, refer to the ####### section in this documentation.




  1. `Discovery Service <#discovery-service>`__ : Provides information about offered TAXII Services
  


