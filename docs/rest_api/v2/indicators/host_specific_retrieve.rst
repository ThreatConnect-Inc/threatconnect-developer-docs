Retrieving Host DNS Resolutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of a DNS History request for a Host within an Organization:

.. code::

    GET /v2/indicators/hosts/example.com/dnsResolutions

Example of a DNS History request for a Host within a Community:

.. code::

    GET /v2/indicators/hosts/example.com/dnsResolutions?owner=Common%20Community

JSON Response:

.. code:: json

    {
     "status": "Success",
     "data": {
      "resultCount": 1,
      "dnsResolution": [{
       "resolutionDate": "2017-01-30T20:49:05Z",
       "addresses": [{
        "id": 123456,
        "ownerName": "Organization Name",
        "dateAdded": "2017-01-20T20:49:05Z",
        "lastModified": "2017-01-27T20:49:05Z",
        "threatAssessRating": 3.0,
        "threatAssessConfidence": 50.0,
        "webLink": "https://demo.threatconnect.com/tc/auth/indicators/details/address.xhtml?address=192.168.100.1&owner=Organization+Name",
        "ip": "192.168.100.1"
       }]
      }]
     }
    }

XML Response:

.. code:: xml

    <dnsResolutionsResponse>
     <Status>Success</Status>
     <Data xsi:type="dnsResolutionListResponseData" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <ResultCount>1</ResultCount>
      <DnsResolution>
       <ResolutionDate>2013-11-18T13:27:35Z</ResolutionDate>
       <Addresses>
        <Id>123456</Id>
        <OwnerName>Organization Name</OwnerName>
        <DateAdded>2017-01-20T20:49:05Z</DateAdded>
        <LastModified>2017-01-27T20:49:05Z</LastModified>
        <ThreatAssessRating>3.0</ThreatAssessRating>
        <ThreatAssessConfidence>50.0</ThreatAssessConfidence>
        <WebLink>https://demo.threatconnect.com/tc/auth/indicators/details/address.xhtml?address=192.168.100.1&amp;owner=Organization+Name</WebLink>
        <Ip>192.168.100.1</Ip>
       </Addresses>
      </DnsResolution>
     </Data>
    </dnsResolutionsResponse>
