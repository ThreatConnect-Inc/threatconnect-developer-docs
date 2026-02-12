Create Posts
------------

.. code:: http

   POST /v3/posts

Create a post and add it to a specific object.

Requirements
^^^^^^^^^^^^

- To create posts in an Organization, your API user account must have an Organization role of Organization Administrator.
- To create posts in a Community or Source, your API user account must have a Community role of Editor or Director for that Community or Source.

Query Parameters
^^^^^^^^^^^^^^^^

The following table outlines the query parameters that may be used when sending a POST request to the ``/v3/posts`` endpoint.

.. list-table::
   :widths: 25 35 15 15 15
   :header-rows: 1

   * - Parameter
     - Description
     - Data Type
     - Default Value
     - Required?
   * - ``createActivityLog``
     - Specifies whether to `create an activity log <https://docs.threatconnect.com/en/latest/rest_api/v3/create_activity_logs.html>`_ for the requested action.
     - Boolean
     - false
     - Optional
   * - ``fields``
     - `Returns additional fields in the API response <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_ based on one or more specified values.
     - String
     - N/A
     - Optional

Example Request
^^^^^^^^^^^^^^^

.. note::
   In addition to the required ``Content-Type`` header, you must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`__.

**Request**

.. code:: http

    POST /v3/posts
    Content-Type: application/json

    {
        "text": "A third post about Bad Guy",        
        "objectType": "Group",        
        "objectId" : 12345
    }

**Response**

.. code:: json

    {
        "data": {
            "id": 30,
            "owner": "Demo Organization",
            "ownerId": 1,
            "name": "Indicator-Address-IPv6",
            "description": "1 fixed, 1 variable",
            "active": true,
            "managed": false
        },
        "message": "Created",
        "status": "Success"
    }