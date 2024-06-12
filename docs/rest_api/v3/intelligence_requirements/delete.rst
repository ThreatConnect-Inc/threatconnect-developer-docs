Delete Intelligence Requirements
--------------------------------

Send a request in the following format to delete an IR. Note that ``{intelRequirementId}`` represents the value of the ``id`` field for an IR, not the value of the ``uniqueId`` field.

**Example Request**

.. code::

    DELETE /v3/intelRequirements/{intelRequirementId}

For example, the following request will delete the IR whose ID is 10:

**Request**

.. code::

    DELETE /v3/intelRequirements/10

**Response**

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }