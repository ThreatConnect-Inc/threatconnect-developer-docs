Update Tags
-----------

The following example illustrates the basic format for updating a Tag:

.. code::

    PUT /v3/tags/{tagId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }

For example, the following request will rename the Tag whose ID is 1 from **Ransomware** to **Ransomware Attack**:

.. code::

    PUT /v3/tags/1
    Content-Type: application/json
    
    {
        "name": "Ransomware Attack"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 1,
            "name": "Ransomware Attack",
            "owner": "Demo Organization",
            "description": "Apply this Tag to objects related to ransomware attacks.",
            "lastUsed": "2021-11-08T18:01:36Z"
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/tags`` endpoint.