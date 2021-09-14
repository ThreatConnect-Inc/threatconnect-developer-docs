Delete Tasks
------------

To delete a Task, the most basic format is:

.. code::

    DELETE /v2/tasks/{taskId}
  
For example, the query below will delete the Task with ID 12345:

.. code::

    DELETE /v2/tasks/12345

JSON Response:

.. code:: json

    {
        "apiCalls": 1,
        "resultCount": 0,
        "status": "Success"
    }

Delete Task Metadata
--------------------

Delete Task Attributes
^^^^^^^^^^^^^^^^^^^^^^

To delete an Attribute from a Task, use the following format:

.. code::

    DELETE /v2/tasks/{taskId}/attributes/{attributeId}

For example, if you want to delete the Attribute with ID 54321 from the Task with ID 12345, you would use the following query:

.. code::

    DELETE /v2/tasks/12345/attributes/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

To delete a Security Label from an Attribute, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    DELETE /v2/tasks/{taskId}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will remove the ``TLP Amber`` Security Label from the Attribute with ID 54321 on the Task:

.. code::

    DELETE /v2/tasks/12345/attributes/54321/securityLabels/TLP%20Amber

Delete Task Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a Security Label from a Task, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label:

.. code::

    DELETE /v2/tasks/{taskId}/securityLabels/{securityLabel}

For example, the query below will delete the ``TLP Amber`` Security Label to the Task with ID 12345:

.. code::

    DELETE /v2/tasks/12345/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Delete Task Tags
^^^^^^^^^^^^^^^^

To delete a Tag from a Task, use the following format, where ``{tagName}`` is replaced with the name of the Tag you wish to remove from the Task:

.. code::

    DELETE /v2/tasks/{taskId}/tags/{tagName}

For example, the query below will delete the ``Nation State`` Tag to the Task with ID 12345:

.. code::

    DELETE /v2/tasks/12345/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Delete/Disassociate Task Associations
-------------------------------------

Disassociate Group from Task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Task from a Group, use a query in the following format:

.. code::

    DELETE /v2/tasks/{taskId}/groups/{associatedGroupType}/{associatedGroupId}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, the query below will disassociate a Task with ID 12345 from an Incident with the ID 54321:

.. code::

    DELETE /v2/tasks/12345/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Disassociate Indicator from Task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Task from an Indicator, use a query in the following format:

.. code::

    DELETE /v2/tasks/{taskId}/indicators/{associatedIndicatorType}/{associatedIndicator}

For example, the query below will disassociate the Task with ID 12345 from the IP Address ``0.0.0.0``:

.. code::

    DELETE /v2/tasks/12345/indicators/addresses/0.0.0.0

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Disassociate Victim Asset from Task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Task from a Victim Asset, use a query in the following format:

.. code::

    DELETE /v2/tasks/{taskId}/victimAssets/{victimAssetType}/{victimAssetId}

For example, the query below will disassociate the Task with ID 12345 from the Victim Asset with ID 54321:

.. code::

    DELETE /v2/tasks/12345/victimAssets/emailAddresses/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }


Disassociate Victim from Task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Task from a Victim, use a query in the following format:

.. code::

    DELETE /v2/tasks/{taskId}/victims/{victimId}

For example, the query below will disassociate the Task with ID 12345 from the Victim with ID 54321:

.. code::

    DELETE /v2/tasks/12345/victims/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
