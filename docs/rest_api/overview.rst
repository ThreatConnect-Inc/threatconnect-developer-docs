Complete List of API Endpoints
==============================

Owners
------

* ``/v2/owners``
* ``/v2/owners/mine``
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
* ``/v2/groups/{type}/{id}/indicators/addresses/{indicatorId}``
* ``/v2/groups/{type}/{id}/indicators/emailAddresses``
* ``/v2/groups/{type}/{id}/indicators/emailAddresses/{indicatorId}``
* ``/v2/groups/{type}/{id}/indicators/{type}/{indicatorId}``
* ``/v2/groups/{type}/{id}/indicators/files``
* ``/v2/groups/{type}/{id}/indicators/files/{indicatorId}``
* ``/v2/groups/{type}/{id}/indicators/hosts``
* ``/v2/groups/{type}/{id}/indicators/hosts/{indicatorId}``
* ``/v2/groups/{type}/{id}/indicators/urls``
* ``/v2/groups/{type}/{id}/indicators/urls/{indicatorId}``
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

* ``/v2/groups/documents``
* ``/v2/groups/documents/{id}``
* ``/v2/groups/documents/{id}/download``
* ``/v2/groups/documents/{id}/upload``

Indicators
----------

* ``/v2/indicators``
* ``/v2/indicators/{type}``
* ``/v2/indicators/{type}/{id}``
* ``/v2/indicators/{type}/{id}/attributes``
* ``/v2/indicators/{type}/{id}/observations``
* ``/v2/indicators/{type}/{id}/observationCount``
* ``/v2/indicators/{type}/{id}/falsePositive``
* ``/v2/indicators/{type}/{id}/attributes/{attributeId}``
* ``/v2/indicators/{type}/{id}/attributes/{attributeId}/securityLabels``
* ``/v2/indicators/{type}/{id}/attributes/{attributeId}/securityLabels/{securityLabel}``
* ``/v2/indicators/{type}/{id}/groups``
* ``/v2/indicators/{type}/{id}/groups/adversaries``
* ``/v2/indicators/{type}/{id}/groups/adversaries/{groupId}``
* ``/v2/indicators/{type}/{id}/groups/documents``
* ``/v2/indicators/{type}/{id}/groups/documents/{groupId}``
* ``/v2/indicators/{type}/{id}/groups/emails``
* ``/v2/indicators/{type}/{id}/groups/emails/{groupId}``
* ``/v2/indicators/{type}/{id}/groups/incidents``
* ``/v2/indicators/{type}/{id}/groups/incidents/{groupId}``
* ``/v2/indicators/{type}/{id}/groups/signatures``
* ``/v2/indicators/{type}/{id}/groups/signatures/{groupId}``
* ``/v2/indicators/{type}/{id}/groups/threats``
* ``/v2/indicators/{type}/{id}/groups/threats/{groupId}``
* ``/v2/indicators/{type}/{id}/indicators``
* ``/v2/indicators/files/{id}/fileOccurrences``
* ``/v2/indicators/files/{id}/fileOccurrences/{fileOccurrenceId}``
* ``/v2/indicators/{type}/{id}/indicators/addresses``
* ``/v2/indicators/{type}/{id}/indicators/addresses/{indicatorId}``
* ``/v2/indicators/{type}/{id}/indicators/emailAddresses``
* ``/v2/indicators/{type}/{id}/indicators/emailAddresses/{indicatorId}``
* ``/v2/indicators/{type}/{uniqueId}/associations/{associationType}/indicators/``
* ``/v2/indicators/{type}/{uniqueId}/associations/{associationType}/indicators/{targetType}``
* ``/v2/indicators/{type}/{uniqueId}/associations/{associationType}/indicators/{targetType}/{targetId}``
* ``/v2/indicators/{type}/{id}/indicators/files``
* ``/v2/indicators/{type}/{id}/indicators/files/{indicatorId}``
* ``/v2/indicators/{type}/{id}/indicators/hosts``
* ``/v2/indicators/{type}/{id}/indicators/hosts/{indicatorId}``
* ``/v2/indicators/{type}/{id}/indicators/urls``
* ``/v2/indicators/{type}/{id}/indicators/urls/{indicatorId}``
* ``/v2/indicators/{type}/{id}/owners``
* ``/v2/indicators/{type}/{id}/securityLabels``
* ``/v2/indicators/{type}/{id}/securityLabels/{securityLabel}``
* ``/v2/indicators/{type}/{id}/tags``
* ``/v2/indicators/{type}/{id}/tags/{tagName}``
* ``/v2/indicators/{type}/{id}/victimAssets``
* ``/v2/indicators/{type}/{id}/victimAssets/emailAddresses``
* ``/v2/indicators/{type}/{id}/victimAssets/emailAddresses/{assetId}``
* ``/v2/indicators/{type}/{id}/victimAssets/networkAccounts``
* ``/v2/indicators/{type}/{id}/victimAssets/networkAccounts/{assetId}``
* ``/v2/indicators/{type}/{id}/victimAssets/phoneNumbers``
* ``/v2/indicators/{type}/{id}/victimAssets/phoneNumbers/{assetId}``
* ``/v2/indicators/{type}/{id}/victimAssets/socialNetworks``
* ``/v2/indicators/{type}/{id}/victimAssets/socialNetworks/{assetId}``
* ``/v2/indicators/{type}/{id}/victimAssets/webSites``
* ``/v2/indicators/{type}/{id}/victimAssets/webSites/{assetId}``
* ``/v2/indicators/{type}/{id}/victims``
* ``/v2/indicators/{type}/{id}/victims/{victimId}``

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
* ``/v2/securityLabels/{id}/indicators/addresses/{indicatorId}``
* ``/v2/securityLabels/{id}/indicators/emailAddresses``
* ``/v2/securityLabels/{id}/indicators/emailAddresses/{indicatorId}``
* ``/v2/securityLabels/{id}/indicators/files``
* ``/v2/securityLabels/{id}/indicators/files/{indicatorId}``
* ``/v2/securityLabels/{id}/indicators/hosts``
* ``/v2/securityLabels/{id}/indicators/hosts/{indicatorId}``
* ``/v2/securityLabels/{id}/indicators/urls``
* ``/v2/securityLabels/{id}/indicators/urls/{indicatorId}``

Tags
----

* ``/v2/tags``
* ``/v2/tags/{id}``
* ``/v2/tags/{id}/groups``
* ``/v2/tags/{id}/groups/adversaries``
* ``/v2/tags/{id}/groups/adversaries/{groupId}``
* ``/v2/tags/{id}/groups/documents``
* ``/v2/tags/{id}/groups/documents/{groupId}``
* ``/v2/tags/{id}/groups/emails``
* ``/v2/tags/{id}/groups/emails/{groupId}``
* ``/v2/tags/{id}/groups/incidents``
* ``/v2/tags/{id}/groups/incidents/{groupId}``
* ``/v2/tags/{id}/groups/signatures``
* ``/v2/tags/{id}/groups/signatures/{groupId}``
* ``/v2/tags/{id}/groups/threats``
* ``/v2/tags/{id}/groups/threats/{groupId}``
* ``/v2/tags/{id}/indicators``
* ``/v2/tags/{id}/indicators/addresses``
* ``/v2/tags/{id}/indicators/addresses/{indicatorId}``
* ``/v2/tags/{id}/indicators/emailAddresses``
* ``/v2/tags/{id}/indicators/emailAddresses/{indicatorId}``
* ``/v2/tags/{id}/indicators/files``
* ``/v2/tags/{id}/indicators/files/{indicatorId}``
* ``/v2/tags/{id}/indicators/hosts``
* ``/v2/tags/{id}/indicators/hosts/{indicatorId}``
* ``/v2/tags/{id}/indicators/urls``
* ``/v2/tags/{id}/indicators/urls/{indicatorId}``

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
* ``/v2/tasks/{id}/indicators/addresses/{indicatorId}``
* ``/v2/tasks/{id}/indicators/emailAddresses``
* ``/v2/tasks/{id}/indicators/emailAddresses/{indicatorId}``
* ``/v2/tasks/{id}/indicators/files``
* ``/v2/tasks/{id}/indicators/files/{indicatorId}``
* ``/v2/tasks/{id}/indicators/hosts``
* ``/v2/tasks/{id}/indicators/hosts/{indicatorId}``
* ``/v2/tasks/{id}/indicators/urls``
* ``/v2/tasks/{id}/indicators/urls/{indicatorId}``
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
* ``/v2/victims/{id}/indicators/addresses/{indicatorId}``
* ``/v2/victims/{id}/indicators/emailAddresses``
* ``/v2/victims/{id}/indicators/emailAddresses/{indicatorId}``
* ``/v2/victims/{id}/indicators/files``
* ``/v2/victims/{id}/indicators/files/{indicatorId}``
* ``/v2/victims/{id}/indicators/hosts``
* ``/v2/victims/{id}/indicators/hosts/{indicatorId}``
* ``/v2/victims/{id}/indicators/urls``
* ``/v2/victims/{id}/indicators/urls/{indicatorId}``
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
