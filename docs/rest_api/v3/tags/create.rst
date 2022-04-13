Create Tags
-----------

The basic format for creating a Tag is:

.. code::

    POST /v3/tags
    {
        "name": "Tag name goes here",
        "description": "Tag description goes here"
    }

For example, the following query will create a ``Phishing`` Tag:

.. code::

    POST /v3/tags
    {
        "name": "Phishing",
        "description": "Apply this Tag to objects related to phishing attacks."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 1,
            "name": "Phishing",
            "owner": "Demo Organization",
            "description": "Apply this Tag to objects related to phishing attacks.",
            "lastUsed": "2021-11-08T18:01:36Z"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``tags`` object.