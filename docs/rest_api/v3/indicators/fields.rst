Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/indicators`` endpoint, including the field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/indicators

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for **all** Indicator types.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example value(s)
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
     - {"data": [{"id": 12345}]}, {"data": [{ "caseId": 1, "summary": "badguy@bad.com", "type": "Email Address"}]}
   * - associatedCases
     - A list of Cases associated to the Indicator
     - `Case Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html>`_
     - FALSE
     - TRUE
     - {"data": [{"id": 12345}]}, {"data": [{"name": "Hacker Investigation", "status": "Open", "severity": "Low" }]}}
   * - associatedGroups
     - A list of Groups associated to the Indicator 
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - {"data": [{"id": 12345}]}, {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - attributes
     - A list of Attributes corresponding to the Indicator 
     - `Indicator Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicator_attributes/indicator_attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Attribute Type", "value": "Attribute Value", "source": "Attribute Source"]}}
   * - confidence
     - The Indicator's Confidence Rating 
     - Integer
     - FALSE
     - TRUE
     - {"data": [{"type": "Attribute Type", "value": "Attribute Value", "source": "Attribute Source"]}}
   * - ownerName
     - The name of the Organization, Community, or Source to which the Indicator belongs 
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
   * - type
     - The type of Indicator being created
     - String
     - TRUE
     - FALSE
     - "Address", "Host", "Registry Key"

Available values for the ``type`` field include:

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

.. note::
    A list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_ can be retrieved with the following query:
    
    ``GET /v3/attributeTypes``

.. note::
    To **associate an existing Artifact, Case, or Group** to an Indicator, use the object's ID when setting the associatedArtifacts, associatedCases, or associatedGroups field, respectively (e.g., ``{"data": [{"id": 12345}]}``).

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
   * - md5
     - The MD5 hash associated with the File Indicator
     - String
     - TRUE*
     - FALSE
   * - sha1
     - The SHA1 hash associated with the File Indicator
     - String
     - TRUE*
     - FALSE
   * - sha256
     - The SHA256 hash associated with the File Indicator
     - String
     - TRUE*
     - FALSE
   * - size
     - The size of the file associated with the File Indicator
     - String
     - FALSE
     - TRUE

.. note::
    When creating a File Indicator, you must **include at least one valid hash**.

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
   * - hostName
     - The host name associated with the Host Indicator
     - String
     - TRUE
     - FALSE
   * - dnsActive
     - Indicates whether the **DNS** feature is active for the Host Indicator
     - Boolean
     - FALSE
     - TRUE
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
   * - Value Type
     - The registry value type associated with the Registry Key Indicator
     - String
     - TRUE
     - FALSE

Available values for the ``Value Type`` field include:

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
