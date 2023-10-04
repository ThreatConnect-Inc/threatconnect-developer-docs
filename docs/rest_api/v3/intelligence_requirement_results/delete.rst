Delete Intelligence Requirement Results
---------------------------------------

Send a request in the following format to delete a result.

**Example Request**

.. code::

    DELETE /v3/intelRequirements/results/{resultId}

For example, the following request will delete the result ID is 14.

**Request**

.. code::

    DELETE /v3/intelRequirements/results/14

**Response**

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }

.. note::
    Deleting a result does not delete the Artifact, Case, Group, Indicator, Tag, or Victim to which it corresponds.