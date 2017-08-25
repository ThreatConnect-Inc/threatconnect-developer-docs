API Overview
============

The following **Group types** are available via ThreatConnect's API:

.. include:: _includes/group_types.rst

In addition to the custom Indicators available in your instance of ThreatConnect, the following **Indicator types** will be available via ThreatConnect's API:

.. include:: _includes/indicator_types.rst

The following **Victim Asset types** will be available via ThreatConnect's API:

.. include:: _includes/victim_asset_types.rst

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
* ``/v2/groups/{type}/{id}/groups/{associatedGroupType}``
* ``/v2/groups/{type}/{id}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/groups/{type}/{id}/indicators``
* ``/v2/groups/{type}/{id}/indicators/{associatedIndicatorType}``
* ``/v2/groups/{type}/{id}/indicators/{associatedIndicatorType}/{associatedIndicator}``
* ``/v2/groups/{type}/{id}/publish``
* ``/v2/groups/{type}/{id}/securityLabels``
* ``/v2/groups/{type}/{id}/securityLabels/{securityLabel}``
* ``/v2/groups/{type}/{id}/tags``
* ``/v2/groups/{type}/{id}/tags/{tagName}``
* ``/v2/groups/{type}/{id}/victimAssets``
* ``/v2/groups/{type}/{id}/victimAssets/{victimAssetType}``
* ``/v2/groups/{type}/{id}/victimAssets/{victimAssetType}/{assetId}``
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
* ``/v2/indicators/{type}/{indicator}/groups/{associatedGroupType}``
* ``/v2/indicators/{type}/{indicator}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/indicators/{type}/{indicator}/indicators``
* ``/v2/indicators/{type}/{indicator}/indicators/{associatedIndicatorType}``
* ``/v2/indicators/{type}/{indicator}/indicators/{associatedIndicatorType}/{associatedIndicator}``
* ``/v2/indicators/files/{indicator}/fileOccurrences``
* ``/v2/indicators/files/{indicator}/fileOccurrences/{fileOccurrenceId}``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/{targetType}``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/{targetType}/{targetId}``
* ``/v2/indicators/{type}/{indicator}/owners``
* ``/v2/indicators/{type}/{indicator}/securityLabels``
* ``/v2/indicators/{type}/{indicator}/securityLabels/{securityLabel}``
* ``/v2/indicators/{type}/{indicator}/tags``
* ``/v2/indicators/{type}/{indicator}/tags/{tagName}``
* ``/v2/indicators/{type}/{indicator}/victimAssets``
* ``/v2/indicators/{type}/{indicator}/victimAssets/{victimAssetType}``
* ``/v2/indicators/{type}/{indicator}/victimAssets/{victimAssetType}/{assetId}``
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
* ``/v2/securityLabels/{id}/groups/{associatedGroupType}``
* ``/v2/securityLabels/{id}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/securityLabels/{id}/indicators``
* ``/v2/securityLabels/{id}/indicators/{associatedIndicatorType}``
* ``/v2/securityLabels/{id}/indicators/{associatedIndicatorType}/{associatedIndicator}``

Tags
----

* ``/v2/tags``
* ``/v2/tags/{tagName}``
* ``/v2/tags/{tagName}/groups``
* ``/v2/tags/{tagName}/groups/{associatedGroupType}``
* ``/v2/tags/{tagName}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/tags/{tagName}/indicators``
* ``/v2/tags/{tagName}/indicators/{associatedIndicatorType}``
* ``/v2/tags/{tagName}/indicators/{associatedIndicatorType}/{associatedIndicator}``

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
* ``/v2/tasks/{id}/groups/{associatedGroupType}``
* ``/v2/tasks/{id}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/tasks/{id}/indicators``
* ``/v2/tasks/{id}/indicators/{associatedIndicatorType}``
* ``/v2/tasks/{id}/indicators/{associatedIndicatorType}/{associatedIndicator}``
* ``/v2/tasks/{id}/attributes``
* ``/v2/tasks/{id}/tags``
* ``/v2/tasks/{id}/tags/{tagName}``

Victims
-------

* ``/v2/victims``
* ``/v2/victims/{id}``
* ``/v2/victims/{id}/groups``
* ``/v2/victims/{id}/groups/{associatedGroupType}``
* ``/v2/victims/{id}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/victims/{id}/indicators``
* ``/v2/victims/{id}/indicators/{associatedIndicatorType}``
* ``/v2/victims/{id}/indicators/{associatedIndicatorType}/{associatedIndicator}``
* ``/v2/victims/{uniqueId}/victimAssets``
* ``/v2/victims/{id}/victimAssets/{victimAssetType}``
* ``/v2/victims/{id}/victimAssets/{victimAssetType}/{assetId}``

Misc
----

Association Types
^^^^^^^^^^^^^^^^^

* ``/v2/types/associationTypes``
* ``/v2/types/associationTypes/{associationType}``

Batch Indicator Commit
^^^^^^^^^^^^^^^^^^^^^^

* ``/v2/batch``
* ``/v2/batch/{id}``
* ``/v2/batch/{id}/errors``

Indicator Types
^^^^^^^^^^^^^^^

* ``/v2/types/indicatorTypes``
* ``/v2/types/indicatorTypes/{indicatorType}``

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
