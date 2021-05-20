Update Artifacts
----------------

To update an Artifact, the basic format is:

.. code::

    PUT /v3/artifacts/{artifactID}
    {
        {updatedField}: {updatedValue}
    }

Refer to the following table for a list of available fields that can be updated for the ``artifacts`` object:

+--------------+-------------------------------------------------------------------------------+----------+
| Field        | Description                                                                   | Type     |
+==============+===============================================================================+==========+
| derivedLink  | Specifies whether the Artifact should be used to potentially associate Cases  | Boolean  |
+--------------+-------------------------------------------------------------------------------+----------+
| fileData     | Base64-encoded file attachment (required only for certain Artifact types)     | String   |
+--------------+-------------------------------------------------------------------------------+----------+
| source       | The name of the user who entered the Artifact into the Case                   | String   |
+--------------+-------------------------------------------------------------------------------+----------+
| summary      | The data contained in the Artifact                                            | String   |
+--------------+-------------------------------------------------------------------------------+----------+

For example, the query below will update the summary for the Artifact with ID 1.

.. code::

    PUT /v3/artifacts/1
    {
      "summary": "verybadguy@bad.com"
    }

JSON Response:

.. code:: json

    {
      "data": {
        "id": 1,
        "summary": "verybadguy@bad.com",
        "type": "Email Address",
        "intelType": "indicator-EmailAddress",
        "dateAdded": "2021-04-22T19:24:06Z",
        "derivedLink": True,
        "hashCode": "bR3jGyx3DqnOrXQ/dI/pYeYOpGOgxalv64tymVN661M="
      },
      "message": "Updated",
      "status": "Success"
    }