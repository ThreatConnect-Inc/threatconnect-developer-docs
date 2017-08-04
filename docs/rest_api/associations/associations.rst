Associations
============

Retrieving Available Associations
---------------------------------

All of the available associations can be viewed by making a ``GET`` request to ``/v2/types/associationTypes``. This will return the name of the association and, if applicable, the Indicator/Group Resources between which the association can be created.

.. code::

    GET /v2/types/associationTypes/

To retrieve information about a specific association, use the following GET request format:

.. code::

    GET /v2/types/associationTypes/{associationTypeName}/

For example, the GET request below will return details about the ``Adversary`` association type:

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

.. note:: Custom association types can be created on an instance of ThreatConnect by a system administrator. Please contact your system administrator to create new types of associations.
