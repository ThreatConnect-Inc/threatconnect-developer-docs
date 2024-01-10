.. list-table::
   :widths: 35 25 15 25
   :header-rows: 1

   * - Field
     - Description
     - Accepted Data Type
     - Required?
   * - attribute
     - An array of Attributes added to the Indicator
     - Array of Objects
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
     - The Indicator's Confidence Rating
     - Integer
     - Optional
   * - description
     - The value of the Indicator's default Description Attribute
     - String
     - Optional
   * - rating
     - The Indicator's Threat Rating
     - Integer
     - Optional
   * - source
     - The value of the Indicator's default Source Attribute
     - String
     - Optional
   * - **summary**
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