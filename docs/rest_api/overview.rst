API Overview
============

Pagination
----------

To enable pagination in an API call, use a query in the following format:

.. code::

    GET /v2/{insert query here...}?resultStart=0&resultLimit=50

For example, the query below will return 50 Incidents:

.. code::

    /v2/groups/incidents?resultStart=0&resultLimit=50

Pagination works by specifying a starting result index, as well as a result limit of items to be returned as HTTP query parameters to the request. For example, requesting a result start index of 50 and a result limit of 100 will retrieve items 50 to 150.

The table below displays the query parameters.

+---------------+-----------------------------------------------+---------+
| HTTP Query    | Description                                   | Default |
| Parameter     |                                               |         |
+===============+===============================================+=========+
| resultStart\* | The starting index of the result list that is | 0       |
|               | returned                                      |         |
+---------------+-----------------------------------------------+---------+
| resultLimit   | The limit to the number of results to return  | 100     |
|               | with the request                              |         |
+---------------+-----------------------------------------------+---------+

\*Specifying a ``resultStart`` other than 0 will omit the ``resultCount`` field in the return data for performance reasons.

A request that does not include the parameters indicated is assumed to use the default values above. A request having a ``resultStart`` value of 0 will return the current count of all items being queried. This count should be saved to iterate over the Collection and to know when all items have been retrieved. The maximum value that can be specified for ``resultLimit`` is 10,000.

.. note:: Pagination counts and indices should not be stored in long-lived applications as a way to return to a result-set. The dataset will change with time, so those range markers might cause objects to be skipped or duplicated if reused at a later time.

Available Endpoints
-------------------

Owner Endpoints
^^^^^^^^^^^^^^^

The following Owner-related endpoints are available:

* ``/v2/owners``
* ``/v2/owners/metrics``
* ``/v2/owners/{id}/metrics``
* ``/v2/owners/mine``
* ``/v2/owners/mine/members``

Group Endpoints
^^^^^^^^^^^^^^^

The following **Group types** are available via ThreatConnect's API:

.. include:: _includes/group_types.rst

The following Group-related endpoints are available:

* ``/v2/groups``
* ``/v2/groups/{type}``
* ``/v2/groups/{type}/{id}``
* ``/v2/groups/{type}/{id}/attributes``
* ``/v2/groups/{type}/{id}/attributes/{attributeId}``
* ``/v2/groups/{type}/{id}/attributes/{attributeId}/securityLabels``
* ``/v2/groups/{type}/{id}/attributes/{attributeId}/securityLabels/{securityLabelName}``
* ``/v2/groups/{type}/{id}/groups``
* ``/v2/groups/{type}/{id}/groups/{associatedGroupType}``
* ``/v2/groups/{type}/{id}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/groups/{type}/{id}/indicators``
* ``/v2/groups/{type}/{id}/indicators/{associatedIndicatorType}``
* ``/v2/groups/{type}/{id}/pdf``
* ``/v2/groups/{type}/{id}/publish``
* ``/v2/groups/{type}/{id}/securityLabels``
* ``/v2/groups/{type}/{id}/securityLabels/{securityLabelName}``
* ``/v2/groups/{type}/{id}/tags``
* ``/v2/groups/{type}/{id}/tags/{tagName}``
* ``/v2/groups/{type}/{id}/victimAssets``
* ``/v2/groups/{type}/{id}/victimAssets/{victimAssetType}``
* ``/v2/groups/{type}/{id}/victimAssets/{victimAssetType}/{assetId}``
* ``/v2/groups/{type}/{id}/victims``
* ``/v2/groups/{type}/{id}/victims/{victimId}``

Adversary-Specific Endpoints
""""""""""""""""""""""""""""

* ``/v2/groups/adversaries/{id}/adversaryAssets``
* ``/v2/groups/adversaries/{id}/adversaryAssets/handles``
* ``/v2/groups/adversaries/{id}/adversaryAssets/handles/{assetId}``
* ``/v2/groups/adversaries/{id}/adversaryAssets/phoneNumbers``
* ``/v2/groups/adversaries/{id}/adversaryAssets/phoneNumbers/{assetId}``
* ``/v2/groups/adversaries/{id}/adversaryAssets/urls``
* ``/v2/groups/adversaries/{id}/adversaryAssets/urls/{assetId}``

Document-Specific Endpoints
"""""""""""""""""""""""""""

* ``/v2/groups/documents/{id}/download``
* ``/v2/groups/documents/{id}/upload``

Signature-Specific Endpoints
""""""""""""""""""""""""""""

* ``/v2/groups/signatures/{id}/download``

Indicator Endpoints
^^^^^^^^^^^^^^^^^^^

In addition to the `Custom Indicators <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#retrieve-available-indicator-types>`_ available in your instance of ThreatConnect, the following **Indicator types** will be available via ThreatConnect's API:

.. include:: _includes/indicator_types.rst

The following Indicator-related endpoints are available:

* ``/v2/indicators``
* ``/v2/indicators/deleted``
* ``/v2/indicators/hosts/deleted``
* ``/v2/indicators/addresses/deleted``
* ``/v2/indicators/urls/deleted``
* ``/v2/indicators/files/deleted``
* ``/v2/indicators/emailAddresses/deleted``
* ``/v2/indicators/{custom Indicator type}/deleted``
* ``/v2/indicators/observed``
* ``/v2/indicators/{type}``
* ``/v2/indicators/{type}/{indicator}``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/{targetType}``
* ``/v2/indicators/{type}/{indicator}/associations/{associationType}/indicators/{targetType}/{targetId}``
* ``/v2/indicators/{type}/{indicator}/attributes``
* ``/v2/indicators/{type}/{indicator}/attributes/{attributeId}``
* ``/v2/indicators/{type}/{indicator}/attributes/{attributeId}/securityLabels``
* ``/v2/indicators/{type}/{indicator}/attributes/{attributeId}/securityLabels/{securityLabelName}``
* ``/v2/indicators/{type}/{indicator}/falsePositive``
* ``/v2/indicators/{type}/{indicator}/groups``
* ``/v2/indicators/{type}/{indicator}/groups/{associatedGroupType}``
* ``/v2/indicators/{type}/{indicator}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/indicators/{type}/{indicator}/indicators``
* ``/v2/indicators/{type}/{indicator}/indicators/{associatedIndicatorType}``
* ``/v2/indicators/{type}/{indicator}/indicators/{associatedIndicatorType}/{associatedIndicator}``
* ``/v2/indicators/{type}/{indicator}/observations``
* ``/v2/indicators/{type}/{indicator}/observationCount``
* ``/v2/indicators/{type}/{indicator}/owners``
* ``/v2/indicators/{type}/{indicator}/securityLabels``
* ``/v2/indicators/{type}/{indicator}/securityLabels/{securityLabelName}``
* ``/v2/indicators/{type}/{indicator}/tags``
* ``/v2/indicators/{type}/{indicator}/tags/{tagName}``
* ``/v2/indicators/{type}/{indicator}/victimAssets``
* ``/v2/indicators/{type}/{indicator}/victimAssets/{victimAssetType}``
* ``/v2/indicators/{type}/{indicator}/victimAssets/{victimAssetType}/{assetId}``
* ``/v2/indicators/{type}/{indicator}/victims``
* ``/v2/indicators/{type}/{indicator}/victims/{associatedVictimId}``

File-Indicator-Specific Endpoints
"""""""""""""""""""""""""""""""""

* ``/v2/indicators/files/{indicator}/fileOccurrences``
* ``/v2/indicators/files/{indicator}/fileOccurrences/{fileOccurrenceId}``

Bulk-Indicator Download
"""""""""""""""""""""""

* ``/v2/indicators/bulk/``
* ``/v2/indicators/bulk/{format}``

Security-Label Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^

The following Security-Label-related endpoints are available:

* ``/v2/securityLabels``
* ``/v2/securityLabels/{securityLabelName}``
* ``/v2/securityLabels/{securityLabelName}/groups``
* ``/v2/securityLabels/{securityLabelName}/groups/{groupType}``
* ``/v2/securityLabels/{securityLabelName}/groups/{groupType}/{groupId}``
* ``/v2/securityLabels/{securityLabelName}/indicators``
* ``/v2/securityLabels/{securityLabelName}/indicators/{indicatorType}``
* ``/v2/securityLabels/{securityLabelName}/indicators/{indicatorType}/{indicator}``
* ``/v2/securityLabels/{securityLabelName}/tasks``
* ``/v2/securityLabels/{securityLabelName}/tasks/{taskId}``
* ``/v2/securityLabels/{securityLabelName}/victims``
* ``/v2/securityLabels/{securityLabelName}/victims/{victimId}``

Tag Endpoints
^^^^^^^^^^^^^

The following Tag-related endpoints are available:

* ``/v2/tags``
* ``/v2/tags/{tagName}``
* ``/v2/tags/{tagName}/groups``
* ``/v2/tags/{tagName}/groups/{associatedGroupType}``
* ``/v2/tags/{tagName}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/tags/{tagName}/indicators``
* ``/v2/tags/{tagName}/indicators/{associatedIndicatorType}``
* ``/v2/tags/{tagName}/tasks``
* ``/v2/tags/{tagName}/tasks/{associatedTaskId}``
* ``/v2/tags/{tagName}/victims``
* ``/v2/tags/{tagName}/victims/{associatedVictimId}``

Task Endpoints
^^^^^^^^^^^^^^

The following Task-related endpoints are available:

* ``/v2/tasks``
* ``/v2/tasks/{id}``
* ``/v2/tasks/{id}/assignees``
* ``/v2/tasks/{id}/assignees/{assigneeId}``
* ``/v2/tasks/{id}/assignees/{userName}``
* ``/v2/tasks/{id}/attributes``
* ``/v2/tasks/{id}/attributes/{attributeId}``
* ``/v2/tasks/{id}/attributes/{attributeId}/securityLabels``
* ``/v2/tasks/{id}/attributes/{attributeId}/securityLabels/{securityLabelName}``
* ``/v2/tasks/{id}/escalatees``
* ``/v2/tasks/{id}/escalatees/{escalateeId}``
* ``/v2/tasks/{id}/escalatees/{userName}``
* ``/v2/tasks/{id}/groups``
* ``/v2/tasks/{id}/groups/{associatedGroupType}``
* ``/v2/tasks/{id}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/tasks/{id}/indicators``
* ``/v2/tasks/{id}/indicators/{associatedIndicatorType}``
* ``/v2/tasks/{id}/tags``
* ``/v2/tasks/{id}/tags/{tagName}``
* ``/v2/tasks/{id}/tasks``
* ``/v2/tasks/{id}/tasks/{associatedTaskId}``

Victim Endpoints
^^^^^^^^^^^^^^^^

The following **Victim-Asset types** will be available via ThreatConnect's API:

.. include:: _includes/victim_asset_types.rst

The following Victim-related endpoints are available:

* ``/v2/victims``
* ``/v2/victims/{id}``
* ``/v2/victims/{id}/attributes``
* ``/v2/victims/{id}/attributes/{attributeId}``
* ``/v2/victims/{id}/attributes/{attributeId}/securityLabels``
* ``/v2/victims/{id}/attributes/{attributeId}/securityLabels/{securityLabelName}``
* ``/v2/victims/{id}/groups``
* ``/v2/victims/{id}/groups/{associatedGroupType}``
* ``/v2/victims/{id}/groups/{associatedGroupType}/{associatedGroupId}``
* ``/v2/victims/{id}/indicators``
* ``/v2/victims/{id}/indicators/{associatedIndicatorType}``
* ``/v2/victims/{id}/tags``
* ``/v2/victims/{id}/tags/{tagName}``
* ``/v2/victims/{id}/tasks``
* ``/v2/victims/{id}/tasks/{associatedTaskId}``
* ``/v2/victims/{id}/victimAssets``
* ``/v2/victims/{id}/victimAssets/{victimAssetType}``
* ``/v2/victims/{id}/victimAssets/{victimAssetType}/{assetId}``

Custom-Metric Endpoints
^^^^^^^^^^^^^^^^^^^^^^^

* ``/v2/customMetrics/``
* ``/v2/customMetrics/{metricId}``
* ``/v2/customMetrics/{metricId}/data``

Miscellaneous Endpoints
^^^^^^^^^^^^^^

Association-Type Endpoints
""""""""""""""""""""""""""

* ``/v2/types/associationTypes``
* ``/v2/types/associationTypes/{associationType}``

Batch-Indicator-Commit Endpoints
""""""""""""""""""""""""""""""""

* ``/v2/batch``
* ``/v2/batch/{id}``
* ``/v2/batch/{id}/errors``

Indicator-Type Endpoints
""""""""""""""""""""""""

* ``/v2/types/indicatorTypes``
* ``/v2/types/indicatorTypes/{indicatorType}``

User-Information Endpoints
""""""""""""""""""""""""""

* ``/v2/whoami``

HTTP Responses
--------------

The API will return appropriate HTTP response codes with a description in the message field as detailed in the table below. This can be helpful when troubleshooting queries.

+--------------------+----------------------------------------------------------+
| HTTP Response      | Explanation                                              |
| Code               |                                                          |
+====================+==========================================================+
| ``200`` - Success  | Successful execution of a request                       |
+--------------------+----------------------------------------------------------+
| ``201`` - Created  | The query successfully created the specified entity.     |
+--------------------+----------------------------------------------------------+
| ``400`` - Bad      | Status returned if the request was not properly          |
| Request            | formatted. The message included with the response will   |
|                    | include details.                                         |
+--------------------+----------------------------------------------------------+
| ``401`` -          | Returned if a user does not have access to the specified |
| Unauthorized       | resource or the method attempted on a resource          |
+--------------------+----------------------------------------------------------+
| ``403`` -          | Returned when specifying an Owner to which the user does |
| Forbidden          | do not have access, or does not exist                   |
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

Specifying an Owner
-------------------

By default, all API calls will operate in the API user account's default organization. To specify a different Owner, use the ``owner`` URL parameter like ``?owner={ownerName}``. For example, the following query will return all Host Indicators in the Common Community:

.. code::

    GET https://api.threatconnect.com/v2/indicators/hosts/?owner=Common%20Community

Retrieving an Item's Tags and Attributes
----------------------------------------

As of ThreatConnect version 5.4, it is possible to retrieve the Tags and Attributes for an item (a Group, Indicator, Task, or Victim).

To retrieve Tags along with the requested items, append the following query string to the query:

.. code::

    ?includeTags=true

To retrieve Attributes along with the requested items, append the following query string to the query:

.. code::

    ?includeAttributes=true

For example, to retrieve all Hosts along with their Tags and Attributes, use the following query:

.. code::

    GET /v2/indicators/hosts?includeTags=true&includeAttributes=true

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "host": [
          {
            "id": 123456,
            "owner": {
              "id": 2,
              "name": "Example Org",
              "type": "Organization"
            },
            "dateAdded": "2017-10-31T16:55:44Z",
            "lastModified": "2017-11-06T13:23:13Z",
            "rating": 4.00,
            "confidence": 85,
            "threatAssessRating": 4.37,
            "threatAssessConfidence": 72.91,
            "threatAssessScore": 650,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=example.org&owner=Example+Org",
            "source": "US-EAST-3 Network Logs",
            "description": "Malicious domain.",
            "attribute": [
              {
                "id": 54321,
                "type": "Description",
                "value": "Malicious domain.",
                "dateAdded": "2017-10-31T16:59:15Z",
                "lastModified": "2017-10-31T16:59:15Z",
                "displayed": true
              }
            ],
            "tag": [
              {
                "name": "Nation State",
                "description": "Activity likely backed or directly related to a nation state.",
                "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Nation+State&owner=Example+Org"
              }
            ],
            "hostName": "example.org",
            "dnsActive": "true",
            "whoisActive": "true"
          }
        ]
      }
    }

In another example, to retrieve all Tasks with their Tags, use the following query:

.. code::

    GET /v2/tasks?includeTags=true

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "task": [
          {
            "id": 123456,
            "name": "Deploy Update Blacklist to Firewall",
            "ownerName": "Example Org",
            "dateAdded": "2017-11-04T13:51:52Z",
            "webLink": "https://app.threatconnect.com/auth/workflow/task.xhtml?task=123456",
            "tag": [
              {
                "name": "Deploy",
                "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Deploy&owner=Example+Org"
              }
            ],
            "status": "Not Started",
            "escalated": false,
            "reminded": false,
            "overdue": false
          }
        ]
      }
    }
