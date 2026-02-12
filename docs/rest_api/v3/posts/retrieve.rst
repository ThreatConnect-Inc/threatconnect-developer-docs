Retrieve Posts
--------------

Requirements
^^^^^^^^^^^^

- To retrieve posts in an Organization, your API user account can have any Organization role.
- To retrieve posts in a Community or Source, your API user account can have any Community role except Banned for that Community or Source.

Retrieve All Posts for a Specific Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: http

   GET /v3/posts?objectId={id}&objectType={type}

Retrieve details about all posts added to the specified object.

Query Parameters
""""""""""""""""

The following table outlines the query parameters that may be used when sending a GET request to the ``/v3/posts`` endpoint.

.. list-table::
   :widths: 25 35 15 15 15
   :header-rows: 1

   * - Parameter
     - Description
     - Data Type
     - Default Value
     - Required?
   * - ``objectId``
     - The ID number of the object to retrieve posts for.
     - Integer
     - N/A
     - Required
   * - ``objectType``
     - | The type of object to retrieve posts for.
       |
       | Acceptable values: **Group**, **Indicator**, **Organization**
     - String
     - N/A
     - Required
   * - ``count``
     - Specifies whether to `return a count of items <https://docs.threatconnect.com/en/latest/rest_api/v3/return_count.html>`_ in the API response.
     - Boolean
     - false
     - Optional
   * - ``fields``
     - `Returns additional fields <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_ in the API response based on one or more specified values.
     - String
     - N/A
     - Optional
   * - ``resultLimit``
     - The maximum number of objects to include each `result set <https://docs.threatconnect.com/en/latest/rest_api/v3/enable_pagination.html>`_ within the API response.
     - Integer
     - 100
     - Optional
   * - ``resultStart``
     - The starting index of the `result set <https://docs.threatconnect.com/en/latest/rest_api/v3/enable_pagination.html>`_ within the API response.
     - Integer
     - 0
     - Optional
   * - ``sorting``
     - The order and field by which to `sort results <https://docs.threatconnect.com/en/latest/rest_api/v3/sort_results.html>`_ in the API response.
     - String
     - N/A
     - Optional
   * - ``tql``
     - `Filters results <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_ based on the provided TQL query.
     - String
     - N/A
     - Optional

Example Request
"""""""""""""""

.. note::
   You must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`_.

**Request**

.. code:: http

   GET /v3/posts?objectId=12345&objectType=Group

**Response**

.. code:: json

    {
        "data": [
            {
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
                "text": "Post about Bad Guy",
                "linkedItems": [
                    {
                        "id": "B12345",
                        "type": "Adversary",
                        "display": "Bad Guy",
                        "owner": "Demo Organization"
                    }
                ],
                "linkedText": "Post generated using the v3 API",
                "aboutLinkedText": "<a href=\"https://app.threatconnect.com/#/details/groups/12345\">Bad Guy</a>",
                "linkedAuthor": "<a href=\"https://app.threatconnect.com/auth/profile/organization.xhtml?name=Demo+Organization\" >Demo Organization</a>&nbsp;/&nbsp;<a href=\"https://app.threatconnect.com/auth/profile/user.xhtml?id=3\" >John Smith</a>",
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
            {
                "id": 2,
                "author": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "owner": "Demo Organization"
                },
                "authorType": "full",
                "dateAdded": "2026-01-11T16:54:55Z",
                "text": "Another post about Bad Guy",
                "linkedItems": [
                    {
                        "id": "B12345",
                        "type": "Adversary",
                        "display": "Bad Guy",
                        "owner": "Demo Organization"
                    }
                ],
                "linkedText": "Another post about Bad Guy",
                "aboutLinkedText": "<a href=\"https://app.threatconnect.com/#/details/groups/12345\">Bad Guy</a>",
                "linkedAuthor": "<a href=\"https://app.threatconnect.com/auth/profile/organization.xhtml?name=Demo+Organization\" >Demo Organization</a>&nbsp;/&nbsp;<a href=\"https://app.threatconnect.com/auth/profile/user.xhtml?id=3\" >John Smith</a>",
                "deleteAvailable": true
            }
        ],
        "status": "Success"
    }

To filter posts by their contents, use the ``tql`` query parameter as follows:

**Request (Decoded URL)**

.. code:: http

   GET /v3/posts?objectId=12345&objectType=Group&tql=text contains "test"


**Request (Encoded URL)**

.. code:: http

    GET /v3/posts?objectId=12345&objectType=Group&tql=text%20contains%20%22test%22

This request will retrieve all posts added to the Group whose ID is 12345 that meet one of the following conditions:

- The post contains the text "test"
- The post has a reply that contains the text "test"

Retrieve a Specific Post
^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: http

   GET /v3/posts/{id}

Retrieve details about a specific post.

Query Parameters
""""""""""""""""

The following table outlines the query parameters that may be used when sending a GET request to the ``/v3/posts/{id}`` endpoint.

.. list-table::
   :widths: 25 35 15 15 15
   :header-rows: 1

   * - Parameter
     - Description
     - Data Type
     - Default Value
     - Required?
   * - ``fields``
     - `Returns additional fields <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_ in the API response based on one or more specified values.
     - String
     - N/A
     - Optional

Example Request
"""""""""""""""

.. note::
   You must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`_.

**Request**

.. code:: http

   GET /v3/posts/2

**Response**

.. code:: json

    {
        "data": {
            "id": 2,
            "author": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "authorType": "full",
            "dateAdded": "2026-01-11T16:54:55Z",
            "text": "Another post about Bad Guy",
            "linkedItems": [
                {
                    "id": "B12345",
                    "type": "Adversary",
                    "display": "Bad Guy",
                    "owner": "Demo Organization"
                }
            ],
            "deleteAvailable": true
        },
        "status": "Success"
    }