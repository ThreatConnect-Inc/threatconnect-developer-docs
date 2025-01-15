Assign Security Coverage to ATT&CK Tags
---------------------------------------

.. attention::
    Only API users with an Organization role of Organization Administrator can assign security coverage to ATT&CK Tags.

Send a request in the following format to update the security coverage assigned to an ATT&CK Tag:

.. code::

    PUT /v3/tags/{att&ckTagId}
    Content-Type: application/json
    
    {
        "securityCoverage": {
            "value": "<securityCoverageLevel>"
        }
    }

* ``securityCoverage``: <*Object*> The details of the security coverage level assigned to the ATT&CK Tag.
    *  ``value``: <*String*> The security coverage level assigned to the ATT&CK Tag. (Accepted values: **None**, **Weak**, **Moderate**, **Strong**)

For example, the following request will assign **Weak** coverage to the ATT&CK Tag whose ID is 750:

.. code::

   PUT /v3/tags/750
   Content-Type: application/json

    {
        "securityCoverage": {
            "value": "Weak"
        }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 750,
            "name": "Data Obfuscation",
            "description": "Adversaries may obfuscate command and control traffic to make it more difficult to detect. Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, or impersonating legitimate protocols. ",
            "lastUsed": "2023-07-28T17:32:32Z",
            "techniqueId": "T1001",
            "tactics": {
                "data": [
                    "Command and Control"
                ],
                "count": 1
            },
            "platforms": {
                "data": [
                    "Linux",
                    "macOS",
                    "Windows"
                ],
                "count": 3
            },
            "securityCoverage": {
                "value": "Weak"
            }
        },
        "message": "Updated",
        "status": "Success"
    }