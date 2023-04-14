Update Tags
-----------

The following example illustrates the basic format for updating a Tag:

.. code::

    PUT /v3/tags/{tagId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following request will rename the Tag whose ID is 1 from **Phishing** to **Phishing Attack**:

.. code::

    PUT /v3/tags/1
    {
        "name": "Phishing Attack"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 1,
            "name": "Phishing Attack",
            "owner": "Demo Organization",
            "description": "Apply this Tag to objects related to phishing attacks.",
            "lastUsed": "2021-11-08T18:01:36Z"
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/tags`` endpoint.