.. list-table::
   :widths: 35 25 15 25
   :header-rows: 1

   * - Field
     - Description
     - Accepted Data Type
     - Required?
   * - associatedGroupXid
     - An array of XIDs for Groups associated to the Group
     - String Array
     - Optional
   * - associatedIndicators
     - An array of Indicators associated to the Group
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
     - An array of Attributes added to the Group
     - Array of Objects
     - Optional
   * - attribute.displayed
     - Specifies whether to display the Attribute as a default Attribute on the **Details** screen for the Group to which it is added (applies to Description and Source Attributes only)
     - Boolean
     - Optional
   * - attribute.pinned
     - Specifies whether to display the Attribute as a pinned Attribute on the **Details** screen for the Group to which it is added
     - Boolean
     - Optional
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
   * - body
     - The body of the email (for Email Groups only)
     - String
     - Required for Email Groups
   * - eventDate
     - The date and time when the security event or incident took place (for Event and Incident Groups only)
     - DateTime
     - Optional
   * - externalDateAdded
     - The date and time when the Group was created externally
     - DateTime
     - Optional
   * - externalDateExpires
     - The date and time when the Group expires externally
     - DateTime
     - Optional
   * - externalLastModified
     - The date and time when the Group was last modified externally
     - DateTime
     - Optional
   * - fileName
     - The name of the Group's file (for Document, Report, and Signature Groups only)
     - String
     - Required for Document, Report, and Signature Groups
   * - fileText
     - The contents of the signature file (for Signature Groups only)
     - String
     - Required for Signature Groups
   * - fileType [2]_
     - The signature file's type (for Signature Groups only)
     - String
     - Required for Signature Groups only
   * - firstSeen
     - The date and time when the Group was first seen
     - DateTime
     - Optional
   * - from
     - The sender's email address for the email (for Email Groups only)
     - String
     - Optional
   * - header
     - The header of the email (for Email Groups only)
     - String
     - Required for Email Groups
   * - insights
     - An AI-generated synopsis of the Group (for Document and Report Groups only)
     - String
     - Optional
   * - lastSeen
     - The date and time when the Group was last seen
     - DateTime
     - Optional
   * - malware
     - Specifies whether the file uploaded to the Group is a malware file (for Document Groups only)
     - Boolean
     - Optional
   * - **name**
     - **The Group's name**
     - **String**
     - **Required**
   * - password
     - The password to access a malware file uploaded to the Group (for Document Groups only)
     - String
     - Required only if ``malware`` is set to **true** for a Document Group
   * - securityLabel
     - An array of Security Labels applied to the Group
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
   * - status [2]_
     - The status of the security event or incident (for Event and Incident Groups only)
     - String
     - Optional
   * - subject
     - The subject line of the email (for Email Groups only)
     - String
     - Required for Email Groups
   * - tag
     - An array of Tags applied to the Group
     - Array of Objects
     - Optional
   * - tag.name
     - The Tag's name
     - String
     - Required if ``tag`` is used
   * - to
     - The recipient's email address (for Email Groups only)
     - String
     - Optional
   * - **type**
     - **The Group's type**
     - **String**
     - **Required**
   * - **xid**
     - **The Group's XID**
     - **String**
     - **Required**

.. [2]  See the `v2 API Groups creation operation documentation <https://docs.threatconnect.com/en/latest/rest_api/v2/groups/groups.html#create-groups>`_ for a list of accepted values for this field.