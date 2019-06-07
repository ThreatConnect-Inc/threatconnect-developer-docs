Filtering Tasks
^^^^^^^^^^^^^^^

When retrieving Tasks from ThreatConnect, it is possible to filter the results. Results can be filtered on the following data points:

+-----------+-----------+--------------+
| Filter    | Data Type | Operator(s)  |
+===========+===========+==============+
| name      | string    | ``=``, ``^`` |
+-----------+-----------+--------------+
| dateAdded | date      | ``<``, ``>`` |
+-----------+-----------+--------------+
| status    | string    | ``=``, ``!`` |
+-----------+-----------+--------------+
| assignee  | string    | ``=``        |
+-----------+-----------+--------------+
| escalatee | string    | ``=``        |
+-----------+-----------+--------------+
| overdue   | boolean   | ``=``        |
+-----------+-----------+--------------+
| escalated | boolean   | ``=``        |
+-----------+-----------+--------------+
| dueDate   | date      | ``<``, ``>`` |
+-----------+-----------+--------------+
| reminded  | boolean   | ``=``        |
+-----------+-----------+--------------+

.. include:: ../_includes/filter_symbol_encoding_note.rst

The following query will return all Tasks that start with "Test" (``name^Test``):

.. code::

    GET /v2/tasks/?filters=name%5ETest

The following query will return all Tasks whose name is "Test" (``name=Test``):

.. code::

    GET /v2/tasks/?filters=name%3DTest

The following query will return all Tasks whose status is "Not Started" (``status=Not Started``):

.. code::

    GET /v2/tasks/?filters=status%3DNot%20Started

The following query will return all Tasks assigned to the user with the username "johndoe@example.com" (``assignee=johndoe@example.com``):

.. code::

    GET /v2/tasks/?filters=assignee%3Djohndoe%40example.com

The following query will return all Tasks that will be escalated to the user with the username "manager@example.com" (``escalatee=manager@example.com``):

.. code::

    GET /v2/tasks/?filters=escalatee%3Dmanager%40example.com

The following query will return all overdue Tasks (``overdue=true``):

.. code::

    GET /v2/tasks/?filters=overdue%3Dtrue

The following query will return all escalated Tasks (``escalated=true``):

.. code::

    GET /v2/tasks/?filters=escalated%3Dtrue

The following query will return all Tasks with a due date after 2017-07-25 (``dueDate>2017-07-25``):

.. code::

    GET /v2/tasks/?filters=dueDate%3E2017-07-25 

The following query will return all Tasks for which a reminder has been sent (``reminded=true``):

.. code::

    GET /v2/tasks/?filters=reminded%3Dtrue
