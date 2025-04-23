Create Indicators
-----------------

The follow example illustrates the basic format for creating an Indicator:

.. code::

    POST /v3/indicators
    Content-Type: application/json

    {
        "type": "Indicator type goes here",
        //required fields for the selected Indicator type
    }

Refer to the `Available Fields <#available-fields>`_ and `Indicator-Specific Fields <#indicator-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request to the ``/v3/indicators`` endpoint.

.. note::
    If you send a POST request to create an Indicator that already exists in the owner where the API request is creating data, the existing Indicator will be updated instead of a new one being created. This is because each owner can have only one copy of a given Indicator. For example, a single Organization can have only one copy of the Email Address Indicator **badguy@bad.com**.

.. note::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/group_attributes/indicator_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to an Indicator in a single POST or PUT request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^

The following request will create an **ultrabadguy.com** Host Indicator. It will also complete the following actions for the Indicator:

- Activate the **DNS** and **Whois** features for the Indicator
- Set the Indicator Status for the Indicator to active
- Associate the existing Group whose ID is 12 to the Indicator, and create a new **Bad Guy** Adversary Group in a Source and associate it to the Indicator
- Add a Description (i.e., a default Description Attribute) to the Indicator
- Set the Indicator's Threat and Confidence Ratings
- Apply the **TLP:AMBER** Security Label to the Indicator
- Apply the **Targeted Attack** standard Tag and the **T1566 - Phishing** ATT&CK® Tag to the Indicator

.. attention::
    To apply an ATT&CK Tag to an Indicator, use either the corresponding technique ID or name. For example, to apply the **T1566 - Phishing** ATT&CK Tag to an Indicator, either set ``name`` to ``"Phishing"`` or ``techniqueId`` to ``"T1566"`` when defining the ATT&CK Tag object in the request body.

    Also, if you applied a new Tag to an Indicator and that Tag matches a synonymous Tag listed in a `Tag normalization rule <https://knowledge.threatconnect.com/docs/tag-normalization>`_, it will be converted to the main Tag listed in the rule. Similarly, if you applied a new Tag to an Indicator and that Tag `matches an ATT&CK Tag <https://knowledge.threatconnect.com/docs/attack-tags#converting-standard-tags-to-attck-tags>`_, it will be converted to that ATT&CK Tag.

.. hint::
    To include the ``associatedGroups``, ``attributes``, ``securityLabels``, and ``tags`` fields in the API response, append ``?fields=associatedGroups&fields=attributes&fields=securityLabels&fields=tags`` to the end of the request URL.

.. code::

    POST /v3/indicators
    Content-Type: application/json
    
    {
        "type": "Host",
        "hostName": "ultrabadguy.com",
        "dnsActive": true,
        "whoisActive": true,
        "active": true,
        "associatedGroups": {
            "data": [
                {
                    "id": 12
                },
                {
                    "name": "Bad Guy",
                    "type": "Adversary",
                    "ownerName": "Demo Source"
                }
            ]
        },
        "attributes": {
            "data": [
                {
                    "type": "Description",
                    "value": "This host is very dangerous",
                    "default": true
                }
            ]
        },
        "confidence": 85,
        "rating": 5,
        "securityLabels": {
            "data": [
                {
                    "name": "TLP:AMBER"
                }
            ]
        },
        "tags": {
            "data": [
                {
                    "name": "Targeted Attack"
                },
                {
                    "techniqueId": "T1566"
                }
            ]
        }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 4,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-05T16:43:17Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
            "type": "Host",
            "lastModified": "2021-11-05T16:43:17Z",
            "rating": 5.00,
            "confidence": 85,
            "description": "This host is very dangerous",
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "hostName": "ultrabadguy.com",
            "dnsActive": true,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "message": "Created",
        "status": "Success"
    }