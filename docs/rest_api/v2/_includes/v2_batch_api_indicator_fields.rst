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
   * - confidence
     - | The Indicator's Confidence Rating
       |
       | Minimum value: **0**
       |
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
   * - firstSeen
     - The date and time when the Indicator was first seen
     - DateTime
     - Optional
   * - lastSeen
     - The date and time when the Indicator was last seen
     - DateTime
     - Optional
   * - md5 [1]_
     - The File Indicator's MD5 file hash
     - String
     - Optional
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
       |
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
   * - sha1 [1]_
     - The File Indicator's SHA1 file hash
     - String
     - Optional
   * - sha256 [1]_
     - The File Indicator's SHA256 file hash
     - String
     - Optional
   * - size
     - The File Indicator's file size
     - Integer
     - Optional
   * - **summary** [1]_
     - **The Indicator's summary**
     - **String**
     - **Required**
   * - tag
     - An array of Tags applied to the Indicator
     - Array of Objects
     - Optional
   * - tag.name
     - The Tag's name
     - String
     - Required if ``tag`` is used
   * - **type**
     - **The Indicator's type**
     - **String**
     - **Required**

.. [1] For File Indicators, you can define their file hashes as a concatenated string using colon delimiters in the ``summary`` field or as separate file hashes in the ``md5``, ``sha1``, and ``sha256`` fields. See the `"File Indicator Considerations" <#id9>`_ section for more information.