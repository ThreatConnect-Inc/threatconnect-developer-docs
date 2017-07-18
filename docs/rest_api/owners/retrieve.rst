Retrieve Owners
---------------

To retrieve a list of all available owners, use the following query:

.. code::

    /v2/owners

Here is an example query:

.. code::

    source

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "owner": [
          {
            "id": 0,
            "name": "Exemplary Organization",
            "type": "Organization"
          },
          {
            "id": 1,
            "name": "Common Community",
            "type": "Community"
          },
        ]
      }
    }

Notes or caviates here...
