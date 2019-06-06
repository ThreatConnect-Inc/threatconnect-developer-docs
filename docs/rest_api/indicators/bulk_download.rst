Bulk Indicator Reports
-----------------------

If retrieving all of the Indicators and their entire context (i.e.,
Tags, Attributes, etc.) from a Source, then the above API calls can
become unwieldy and require a high volume of successive calls.
ThreatConnect can be configured to publish a daily bulk report of all
Indicators per Owner for Sources and Communities within the Graphical
User Interface (GUI). These reports can be accessed via the V2 API, and
users should contact their ThreatConnect System Administrator to enable
bulk reporting.

Checking the Status of Bulk Indicator Reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of verifying that a Community or Source has bulk-reporting
enabled:

.. code::

    GET /v2/indicators/bulk?owner=Demo+Customer+Community

Checking bulkStatus Object JSON Response:

.. code:: json

    {
     "bulkStatus": {
      "name": "Demo Customer Community",
      "csvEnabled": true,
      "jsonEnabled": true,
      "nextRun": "2015-03-27T05:00:00Z",
      "lastRun": "2015-03-26T19:06:53Z",
      "status": "Complete"
     }
    }

Checking bulkStatus Object XML Response:

.. code:: xml

    <BulkStatus>
     <Name>Demo Customer Community</Name>
     <CsvEnabled>true</CsvEnabled>
     <JsonEnabled>true</JsonEnabled>
     <NextRun>2015-03-27T05:00:00Z</NextRun>
     <LastRun>2015-03-26T19:06:53.344Z</LastRun>
     <Status>Complete</Status>
    </BulkStatus>

The response body will contain a bulkStatus object, which provides details of the configuration for the bulk-reporting feature of this Community or Source:

* "name": The name of the Owner queried
* "csvEnabled": Whether the owner has enabled Comma Separated Values (CSV) reports to be generated (true/false), thus determining if the respective endpoint will yield data
* "jsonEnabled": Whether the owner has enabled JSON reports to be generated (true/false), thus determining if the respective endpoint will yield data
* "nextRun": The ISO 8601 time-stamp representing when the report generator will run next
* "lastRun": The ISO 8601 time-stamp representing when the report generator was last run
* "status": A string representing the status of the most-recent report job (Complete, Failure, etc.)

Retrieving Bulk Reports
^^^^^^^^^^^^^^^^^^^^^^^

Reports can be retrieved in JSON or CSV format. The JSON format will contain additional context in a new format, including Attributes and Tags, if relevant. CSV reports contain an Indicator, its Type, its Threat Rating, and its Confidence value.

JSON Bulk Reports
"""""""""""""""""

To retrieve a JSON report for an Owner, execute the query below, and include the Owner to be queried. The API will return the latest version of the JSON report with a content-type header of "application/json." The output is very similar to that returned by the Indicators Collection (e.g., in /v2/indicators), with the addition of Attributes and Tags where relevant.

.. code::

    GET /v2/indicators/bulk/json?owner=Demo+Customer+Community

.. note:: In order to retrieve a JSON report for an Owner, the Owner must have JSON Report publication enabled.

Retrieving Bulk Reports JSON Response:

.. code:: json

    {
     "indicator": [{
        "id": 126650,
        "ownerName": "Demo Customer Community",
        "type": "Host",
        "dateAdded": "2013-11-15T21:32:39Z",
        "lastModified": "2015-03-13T06:22:03Z",
        "rating": 5.0,
        "confidence": 73,
        "threatAssessRating": 4.38,
        "threatAssessConfidence": 93.43,
        "webLink": "https://app.threatconnect.com/tc/auth/indicators/details/host.xhtml?host=example.com&owner=Demo+Customer+Community",
        "description": "This is probably a bad domain.",
        "summary": "example.com",
        "attribute": [{
         "id": 131253,
         "type": "Source",
         "dateAdded": "2013-11-15T21:32:40Z",
         "lastModified": "2013-11-15T21:32:40Z",
         "displayed": true,
         "value": "ThreatConnect Intelligence Research Team Enrichment"
        }, {
         "id": 149457,
         "type": "Description",
         "dateAdded": "2013-11-15T21:32:40Z",
         "lastModified": "2013-11-15T21:32:40Z",
         "displayed": true,
         "value": "This is probably a bad domain."
        }],
        "tag": [{
         "name": "China",
         "webLink": "https://app.threatconnect.com/tc/auth/tags/tag.xhtml?tag=China&owner=Demo Customer Community"
        }]
       }]
     }

An optional URL parameter ``runNow=true`` can be added (as shown below) to force the report to be recreated. By default, reports are created once a day.

.. code::

 GET /v2/indicators/bulk/json?owner=Demo+Customer+Community&runNow=true

CSV Bulk Reports
""""""""""""""""

To retrieve a CSV report for an Owner, execute the query below, and include the Owner to be queried. The API will return the latest CSV report with a content-type header of "text/csv." The report will contain all of the Indicators in that Owner and their Indicator Type. It will also include each Indicator’s Threat and Confidence ratings, if set, or null otherwise.

.. code::

    GET /v2/indicators/bulk/csv?owner=Demo+Customer+Community

.. note:: In order to retrieve a CSV report for an Owner, the Owner must have CSV Report publication enabled.

The example below displays the output from a CSV report:

.. code::

    Type,Value,Rating,Confidence
    Host,example.com,null,null
    Address,192.168.31.136,3.00,0
    File,ABCDE123456804A61F2A704811F51BC,3.00,55
    URL,http://www.example.com/malware.exe,null,0
    EmailAddress,spearphisher@example.com,3.00,62

An optional URL parameter ``runNow=true`` can be added (as shown below) to force the report to be recreated. By default, reports are created once a day.

.. code::

 GET /v2/indicators/bulk/csv?owner=Demo+Customer+Community&runNow=true
