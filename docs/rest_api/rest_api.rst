.. include:: <isonum.txt> 
REST API
===========

Getting Started
---------------

.. toctree::
   :maxdepth: 2

   quick_start

----

v3 API
------

Overview
^^^^^^^^
.. toctree::
   :maxdepth: 1

   v3/available_endpoints
   v3/postman_config

Features
^^^^^^^^

.. toctree::
   :maxdepth: 1

   v3/create_activity_logs
   v3/associations
   v3/bulk_delete
   v3/enable_pagination
   v3/filter_results
   v3/http_status_codes
   v3/additional_fields
   v3/retrieve_fields
   v3/retrieve_open_api_doc
   v3/return_count
   v3/sort_results
   v3/specify_owner
   v3/update_metadata

Case Management Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: v3/case_management/case_management.rst

.. attention::
   To add, edit, and delete Case Management data, the API user must have an Organization role of **Organization Administrator**.

.. toctree::
   :maxdepth: 2
   
   v3/case_management/artifact_types/artifact_types
   v3/case_management/artifacts/artifacts
   v3/case_management/case_attributes/case_attributes
   v3/case_management/cases/cases
   v3/case_management/notes/notes
   v3/case_management/tasks/tasks
   v3/case_management/workflow_events/workflow_events
   v3/case_management/workflow_templates/workflow_templates

Threat Intelligence Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   v3/group_attributes/group_attributes
   v3/groups/groups
   v3/indicator_attributes/indicator_attributes
   v3/indicator_enrichment/indicator_enrichment
   v3/indicators/indicators
   v3/exclusion_lists/exclusion_lists
   v3/intelligence_requirements/intelligence_requirements
   v3/intelligence_requirement_categories/intelligence_requirement_categories
   v3/intelligence_requirement_results/intelligence_requirement_results
   v3/intelligence_requirement_subtypes/intelligence_requirement_subtypes
   v3/posts/posts
   v3/security_labels/security_labels
   v3/tags/tags
   v3/victim_assets/victim_assets
   v3/victim_attributes/victim_attributes
   v3/victims/victims

Miscellaneous Endpoints
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   v3/attribute_types/attribute_types
   v3/job_executions/job_executions
   v3/jobs/jobs
   v3/owner_roles/owner_roles
   v3/owners/owners
   v3/playbook_executions/playbook_executions
   v3/playbooks/playbooks
   v3/system_roles/system_roles
   v3/user_groups/user_groups
   v3/users/users

TC Exchange Administration Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   v3/tc_exchange_administration/tc_exchange_administration

----

v2 API
------

.. toctree::
   :maxdepth: 2

   overview
   v2/associations/associations
   v2/attributes/attributes
   v2/batch_api/batch_api
   v2/custom_metrics/custom_metrics
   v2/groups/groups
   v2/indicators/indicators
   v2/notifications/notifications
   v2/owners/owners
   v2/playbooks/playbooks
   v2/security_labels/security_labels
   v2/tags/tags
   v2/tasks/tasks
   v2/victims/victims

----

TAXII Services
--------------

.. toctree::
   :maxdepth: 2

   taxii/taxii_2.1
   taxii/taxii