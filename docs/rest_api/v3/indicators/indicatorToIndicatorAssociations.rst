Indicator-to-Indicator Associations
-----------------------------------

In ThreatConnect, you can associate two Indicators of certain types to one another using the following methods:

- Create an Indicator-to-Indicator Association
- Create a `File Action <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#file-actions>`_ (for File Indicators)

Create an Indicator-to-Indicator Association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each type of Indicator-to-Indicator association contains one primary (or parent) Indicator type and at least one non-primary (or child) Indicator type, as defined on the **Indicators** tab of the **System Settings** screen in ThreatConnect. When creating Indicator-to-Indicator associations using the v3 API, you can only associate Indicators of the non-primary type(s) to Indicators of the primary type. For example, in an **ASN to Address** association, the ASN Indicator is the primary Indicator type and the Address Indicator is the non-primary Indicator type. This means you can associate an Address Indicator to an ASN Indicator, but you cannot associate an ASN Indicator to an Address Indicator.

When creating Indicator-to-Indicator associations using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Indicator of the non-primary type, include `all fields required to create the type of Indicator <#available-fields>`_ when setting the ``associatedIndicators`` field. To create the Indicator in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Indicator when setting the ``associatedIndicators`` field.
- To create an association to an existing Indicator of the non-primary type, use the Indicator's ID, or use its type and summary type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field. To create an association to an Indicator that exists in a Community or Source using the Indicator's summary and type, include the ``ownerId`` or ``ownerName`` field and specify the ID or name, respectively, of the Community or Source to which the Indicator belongs when setting the ``associatedIndicators`` field.

The following table outlines the default Indicator-to-Indicator associations in ThreatConnect and the Indicator types each association supports.

.. list-table::
   :widths: 33 33 33
   :header-rows: 1

   * - Association Name
     - Primary Indicator Type
     - Non-Primary Indicator Type(s)
   * - Address to User Agent
     - Address
     - User Agent
   * - ASN to Address
     - ASN
     - Address
   * - ASN to CIDR
     - ASN
     - CIDR
   * - CIDR to Address
     - CIDR
     - Address
   * - DNS PTR Record
     - Address
     - Host
   * - Domain Registrant Email
     - Host
     - EmailAddress
   * - Domain Registrant Email
     - Host
     - EmailAddress
   * - File Download
     - URL
     - File
   * - URL Host
     - URL
     - Host, Address

.. note::
    In addition to the association types listed in this table, customer-configured custom associations are also supported. Your System Administrator can retrieve information for these association types, including the primary and non-primary Indicator types the association supports, on the **Indicators** tab of the **System Settings** screen.

In the following example, the request will associate an existing Address Indicator to an existing ASN Indicator. Because the ``associatedIndicators`` field is not included in the API response by default, the ``fields`` query parameter is added to the request URL and assigned a value of ``associatedIndicators`` so that this field is included in the response.

.. code::

    PUT /v3/indicators/ASN204288?fields=associatedIndicators
    Content-Type: application/json

    {
      "associatedIndicators": {
        "data": [
          {
            "ip": "66.96.146.129", 
            "type": "Address"
          }
        ]
      }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 15,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2022-03-11T19:25:43Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/15/overview",
            "type": "ASN",
            "lastModified": "2022-06-13T18:25:30Z",
            "summary": "ASN204288",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedIndicators": {
                "data": [
                    {
                        "id": 14,
                        "ownerId": 1,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-10-08T13:48:05Z",
                        "webLink": "https://app.threatconnect.com/#/details/indicators/14/overview",
                        "type": "Address",
                        "lastModified": "2022-06-13T18:25:30Z",
                        "summary": "66.96.146.129",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "ip": "66.96.146.129",
                        "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=66.96.146.129&owner=Demo+Organization"
                    }
                ]
            },
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=15&owner=Demo+Organization",
            "AS Number": "ASN204288"
        },
        "message": "Updated",
        "status": "Success"
    }

If you try to associate an ASN Indicator to an Address Indicator, as in the following example, an error message will be returned stating that the association cannot be applied to the Indicator types.

.. code::

    PUT /v3/indicators/66.96.146.129
    Content-Type: application/json

    {
      "associatedIndicators": {
        "data": [
          {
            "AS Number": "ASN204288",
            "type": "ASN"
          }
        ]
      }
    }

JSON Response

.. code:: json

    {
        "errCode": "0x1001",
        "message": "Association cannot be applied to the indicator types.",
        "status": "Error"
    }

.. note::
    In this example, the two Indicators would be associated and no error would be returned only if your System Administrator created a custom association where Address Indicators are the primary Indicator type and ASN Indicators are the non-primary Indicator type.

Manage an Indicator's Indicator-to-Indicator Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can append, replace, and delete Indicator-to-Indicator associations via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information on using this field.