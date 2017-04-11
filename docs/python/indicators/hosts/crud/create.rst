Create Hosts
^^^^^^^^^^^^

The example below demonstrates how to create a Host Indicator Resource
in the ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('example.com', owner)
    indicator.set_confidence(75)
    indicator.set_rating(2.5)

    indicator.add_attribute('Description', 'Example Attribute')
    indicator.add_tag('EXAMPLE')
    indicator.set_security_label('TLP Green')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

Automatically enrich indicator with DNS resolution or ownership
information from a third-party service

.. code-block:: python
    :linenos:

    # Query PTR record for a given domain, or {A, AAAA} record for a given IP
    indicator.set_dns_active(True)

    # Look up IP or domain ownership information 
    indicator.set_whois_active(True) 

Code Highlights

+----------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                          |
+==============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``     | Instantiate the ThreatConnect object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``             | Instantiate an Indicator container object.                                           |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator = indicators.add('example.....`` | Add a Resource object setting the value and Owner.                                   |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``             | Set the Confidence value for this Indicator.                                         |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``                | Set the Rating value for this Indicator.                                             |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...``  | Add an Attribute of type **Description** to the Resource.                            |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``             | Add a Tag to the Resource.                                                           |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..``  | Add a Security Label to the Resource.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.commit()``                       | Trigger multiple API calls to write Resource, Attributes, Security Labels, and Tags. |
+----------------------------------------------+--------------------------------------------------------------------------------------+
