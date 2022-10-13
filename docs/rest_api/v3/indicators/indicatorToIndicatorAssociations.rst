Indicator-to-Indicator Associations
-----------------------------------

In ThreatConnect, you can associate two Indicators of certain types to one another using the following methods:

- Create an Indicator-to-Indicator Association
- Create a `File Action <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#file-actions>`_ (for File Indicators)

Create an Indicator-to-Indicator Association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each type of Indicator-to-Indicator association contains one primary (or parent) Indicator type and at least one non-primary (or child) Indicator type, as defined on the Indicators tab of the System Settings screen in ThreatConnect. When creating Indicator-to-Indicator associations, you can only associate Indicators of the non-primary type(s) to Indicators of the primary type.

For example, when creating an **ASN to Address** association, you can associate an Address Indicator (the non-primary Indicator type) to an ASN Indicator (the primary Indicator type). If you try to associate an ASN Indicator (the primary Indicator type) to an Address Indicator (the non-primary Indicator type) when creating the association, an error will be returned.

The following table outlines the default Indicator-to-Indicator associations in ThreatConnect and the Indicator types each association supports.

.. hint::
  If the Indicator of the non-primary type belongs to a Community or Source, use the Indicator's ID when setting the ``associatedIndicators`` field (e.g., ``"associatedIndicators": {"data": [{"id": 12345}]}``). For instructions on retrieving an Indicator's ID, see the `"Retrieve Indicators" section <#retrieve-indicators>`_.

  If the Indicator of the non-primary type belongs to an Organization, use the Indicator's ID, or use its type and summary type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field.

  To create an association to a new Indicator, include `all fields required to create the type of Indicator <#available-fields>`_ when setting the ``associatedIndicators`` field.

.. note::
    In addition to the association types listed in this table, customer-configured custom associations are also supported. Your System Administrator can retrieve information for these association types, including the primary and non-primary Indicator types the association supports, on the **Indicators** tab of the **System Settings** screen.

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

In the following example, the query will associate an Address Indicator to an existing ASN Indicator:

.. code::

    PUT /v3/indicators/ASN204288
    {
        "associatedIndicators": {"data": [{"ip": "66.96.146.129", "type": "Address"}]}
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 15,
            "ownerName": "Demo Organization",
            "dateAdded": "2022-03-11T19:25:43Z",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=15",
            "tags": {},
            "securityLabels": {},
            "type": "ASN",
            "lastModified": "2022-06-13T18:25:30Z",
            "summary": "ASN204288",
            "privateFlag": true,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {},
            "associatedIndicators": {
                "data": [
                    {
                        "id": 14,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-10-08T13:48:05Z",
                        "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=66.96.146.129",
                        "type": "Address",
                        "lastModified": "2022-06-13T18:22:47Z",
                        "summary": "66.96.146.129",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "ip": "66.96.146.129"
                    }
                ]
            },
            "fileActions": {
                "count": 0
            },
            "attributes": {},
            "associatedCases": {},
            "associatedArtifacts": {},
            "AS Number": "ASN204288"
        },
        "message": "Updated",
        "status": "Success"
    }

If you try to associate an ASN Indicator (i.e., the Indicator with ID 15) to an Address Indicator, as in the following example, an error message will be returned stating that the association cannot be applied to the Indicator types.

.. code::

    PUT /v3/indicators/66.96.146.129
    {
        "associatedIndicators": {"data": [{"id": 15}]}
    }

JSON Response

.. code:: json

    {
        "errCode": "0x1001",
        "message": "Association cannot be applied to the indicator types.",
        "status": "Error"
    }

.. note::
    If your System Administrator created a **custom** association where Address Indicators are the primary Indicator type and ASN Indicators are the non-primary Indicator type, then the two Indicators will be associated and no error will be returned.

Manage an Indicator's Indicator-to-Indicator Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can append, replace, and delete Indicator-to-Indicator associations via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information on using this field.