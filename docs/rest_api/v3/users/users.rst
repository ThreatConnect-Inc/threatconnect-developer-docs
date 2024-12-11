=====
Users
=====

Users can perform a variety of actions in ThreatConnect depending on their user account type and their System and Organization role. In addition, users can be assigned to `Workflow Cases <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html>`_, `Workflow Tasks <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/tasks/tasks.html>`_, and `Task Groups <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html#task>`_.

Endpoint: ``/api/v3/security/users``

.. attention::

    Only API users with an Organization role of Organization Administrator can create, update, and delete users; however, they may not perform these actions for users whose System role is **Administrator**, **Community Leader**, **Operations Administrator**, or **Super User**. API users with any other Organization role can only retrieve users.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst