Indicator to Indicator Associations
-----------------------------------

In ThreatConnect, some types of Indicators can be related with certain other types. At a high level, there are two ways to relate Indicators with one another:

1. As an `Association <#association>`__
2. As a `File Action <#file-action>`__

Association
^^^^^^^^^^^

An Association allows two Indicators of certain types to be related to one another in the manner that Indicators can be associated to Groups. Below is a list of the Indicator-to-Indicator Associations possible in the ThreatConnect Cloud, along with the Indicator types that can be associated with one another using each Association.

+-----------------------+-------------------------+------------------------+
| Name                  | API Branch              | Indicators Associated  |
+=======================+=========================+========================+
| Address to User Agent | ``/addressToUserAgent`` | Address <-> User Agent |
+-----------------------+-------------------------+------------------------+
| ASN to Address        | ``/asnToAddress``       | ASN <-> Address        |
+-----------------------+-------------------------+------------------------+
| ASN to CIDR           | ``/asnToCidr``          | ASN <-> CIDR           |
+-----------------------+-------------------------+------------------------+
| CIDR to Address       | ``/cidrToAddress``      | CIDR <-> Address       |
+-----------------------+-------------------------+------------------------+

To retrieve Indicators associated with another Indicator using a custom Association, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/associations/{associationType}/indicators

For example, the following query will retrieve all of the CIDR Indicators associated with an ASN:

.. code::

    GET /v2/indicators/asns/ASN12345/associations/asnToCidr/indicators

asnToCidr Associations retrieve JSON:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "indicator": [
          {
            "id": 123456,
            "ownerName": "Organization Name",
            "type": "CIDR",
            "dateAdded": "2016-11-22T00:38:03Z",
            "lastModified": "2016-11-22T01:50:53Z",
            "rating": 1.00,
            "confidence": 100,
            "threatAssessRating": 1.0,
            "threatAssessConfidence": 100.0,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=123456&owner=Organization+Name",
            "summary": "192.168.0.1/24"
          }
        ]
      }
    }

asnToCidr Associations retrieve XML:

.. code:: xml

    <indicatorsResponse>
      <Status>Success</Status>
      <Data xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="indicatorListResponseData">
        <ResultCount>1</ResultCount>
        <Indicator>
          <Id>123456</Id>
          <OwnerName>Organization Name</OwnerName>
          <Type>CIDR</Type>
          <DateAdded>2016-11-22T00:38:03Z</DateAdded>
          <LastModified>2016-11-22T01:50:53Z</LastModified>
          <Rating>1.00</Rating>
          <Confidence>100</Confidence>
          <ThreatAssessRating>1.0</ThreatAssessRating>
          <ThreatAssessConfidence>100.0</ThreatAssessConfidence>
          <WebLink>https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=123456&amp;owner=Organization+Name</WebLink>
          <Summary>192.168.0.1/24</Summary>
        </Indicator>
      </Data>
    </indicatorsResponse>

To create an Association between two Indicators, use the following POST request format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/associations/{associationType}/indicators/{indicatorType}/{indicator}

For example, the query below will associate the IP Address ``192.168.0.1`` with the CIDR Range ``192.168.0.0/24``.

.. code::

    POST /v2/indicators/addresses/192.168.0.1/associations/cidrToAddress/indicators/cidrBlocks/192.168.0.0%2F24

JSON Response:

.. code-block:: json

    {
      "status": "Success"
    }

File Action
^^^^^^^^^^^

A file action adds one Indicator to the behavior graph of a File Indicator. Below is a list of the file actions available in the ThreatConnect Cloud, along with the Indicator type that can be related via each file action.

+-------------------+------------------+-------------------------------------+
| Name              | API Branch       | Indicator Type Associated with File |
+===================+==================+=====================================+
| File Archive      | ``/archive``     | File                                |
+-------------------+------------------+-------------------------------------+
| File Drop         | ``/drop``        | File                                |
+-------------------+------------------+-------------------------------------+
| File Traffic      | ``/traffic``     | Address, Host, URL                  |
+-------------------+------------------+-------------------------------------+
| File Mutex        | ``/mutex``       | Mutex                               |
+-------------------+------------------+-------------------------------------+
| File Registry Key | ``/registryKey`` | Registry Key                        |
+-------------------+------------------+-------------------------------------+
| File User Agent   | ``/userAgent``   | User Agent                          |
+-------------------+------------------+-------------------------------------+
| File DNS Query    | ``/dnsQuery``    | Host                                |
+-------------------+------------------+-------------------------------------+

To retrieve Indicators associated with a file using a file action, use the following GET request format:

.. code::

    GET /v2/indicators/files/{fileHash}/actions/{fileAction}/indicators

For example, the query below retrieves all of the Mutex Indicators associated with the File Indicator represented by the hash ``8743b52063cd84097a65d1633f5c74f5`` using the File Mutex action:

.. code::

    GET /v2/indicators/files/8743b52063cd84097a65d1633f5c74f5/actions/mutex/indicators

Mutex file action retrieve JSON:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "indicator": [
          {
            "id": 123456,
            "ownerName": "Organization Name",
            "type": "Mutex",
            "dateAdded": "2016-11-23T16:21:53Z",
            "lastModified": "2016-11-23T16:21:53Z",
            "threatAssessRating": 3.0,
            "threatAssessConfidence": 50.0,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=123456&owner=Organization+Name",
            "description": "Mutex for file with hash **8743b52063cd84097a65d1633f5c74f5**.",
            "summary": "50F163F13C2FF8FDB5262A672EB39B19"
          },
          {
            "id": 123457,
            "ownerName": "Organization Name",
            "type": "Mutex",
            "dateAdded": "2016-11-23T16:20:40Z",
            "lastModified": "2016-11-23T16:20:40Z",
            "threatAssessRating": 3.0,
            "threatAssessConfidence": 50.0,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=123457&owner=Organization+Name",
            "description": "Mutex for file with hash **8743b52063cd84097a65d1633f5c74f5**.",
            "summary": "CTF.TimListCache.FMPDefaultS-1-5-21-1547161642-507921405-839522115-1004MUTEX.DefaultS-1-5-21-1547161642-507921405-839522115-1004"
          }
        ]
      }
    }

Mutex file action retrieve XML:

.. code:: xml

    <indicatorsResponse>
      <Status>Success</Status>
      <Data xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="indicatorListResponseData">
        <ResultCount>2</ResultCount>
        <Indicator>
          <Id>123456</Id>
          <OwnerName>Organization Name</OwnerName>
          <Type>Mutex</Type>
          <DateAdded>2016-11-23T16:21:53Z</DateAdded>
          <LastModified>2016-11-23T16:21:53Z</LastModified>
          <ThreatAssessRating>3.0</ThreatAssessRating>
          <ThreatAssessConfidence>50.0</ThreatAssessConfidence>
          <WebLink>https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=123456&amp;owner=Organization+Name</WebLink>
          <Description>Mutex for file with hash **8743b52063cd84097a65d1633f5c74f5**.</Description>
          <Summary>50F163F13C2FF8FDB5262A672EB39B19</Summary>
        </Indicator>
        <Indicator>
          <Id>123457</Id>
          <OwnerName>Organization Name</OwnerName>
          <Type>Mutex</Type>
          <DateAdded>2016-11-23T16:20:40Z</DateAdded>
          <LastModified>2016-11-23T16:20:40Z</LastModified>
          <ThreatAssessRating>3.0</ThreatAssessRating>
          <ThreatAssessConfidence>50.0</ThreatAssessConfidence>
          <WebLink>https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=123457&amp;owner=Organization+Name</WebLink>
          <Description>Mutex for file with hash **8743b52063cd84097a65d1633f5c74f5**.</Description>
          <Summary>CTF.TimListCache.FMPDefaultS-1-5-21-1547161642-507921405-839522115-1004MUTEX.DefaultS-1-5-21-1547161642-507921405-839522115-1004</Summary>
        </Indicator>
      </Data>
    </indicatorsResponse>

To create an association between two Indicators using a file action, use the following POST request format:

.. code::

    POST /v2/indicators/files/{fileHash}/actions/{fileAction}/indicators/{indicatorType}/{indicator}
