Update Tags
-----------

The basic format for updating a Tag is:

.. code::

    PUT /v3/tags/{tagId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can included in the body of a PUT request for the ``tags`` object.

For example, the following query will rename the Tag with ID 1 to ``Phishing Attack``:

.. code::

    PUT/v3/tags/1
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