.. list-table::
   :widths: 35 25 15 25
   :header-rows: 1

   * - Field
     - Description
     - Accepted Data Type
     - Required?
   * - active
     - | Specifies whether the Indicator's status is active (**true**) or inactive (**false**)
       |
       | Default value: **true**
     - Boolean
     - Optional
   * - activeLocked
     - | Specifies whether to prevent CAL™ from updating the Indicator's status
       |
       | Default value: **false**
     - Boolean
     - Optional
   * - address
     - A valid email address (for Email Address Indicators only)
     - String
     - Required for Email Address Indicators if ``summary`` is not used
   * - AS Number
     - An autonomous system (AS) number that uniquely identifies each network on the Internet (for ASN Indicators only)
     - String
     - Required for ASN Indicators if ``summary`` is not used
   * - associatedGroups
     - An array of Groups associated to the Indicator
     - Array of Objects
     - Optional
   * - associatedGroups.groupXid
     - The associated Group's XID
     - String
     - Required if ``associatedGroups`` is used
   * - associatedIndicators
     - An array of Indicators associated to the Indicator
     - Array of Objects
     - Optional
   * - associatedIndicators.indicatorType
     - The associated Indicator's type
     - String
     - Required if ``associatedIndicators`` is used
   * - associatedIndicators.summary
     - The associated Indicator's summary
     - String
     - Required if ``associatedIndicators`` is used
   * - attribute
     - An array of Attributes added to the Indicator
     - Array of Objects
     - Optional
   * - attribute.displayed
     - | Specifies whether to display the Attribute as a default Attribute on the **Details** screen for the Indicator to which it is added (applies to Description and Source Attributes only)
       |
       | Default value: **false**
     - Boolean
     - Optional
   * - attribute.pinned
     - | Specifies whether to display the Attribute as a pinned Attribute on the **Details** screen for the Indicator to which it is added
       |
       | Default value: **false**
     - Boolean
     - Optional
   * - attribute.securityLabel
     - An array of Security Labels applied to the Attribute
     - Array of Objects
     - Optional
   * - attribute.securityLabel.color
     - The hex color code (e.g., FF0000) for the Security Label's color
     - String
     - Required if ``securityLabel`` is used within ``attribute`` and the Security Label does not exist
   * - attribute.securityLabel.description
     - The Security Label's description
     - String
     - Required if ``securityLabel`` is used within ``attribute`` and the Security Label does not exist
   * - attribute.securityLabel.name
     - The Security Label's name
     - String
     - Required if ``securityLabel`` is used within ``attribute``
   * - attribute.source
     - The Attribute's source
     - String
     - Optional
   * - attribute.type
     - The Attribute's Type
     - String
     - Required if ``attribute`` is used
   * - attribute.value
     - The Attribute's value
     - String
     - Required if ``attribute`` is used
   * - Block
     - A block of network IP addresses (for CIDR Indicators only)
     - String
     - Required for CIDR Indicators if ``summary`` is not used
   * - confidence
     - | The Indicator's Confidence Rating
       |
       | Minimum value: **0**
       | Maximum value: **100**
     - Integer
     - Optional
   * - description
     - The value of the Indicator's default Description Attribute
     - String
     - Optional
   * - externalDateAdded
     - The date and time when the Indicator was created externally
     - DateTime
     - Optional
   * - externalDateExpires
     - The date and time when the Indicator expires externally
     - DateTime
     - Optional
   * - externalLastModified
     - The date and time when the Indicator was last modified externally
     - DateTime
     - Optional
   * - fileOccurrence
     - The Indicator's File Occurrences (for File Indicators only)
     - Object
     - Optional
   * - fileOccurrence.date
     - The date and time of the File Occurrence
     - DateTime
     - Optional [1]_
   * - fileOccurrence.fileName
     - The name of the file corresponding to the File Occurrence
     - String
     - Optional [1]_
   * - fileOccurrence.path
     - The run path for the file corresponding to the File Occurrence
     - String
     - Optional [1]_
   * - firstSeen
     - The date and time when the Indicator was first seen
     - DateTime
     - Optional
   * - Hashtag
     - A hashtag term used in social media (for Hashtag Indicators only)
     - String
     - Required for Hashtag Indicators if ``summary`` is not used
   * - hostName
     - A valid hostname or domain (for Host Indicators only)
     - String
     - Required for Host Indicators if ``summary`` is not used
   * - ip
     - A valid IPv4 or IPv6 address (for Address Indicators only)
     - String
     - Required for Address Indicators if ``summary`` is not used
   * - Key Name
     - A node in a hierarchical database (i.e., key) that contains data critical for the operation of Windows and the applications and services that run on Windows (for Registry Key Indicators only)
     - String
     - Required for Registry Indicators if ``summary`` is not used
   * - lastSeen
     - The date and time when the Indicator was last seen
     - DateTime
     - Optional
   * - md5
     - The File Indicator's MD5 file hash
     - String
     - If ``summary`` is not used, at least one file hash field (``md5``, ``sha1``, or ``sha256``) is required [2]_
   * - Mutex
     - A synchronization primitive used to identify malware files and related malware families (for Mutex Indicators only)
     - String
     - Required for Mutex Indicators if ``summary`` is not used
   * - privateFlag
     - | Specifies whether to mark the Indicator as private (requires private Indicators being enabled on for your ThreatConnect instance)
       |
       | Default value: **false**
     - Boolean
     - Optional
   * - rating
     - | The Indicator's Threat Rating
       |
       | Minimum value: **0**
       | Maximum value: **5**
     - Integer
     - Optional
   * - securityLabel
     - An array of Security Labels applied to the Indicator
     - Array of Objects
     - Optional
   * - securityLabel.color
     - The hex color code (e.g., FF0000) for the Security Label's color
     - String
     - Required if ``securityLabel`` is used and the Security Label does not exist
   * - securityLabel.description
     - The Security Label's description
     - String
     - Required if ``securityLabel`` is used and the Security Label does not exist
   * - securityLabel.name
     - The Security Label's name
     - String
     - Required if ``securityLabel`` is used
   * - sha1
     - The File Indicator's SHA1 file hash
     - String
     - If ``summary`` is not used, at least one file hash field (``md5``, ``sha1``, or ``sha256``) is required [2]_
   * - sha256
     - The File Indicator's SHA256 file hash
     - String
     - If ``summary`` is not used, at least one file hash field (``md5``, ``sha1``, or ``sha256``) is required [2]_
   * - size
     - The File Indicator's file size
     - Integer
     - Optional
   * - Subject
     - The subject line of an email (for Email Subject Indicators only)
     - String
     - Required for Email Subject Indicators if ``summary`` is not used
   * - summary
     - The Indicator's summary
     - String
     - Required if the field that contains the Indicator's value for the specified Indicator type (e.g., ``ip`` for Address Indicators) is not used
   * - tag
     - An array of Tags applied to the Indicator
     - Array of Objects
     - Optional
   * - tag.name
     - The Tag's name
     - String
     - Required if ``tag`` is used
   * - text
     - A valid URL, including protocol (for URL Indicators only)
     - String
     - Required for URL Indicators if ``summary`` is not used
   * - **type**
     - **The Indicator's type**
     - **String**
     - **Required**
   * - User Agent String
     - A characteristic identification string that a software agent uses when operating in a network protocol (for User Agent Indicators only)
     - String
     - Required for User Agent Indicators if ``summary`` is not used
   * - Value Name
     - A registry value associated with the specified registry key (for Registry Key Indicators only)
     - String
     - Required for Registry Key Indicators if ``summary`` is not used
   * - Value Type
     - | A registry key value type (for Registry Key Indicators only)
       |
       | Acceptable values:
       |
       | * REG_NONE
       | * REG_BINARY
       | * REG_DWORD
       | * REG_DWORD_LITTLE_ENDIAN
       | * REG_DWORD_BIG_ENDIAN
       | * REG_EXPAND_SZ
       | * REG_LINK
       | * REG_MULTI_SZ
       | * REG_QWORD
       | * REG_QWORD_LITTLE_ENDIAN
       | * REG_SZ
     - String
     - Required for Registry Key Indicators if ``summary`` is not used

.. [1] 1 When creating File Occurrences, you must include *at least one* of the following fields in each File Occurrence object: ``date``, ``fileName``, or ``path``.

.. [2] For File Indicators, you can define their file hashes as a concatenated string using colon delimiters in the ``summary`` field or as separate file hashes in the ``md5``, ``sha1``, and ``sha256`` fields. See the `"File Indicator Considerations" <#id11>`_ section for more information.