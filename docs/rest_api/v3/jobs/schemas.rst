Schemas
-------

Response Body
^^^^^^^^^^^^^

The default response returned from a successful GET request to the ``/v3/jobs`` endpoint includes one or more objects with the following fields:

* ``id``: <*Integer*> The Job's ID number.
* ``name``: <*String*> The Job's name.
* ``displayName``: <*String*> The name of the App to which the Job corresponds. This is the name of the App as it is shown in TC Exchange.
* ``programName``: <*String*> The name of the App to which the Job corresponds.
* ``programVersion``: <*String*> The version of the App to which the Job corresponds.
* ``active``: <*Boolean*> Specifies whether the Job is active.

**Example**

.. code:: json

    {
        "id": <int>,
        "name": "<string>",
        "displayName": "<string>",
        "programName": "<string>",
        "programVersion": "<string>",
        "active": <boolean>
    }