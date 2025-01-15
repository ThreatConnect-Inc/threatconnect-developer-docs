Intelligence Reviews
--------------------

Intelligence Reviews provide members of an organization a way to solicit and provide feedback on a given piece of threat intelligence data in ThreatConnect. Consumers of threat intelligence can use Intelligence Reviews to rate the quality and usefulness of a Group object, identify whether the Group's intelligence was helpful, and provide narrative comments for the Group. Producers of threat intelligence, on the other hand, can use Intelligence Reviews to collect feedback from stakeholders and determine whether the intelligence they are providing is helpful.

.. attention::
    As of ThreatConnect 7.8, Intelligence Reviews are available for Report Groups only.

Requirements
^^^^^^^^^^^^

-  To create Intelligence Reviews in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer.
-  To create Intelligence Reviews in a Community or Source, your API user account must have a Community role of Contributor, Editor, or Director for that Community or Source.
-  To update and delete Intelligence Reviews you created in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer.
-  To update and delete Intelligence Reviews you created in a Community or Source, your API user account must have a Community role of Contributor, Editor, or Director for that Community or Source.
-  To delete Intelligence Reviews any user in an Organization created in the Organization or Communities and Sources the Organization is a member of, your API user account must have an Organization role of Organization Administrator.

Intelligence Review Object Schema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request Body
============

The following is the request body schema for an Intelligence Review object that can be used when creating or updating a Group:

- ``reviews``: <*Object*> The Intelligence Review to add to the Group. Note that each user may add only one Intelligence Review per Group.
    - ``data``: <*Array of Objects*> The details of the Intelligence Review.
        - ``rating``: <*Integer*> Indicates how valuable you found the Group's intelligence on a scale of **1** (not valuable) to **5** (very valuable). This field is required if you are creating an Intelligence Review.
        - ``reviewHelpful``: <*Boolean*> Specifies whether you found the Group's intelligence to be helpful (**true**) or unhelpful (**false**). This field is required if you are creating an Intelligence Review.
        - ``comments``: <*String*> The additional comments provided with the Intelligence Review. (Maximum character length: **500**)

**Example**

.. code:: json

    "reviews": {
        "data": [
            {
                "rating": 1,
                "reviewHelpful": false,
                "comments": "<string>"
            }            
        ]
    }


Response Body
=============

The following is the response body schema for an Intelligence Review object that is included in API responses from the ``/v3/groups`` endpoint. Note that you must use the ``fields`` query parameter in your request and assign it a value of ``intelReviews`` to include Intelligence Reviews in API responses:

- ``reviews``: <*Object*> A list of Intelligence Reviews added to the Group.
    - ``data``: <*Array of Objects*> The details of the Intelligence Reviews.
        - ``id``: <*Integer*> The Intelligence Review's ID number.
        - ``rating``: <*Integer*> Indicates how valuable the user found the Group's intelligence on a scale of **1** (not valuable) to **5** (very valuable).
        - ``dateAdded``: <*DateTime*> The date and time when the Intelligence Review was created (ISO 8601 format).
        - ``lastModified``: <*DateTime*> The date and time when the Intelligence Review was last modified (ISO 8601 format).
        - ``createdBy``: <*Object*> The details of the user who submitted the Intelligence Review.
            - ``id``: <*Integer*> The user's ID number.
            - ``userName``: <*String*> The user's username.
            - ``firstName``: <*String*> The user's first name.
            - ``lastName``: <*String*> The user's last name.
            - ``pseudonym``: <*String*> The user's pseudonym.
            - ``owner``: <*String*> The Organization to which the user belongs.
        - ``comments``: <*String*> The additional comments the user provided with the Intelligence Review. This field is only included for Intelligence Reviews with comments.
        - ``editable``: <*Boolean*> Specifies whether you can edit the Intelligence Review.
        - ``deletable``: <*Boolean*> Specifies whether you can delete the Intelligence Review.
        - ``reviewHelpful``: <*Boolean*> Specifies whether the user found the Group's intelligence to be helpful (**true**) or unhelpful (**false**).

**Example**

.. code:: json

    "reviews": {
        "data": [
            {
                "id": 1,
                "rating": 1,
                "dateAdded": "<datetime>",
                "lastModified": "<datetime>",
                "createdBy": {
                    "id": 1,
                    "userName": "<string>",
                    "firstName": "<string>",
                    "lastName": "<string>",
                    "pseudonym": "<string>",
                    "owner": "<string>"
                },
                "comments": "<string>",
                "editable": false,
                "deletable": false,
                "reviewHelpful": false
            }
        ]
    }

Create Intelligence Reviews
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating a Group or updating an existing one, you can add an Intelligence Review to the Group. The following request demonstrates how to add an Intelligence Review to an existing Group. Because Intelligence Review data are not included in the API response by default, the ``fields`` query parameter is used and assigned a value of ``intelReviews`` to include those data in the response.

**Request**

.. code:: http

    PUT /v3/groups/216456?fields=intelReviews
    Content-Type: application/json

    {
        "reviews": {
            "data": [
                {
                    "rating": 5,
                    "reviewHelpful": true,
                    "comments": "I found the contents of this Report Group to be very helpful and informative during the course of my investigation."
                }
            ]
        }
    }

.. note::
    You can add only one Intelligence Review per Group.

Retrieve Intelligence Reviews
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When retrieving all Groups or a specific one, you can retrieve Intelligence Reviews by using the ``fields`` query parameter and assigning it a value of ``intelReviews``. The following request demonstrates how to include Intelligence Reviews in the API response when retrieving a specific Group.

**Request**

.. code:: http
    
    GET /v3/groups/216456?fields=intelReviews

Update Intelligence Reviews
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can update an Intelligence Review only if its ``editable`` field is set to **true**. The following request demonstrates how to update an Intelligence Review added to an existing Group. Because Intelligence Review data are not included in the API response by default, the ``fields`` query parameter is used and assigned a value of ``intelReviews`` to include those data in the response.

**Request**

.. code:: http

    PUT /v3/groups/216456?fields=intelReviews
    Content-Type: application/json

    {
        "reviews": {
            "data": [
                {
                    "rating": 2,
                    "reviewHelpful": false,
                    "comments": "On second thought, I did not find this Report Group to be helpful."
                }
            ]
        }
    }

Delete Intelligence Reviews
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can delete an Intelligence Review only if its deletable field is set to **true**. The following request demonstrates how to delete an Intelligence Review added to an existing Group. Because Intelligence Review data are not included in the API response by default, the ``fields`` query parameter is used and assigned a value of ``intelReviews`` to include those data in the response.

**Request**

.. code:: http

    PUT /v3/groups/216456?fields=intelReviews
    Content-Type: application/json

    {
        "reviews": {
            "data": [
                {
                    "id": 1
                }
            ],
            "mode": "delete"
        }
    }