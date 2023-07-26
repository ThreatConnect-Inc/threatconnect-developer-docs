Create Tags
-----------

The following example illustrates the basic format for creating a Tag:

.. code::

    POST /v3/tags
    {
        "name": "Tag name goes here",
        "description": "Tag description goes here"
    }

For example, the following request will create a Tag named **Ransomware**:

.. code::

    POST /v3/tags
    {
        "name": "Ransomware",
        "description": "Apply this Tag to objects related to ransomware attacks."
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

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request to the ``/v3/tags`` endpoint.

.. attention::
    If you created a new Tag that matches a synonymous Tag listed in a `Tag normalization rule <https://knowledge.threatconnect.com/docs/tag-normalization>`_, it will be converted to the main Tag listed in the rule. Similarly, if you created a new Tag that `matches an ATT&CK Tag <https://knowledge.threatconnect.com/docs/attack-tags#converting-standard-tags-to-attck-tags>`_, it will be converted to that ATT&CK Tag.