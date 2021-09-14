Taxii Services
==============

To use Taxii endpoints, you need to have a Taxii user created in your ThreatConnect Organization. To do this, follow the instructions for `Creating a Taxii-user <https://training.threatconnect.com/learn/article/using-the-threatconnect-taxii-server-kb-article>`_.

ThreatConnect offers three Taxii Services: 

  1. `Discovery Service <#discovery-service>`__ : Provides information about offered TAXII Services
  2. `Collection Management Service <#collection-management-service>`__ : Supports management of TAXII Data Collection subscriptions
  3. `Poll Service <#poll-service>`__ : Supports consumer-initiated pulls of cyber-threat information (i.e., pull messaging)

.. hint:: The descriptions above are taken from the `Taxii Services Specification <https://taxiiproject.github.io/releases/1.1/TAXII_Services_Specification.pdf>`_ documentation, which you may find helpful for further reference.

Authentication
--------------

Requests to a Taxii endpoint must be authenticated using `Basic Authentication <https://en.wikipedia.org/wiki/Basic_access_authentication>`_ with the username and password of a Taxii-user account. The value created by the basic authentication should be sent with the request with the ``Authorization`` header. Note that this is different than the authentication scheme used for normal API requests.

For example, the ``Authorization`` header for requests to Taxii endpoints should look like: ``Authorization: Basic b1gB1rdz007``.

Discovery Service
-----------------

The discovery service is available at ``/taxii/discovery/``.

Sample Discovery Request
^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    POST /taxii/discovery/ HTTP/1.1
    Authorization: Basic b1gB1rdz007
    Accept: application/xml
    Content-Type: application/xml
    X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
    X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
    Cache-Control: no-cache
    X-TAXII-Services: urn:taxii.mitre.org:services:1.1
    X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.8
    Host: api.threatconnect.com
    Connection: close
    Content-Length: 97

    <Discovery_Request xmlns="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" message_id="1"/>

.. hint:: The XML at the bottom of the request above goes in the body of the request.

Sample Discovery Response
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <taxii_11:Discovery_Response xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" xmlns:xmldsig="http://www.w3.org/2000/09/xmldsig#" in_response_to="1" message_id="urn:uuid:09117d83-6b01-4ae3-914e-744358411486">
      <taxii_11:Service_Instance service_type="POLL" available="true" service_version="urn:taxii.mitre.org:services:1.1">
        <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
        <taxii_11:Address>https://api.threatconnect.com/taxii/poll</taxii_11:Address>
        <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
      </taxii_11:Service_Instance>
      <taxii_11:Service_Instance service_type="COLLECTION_MANAGEMENT" available="true" service_version="urn:taxii.mitre.org:services:1.1">
        <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
        <taxii_11:Address>https://api.threatconnect.com/taxii/collection-management</taxii_11:Address>
        <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
      </taxii_11:Service_Instance>
      <taxii_11:Service_Instance service_type="DISCOVERY" available="true" service_version="urn:taxii.mitre.org:services:1.1">
        <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
        <taxii_11:Address>https://api.threatconnect.com/taxii/discovery</taxii_11:Address>
        <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
      </taxii_11:Service_Instance>
    </taxii_11:Discovery_Response>

Collection Management Service
-----------------------------

The Collection Management Service is available at ``/taxii/collection-management/``.

Sample Collection Management Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    POST /taxii/collection-management/ HTTP/1.1
    Authorization: Basic b1gB1rdz007
    Accept: application/xml
    Content-Type: application/xml
    X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
    X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
    Cache-Control: no-cache
    X-TAXII-Services: urn:taxii.mitre.org:services:1.1
    X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.8
    Host: api.threatconnect.com
    Connection: close
    Content-Length: 132

    <taxii_11:Collection_Information_Request xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" message_id="26300"/>

.. hint:: The XML at the bottom of the request above goes in the body of the request.

Sample Collection Management Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <taxii_11:Collection_Information_Response xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" xmlns:xmldsig="http://www.w3.org/2000/09/xmldsig#" in_response_to="26300" message_id="urn:uuid:9d0b44f5-b034-4b47-816e-de7d63fed1bc">
      <taxii_11:Collection collection_name="Example Organization" collection_type="DATA_FEED" available="true">
        <taxii_11:Description>ThreatConnect Organization Data</taxii_11:Description>
        <taxii_11:Content_Binding binding_id="CB_STIX_XML_111"/>
        <taxii_11:Polling_Service xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="taxii_11:ServiceInstanceType">
          <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
          <taxii_11:Address>https://api.threatconnect.com/taxii/poll</taxii_11:Address>
          <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Polling_Service>
      </taxii_11:Collection>
      <taxii_11:Collection collection_name="Finance Branch Log Analysis" collection_type="DATA_FEED" available="true">
        <taxii_11:Description>ThreatConnect Source Data</taxii_11:Description>
        <taxii_11:Content_Binding binding_id="CB_STIX_XML_111"/>
        <taxii_11:Polling_Service xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="taxii_11:ServiceInstanceType">
          <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
          <taxii_11:Address>https://api.threatconnect.com/taxii/poll</taxii_11:Address>
          <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Polling_Service>
      </taxii_11:Collection>
    </taxii_11:Collection_Information_Response>

Poll Service
------------

The Poll Service is available at ``/taxii/poll/``.

Sample Poll Request
^^^^^^^^^^^^^^^^^^^

.. code::

    POST /taxii/poll/ HTTP/1.1
    Authorization: Basic b1gB1rdz007
    Accept: application/xml
    Content-Type: application/xml
    X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
    X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
    Cache-Control: no-cache
    X-TAXII-Services: urn:taxii.mitre.org:services:1.1
    X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.8
    Host: api.threatconnect.com
    Connection: close
    Content-Length: 514

    <taxii_11:Poll_Request 
        xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"
        message_id="1"
        collection_name="Finance Branch Log Analysis">
        <taxii_11:Exclusive_Begin_Timestamp>2017-07-13T00:00:00Z</taxii_11:Exclusive_Begin_Timestamp>
        <taxii_11:Inclusive_End_Timestamp>2017-07-13T23:00:00Z</taxii_11:Inclusive_End_Timestamp>
        <taxii_11:Poll_Parameters allow_asynch="false">
            <taxii_11:Response_Type>FULL</taxii_11:Response_Type>
        </taxii_11:Poll_Parameters>
    </taxii_11:Poll_Request>

.. hint:: The XML at the bottom of the request above goes in the body of the request.

.. note:: The maximum date range (in hours) between the ``Exclusive_Begin_Timestamp`` and the ``Inclusive_End_Timestamp`` is 24 hours.

Sample Poll Response
^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

    <taxii_11:Poll_Response xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" xmlns:xmldsig="http://www.w3.org/2000/09/xmldsig#" collection_name="Finance Branch Log Analysis" more="false" result_id="1514419200000:1514502000000" result_part_number="1" in_response_to="1" message_id="urn:uuid:01984d12-7c89-4ec5-9e2b-8c73553aa2b8">
      <taxii_11:Exclusive_Begin_Timestamp>2017-07-13T00:00:00Z</taxii_11:Exclusive_Begin_Timestamp>
      <taxii_11:Inclusive_End_Timestamp>2017-07-13T23:00:00Z</taxii_11:Inclusive_End_Timestamp>
      <taxii_11:Record_Count partial_count="false">1</taxii_11:Record_Count>
      <taxii_11:Content_Block>
        <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
        <taxii_11:Content>
          <stix:STIX_Package xmlns="http://xml/metadataSharing.xsd" xmlns:indicator="http://stix.mitre.org/Indicator-2" xmlns:stixCommon="http://stix.mitre.org/common-1" xmlns:cyboxDN="http://cybox.mitre.org/objects#DomainNameObject-1" xmlns:stix="http://stix.mitre.org/stix-1" xmlns:threatconnect="http://threatconnect.com/" xmlns:cyboxCommon="http://cybox.mitre.org/common-2" xmlns:cybox="http://cybox.mitre.org/cybox-2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="threatconnect:STIXPackage-ef82c390-33ae-4e39-b340-4deaa4d60541" timestamp="2017-07-13T16:38:52.052Z" version="1.1.1" xsi:schemaLocation="http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd http://cybox.mitre.org/common-2 http://cybox.mitre.org/XMLSchema/common/2.1/cybox_common.xsd http://cybox.mitre.org/objects#DomainNameObject-1 http://cybox.mitre.org/XMLSchema/objects/Domain_Name/1.0/Domain_Name_Object.xsd http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.1/cybox_core.xsd http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd">
            <stix:STIX_Header>
              <stix:Title>Report: Finance Branch Log Analysis</stix:Title>
              <stix:Package_Intent>INDICATORS</stix:Package_Intent>
            </stix:STIX_Header>
            <stix:Indicators>
              <stix:Indicator id="threatconnect:Indicator-fbaf13c7-f3f8-49ef-8656-dfb4e8e5b70d" timestamp="2017-07-13T15:49:05.000Z" xsi:type="indicator:IndicatorType">
                <indicator:Type>Domain Watchlist</indicator:Type>
                <indicator:Description>Host: example.com|threatassess: 450|falsepositives: 1|owner: Finance Branch Log Analysis</indicator:Description>
                <indicator:Observable id="threatconnect:Observable-6788a246-4975-4f67-8d03-73537e56e885">
                  <cybox:Object>
                    <cybox:Properties xsi:type="cyboxDN:DomainNameObjectType">
                      <cyboxDN:Value apply_condition="ANY" condition="Equals">example.com</cyboxDN:Value>
                    </cybox:Properties>
                  </cybox:Object>
                </indicator:Observable>
                <indicator:Confidence>
                  <stixCommon:Value>0</stixCommon:Value>
                </indicator:Confidence>
                <indicator:Sightings sightings_count="0"/>
                <indicator:Producer>
                  <stixCommon:Identity id="threatconnect:Identity-2251f2bd-930e-4328-b657-61941d7d1505">
                    <stixCommon:Name>ThreatConnect - Finance Branch Log Analysis</stixCommon:Name>
                  </stixCommon:Identity>
                  <stixCommon:Time>
                    <cyboxCommon:Produced_Time>2017-07-13T15:49:05.000Z</cyboxCommon:Produced_Time>
                  </stixCommon:Time>
                  <stixCommon:References>
                    <stixCommon:Reference>https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=example.com</stixCommon:Reference>
                  </stixCommon:References>
                </indicator:Producer>
              </stix:Indicator>
            </stix:Indicators>
          </stix:STIX_Package>
        </taxii_11:Content>
      </taxii_11:Content_Block>
    </taxii_11:Poll_Response>
