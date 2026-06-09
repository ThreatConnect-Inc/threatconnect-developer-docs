AI Summaries
------------

As of ThreatConnect 8.0.1, when creating or updating Document, Event, and Report Groups, you can provide an AI-generated summary of the Group. In ThreatConnect, a Group's AI-generated summary displays on the **AI Insights** card on the Group's **Details** screen.

.. warning::
    In ThreatConnect, AI-generated summaries are automatically provided for the following Groups:

    -	Report Groups in the **CAL Automated Threat Library** Source
    -	Event Groups in the **Dataminr Cyber Pulse Limited** or **Dataminr Pulse Alerts Engine** feeds

    In the v3 API, AI-generated summaries for these Groups are stored in the Group's ``insights`` field. If you assign a value to the ``customAiContent`` field for one of these Groups, the AI-generated summary on the **AI Insights** card on the Group's **Details** screen will be replaced with the one stored in the ``customAiContent`` field. However, you can still view the previous AI-generated summary stored in the Group's ``insights`` field when interacting with the Group via the v3 API.

.. note::
    For Event Groups, the **AI Insights** card is available on the **Details** screen only for Events in the **Dataminr Cyber Pulse Limited** or **Dataminr Pulse Alerts Engine** feeds.


Requirements
^^^^^^^^^^^^

- To provide AI-generated summaries for Document, Event, and Report Groups in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer.
- To provide AI-generated summaries for Document, Event, and Report Groups in a Community or Source, your API user account must have a Community role of Contributor, Editor, or Director for that Community or Source.


Custom AI Content Object Schema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request Body
============

The following is the request body schema for a custom AI content object that can be used when creating or updating a Document, Event, or Report Group:

- ``customAiContent``: <*Object*> The details of the AI-generated summary of the Group.
    - ``aiProvider``: <*String*> **REQUIRED** The source that provided the AI-generated summary.
    - ``summary``: <*String*> **CONDITIONALLY REQUIRED** The AI-generated summary in paragraph format. Required if ``bullets`` is omitted from the request body.
    - ``bullets``: <*Array of Strings*> **CONDITIONALLY REQUIRED** The AI-generated summary in bullet-point format. Required if ``summary`` is omitted from the request body.
    - ``app``: <*String*> The app that was used to generate the AI summary.


**Example**

.. code:: json

    "customAiContent": {
        "aiProvider": "<string>",
        "summary": "<string>",
        "bullets": [
            "<string>",
            "<string>"
        ],
        "app": "<string>"
    }

.. attention::
    If you are updating a Group that has a value assigned to its ``customAiContent`` field, including an empty ``customAiContent`` object in the request body will clear the assigned value and remove the AI-generated summary from the Group.

Response Body
=============

The following is the response body schema for a custom AI content object that is included in API responses. Note that you must use the ``fields`` query parameter in your request and assign it a value of ``insights`` to include custom AI content in API responses:

- ``customAiContent``: <*Object*> The details of the AI-generated summary of the Group.
  - ``summary``: <*String*> The AI-generated summary in paragraph format. If ``summary`` has no value, it is omitted from the response body.
  - ``app``: <*String*> The app that was used to generate the AI summary. If ``app`` has no value, it is omitted from the response body.
  - ``aiProvider``: <*String*> The source that provided the AI-generated summary.
  - ``markdown``: <*String*> The AI-generated summary in Markdown format.
  - ``bullets``: <*Array of Strings*> The AI-generated summary in bullet-point format. If ``bullets`` has no value, it is omitted from the response body.
  - ``lastRetrievalDate``: <*DateTime*> The date and time the AI-generated summary was last retrieved from its source.
  - ``generatedBy``: <*Object*> The user who added the AI-generated summary to the Group.
    - ``id``: <*Integer*> The unique numeric identifier of the user.
    - ``userName``: <*String*> The username of the user.
    - ``firstName``: <*String*> The first name of the user.
    - ``lastName``: <*String*> The last name of the user.
    - ``pseudonym``: <*String*> The pseudonym of the user.
    - ``owner``: <*String*> The Organization to which the user belongs.

**Example**

.. code:: json

    "customAiContent": {
        "summary": "<string>",
        "app": "<string>",
        "aiProvider": "<string>",
        "markdown": "<string>",
        "bullets": [
            "<string>",
            "<string>"
        ],
        "lastRetrievalDate": "<datetime>",
        "generatedBy": {
            "id": 0,
            "userName": "<string>",
            "firstName": "<string>",
            "lastName": "<string>",
            "pseudonym": "<string>",
            "owner": "<string>"
        }
    }

Providing an AI Summary for a Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following request demonstrates how to provide an AI-generated summary when creating a new Report Group. Because AI summary data are not included in the API response by default, the ``fields`` query parameter is used and assigned a value of ``insights`` to include those data in the response.
 
**Request**
 
.. code:: http
 
   POST /v3/groups?fields=insights
   Content-Type: application/json
 
   {
       "name": "Emotet Resurgence – Malspam Campaign Targeting Financial Sector",
       "type": "Report",
       "publishDate": "2026-05-27",
       "customAiContent": {
           "summary": "A renewed Emotet campaign was observed in May 2026 targeting financial institutions via malspam. Emails contained macro-enabled Word documents that, when opened, downloaded Emotet and subsequently dropped Cobalt Strike beacons for lateral movement.",
           "aiProvider": "Anthropic Claude",
           "bullets": [
               "Emotet resurfaced in May 2026 targeting financial institutions via malspam.",
               "Macro-enabled Word documents served as the initial infection vector.",
               "Cobalt Strike beacons were deployed post-infection to facilitate lateral movement.",
               "Organizations should block macro execution in Office documents and monitor for Emotet IOCs."
           ]
       }
   }
 
**Response**
 
.. code:: json
 
   {
       "data": {
           "id": 47434,
           "dateAdded": "2026-05-29T20:33:29Z",
           "ownerId": 1,
           "ownerName": "Demo Organization",
           "webLink": "https://app.threatconnect.com/#/details/groups/47434",
           "type": "Report",
           "name": "Example Report Group with AI Summary",
           "createdBy": {
               "id": 3,
               "userName": "11112222333344445555",
               "firstName": "John",
               "lastName": "Smith",
               "pseudonym": "jsmithAPI",
               "owner": "Demo Organization"
           },
           "upVoteCount": "0",
           "downVoteCount": "0",
           "generatedReport": false,
           "status": "Awaiting Upload",
           "documentType": "None",
           "customAiContent": {
               "summary": "A renewed Emotet campaign was observed in May 2026 targeting financial institutions via malspam. Emails contained macro-enabled Word documents that, when opened, downloaded Emotet and subsequently dropped Cobalt Strike beacons for lateral movement.",
               "aiProvider": "Anthropic Claude",
               "markdown": "Here is a concise bullet point report and summary based on the cyber threat report:\n\nBULLET POINTS:\n\n* Emotet resurfaced in May 2026 targeting financial institutions via malspam.\n* Macro-enabled Word documents served as the initial infection vector.\n* Cobalt Strike beacons were deployed post-infection to facilitate lateral movement.\n* Organizations should block macro execution in Office documents and monitor for Emotet IOCs.\n\nSUMMARY:\n\nA renewed Emotet campaign was observed in May 2026 targeting financial institutions via malspam. Emails contained macro-enabled Word documents that, when opened, downloaded Emotet and subsequently dropped Cobalt Strike beacons for lateral movement.\n",
               "bullets": [
                   "Emotet resurfaced in May 2026 targeting financial institutions via malspam.",
                   "Macro-enabled Word documents served as the initial infection vector.",
                   "Cobalt Strike beacons were deployed post-infection to facilitate lateral movement.",
                   "Organizations should block macro execution in Office documents and monitor for Emotet IOCs."
               ],
               "lastRetrievalDate": "2026-06-01T22:32:56Z",
               "generatedBy": {
                   "id": 3,
                   "userName": "11112222333344445555",
                   "firstName": "John",
                   "lastName": "Smith",
                   "pseudonym": "jsmithAPI",
                   "owner": "Demo Organization"
               }
           },
           "documentDateAdded": "2026-05-29T20:33:29Z",
           "lastModified": "2026-05-29T20:33:29Z",
           "legacyLink": "https://app.threatconnect.com/auth/report/report.xhtml?report=47434",
           "publishDate": "2026-05-27T00:00:00Z"
       },
       "message": "Created",
       "status": "Success"
   }