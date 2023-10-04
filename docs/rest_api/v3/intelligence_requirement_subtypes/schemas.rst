Schemas
-------

Response Body
^^^^^^^^^^^^^

The default response returned from successful GET requests to the ``/v3/intelRequirements/subtypes`` endpoint includes one or more objects with the following fields:

* ``id``: <*Integer*> The IR subtype's ID number.
* ``name``: <*String*> The IR subtype's name.
* ``description``: <*String*> The IR subtype's description.

**Example**

.. code:: json

    {
        "id": <int>,
        "name": "<string>",
        "description": "<string>"
    }