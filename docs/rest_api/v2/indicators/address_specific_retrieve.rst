Retrieving Address DNS Resolutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of DNS History request for an Address within an Organization:

.. code::

    GET /v2/indicators/addresses/192.168.0.1/dnsResolutions

Example of DNS History request for an Address within a Community:

.. code::

    GET /v2/indicators/addresses/192.168.0.1/dnsResolutions?owner=Common%20Community

JSON Response:

.. code:: json

    {
     "status": "Success",
     "data": {
      "resultCount": 1,
      "indicator": [{
       "id": 123456,
       "ownerName": "Organization Name",
       "type": "Host",
       "dateAdded": "2015-07-21T17:45:32Z",
       "lastModified": "2017-01-21T18:17:52Z",
       "rating": 5.00,
       "confidence": 85,
       "threatAssessRating": 4.36,
       "threatAssessConfidence": 80.67,
       "webLink": "https://demo.threatconnect.com/tc/auth/indicators/details/host.xhtml?host=example.com&owner=Organization+Name",
       "description": "Host retrieved from malware analysis.",
       "summary": "example.com"
       }
      ]
     }
    }

XML Response:  

.. code:: xml

    <dnsResolutionsResponse>
     <Status>Success</Status>
     <Data xsi:type="dnsResolutionListResponseData" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <ResultCount>1</ResultCount>
      <Indicator>
        <Id>123456</Id>
        <OwnerName>Organization Name</OwnerName>
        <Type>Host</Type>
        <DateAdded>2015-07-21T17:45:32Z</DateAdded>
        <LastModified>2017-01-13T18:17:52Z</LastModified>
        <Rating>5.00</Rating>
        <Confidence>85</Confidence>
        <ThreatAssessRating>4.36</ThreatAssessRating>
        <ThreatAssessConfidence>80.67</ThreatAssessConfidence>
        <WebLink>https://demo.threatconnect.com/tc/auth/indicators/details/host.xhtml?host=example.com&amp;owner=Organization+Name</WebLink>
        <Summary>example.com</Summary>
      </Indicator>
     </Data>
    </dnsResolutionsResponse>
