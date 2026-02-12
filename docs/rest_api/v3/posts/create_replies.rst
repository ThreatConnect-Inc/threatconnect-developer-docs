Create Post Replies
-------------------

.. code:: http

   POST /v3/posts/reply

Create a reply to a specific post.

Requirements
^^^^^^^^^^^^

- To create post replies in an Organization, your API user account must have an Organization role of Organization Administrator.
- To create post replies in a Community or Source, your API user account must have a Community role of Editor or Director for that Community or Source.

Query Parameters
^^^^^^^^^^^^^^^^

The following table outlines the query parameters that may be used when sending a POST request to the ``/v3/posts/reply`` endpoint.

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

    POST /v3/posts/reply
    Content-Type: application/json

    {
        "id": 1,
        "objectType": "Group",
        "objectId" : 12345,
        "replies": [
            {
                "text": "Reply to post about Bad Guy"
            }
        ]
    }

**Response**

.. code:: json

    {
        "data": {
            "id": 1,
            "author": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "authorType": "full",
            "dateAdded": "2026-01-10T20:56:55Z",
            "text": "Post generated using the v3 API",
            "linkedItems": [
                {
                    "id": "B12345",
                    "type": "Adversary",
                    "display": "Bad Guy",
                    "owner": "Demo Organization"
                }
            ],
            "deleteAvailable": true,
            "replies": [
                {
                    "sequenceId": "1.1",
                    "author": {
                        "id": 3,
                        "userName": "11112222333344445555",
                        "firstName": "John",
                        "lastName": "Smith",
                        "pseudonym": "jsmithAPI",
                        "owner": "Demo Organization"
                    },
                    "authorType": "full",
                    "text": "Reply to post about Bad Guy",
                    "deleteAvailable": true
                }
            ]
        },
        "message": "Created",
        "status": "Success"
    }