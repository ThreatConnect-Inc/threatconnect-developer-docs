Schemas
-------

Request Body (POST)
^^^^^^^^^^^^^^^^^^^

Posts
"""""

The following is the request body schema for a POST request to the ``/v3/posts`` endpoint:

- ``objectId``: <*Integer*> **REQUIRED** The ID number of the object to add the post to.
- ``objectType``: <*String*> **REQUIRED** The type of object to add the post to. (Acceptable values: **Group**, **Indicator**, **Tag**, **Victim**)
- ``text``: <*String*> **REQUIRED** The contents of the post.

**Example**

.. code:: json

    {
        "objectId" : 0,
        "objectType": "<string>",
        "text": "<string>"
    }

Post Replies
""""""""""""

The following is the request body schema for a POST request to the ``/v3/posts/reply`` endpoint:

- ``id``: <*Integer*> **REQUIRED** The ID number of the post to add the reply to.
- ``objectId``: <*Integer*> **REQUIRED** The ID number of the object to add the reply to.
- ``objectType``: <*String*> **REQUIRED** The type of object to add the reply to. (Acceptable values: **Group**, **Indicator**, **Tag**, **Victim**)
- ``replies``: <*Array of Objects*> **REQUIRED** The replies to add to the specified post.
    - ``text``: <*String*> **REQUIRED** The contents of the reply.

**Example**

.. code:: json

    {
        "id": 0,
        "objectId" : 0,
        "objectType": "<string>",
        "replies": [
            {
                "text": "<string>"
            }
        ]
    }

Request Body (DELETE)
^^^^^^^^^^^^^^^^^^^^^

Posts
"""""

The following is the request body schema for a DELETE request to the ``/v3/posts`` endpoint:

- ``id``: <*Integer*> **REQUIRED** The ID number of the post to delete.

**Example**

.. code:: json

    {
        "id" : 0
    }

Post Replies
""""""""""""

The following is the request body schema for a DELETE request to the ``/v3/posts/reply`` endpoint:

- ``id``: <*Integer*> **REQUIRED** The ID number of the post that contains the reply to delete.
- ``replies``: <*Array of Objects*> **REQUIRED** The details of the reply to delete.
    - ``sequenceId``: <*String*> **REQUIRED** The sequence ID number of the reply to delete.

**Example**

.. code:: json

    {
        "id": 0,
        "replies": [
            {
                "sequenceId": "<string>"   
            }
        ]
    }

Response Body
^^^^^^^^^^^^^

The default response returned for successful GET and POST requests to the ``/v3/posts`` or ``/v3/posts/reply`` endpoint may include one or more objects with the following fields:

- ``id``: <*Integer*> The post's ID number.
- ``author``: <*Object*> The user who created the post. The amount of data returned for this field depends on where the author's user account exists and the settings configured for the owner where the post was created.
    - ``id``: <*Integer*> The ID number of the user who created the post.
    - ``userName``: <*String*> The username of the user who created the post.
    - ``firstName``: <*String*> The first name of the user who created the post.
    - ``lastName``: <*String*> The last name of the user who created the post.
    - ``pseudonym``: <*String*> The pseudonym of the user who created the post.
    - ``owner``: <*String*> The Organization that the user who created the post belongs to.
- ``authorType``: <*String*> Indicates how the user who created the post will be identified when viewing the post in ThreatConnect and whether the user can delete the post. (Possible values: **full**, **restricted**, **pseudonym**)
- ``dateAdded``: <*DateTime*> The date and time the post was created (ISO 8601).
- ``text``: <*String*> The contents of the post.
- ``linkedItems``: <*Array of Objects*> The objects that the post is linked to.
    - ``id``: <*Integer*> The type and ID combination of the object that the post is added to (e.g., B12345). Possible type identifiers include **B** (Group), **I** (Indicator), **T** (Tag), and **V** (Victim).
    - ``type``: <*String*> The object's type (e.g., Adversary).
    - ``display``: <*String*> The object's name/summary.
    - ``owner``: <*String*> The object's owner.
- ``linkedText``: <*String*>  The contents of the post with embedded hyperlinks, including links to objects that were added using the **ADD LINK...** feature on the **Posts** screen or legacy **Details** screen. This field is included only when retrieving all posts added to a specific object.
- ``aboutLinkedText``: <*String*> The URL of the object that the post is added to. This field is included only when retrieving all posts added to a specific object.
- ``linkedAuthor``: <*String*> The URL of the Organization where the post was created and the URL of the author who created the post. This field is included only when retrieving all posts added to a specific object.
- ``deleteAvailable``: <*Boolean*> Specifies whether your API user account can delete the post.
- ``replies``: <*Array of Objects*> The replies added to the post. This field is included only for posts that have one or more replies.
    - ``sequenceId``: <*String*> Indicates the reply's position in the thread of replies.
    - ``author``: <*Object*> The user who created the reply. The amount of data returned for this field depends on where the author's user account exists and the settings configured for the owner where the post was created.
        - ``id``: <*Integer*> The ID number of the user who created the reply.
        - ``userName``: <*String*> The username of the user who created the reply.
        - ``firstName``: <*String*> The first name of the user who created the reply.
        - ``lastName``: <*String*> The last name of the user who created the reply.
        - ``pseudonym``: <*String*> The pseudonym of the user who created the reply.
        - ``owner``: <*String*> The Organization that the user who created the reply belongs to.
    - ``authorType``: <*String*> The author's permission level for posts.
    - ``text``: <*String*> The contents of the reply.
    - ``deleteAvailable``: <*Boolean*> Specifies whether your API user account can delete the reply.

**Example**

.. code:: json

    {
        "id": 0,
        "author": {
            "id": 0,
            "userName": "<string>",
            "firstName": "<string>",
            "lastName": "<string>",
            "pseudonym": "<string>",
            "owner": "<string>"
        },
        "authorType": "<string>",
        "dateAdded": "<datetime>",
        "text": "<string>",
        "linkedItems": [
            {
                "id": "<string>",
                "type": "<string>",
                "display": "<string>",
                "owner": "<string>"
            }
        ],
        "linkedText": "<string>",
        "aboutLinkedText": "<string>",
        "linkedAuthor": "<string>",
        "deleteAvailable": true,
        "replies": [
            {
                "sequenceId": "<string>",
                "author": {
                    "id": 0,
                    "userName": "<string>",
                    "firstName": "<string>",
                    "lastName": "<string>",
                    "pseudonym": "<string>",
                    "owner": "<string>"
                },
                "authorType": "<string>",
                "text": "<string>",
                "deleteAvailable": true
            }
        ]
    }