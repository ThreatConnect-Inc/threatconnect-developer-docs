Schemas
-------

Response Body
^^^^^^^^^^^^^

The default response returned from successful GET requests to the ``/v3/intelRequirements/categories`` endpoint includes one or more objects with the following fields:

* ``id``: <*Integer*> The IR category's ID number.
* ``name``: <*String*> The IR category's name.
* ``description``: <*String*> The IR category's description.

**Example**

.. code:: json

    {
        "id": <int>,
        "name": "<string>",
        "description": "<string>"
    }