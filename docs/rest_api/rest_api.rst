.. include:: <isonum.txt> 
REST API
===========

Getting Started
---------------

.. toctree::
   :maxdepth: 2

   quick_start

v3 REST API
-----------

Case Management
^^^^^^^^^^^^^^^

.. include:: v3/case_management/case_management.rst

.. toctree::
   :maxdepth: 2

   v3/case_management/artifacts/artifacts
   v3/case_management/artifact_types/artifact_types
   v3/case_management/cases/cases
   v3/case_management/notes/notes
   v3/case_management/tasks/tasks
   v3/case_management/workflow_events/workflow_events
   v3/case_management/workflow_templates/workflow_templates
    
.. note:: To add, edit, and delete Case Management data, the API user’s Organization role must be set to **Organization Administrator**.

Attribute Types
^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   v3/attribute_types/attribute_types


Additional Actions
^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   v3/additional_fields
   v3/bulk_delete
   v3/filter_results
   v3/users_list

v2 REST API
-----------

.. toctree::
   :maxdepth: 2

   overview
   v2/associations/associations
   v2/attributes/attributes
   v2/custom_metrics/custom_metrics
   v2/groups/groups
   v2/indicators/indicators
   v2/notifications/notifications
   v2/owners/owners
   v2/playbooks/playbooks
   v2/security_labels/security_labels
   v2/tags/tags
   v2/tasks/tasks
   v2/taxii/taxii
   v2/victims/victims
