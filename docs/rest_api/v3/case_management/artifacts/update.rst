Update Artifacts
----------------

The following example illustrates the basic format for updating an Artifact:

.. code::

    PUT /v3/artifacts/{artifactId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following request will update the summary of the Artifact whose ID is 1:

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
            "derivedLink": true,
            "hashCode": "bR3jGyx3DqnOrXQ/dI/pYeYOpGOgxalv64tymVN661M="
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request to the ``/v3/artifacts`` endpoint.

.. hint::
    When updating an Artifact, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedGroups``
    - ``associatedIndicators``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.

.. note::
    To update an Artifact's ``fieldName``, the Artifact must belong to a Task, and that Task must contain multiple Artifact Fields that accept the Artifact's type. For more information about Artifact Fields, see the `"Artifact Fields" section of the Adding Tasks to a Case <https://knowledge.threatconnect.com/docs/adding-tasks-to-a-case#artifact-fields>`_ knowledge base article.