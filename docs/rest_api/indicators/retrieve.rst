Retrieve Indicators
-------------------

.. include:: filters.rst

Retrieve Available Indicator Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To find the available Indicator types on your instance of ThreatConnect, use the following query:

.. code::

    GET /v2/types/indicatorTypes

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 10,
        "indicatorType": [
          {
            "name": "Address",
            "custom": "false",
            "parsable": "true",
            "apiBranch": "addresses",
            "apiEntity": "address"
          },
          {
            "name": "EmailAddress",
            "custom": "false",
            "parsable": "true",
            "apiBranch": "emailAddresses",
            "apiEntity": "emailAddress"
          },
          {
            "name": "File",
            "custom": "false",
            "parsable": "true",
            "apiBranch": "files",
            "apiEntity": "file"
          },
          {
            "name": "Host",
            "custom": "false",
            "parsable": "true",
            "apiBranch": "hosts",
            "apiEntity": "host"
          },
          {
            "name": "URL",
            "custom": "false",
            "parsable": "true",
            "apiBranch": "urls",
            "apiEntity": "url"
          },
          {
            "name": "ASN",
            "custom": "true",
            "parsable": "true",
            "apiBranch": "asns",
            "apiEntity": "asn",
            "casePreference": "upper",
            "value1Label": "AS Number",
            "value1Type": "text",
            "value2Label": ""
          },
          {
            "name": "CIDR",
            "custom": "true",
            "parsable": "true",
            "apiBranch": "cidrBlocks",
            "apiEntity": "cidrBlock",
            "casePreference": "lower",
            "value1Label": "Block",
            "value1Type": "text",
            "value2Label": ""
          },
          {
            "name": "Mutex",
            "custom": "true",
            "parsable": "false",
            "apiBranch": "mutexes",
            "apiEntity": "mutex",
            "casePreference": "sensitive",
            "value1Label": "Mutex",
            "value1Type": "text",
            "value2Label": ""
          },
          {
            "name": "Registry Key",
            "custom": "true",
            "parsable": "false",
            "apiBranch": "registryKeys",
            "apiEntity": "registryKey",
            "casePreference": "sensitive",
            "value1Label": "Key Name",
            "value1Type": "text",
            "value2Label": "Value Name",
            "value2Type": "text"
          },
          {
            "name": "User Agent",
            "custom": "true",
            "parsable": "false",
            "apiBranch": "userAgents",
            "apiEntity": "userAgent",
            "casePreference": "sensitive",
            "value1Label": "User Agent String",
            "value1Type": "text",
            "value2Label": ""
          }
        ]
      }
    }

XML Response:

.. code:: xml

    <indicatorTypesResponse>
      <Status>Success</Status>
      <Data xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="indicatorTypeListResponseData">
        <ResultCount>10</ResultCount>
        <IndicatorType>
          <Name>Address</Name>
          <Custom>false</Custom>
          <Parsable>true</Parsable>
          <ApiBranch>addresses</ApiBranch>
          <ApiEntity>address</ApiEntity>
        </IndicatorType>
        <IndicatorType>
          <Name>EmailAddress</Name>
          <Custom>false</Custom>
          <Parsable>true</Parsable>
          <ApiBranch>emailAddresses</ApiBranch>
          <ApiEntity>emailAddress</ApiEntity>
        </IndicatorType>
        <IndicatorType>
          <Name>File</Name>
          <Custom>false</Custom>
          <Parsable>true</Parsable>
          <ApiBranch>files</ApiBranch>
          <ApiEntity>file</ApiEntity>
        </IndicatorType>
        <IndicatorType>
          <Name>Host</Name>
          <Custom>false</Custom>
          <Parsable>true</Parsable>
          <ApiBranch>hosts</ApiBranch>
          <ApiEntity>host</ApiEntity>
        </IndicatorType>
        <IndicatorType>
          <Name>URL</Name>
          <Custom>false</Custom>
          <Parsable>true</Parsable>
          <ApiBranch>urls</ApiBranch>
          <ApiEntity>url</ApiEntity>
        </IndicatorType>
        <IndicatorType>
          <Name>ASN</Name>
          <Custom>true</Custom>
          <Parsable>true</Parsable>
          <ApiBranch>asns</ApiBranch>
          <ApiEntity>asn</ApiEntity>
          <casePreference>upper</casePreference>
          <value1Label>AS Number</value1Label>
          <value1Type>text</value1Type>
          <value2Label/>
        </IndicatorType>
        <IndicatorType>
          <Name>CIDR</Name>
          <Custom>true</Custom>
          <Parsable>true</Parsable>
          <ApiBranch>cidrBlocks</ApiBranch>
          <ApiEntity>cidrBlock</ApiEntity>
          <casePreference>lower</casePreference>
          <value1Label>Block</value1Label>
          <value1Type>text</value1Type>
          <value2Label/>
        </IndicatorType>
        <IndicatorType>
          <Name>Mutex</Name>
          <Custom>true</Custom>
          <Parsable>false</Parsable>
          <ApiBranch>mutexes</ApiBranch>
          <ApiEntity>mutex</ApiEntity>
          <casePreference>sensitive</casePreference>
          <value1Label>Mutex</value1Label>
          <value1Type>text</value1Type>
          <value2Label/>
        </IndicatorType>
        <IndicatorType>
          <Name>Registry Key</Name>
          <Custom>true</Custom>
          <Parsable>false</Parsable>
          <ApiBranch>registryKeys</ApiBranch>
          <ApiEntity>registryKey</ApiEntity>
          <casePreference>sensitive</casePreference>
          <value1Label>Key Name</value1Label>
          <value1Type>text</value1Type>
          <value2Label>Value Name</value2Label>
          <value2Type>text</value2Type>
        </IndicatorType>
        <IndicatorType>
          <Name>User Agent</Name>
          <Custom>true</Custom>
          <Parsable>false</Parsable>
          <ApiBranch>userAgents</ApiBranch>
          <ApiEntity>userAgent</ApiEntity>
          <casePreference>sensitive</casePreference>
          <value1Label>User Agent String</value1Label>
          <value1Type>text</value1Type>
          <value2Label/>
        </IndicatorType>
      </Data>
    </indicatorTypesResponse>

.. note:: The responses above are taken from the ThreatConnect public cloud (https://app.threatconnect.com/).

To get information about a specific Indicator type, you can use a query in the following format:

.. code::

    GET /v2/types/indicatorTypes/{indicatorType}

For example, to retrieve information for Mutexes, you would use the following query:

.. code::

    GET /v2/types/indicatorTypes/mutex

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "indicatorType": {
          "name": "Mutex",
          "custom": "true",
          "parsable": "false",
          "apiBranch": "mutexes",
          "apiEntity": "mutex",
          "casePreference": "sensitive",
          "value1Label": "Mutex",
          "value1Type": "text"
        }
      }
    }

In ThreatConnect version 5.2+, it is possible to retrieve the regular expression(s) (regex(es)) used to detect and validate an Indicator of a given type. These regexes can be retrieved by adding the ``includeAdditional=true`` parameter as follows:

.. code::

    GET /v2/types/indicatorTypes/{indicatorType}?includeAdditional=true

The following example will return the regexes used to validate File Indicators:

.. code::

    GET /v2/types/indicatorTypes/file?includeAdditional=true

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "indicatorType": {
          "name": "File",
          "custom": "false",
          "parsable": "true",
          "apiBranch": "files",
          "apiEntity": "file",
          "value1Label": "MD5",
          "value1Type": "text",
          "value2Label": "SHA-1",
          "value2Type": "text",
          "value3Label": "SHA-256",
          "value3Type": "text",
          "regexes": [
            "\\b([a-fA-F\\d]{32})\\b",
            "\\b([a-fA-F\\d]{40})\\b",
            "\\b([a-fA-F\\d]{64})\\b"
          ]
        }
      }
    }

Retrieve All Indicators
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve Indicators of all types, use the following query:

.. code::

    GET /v2/indicators

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "indicator": [
          {
            "id": "54321",
            "ownerName": "Example Organization",
            "type": "URL",
            "dateAdded": "2017-07-13T17:50:17",
            "lastModified": "2017-07-19T17:35:31Z",
            "threatAssessRating": 3,
            "threatAssessConfidence": 50,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/url.xhtml?orgid=54321&owner=Example+Organization",
            "summary": "http://example.com/login.php"
          },
          {
            "id": "54322",
            "ownerName": "Example Organization",
            "type": "EmailAddress",
            "dateAdded": "2017-07-13T17:51:17",
            "lastModified": "2017-07-19T17:35:29Z",
            "threatAssessRating": 4,
            "threatAssessConfidence": 75,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=bad%40gmail.com&owner=Example+Organization",
            "summary": "bad@gmail.com"
          }
        ]
      }
    }

Retrieve Multiple Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve multiple indicators of a certain type, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}

The ``{indicatorType}`` can be any one of the available Indicator types below or any of the custom Indicator types available in your instance of threatconnect:

.. include:: ../_includes/indicator_types.rst

For example, the query below will retrieve a list of all Email Address Indicators in the default owner:

.. code::

    GET /v2/indicators/emailAddresses

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "emailAddress": [
          {
            "id": "54321",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:50:17",
            "lastModified": "2017-07-19T17:53:50Z",
            "threatAssessRating": 3,
            "threatAssessConfidence": 50,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=phish%40example.com&owner=Example+Organization",
            "address": "phish@example.com"
          },
          {
            "id": "54322",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:51:17",
            "lastModified": "2017-07-19T17:53:49Z",
            "threatAssessRating": 3,
            "threatAssessConfidence": 50,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=bad%40gmail.com&owner=Example+Organization",
            "address": "bad@gmail.com"
          }
        ]
      }
    }

Retrieve a Single Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a single Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}

For example, if you wanted to retrieve the URL ``http://example.com/``, you would use the following query:

.. code::

    GET /v2/indicators/urls/http%3A%2F%2Fexample.com%2F

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "url": {
          "id": "54321",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-03-29T12:53:49Z",
          "threatAssessRating": 1.67,
          "threatAssessConfidence": 18.33,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/url.xhtml?orgid=54321&owner=Example+Organization",
          "text": "http://example.com/"
        }
      }
    }

Retrieving a Custom Indicator
"""""""""""""""""""""""""""""

To retrieve a Custom Indicator from ThreatConnect:

1. Use the `available Indicator types <#retrieve-available-indicator-types>`_ to identify the ``apiBranch`` for the Indicator type you would like to retrieve.
2. Make a GET request in the format below.

.. code::

    GET /v2/indicators/{customIndicatorType}/{customIndicator}

For example, to retrieve the Mutex ``8F6F00C4-B901-45fd-08CF-72FDEFF``, you use the following query:

.. code::

    GET /v2/indicators/mutexes/8F6F00C4-B901-45fd-08CF-72FDEFF

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "mutex": {
          "id": 123456,
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "type": "Mutex",
          "dateAdded": "2017-05-19T15:40:28Z",
          "lastModified": "2017-05-19T15:43:49Z",
          "webLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=123456&owner=Example+Organization",
          "Mutex": "8F6F00C4-B901-45fd-08CF-72FDEFF",
          "rating": 4.00,
          "confidence": 85,
          "threatAssessRating": 4.0,
          "threatAssessConfidence": 85.0,
          "source": "https://heimdalsecurity.com/blog/bluedoom-worm-eternablue-nsa-exploits/",
          "description": "Mutex created by BlueDoom / EternalRocks malware to ensure first payload is not run more than once on a target system."
        }
      }
    }

Retrieve the Owners in which an Indicator Exists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all of the owners in which an Indicator exists, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/owners

For example, if you wanted to retrieve all of the owners in which the URL ``http://example.com/`` exists, you would use the following query:

.. code::

    GET /v2/indicators/urls/http%3A%2F%2Fexample.com%2F/owners

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "owner": [
          {
            "id": 0,
            "name": "Example Organization",
            "type": "Organization"
          },
          {
            "id": 1,
            "name": "Common Community",
            "type": "Community"
          },
          {
            "id": 2,
            "name": "Example Community",
            "type": "Community"
          }
        ]
      }
    }

Retrieve Indicator Metadata
---------------------------

Retrieve Indicator Observations and False Positives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To find the number of times an Indicator has been observed or reported as a False Positive, use a request in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}?includeAdditional=true

For example, the query below will retrieve additional information about the Host ``example.com``:

.. code::

    GET /v2/indicators/hosts/example.com?includeAdditional=true

JSON Response:

.. code:: json

    {
      "status" : "Success",
      "data" : {
        "host" : {
          "id" : 12345,
          "owner" : {
            "id" : 1,
            "name" : "Example Organization",
            "type" : "Organization"
          },
          "dateAdded" : "2017-06-21T17:50:25-05:00",
          "lastModified" : "2017-07-13T17:50:25-05:00",
          "webLink" : "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=example.com&owner=Example%20Organization",
          "observationCount" : 5,
          "lastObserved" : "2016-07-13T17:50:25-05:00",
          "falsePositiveCount" : 1,
          "falsePositiveLastReported" : "2017-07-13T17:50:25-05:00",
          "hostName" : "example.com",
          "dnsActive" : "false",
          "whoisActive" : "false"
        }
      }
    }

The ``observationCount`` field provides the total number of observations on the indicator and the ``lastObserved`` field gives the date on which the Indicator was most recently observed. The ``falsePositiveCount`` field gives the total number times the Indicator has been reported as a false positive and the ``falsePositiveLastReported`` field gives the date on which the most recent false positive was reported.

Retrieve Indicator Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving Recent Observations
""""""""""""""""""""""""""""""

As of ThreatConnect 5.0, the API branch below provides the ten Indicators with the most observations since a given date. If no date is given, the default query returns the ten Indicators which have had the most observations over the past day. In this context, a "day" includes all of the previous day and all data from the current day up to the current moment in time.

.. code::

    GET /v2/indicators/observed

To view Indicators with the most observations since a specific date, use the ``dateObserved`` parameter, as demonstrated below:

.. code::

    GET /v2/indicators/observed?dateObserved=2017-01-13

This request will return the following data:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "indicator": [
          {
            "summary": "192.168.0.1",
            "userObservedList": [
              {
                "userName": "12345678901234567890",
                "count": 12
              }
            ]
          },
          {
            "summary": "example.com",
            "userObservedList": [
              {
                "userName": "12345678901234567890",
                "count": 2
              }
            ]
          }
        ]
      }
    }

.. note:: Only observations reported using API accounts that are configured to be included in Observations and False Positives will show up in the list of recent observations. For more details on how to configure an API account in this way, refer to the knowledge base article `here <http://kb.threatconnect.com/customer/en/portal/articles/2324809-reporting-false-positives>`__.

Retrieving Total Indicator Observations
"""""""""""""""""""""""""""""""""""""""

To retrieve the total count of observations for an Indicator, you can use the following query:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/observations

For example, the query below will retrieve the observations for the Host ``example.com``:

.. code::

    GET /v2/indicators/hosts/example.com/observations

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "observation": [
          {
            "count": 5,
            "dateObserved": "2016-07-13T17:50:25-05:00Z"
          }
        ]
      }
    }

Retrieving Observations from Your Organization
""""""""""""""""""""""""""""""""""""""""""""""

To view how many of an Indicator's observations came from your organization, you can use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/observationCount

For example, the query below will retrieve the observation counts for the Host ``example.com``:

.. code::

    GET /v2/indicators/hosts/example.com/observationCount

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "observationCount": {
          "count": 5,
          "lastObserved": "2016-07-13T17:50:25-05:00Z",
          "yourCount": 2,
          "yourLastObserved": "2016-07-13T17:50:25-05:00Z"
        }
      }
    }

The ``yourCount`` field shows the total number of observations on the Indicator that came your organization (and ``yourLastObserved`` provides the date of the most recent observation). The ``count`` and ``lastObserved`` describe observations from any ThreatConnect user.

Retrieve Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve an Indicator's Attributes, use the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/attributes

For example, if you wanted to retrieve the attributes on the Email Address ``bad@example.com``, you would use the following query:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/attributes

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "attribute": [
          {
            "id": "54321",
            "type": "Description",
            "dateAdded": "2016-07-13T17:50:17",
            "lastModified": "2017-05-02T18:40:22Z",
            "displayed": true,
            "value": "Description Example"
          },
          {
            "id": "54322",
            "type": "Source",
            "dateAdded": "2016-07-13T17:51:17",
            "lastModified": "2017-05-02T18:40:22Z",
            "displayed": true,
            "value": "Source Example"
          }
        ]
      }
    }

To retrieve the Security Labels that are on an attribute, use the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}/securityLabels

Here is an example query:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/attributes/54321/securityLabels

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "securityLabel": [
          {
            "name": "TLP Amber",
            "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
            "dateAdded": "2017-07-13T17:50:17"
          }
        ]
      }
    }

Retrieve Indicator Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the Security Labels for an Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/securityLabels

For example, the query below will retrieve all Security Labels for the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/securityLabels

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "securityLabel": [
          {
            "name": "TLP Amber",
            "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
            "dateAdded": "2017-07-13T17:50:17"
          }
        ]
      }
    }

Retrieve Indicator Tags
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the Tags for an Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/tags

For example, the query below will retrieve all Tags for the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/tags

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "tag": [
          {
            "name": "Nation State",
            "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Nation+State&owner=Common+Community"
          }
        ]
      }
    }

.. include:: address_specific_retrieve.rst

.. include:: file_specific_retrieve.rst

.. include:: host_specific_retrieve.rst

Retrieve Indicator Associations
-------------------------------

Group to Indicator Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Groups associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/groups

For example, the query below will retrieve all of the Groups associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/groups

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "group": [
          {
            "id": "54321",
            "name": "New Incident",
            "type": "Incident",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:50:17",
            "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=54321"
          }
        ]
      }
    }

You can also find associated Groups of a given type using the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/groups/{associatedGroupType}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, we could use the following query to find all Incidents associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/groups/incidents

We can also drill down even further by adding the ID of an associated Group to the end of the query like:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/groups/incidents/54321

Where ``54321`` is the ID of an Incident associated with the Email Address ``bad@example.com``.

.. The heading needs to be singular (even though this breaks the pattern of this file) so the heading doesn't collide with another heading.

Indicator to Indicator Association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/indicators

For example, the query below will retrieve all of the Indicators associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/indicators

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "indicator": [
          {
            "id": "54321",
            "ownerName": "Example Organization",
            "type": "Address",
            "dateAdded": "2016-07-13T17:50:17",
            "lastModified": "2017-05-01T21:32:54Z",
            "rating": 3.0,
            "confidence": 55,
            "threatAssessRating": 3.0,
            "threatAssessConfidence": 55.0,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=0.0.0.0&owner=Example+Organization",
            "summary": "0.0.0.0"
          }
        ]
      }
    }

You can also find associated Indicators of a given type using the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/indicators/{associatedIndicatorType}

For example, we could use the following query to find all Address Indicators associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/indicators/addresses

.. note:: There is more documentation on retrieving Indicator-to-Indicator associations `here <#indicator-to-indicator-associations>`__.

Victim Assets to Indicator Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victim Assets associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/victimAssets

For example, the query below will retrieve all of the Victim Assets associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/victimAssets

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "victimAsset": [
          {
            "id": "54321",
            "name": "bad@badguys.com",
            "type": "EmailAddress",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=123"
          },
          {
            "id": "54322",
            "name": "nobody@gmail.com",
            "type": "EmailAddress",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=123"
          }
        ]
      }
    }

You can also find associated Victim Assets of a given type using the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/victimAssets/{victimAssetType}

The available Victim Asset types are:

.. include:: ../_includes/victim_asset_types.rst

For example, we could use the following query to find all Victim Assets that are Email Addresses which are associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/victimAssets/emailAddresses

We can also drill down even further by adding the ID of an associated Victim Asset to the end of the query like:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/victimAssets/emailAddresses/54321

Where ``54321`` is the ID of a Victim Asset associated with the Email Address ``bad@example.com``.

Victim to Indicator Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/victims

For example, the query below will retrieve all of the Victims associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/victims

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "victim": [
          {
            "id": "54321",
            "name": "Bad Guy",
            "org": "Example Organization",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=54321"
          }
        ]
      }
    }

We can also drill down even further by adding the ID of an associated Victim to the end of the query like:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com/victims/54321

Where ``54321`` is the ID of a Victim associated with the Email Address ``bad@example.com``.
