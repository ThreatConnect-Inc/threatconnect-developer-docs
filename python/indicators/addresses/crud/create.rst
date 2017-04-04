Create IP Addresses
^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to create an Address Indicator
resource in the ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('4.3.254.1', owner)
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

Code Highlights

+---------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                     | Description                                                                          |
+=============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``    | Instantiate the ThreatConnect object.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``            | Instantiate an Indicator container object.                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator = indicators.add('4.3.254....`` | Add a Resource object setting the value and Owner.                                   |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``            | Set the Confidence value for this Indicator.                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``               | Set the Rating value for this Indicator.                                             |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...`` | Add an Attribute of type **Description** to the Resource.                            |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``            | Add a Tag to the Resource.                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..`` | Add a Security Label to the Resource.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.commit()``                      | Trigger multiple API calls to write Resource, Attributes, Security Labels, and Tags. |
+---------------------------------------------+--------------------------------------------------------------------------------------+
