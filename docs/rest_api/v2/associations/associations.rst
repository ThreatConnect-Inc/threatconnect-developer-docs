Associations
============

Group Associations
------------------

* `Retrieve Group Associations <../groups/groups.html#retrieve-group-associations>`__
* `Create Group Associations <../groups/groups.html#create-group-associations>`__
* `Delete Group Associations <../groups/groups.html#delete-disassociate-group-associations>`__

Indicator Associations
----------------------

* `Retrieve Indicator Associations <../indicators/indicators.html#retrieve-indicator-associations>`__
* `Create Indicator Associations <../indicators/indicators.html#create-indicator-associations>`__
* `Delete Indicator Associations <../indicators/indicators.html#delete-disassociate-indicator-associations>`__

Tag Associations
----------------

* `Retrieve Tag Associations <../tags/tags.html#retrieve-tag-associations>`__

Task Associations
-----------------

* `Retrieve Task Associations <../tasks/tasks.html#retrieve-task-associations>`__
* `Create Task Associations <../tasks/tasks.html#create-task-associations>`__
* `Delete Task Associations <../tasks/tasks.html#delete-disassociate-task-associations>`__

Victim Associations
-------------------

* `Retrieve Victim Associations <../victims/victims.html#retrieve-victim-associations>`__
* `Create Victim Associations <../victims/victims.html#create-victim-associations>`__
* `Delete Victim Associations <../victims/victims.html#delete-disassociate-victim-associations>`__

Retrieving Available Associations
---------------------------------

All of the available Associations can be viewed by making a ``GET`` request to ``/v2/types/associationTypes``. This will return the name of the Association and, if applicable, the Indicator/Group Resources between which the Association can be created.

.. code::

    GET /v2/types/associationTypes/

To retrieve information about a specific Association, use the following GET request format:

.. code::

    GET /v2/types/associationTypes/{associationTypeName}/

For example, the GET request below will return details about the ``Adversary`` Association type:

.. code::

    GET /v2/types/associationTypes/Adversary/

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "associationType": {
          "name": "Adversary",
          "custom": "false",
          "fileAction": "false",
          "apiBranch": "adversaries"
        }
      }
    }

.. note:: Custom Association types can be created on an instance of ThreatConnect by a system administrator. Contact your system administrator to create new types of Associations.
