Schemas
-------

Request Body (POST)
^^^^^^^^^^^^^^^^^^^

The following is the request body schema for a POST request to the ``/v3/intelRequirements`` endpoint:

* ``associatedArtifacts``: <*Object*> A list of Artifacts associated to the IR.
    * ``data``: <*Array of Artifact Objects*> The `details of the Artifacts <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_.
* ``associatedCases``: <*Object*> A list of Cases associated to the IR.
    * ``data``: <*Array of Case Objects*> The `details of the Cases <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html>`_.
* ``associatedGroups``: <*Object*> A list of Groups associated to the IR.
    * ``data``: <*Array of Group Objects*> The `details of the Groups <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_.
* ``associatedIndicators``: <*Object*> A list of Indicators associated to the IR.
    * ``data``: <*Array of Indicator Objects*> The `details of the Indicators <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_.
* ``associatedVictimAssets``: <*Object*> A list of Victim Assets associated to the IR.
    * ``data``: <*Array of Victim Asset Objects*> The `details of the Victim Assets <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html>`_.
* ``category``: <*Object*> The IR's `category <https://docs.threatconnect.com/en/latest/rest_api/v3/intelligence_requirement_categories/intelligence_requirement_categories.html>`_. To specify the category, use its ID number, name, or both.
    * ``id``: <*Integer*> The IR category's ID number.
    * ``name``: <*String*> The IR category's name.
* ``description``: <*String*> A description of the IR.
* ``keywordSections``: <*Array*> **REQUIRED** The sections that the IR's keyword query contains.
    * ``compareValue``: <*String*> **REQUIRED** Specifies whether the section is an **includes** or **excludes** section. (Accepted values: **includes**, **excludes**)
    * ``keywords``: <*Array of Objects*> **REQUIRED** A list of keywords that the section contains. Note that the total number of keywords added to an IR must not exceed the IR keyword limit configured by your System Administrator (the default limit is 300 keywords). Otherwise, a **400 Bad Request** error will be returned.
        * ``value``: <*String*> **REQUIRED** The keyword's value. For best practices on defining keywords in IR keyword queries, see the `Best Practices: Keywords for Intelligence Requirements <https://knowledge.threatconnect.com/docs/best-practices-keywords-for-intelligence-requirements>`_ knowledge base article.
    * ``sectionNumber``: <*Integer*> **REQUIRED** The section number for the keyword section.
* ``requirementText``: <*String*> **REQUIRED** The IR's summary (i.e., the question, topic, or statement on which the IR focuses). The summary provided cannot be the same as the summary for an existing IR on the ThreatConnect instance.
* ``resetResults``: <*Boolean*> Specifies whether to include results that have been archived or marked as false results the next time results are retrieved for the IR.
* ``subtype``: <*Object*> **REQUIRED** The IR's subtype. 
    * ``id``: <*Integer*> **REQUIRED** The `ID of the subtype <https://docs.threatconnect.com/en/latest/rest_api/v3/intelligence_requirement_subtypes/intelligence_requirement_subtypes.html>`_.
* ``tags``: <*Object*> A list of Tags applied to the IR.
    * ``data``: <*Array of Tag Objects*> The `details of the Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_.
* ``uniqueId``: <*String*> **REQUIRED** The IR's unique ID. The ID provided cannot be the same as the ID for an existing IR on the ThreatConnect instance.
* ``xid``: <*String*> The IR's unique XID. The XID provided cannot be the same as the XID for an existing IR on the ThreatConnect instance.

**Example**

.. code:: json
    
    {
        "associatedArtifacts": {
            "data": [
                {
                    "<artifactsFieldName>": <artifactsFieldValue>
                }
            ]
        },
        "associatedCases": {
            "data": [
                {
                    "<casesFieldName>": <casesFieldValue>
                }
            ]
        },
        "associatedGroups": {
            "data": [
                {
                    "<groupsFieldName>": <groupsFieldValue>
                }
            ]
        },
        "associatedIndicators": {
            "data": [
                {
                    "<indicatorsFieldName>": <indicatorsFieldValue>
                }
            ]
        },
        "associatedVictimAssets": {
            "data": [
                {
                    "<victimAssetsFieldName>": <victimAssetsFieldValue>
                }
            ]
        },
        "category": {
            "id": <int>,
            "name": <string>
        },
        "description": "<string>",
        "keywordSections": [
            {
                "compareValue": "<string>",
                "keywords": [
                    {
                        "value": "<string>"
                    }
                ],
                "sectionNumber": <int>
            }
        ],
        "requirementText": "<string>",
        "resetResults": <boolean>,
        "subtype": {
            "id": <int>
        },
        "tags": {
            "data": [
                {
                    "<tagsFieldName>": <tagsFieldValue>
                }
            ]
        },
        "uniqueId": "<string>", 
        "xid": "<string>"
    }

Request Body (PUT)
^^^^^^^^^^^^^^^^^^^

The following is the request body schema for a PUT request to the ``/v3/intelRequirements`` endpoint:

* ``associatedArtifacts``: <*Object*> A list of Artifacts associated to the IR.
    * ``data``: <*Array of Artifact Objects*> The `details of the Artifacts <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_.
    * ``mode``: <*String*> Specifies the `action to perform <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ with the objects defined in the ``data`` field. (Accepted values: **append**, **delete**, **replace**; Default value: **append**).
* ``associatedCases``: <*Object*> A list of Cases associated to the IR.
    * ``data``: <*Array of Case Objects*> The `details of the Cases <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html>`_.
    * ``mode``: <*String*> Specifies the `action to perform <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ with the objects defined in the ``data`` field. (Accepted values: **append**, **delete**, **replace**; Default value: **append**).
* ``associatedGroups``: <*Object*> A list of Groups associated to the IR.
    * ``data``: <*Array of Group Objects*> The `details of the Groups <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_.
    * ``mode``: <*String*> Specifies the `action to perform <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ with the objects defined in the ``data`` field. (Accepted values: **append**, **delete**, **replace**; Default value: **append**).
* ``associatedIndicators``: <*Object*> A list of Indicators associated to the IR.
    * ``data``: <*Array of Indicator Objects*> The `details of the Indicators <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_.
    * ``mode``: <*String*> Specifies the `action to perform <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ with the objects defined in the ``data`` field. (Accepted values: **append**, **delete**, **replace**; Default value: **append**).
* ``associatedVictimAssets``: <*Object*> A list of Victim Assets associated to the IR.
    * ``data``: <*Array of Victim Asset Objects*> The `details of the Victim Assets <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html>`_.
    * ``mode``: <*String*> Specifies the `action to perform <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ with the objects defined in the ``data`` field. (Accepted values: **append**, **delete**, **replace**; Default value: **append**).
* ``category``: <*Object*> The IR's `category <https://docs.threatconnect.com/en/latest/rest_api/v3/intelligence_requirement_categories/intelligence_requirement_categories.html>`_. To specify the category, use its ID number, name, or both.
    * ``id``: <*Integer*> The IR category's ID number.
    * ``name``: <*String*> The IR category's name.
* ``description``: <*String*> A description of the IR.
* ``keywordSections``: <*Array*> The sections that the IR's keyword query contains.
    * ``compareValue``: <*String*> Specifies whether the section is an **includes** or **excludes** section. (Accepted values: **includes**, **excludes**)
    * ``keywords``: <*Array of Objects*> A list of keywords that the section contains. Note that the total number of keywords added to an IR must not exceed the IR keyword limit configured by your System Administrator (the default limit is 300 keywords). Otherwise, a **400 Bad Request** error will be returned.
        * ``value``: <*String*> The keyword's value. For best practices on defining keywords in IR keyword queries, see the `Best Practices: Keywords for Intelligence Requirements <https://knowledge.threatconnect.com/docs/best-practices-keywords-for-intelligence-requirements>`_ knowledge base article.
    * ``sectionNumber``: <*Integer*> The section number for the keyword section.
* ``requirementText``: <*String*> The IR's summary (i.e., the question, topic, or statement on which the IR focuses). The summary provided cannot be the same as the summary for an existing IR on the ThreatConnect instance.
* ``resetResults``: <*Boolean*> Specifies whether to include results that have been archived or marked as false results the next time results are retrieved for the IR.
* ``subtype``: <*Object*> The IR's subtype. 
    * ``id``: <*Integer*> The `ID of the subtype <https://docs.threatconnect.com/en/latest/rest_api/v3/intelligence_requirement_subtypes/intelligence_requirement_subtypes.html>`_.
* ``tags``: <*Object*> A list of Tags applied to the IR.
    * ``data``: <*Array of Tag Objects*> The `details of the Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_.
    * ``mode``: <*String*> Specifies the `action to perform <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ with the objects defined in the ``data`` field. (Accepted values: **append**, **delete**, **replace**; Default value: **append**).
* ``uniqueId``: <*String*> The IR's unique ID. The ID provided cannot be the same as the ID for an existing IR on the ThreatConnect instance.

**Example**

.. code:: json

    {
        "associatedArtifacts": {
            "data": [
                {
                    "<artifactsFieldName>": <artifactsFieldValue>
                }
            ],
            "mode": "<string>"
        },
        "associatedCases": {
            "data": [
                {
                    "<casesFieldName>": <casesFieldValue>
                }
            ],
            "mode": "<string>"
        },
        "associatedGroups": {
            "data": [
                {
                    "<groupsFieldName>": <groupsFieldValue>
                }
            ],
            "mode": "<string>"
        },
        "associatedIndicators": {
            "data": [
                {
                    "<indicatorsFieldName>": <indicatorsFieldValue>
                }
            ],
            "mode": "<string>"
        },
        "associatedVictimAssets": {
            "data": [
                {
                    "<victimAssetsFieldName>": <victimAssetsFieldValue>
                }
            ],
            "mode": "<string>"
        },
        "category": {
            "id": <int>,
            "name": <string>
        },
        "description": "<string>",
        "keywordSections": [
            {
                "compareValue": "<string>",
                "keywords": [
                    {
                        "value": "<string>"
                    }
                ],
                "sectionNumber": <int>
            }
        ],
        "requirementText": "<string>",
        "resetResults": <boolean>,
        "subtype": {
            "id": <int>
        },
        "tags": {
            "data": [
                {
                    "<tagsFieldName>": <tagsFieldValue>
                }
            ],
            "mode": "<string>"
        },
        "uniqueId": "<string>"
    }

Response Body
^^^^^^^^^^^^^

The default response returned from successful GET, POST, and PUT requests to the ``/v3/intelRequirements`` endpoint includes one or more objects with the following fields:

* ``id``: <*Integer*> The IR's ID number. Note that this is not the same ID as the one specified for the uniqueId field when the IR was created or updated.
* ``xid``: <*String*> The IR's XID. This field is only included in the response body when a value has been assigned to it.
* ``createdBy``: <*Object*> The details of the user who created the IR.
    * ``id``: <*Integer*> The ID of the user's account.
    * ``username``: <*String*> The username of the user's account.
    * ``firstName``: <*String*> The user's first name.
    * ``lastName``: <*String*> The user's last name.
    * ``pseudonym``: <*String*> The user's pseudonym.
    * ``owner``: <*String*> The Organization to which the user's account belongs.
* ``lastModified``: <*DateTime*> The date and time when the IR was last modified (ISO 8601 format).
* ``webLink``: <*String*> The URL for the IR's Details screen in ThreatConnect.
* ``dateAdded``: <*DateTime*> The date and time when the IR was created (ISO 8601 format).
* ``uniqueId``: <*String*> The IR's unique ID.
* ``requirementText``: <*String*> The IR's summary (i.e., the question, topic, or statement on which the IR focuses).
* ``subtype``: <*Object*> The details of the IR's subtype.
    * ``name``: <*String*> The name of the IR's subtype.
    * ``description``: <*String*> A description of the IR's subtype.
* ``category``: <*Object*> The details of the IR's category. This field is only included in the response body when a value has been assigned to it.
    * ``name``: <*String*> The value of the IR's category.
    * ``description``: <*String*> A description of the IR's category.
* ``description``: <*String*> A description of the IR. This field is only included in the response body when a value has been assigned to it.
* ``keywordSections``: <*Array of Objects*> The details of the sections that the IR's keyword query contains.
    * ``compareValue``: <*String*> Specifies whether the section is an includes or excludes section.
    * ``keywords``: <*Array of Objects*> A list of keywords that the section contains.
        * ``value``: <*String*> The keyword's value.
* ``resultsLink``: <*String*> A link to view the local and global results for the IR's keyword query.

**Example**

.. code:: json

    {
        "id": <int>,
        "xid": "<string>",
        "createdBy": {
            "id": <int>,
            "userName": "<string>",
            "firstName": "<string>",
            "lastName": "<string>",
            "pseudonym": "<string>",
            "owner": "<string>"
        },
        "lastModified": "<datetime>",
        "webLink": "<string>",
        "dateAdded": "<datetime>",
        "uniqueId": "<string>",
        "requirementText": "<string>",
        "subtype": {
            "name": "<string>",
            "description": "<string>
        },
        "category": {
            "name": "<string>",
            "description": "<string>"
        },
        "description": "<string>",
        "keywordSections": [
            {
                "compareValue": "<string>",
                "keywords": [
                    {
                        "value": "<string>"
                    } 
                ]
            }
        ],
        "resultsLink": "<string>"
    }