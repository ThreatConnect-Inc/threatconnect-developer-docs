Delete Posts
------------

.. code:: http

   DELETE /v3/posts

Delete a specific post.

Requirements
^^^^^^^^^^^^

- To delete posts in an Organization, your API user account must have an Organization role of Organization Administrator.
- To delete posts in a Community or Source, your API user account must have a Community role of Editor or Director for that Community or Source.

Query Parameters
^^^^^^^^^^^^^^^^

The following table outlines the query parameters that may be used when sending a DELETE request to the ``/v3/posts`` endpoint.

.. list-table::
   :widths: 25 35 15 15 15
   :header-rows: 1

   * - Parameter
     - Description
     - Data Type
     - Default Value
     - Required?
   * - ``createActivityLog``
     - Specifies whether to `create an activity log <hhttps://docs.threatconnect.com/en/latest/rest_api/v3/create_activity_logs.html>`_ for the requested action.
     - Boolean
     - false
     - Optional

Example Request
^^^^^^^^^^^^^^^

.. note::
   In addition to the required ``Content-Type`` header, you must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`__.

**Request**

.. code:: http

    DELETE /v3/posts
    Content-Type: application/json

    {
        "id": 3
    }

**Response**

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }