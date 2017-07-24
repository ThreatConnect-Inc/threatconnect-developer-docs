All API Endpoints and Responses
===============================

Owners
------

* ``/v2/owners``
* ``/v2/owners/mine``
* ``/v2/owners/mine/members``
* ``/v2/owners/metrics``
* ``/v2/owners/{id}/metrics``

Groups
------

* ``/v2/groups``
* ``/v2/groups/{type}``
* ``/v2/groups/{type}/{id}``
* ``/v2/groups/{type}/{id}/attributes``
* ``/v2/groups/{type}/{id}/attributes/{attributeId}``
* ``/v2/groups/{type}/{id}/attributes/{attributeId}/securityLabels``
* ``/v2/groups/{type}/{id}/attributes/{attributeId}/securityLabels/{securityLabel}``
* ``/v2/groups/{type}/{id}/groups``
* ``/v2/groups/{type}/{id}/groups/adversaries``
* ``/v2/groups/{type}/{id}/groups/adversaries/{groupId}``
* ``/v2/groups/{type}/{id}/groups/documents``
* ``/v2/groups/{type}/{id}/groups/documents/{groupId}``
* ``/v2/groups/{type}/{id}/groups/emails``
* ``/v2/groups/{type}/{id}/groups/emails/{groupId}``
* ``/v2/groups/{type}/{id}/groups/incidents``
* ``/v2/groups/{type}/{id}/groups/incidents/{groupId}``
* ``/v2/groups/{type}/{id}/groups/signatures``
* ``/v2/groups/{type}/{id}/groups/signatures/{groupId}``
* ``/v2/groups/{type}/{id}/groups/threats``
* ``/v2/groups/{type}/{id}/groups/threats/{groupId}``
* ``/v2/groups/{type}/{id}/indicators``
* ``/v2/groups/{type}/{id}/indicators/addresses``
* ``/v2/groups/{type}/{id}/indicators/addresses/{indicator}``
* ``/v2/groups/{type}/{id}/indicators/emailAddresses``
* ``/v2/groups/{type}/{id}/indicators/emailAddresses/{indicator}``
* ``/v2/groups/{type}/{id}/indicators/{type}/{indicator}``
* ``/v2/groups/{type}/{id}/indicators/files``
* ``/v2/groups/{type}/{id}/indicators/files/{indicator}``
* ``/v2/groups/{type}/{id}/indicators/hosts``
* ``/v2/groups/{type}/{id}/indicators/hosts/{indicator}``
* ``/v2/groups/{type}/{id}/indicators/urls``
* ``/v2/groups/{type}/{id}/indicators/urls/{indicator}``
* ``/v2/groups/{type}/{id}/publish``
* ``/v2/groups/{type}/{id}/securityLabels``
* ``/v2/groups/{type}/{id}/securityLabels/{securityLabel}``
* ``/v2/groups/{type}/{id}/tags``
* ``/v2/groups/{type}/{id}/tags/{tagName}``
* ``/v2/groups/{type}/{id}/victimAssets``
* ``/v2/groups/{type}/{id}/victimAssets/emailAddresses``
* ``/v2/groups/{type}/{id}/victimAssets/emailAddresses/{assetId}``
* ``/v2/groups/{type}/{id}/victimAssets/networkAccounts``
* ``/v2/groups/{type}/{id}/victimAssets/networkAccounts/{assetId}``
* ``/v2/groups/{type}/{id}/victimAssets/phoneNumbers``
* ``/v2/groups/{type}/{id}/victimAssets/phoneNumbers/{assetId}``
* ``/v2/groups/{type}/{id}/victimAssets/socialNetworks``
* ``/v2/groups/{type}/{id}/victimAssets/socialNetworks/{assetId}``
* ``/v2/groups/{type}/{id}/victimAssets/webSites``
* ``/v2/groups/{type}/{id}/victimAssets/webSites/{assetId}``
* ``/v2/groups/{type}/{id}/victims``
* ``/v2/groups/{type}/{id}/victims/{victimId}``

Adversary Specific Branches
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``/v2/groups/adversaries/{id}/adversaryAssets``
* ``/v2/groups/adversaries/{id}/adversaryAssets/handles``
* ``/v2/groups/adversaries/{id}/adversaryAssets/phoneNumbers``
* ``/v2/groups/adversaries/{id}/adversaryAssets/urls``
* ``/v2/groups/adversaries/{id}/adversaryAssets/handles/{assetId}``
* ``/v2/groups/adversaries/{id}/adversaryAssets/phoneNumbers/{assetId}``
* ``/v2/groups/adversaries/{id}/adversaryAssets/urls/{assetId}``

Document Specific Branches
^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``/v2/groups/documents/{id}/download``
* ``/v2/groups/documents/{id}/upload``

Signature Specific Branch
^^^^^^^^^^^^^^^^^^^^^^^^^

* ``/v2/groups/signatures/{id}/download``

Indicators
----------

* ``/v2/indicators``
* ``/v2/indicators/observed``
* ``/v2/indicators/{type}``
* ``/v2/indicators/{type}/{indicator}``
* ``/v2/indicators/{type}/{indicator}/attributes``
* ``/v2/indicators/{type}/{indicator}/observations``
* ``/v2/indicators/{type}/{indicator}/observationCount``
* ``/v2/indicators/{type}/{indicator}/falsePositive``
* ``/v2/indicators/{type}/{indicator}/attributes/{attributeId}``
* ``/v2/indicators/{type}/{indicator}/attributes/{attributeId}/securityLabels``
* ``/v2/indicators/{type}/{indicator}/attributes/{attributeId}/securityLabels/{securityLabel}``
* ``/v2/indicators/{type}/{indicator}/groups``
* ``/v2/indicators/{type}/{indicator}/groups/adversaries``
* ``/v2/indicators/{type}/{indicator}/groups/adversaries/{groupId}``
* ``/v2/indicators/{type}/{indicator}/groups/documents``
* ``/v2/indicators/{type}/{indicator}/groups/documents/{groupId}``
* ``/v2/indicators/{type}/{indicator}/groups/emails``
* ``/v2/indicators/{type}/{indicator}/groups/emails/{groupId}``
* ``/v2/indicators/{type}/{indicator}/groups/incidents``
* ``/v2/indicators/{type}/{indicator}/groups/incidents/{groupId}``
* ``/v2/indicators/{type}/{indicator}/groups/signatures``
* ``/v2/indicators/{type}/{indicator}/groups/signatures/{groupId}``
* ``/v2/indicators/{type}/{indicator}/groups/threats``
* ``/v2/indicators/{type}/{indicator}/groups/threats/{groupId}``
* ``/v2/indicators/{type}/{indicator}/indicators``
* ``/v2/indicators/files/{indicator}/fileOccurrences``
* ``/v2/indicators/files/{indicator}/fileOccurrences/{fileOccurrenceId}``
* ``/v2/indicators/{type}/{indicator}/indicators/addresses``
* ``/v2/indicators/{type}/{indicator}/indicators/addresses/{indicator}``
* ``/v2/indicators/{type}/{indicator}/indicators/emailAddresses``
* ``/v2/indicators/{type}/{indicator}/indicators/emailAddresses/{indicator}``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/{targetType}``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/{targetType}/{targetId}``
* ``/v2/indicators/{type}/{indicator}/indicators/files``
* ``/v2/indicators/{type}/{indicator}/indicators/files/{indicator}``
* ``/v2/indicators/{type}/{indicator}/indicators/hosts``
* ``/v2/indicators/{type}/{indicator}/indicators/hosts/{indicator}``
* ``/v2/indicators/{type}/{indicator}/indicators/urls``
* ``/v2/indicators/{type}/{indicator}/indicators/urls/{indicator}``
* ``/v2/indicators/{type}/{indicator}/owners``
* ``/v2/indicators/{type}/{indicator}/securityLabels``
* ``/v2/indicators/{type}/{indicator}/securityLabels/{securityLabel}``
* ``/v2/indicators/{type}/{indicator}/tags``
* ``/v2/indicators/{type}/{indicator}/tags/{tagName}``
* ``/v2/indicators/{type}/{indicator}/victimAssets``
* ``/v2/indicators/{type}/{indicator}/victimAssets/emailAddresses``
* ``/v2/indicators/{type}/{indicator}/victimAssets/emailAddresses/{assetId}``
* ``/v2/indicators/{type}/{indicator}/victimAssets/networkAccounts``
* ``/v2/indicators/{type}/{indicator}/victimAssets/networkAccounts/{assetId}``
* ``/v2/indicators/{type}/{indicator}/victimAssets/phoneNumbers``
* ``/v2/indicators/{type}/{indicator}/victimAssets/phoneNumbers/{assetId}``
* ``/v2/indicators/{type}/{indicator}/victimAssets/socialNetworks``
* ``/v2/indicators/{type}/{indicator}/victimAssets/socialNetworks/{assetId}``
* ``/v2/indicators/{type}/{indicator}/victimAssets/webSites``
* ``/v2/indicators/{type}/{indicator}/victimAssets/webSites/{assetId}``
* ``/v2/indicators/{type}/{indicator}/victims``
* ``/v2/indicators/{type}/{indicator}/victims/{victimId}``

Bulk Indicator Download
^^^^^^^^^^^^^^^^^^^^^^^

* ``/v2/indicators/bulk/``
* ``/v2/indicators/bulk/{format}``

Security Labels
---------------

* ``/v2/securityLabels``
* ``/v2/securityLabels/{id}``
* ``/v2/securityLabels/{id}/groups``
* ``/v2/securityLabels/{id}/groups/adversaries``
* ``/v2/securityLabels/{id}/groups/adversaries/{groupId}``
* ``/v2/securityLabels/{id}/groups/documents``
* ``/v2/securityLabels/{id}/groups/documents/{groupId}``
* ``/v2/securityLabels/{id}/groups/emails``
* ``/v2/securityLabels/{id}/groups/emails/{groupId}``
* ``/v2/securityLabels/{id}/groups/incidents``
* ``/v2/securityLabels/{id}/groups/incidents/{groupId}``
* ``/v2/securityLabels/{id}/groups/signatures``
* ``/v2/securityLabels/{id}/groups/signatures/{groupId}``
* ``/v2/securityLabels/{id}/groups/threats``
* ``/v2/securityLabels/{id}/groups/threats/{groupId}``
* ``/v2/securityLabels/{id}/indicators``
* ``/v2/securityLabels/{id}/indicators/addresses``
* ``/v2/securityLabels/{id}/indicators/addresses/{indicator}``
* ``/v2/securityLabels/{id}/indicators/emailAddresses``
* ``/v2/securityLabels/{id}/indicators/emailAddresses/{indicator}``
* ``/v2/securityLabels/{id}/indicators/files``
* ``/v2/securityLabels/{id}/indicators/files/{indicator}``
* ``/v2/securityLabels/{id}/indicators/hosts``
* ``/v2/securityLabels/{id}/indicators/hosts/{indicator}``
* ``/v2/securityLabels/{id}/indicators/urls``
* ``/v2/securityLabels/{id}/indicators/urls/{indicator}``

Tags
----

* ``/v2/tags``
* ``/v2/tags/{tagName}``
* ``/v2/tags/{tagName}/groups``
* ``/v2/tags/{tagName}/groups/adversaries``
* ``/v2/tags/{tagName}/groups/adversaries/{groupId}``
* ``/v2/tags/{tagName}/groups/documents``
* ``/v2/tags/{tagName}/groups/documents/{groupId}``
* ``/v2/tags/{tagName}/groups/emails``
* ``/v2/tags/{tagName}/groups/emails/{groupId}``
* ``/v2/tags/{tagName}/groups/incidents``
* ``/v2/tags/{tagName}/groups/incidents/{groupId}``
* ``/v2/tags/{tagName}/groups/signatures``
* ``/v2/tags/{tagName}/groups/signatures/{groupId}``
* ``/v2/tags/{tagName}/groups/threats``
* ``/v2/tags/{tagName}/groups/threats/{groupId}``
* ``/v2/tags/{tagName}/indicators``
* ``/v2/tags/{tagName}/indicators/addresses``
* ``/v2/tags/{tagName}/indicators/addresses/{indicator}``
* ``/v2/tags/{tagName}/indicators/emailAddresses``
* ``/v2/tags/{tagName}/indicators/emailAddresses/{indicator}``
* ``/v2/tags/{tagName}/indicators/files``
* ``/v2/tags/{tagName}/indicators/files/{indicator}``
* ``/v2/tags/{tagName}/indicators/hosts``
* ``/v2/tags/{tagName}/indicators/hosts/{indicator}``
* ``/v2/tags/{tagName}/indicators/urls``
* ``/v2/tags/{tagName}/indicators/urls/{indicator}``

Tasks
-----

* ``/v2/tasks``
* ``/v2/tasks/{id}``
* ``/v2/tasks/{id}/escalatees``
* ``/v2/tasks/{id}/assignees``
* ``/v2/tasks/{id}/assignees/{assigneeId}``
* ``/v2/tasks/{id}/escalatees/{escalateeId}``
* ``/v2/tasks/{id}/escalatees/{userName}``
* ``/v2/tasks/{id}/assignees/{userName}``
* ``/v2/tasks/{id}/groups``
* ``/v2/tasks/{id}/groups/adversaries``
* ``/v2/tasks/{id}/groups/adversaries/{groupId}``
* ``/v2/tasks/{id}/groups/documents``
* ``/v2/tasks/{id}/groups/documents/{groupId}``
* ``/v2/tasks/{id}/groups/emails``
* ``/v2/tasks/{id}/groups/emails/{groupId}``
* ``/v2/tasks/{id}/groups/incidents``
* ``/v2/tasks/{id}/groups/incidents/{groupId}``
* ``/v2/tasks/{id}/groups/signatures``
* ``/v2/tasks/{id}/groups/signatures/{groupId}``
* ``/v2/tasks/{id}/groups/threats``
* ``/v2/tasks/{id}/groups/threats/{groupId}``
* ``/v2/tasks/{id}/indicators``
* ``/v2/tasks/{id}/indicators/addresses``
* ``/v2/tasks/{id}/indicators/addresses/{indicator}``
* ``/v2/tasks/{id}/indicators/emailAddresses``
* ``/v2/tasks/{id}/indicators/emailAddresses/{indicator}``
* ``/v2/tasks/{id}/indicators/files``
* ``/v2/tasks/{id}/indicators/files/{indicator}``
* ``/v2/tasks/{id}/indicators/hosts``
* ``/v2/tasks/{id}/indicators/hosts/{indicator}``
* ``/v2/tasks/{id}/indicators/urls``
* ``/v2/tasks/{id}/indicators/urls/{indicator}``
* ``/v2/tasks/{id}/attributes``
* ``/v2/tasks/{id}/tags``
* ``/v2/tasks/{id}/tags/{tagName}``

Victims
-------

* ``/v2/victims``
* ``/v2/victims/{id}``
* ``/v2/victims/{id}/groups``
* ``/v2/victims/{id}/groups/adversaries``
* ``/v2/victims/{id}/groups/adversaries/{groupId}``
* ``/v2/victims/{id}/groups/documents``
* ``/v2/victims/{id}/groups/documents/{groupId}``
* ``/v2/victims/{id}/groups/emails``
* ``/v2/victims/{id}/groups/emails/{groupId}``
* ``/v2/victims/{id}/groups/incidents``
* ``/v2/victims/{id}/groups/incidents/{groupId}``
* ``/v2/victims/{id}/groups/signatures``
* ``/v2/victims/{id}/groups/signatures/{groupId}``
* ``/v2/victims/{id}/groups/threats``
* ``/v2/victims/{id}/groups/threats/{groupId}``
* ``/v2/victims/{id}/indicators``
* ``/v2/victims/{id}/indicators/addresses``
* ``/v2/victims/{id}/indicators/addresses/{indicator}``
* ``/v2/victims/{id}/indicators/emailAddresses``
* ``/v2/victims/{id}/indicators/emailAddresses/{indicator}``
* ``/v2/victims/{id}/indicators/files``
* ``/v2/victims/{id}/indicators/files/{indicator}``
* ``/v2/victims/{id}/indicators/hosts``
* ``/v2/victims/{id}/indicators/hosts/{indicator}``
* ``/v2/victims/{id}/indicators/urls``
* ``/v2/victims/{id}/indicators/urls/{indicator}``
* ``/v2/victims/{uniqueId}/victimAssets``
* ``/v2/victims/{id}/victimAssets/emailAddresses``
* ``/v2/victims/{id}/victimAssets/emailAddresses/{assetId}``
* ``/v2/victims/{id}/victimAssets/networkAccounts``
* ``/v2/victims/{id}/victimAssets/networkAccounts/{assetId}``
* ``/v2/victims/{id}/victimAssets/phoneNumbers``
* ``/v2/victims/{id}/victimAssets/phoneNumbers/{assetId}``
* ``/v2/victims/{id}/victimAssets/socialNetworks``
* ``/v2/victims/{id}/victimAssets/socialNetworks/{assetId}``
* ``/v2/victims/{id}/victimAssets/webSites``
* ``/v2/victims/{id}/victimAssets/webSites/{assetId}``


Misc
----

Batch Indicator Commit
^^^^^^^^^^^^^^^^^^^^^^

* ``/v2/batch``
* ``/v2/batch/{id}``
* ``/v2/batch/{id}``
* ``/v2/batch/{id}/errors``

User Information
^^^^^^^^^^^^^^^^

* ``/v2/whoami``

HTTP Responses
--------------

The API will return appropriate HTTP response codes with a description in the message field as detailed in the table below. This can be helpful when troubleshooting queries.

+--------------------+----------------------------------------------------------+
| HTTP Response      | Explanation                                              |
| Code               |                                                          |
+====================+==========================================================+
| ``200`` - Success  | Successful execution of a request.                       |
+--------------------+----------------------------------------------------------+
| ``201`` - Created  | The query successfully created the specified entity.     |
+--------------------+----------------------------------------------------------+
| ``400`` - Bad      | Status returned if the request was not properly          |
| Request            | formatted. The message included with the response will   |
|                    | include details.                                         |
+--------------------+----------------------------------------------------------+
| ``401`` -          | Returned if a user does not have access to the specified |
| Unauthorized       | resource or the method attempted on a resource.          |
+--------------------+----------------------------------------------------------+
| ``403`` -          | Returned when specifying an Owner to which the user does |
| Forbidden          | do not have access, or does not exist.                   |
+--------------------+----------------------------------------------------------+
| ``403`` - Bad      | This Indicator is included in a system-wide exclusion    |
| Request            | list.                                                    |
+--------------------+----------------------------------------------------------+
| ``404`` - Not      | The service or resource specified in the path does not   |
| Found              | exist.                                                   |
+--------------------+----------------------------------------------------------+
| ``500`` - Internal | An unknown internal error                                |
| Server Error       |                                                          |
+--------------------+----------------------------------------------------------+
| ``503`` - Service  | The Instance of ThreatConnect is not licensed to enable  |
| Unavailable        | the API.                                                 |
+--------------------+----------------------------------------------------------+
