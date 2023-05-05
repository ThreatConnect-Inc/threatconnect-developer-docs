Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/indicators`` endpoint:

.. code::

    OPTIONS /v3/indicators

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request for **all** Indicator types.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - active
     - Indicates whether the Indicator is active
     - Boolean
     - FALSE
     - TRUE
     - true, false
   * - activeLocked
     - Indicates whether the active Indicator Status is locked
     - Boolean
     - FALSE
     - TRUE
     - true, false
   * - associatedArtifacts
     - A list of Artifacts associated to the Indicator
     - `Artifact Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{ "caseId": 1, "summary": "badguy@bad.com", "type": "Email Address"}]}
   * - associatedCases
     - A list of Cases associated to the Indicator
     - `Case Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Hacker Investigation", "status": "Open", "severity": "Low" }]}
   * - associatedGroups
     - A list of Groups associated to the Indicator 
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - associatedIndicators
     - A list of Indicators associated to the Indicator 
     - Indicator Object
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"hostName": "badguy.com", "type": "Host"}]}
   * - attributes [1]_
     - A list of Attributes added to the Indicator 
     - `Indicator Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicator_attributes/indicator_attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Attribute Type", "value": "Attribute Value", "source": "Attribute Source"}]}
   * - confidence
     - The Indicator's Confidence Rating 
     - Integer
     - FALSE
     - TRUE
     - 1, 2, 3,...100
   * - ownerId [2]_
     - The ID of the `owner <https://docs.threatconnect.com/en/latest/rest_api/v3/owners/owners.html>`_ to which the Indicator belongs 
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3,...100
   * - ownerName [2]_
     - The name of the owner to which the Indicator belongs
     - String
     - FALSE
     - FALSE
     - "Demo Community"
   * - privateFlag
     - Indicates where the Indicator is private
     - Boolean
     - FALSE
     - TRUE
     - true, false
   * - rating
     - The Indicator's Threat Rating
     - Big Decimal
     - FALSE
     - TRUE
     - 1.0, 2.0, 3.0, 4.0, 5.0
   * - securityLabels
     - A list of Security Labels applied to the Indicator
     - `Security Label Object <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "TLP:AMBER"}]}
   * - tags
     - A list of Tags applied to the Indicator
     - `Tag Object <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "Targeted Attack"}]}
   * - type [3]_
     - The type of Indicator being created
     - String
     - TRUE
     - FALSE
     - "Address", "Host", "Registry Key"

.. [1] To retrieve a list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_, send the following request: ``GET /v3/attributeTypes``.
.. [2] By default, Indicators will be created in the Organization in which your API user account resides. To create an Indicator in a Community or Source, include the ``ownerId`` or ``ownerName`` field in your request. Alternatively, use the ``owner`` query parameter to `specify the owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ in which to create the Indicator.
.. [3] The following are accepted values for the ``type`` field:

    - ``Address``
    - ``EmailAddress``
    - ``File``
    - ``Host``
    - ``URL``
    - ``ASN``
    - ``CIDR``
    - ``EmailSubject``
    - ``Hashtag``
    - ``Mutex``
    - ``Registry Key``
    - ``User Agent``

Indicator-Specific Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

Based on the type of Indicator being created, you may need to include additional fields in the body of a POST request. Similarly, some Indicator types include additional fields that may be updated via a PUT request.

The following tables list valid fields, some of which are required, that can be included in the body of a POST or PUT request for each Indicator type.

Address
=======

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - ip
     - The IP address associated with the Address Indicator
     - String
     - TRUE
     - FALSE

EmailAddress
============

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - address
     - The email address associated with the Email Address Indicator
     - String
     - TRUE
     - FALSE

File
====

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - fileActions
     - A list of File Actions associated with the File Indicator
     - `File Action Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#file-actions>`_
     - FALSE
     - TRUE
   * - fileOccurrences
     - A list of File Occurrences associated with the File Indicator
     - `File Occurrence Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#file-occurrences>`_
     - FALSE
     - TRUE
   * - md5
     - The MD5 hash associated with the File Indicator
     - String
     - TRUE [4]_
     - FALSE
   * - sha1
     - The SHA1 hash associated with the File Indicator
     - String
     - TRUE [4]_
     - FALSE
   * - sha256
     - The SHA256 hash associated with the File Indicator
     - String
     - TRUE [4]_
     - FALSE
   * - size
     - The size of the file associated with the File Indicator
     - String
     - FALSE
     - TRUE

.. [4] When creating a File Indicator, you must include at least one valid hash.

Host
====

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - dnsActive
     - Indicates whether the **DNS** feature is active for the Host Indicator
     - Boolean
     - FALSE
     - TRUE
   * - hostName
     - The host name associated with the Host Indicator
     - String
     - TRUE
     - FALSE
   * - whoisActive
     - Indicates whether the **Whois** feature is active for the Host Indicator
     - Boolean
     - FALSE
     - TRUE

URL
===

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - text
     - The URL associated with the URL Indicator
     - String
     - TRUE
     - FALSE

ASN
===

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - AS Number
     - The AS number associated with the ASN Indicator
     - String
     - TRUE
     - FALSE

CIDR
====

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - Block
     - The block of network IP addresses associated with the CIDR Indicator
     - String
     - TRUE
     - FALSE

EmailSubject
============

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - Subject
     - The subject line of the email associated with the Email Subject Indicator
     - String
     - TRUE
     - FALSE

Hashtag
=======

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - Hashtag
     - The hashtag term associated with the Hashtag Indicator
     - String
     - TRUE
     - FALSE

Mutex
=====

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - Mutex
     - The synchronization primitive used to identify malware files that is associated with the Mutex
     - String
     - TRUE
     - FALSE

Registry Key
============

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - Key Name
     - The name of the registry key associated with the Registry Key Indicator
     - String
     - TRUE
     - FALSE
   * - Value Name
     - The registry value associated with the Registry Key Indicator
     - String
     - TRUE
     - FALSE
   * - Value Type [5]_
     - The registry value type associated with the Registry Key Indicator
     - String
     - TRUE
     - FALSE

.. [5] The following are accepted values for a Registry Key Indicator's ``Value Type`` field:

    - ``REG_NONE``
    - ``REG_BINARY``
    - ``REG_DWORD``
    - ``REG_DWORD_LITTLE_ENDIAN``
    - ``REG_DWORD_BIG_ENDIAN``
    - ``REG_EXPAND_SZ``
    - ``REG_LINK``
    - ``REG_MULTI_SZ``
    - ``REG_QWORD``
    - ``REG_QWORD_LITTLE_ENDIAN``
    - ``REG_SZ``

User Agent
==========

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - User Agent String
     - The characteristic identification string associated with the User Agent Indicator
     - String
     - TRUE
     - FALSE

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/indicators`` endpoint:

.. code::

    OPTIONS /v3/indicators/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/indicators`` endpoint:

.. code::

    OPTIONS /v3/indicators/tql