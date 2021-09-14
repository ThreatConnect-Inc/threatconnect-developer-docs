Create Indicators
-----------------

To create an Indicator, the most basic format is:

.. code::

    POST /v2/indicators/{indicatorType}
    Content-type: application/json; charset=utf-8

    {
      // required fields here...
    }

The following are all considered valid paths for creating Indicators:

.. code::

    POST /v2/indicators/addresses
    POST /v2/indicators/emailAddresses
    POST /v2/indicators/files
    POST /v2/indicators/hosts
    POST /v2/indicators/urls

The table below illustrates valid fields for the body of the POST request when creating an Indicator.

Indicator Fields
^^^^^^^^^^^^^^^^

+----------------+--------------+----------+
| Indicator Type | Valid Fields | Required |
+================+==============+==========+
| addresses      | ip           | TRUE     |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
|                | active       | FALSE    |
+----------------+--------------+----------+
|                | activeLocked | FALSE    |
+----------------+--------------+----------+
| emailAddresses | address      | TRUE     |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
|                | active       | FALSE    |
+----------------+--------------+----------+
|                | activeLocked | FALSE    |
+----------------+--------------+----------+
| files          | md5          | TRUE\*   |
+----------------+--------------+----------+
|                | sha1         | TRUE\*   |
+----------------+--------------+----------+
|                | sha256       | TRUE\*   |
+----------------+--------------+----------+
|                | size         | FALSE    |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
|                | active       | FALSE    |
+----------------+--------------+----------+
|                | activeLocked | FALSE    |
+----------------+--------------+----------+
| hosts          | hostName     | TRUE     |
+----------------+--------------+----------+
|                | dnsActive    | FALSE    |
+----------------+--------------+----------+
|                | whoisActive  | FALSE    |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
|                | active       | FALSE    |
+----------------+--------------+----------+
|                | activeLocked | FALSE    |
+----------------+--------------+----------+
| urls           | text         | TRUE     |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
|                | active       | FALSE    |
+----------------+--------------+----------+
|                | activeLocked | FALSE    |
+----------------+--------------+----------+

\*Files are required to be submitted with at least one valid hash.

.. note:: The activeLocked field only prevents CAL from updating the status.

.. hint:: If you are unable to create an Indicator, view some `Common Indicator Creation Errors <https://docs.threatconnect.com/en/latest/common_errors.html#creating-indicators>`__.

Create Address Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/addresses
    Content-type: application/json; charset=utf-8

    {
      "ip": "192.168.0.1",
      "rating": 5.0,
      "confidence": 100
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "address": {
          "id": "54321",
          "owner": {
            "id": 5,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-08-03T16:00:37Z",
          "rating": 5.0,
          "confidence": 100,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=192.168.0.1&owner=Example+Organization",
          "ip": "192.168.0.1"
        }
      }
    }

Create Email Address Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/emailAddresses
    Content-type: application/json; charset=utf-8

    {
      "address": "badguy@example.com",
      "rating": 5.0,
      "confidence": 100
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "emailAddress": {
          "id": "54321",
          "owner": {
            "id": 5,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-08-03T16:00:07Z",
          "rating": 5.0,
          "confidence": 100,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=badguy%40example.com&owner=Example+Organization",
          "address": "badguy@example.com"
        }
      }
    }

Create File Indicators
^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/files
    Content-type: application/json; charset=utf-8

    {
      "md5": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
      "sha1": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
      "sha256": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
      "size": 5366,
      "rating": 5.0,
      "confidence": 100
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "file": {
          "id": "54321",
          "owner": {
            "id": 5,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-08-03T15:59:19Z",
          "rating": 5.0,
          "confidence": 100,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&owner=Example+Organization",
          "md5": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
          "sha1": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
          "sha256": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
          "size": 5366
        }
      }
    }

.. note:: A File Indicator requires only one, valid hash. It can be an md5, sha1, or sha256 hash, or any combination thereof.

Create Host Indicators
^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/hosts
    Content-type: application/json; charset=utf-8

    {
      "hostName": "example.com",
      "dnsActive": "false",
      "whoisActive": "true",
      "rating": 5.0,
      "confidence": 100
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "host": {
          "id": "54321",
          "owner": {
            "id": 5,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-08-03T15:55:40Z",
          "rating": 5.0,
          "confidence": 100,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=example.com&owner=Example+Organization",
          "hostName": "example.com",
          "dnsActive": "false",
          "whoisActive": "true"
        }
      }
    }

Create URL Indicators
^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/urls
    Content-type: application/json; charset=utf-8

    {
      "text": "http://example.com/bad.php",
      "rating": 5.0,
      "confidence": 100
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "url": {
          "id": "54321",
          "owner": {
            "id": 5,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-08-03T15:53:31Z",
          "rating": 5.0,
          "confidence": 100,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/url.xhtml?orgid=54321&owner=Example+Organization",
          "text": "http://example.com/bad.php"
        }
      }
    }

Create a Custom Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^

To create a Custom Indicator in ThreatConnect:

1. Use the `available Indicator types <#retrieve-available-indicator-types>`_ to identify the ``apiBranch`` and required fields (usually titled ``value1Label``, ``value2Label``, etc) for the Indicator type you would like to create.
2. Make a POST request in the format below with a body containing the required key-value pairs.

.. code::

    POST /v2/indicators/{indicatorApiBranch}
    Content-type: application/json; charset=utf-8

    {
      {value1Label}: {value1}
      {value2Label}: {value2}
      ...
    }

For example, to create a Registry Key via API, you would first use the `available Indicator types <#retrieve-available-indicator-types>`_ to identify the ``apiBranch`` and required values needed to create the Registry Key Indicator. To get this information, make the following request:

.. code::

    GET /v2/types/indicatorTypes

From this, find the entry for Registry Keys:

.. code:: json

    ...
    {
      "name": "Registry Key",
      "custom": "true",
      "parsable": "false",
      "apiBranch": "registryKeys",
      "apiEntity": "registryKey",
      "casePreference": "sensitive",
      "value1Label": "Key Name",
      "value1Type": "text",
      "value2Label": "Value Name",
      "value2Type": "text",
      "value3Label": "Value Type",
      "value3Type": "selectone",
      "value3Option": "REG_NONE;REG_BINARY;REG_DWORD;REG_DWORD_LITTLE_ENDIAN;REG_DWORD_BIG_ENDIAN;REG_EXPAND_SZ;REG_LINK;REG_MULTI_SZ;REG_QWORD;REG_QWORD_LITTLE_ENDIAN;REG_SZ"
    },
    ...

The ``apiBranch`` for Registry Keys is ``registryKeys`` and each Registry Key requires three values:

* ``Key Name`` - text
* ``Value Name`` - text
* ``Value Type`` - One of the following: REG_NONE, REG_BINARY, REG_DWORD, REG_DWORD_LITTLE_ENDIAN, REG_DWORD_BIG_ENDIAN, REG_EXPAND_SZ, REG_LINK, REG_MULTI_SZ, REG_QWORD, REG_QWORD_LITTLE_ENDIAN, or REG_SZ

This allows you to create the following POST request to create a new Registry Key:

.. code::

    POST /v2/indicators/registryKeys
    Content-type: application/json; charset=utf-8

    {
      "Key Name": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\DRM\\{cd704ff3-cd05-479e-acf7-6474908031dd}",
      "Value Name": "Example Value",
      "Value Type": "REG_NONE"
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "registryKey": {
          "id": "54321",
          "owner": {
            "id": 5,
            "name": "Common Community",
            "type": "Community"
          },
          "type": "Registry Key",
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-08-09T13:29:51Z",
          "webLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=25286094&owners=631&owner=Common%20Community",
          "Key Name": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\DRM\\{cd704ff3-cd05-479e-acf7-6474908031dd}",
          "Value Name": "Example Value",
          "Value Type": "REG_NONE"
        }
      }
    }

Create Indicator Metadata
-------------------------

Add Indicator False Positive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To `report a false positive <http://kb.threatconnect.com/customer/portal/articles/2324809>`_ for an Indicator, use a request in the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/falsePositive

For example, the following query will report a false positive for the Host Indicator ``example.com``:

.. code::

    POST v2/indicators/hosts/example.com/falsePositive

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "falsePositive": {
          "count": 1,
          "lastReported": "2017-07-13T17:04:54Z"
        }
      }
    }

.. note:: There can only be one false positive reported per user, per Indicator, per day. In other words, your API user can only report a false positive for a given Indicator once per day.

Add Indicator Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^

To add Observations to an Indicator, use a request in the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/observations
    Content-type: application/json; charset=utf-8

    {
      "count" : 10
    }

For example, the following query will report two Observations for the File Indicator ``AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA``:

.. code::

    POST /v2/indicators/files/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/observations
    Content-type: application/json; charset=utf-8

    {
      "count" : 2
    }

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

Create Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add an Attribute to an Indicator, use the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/attributes
    Content-type: application/json; charset=utf-8

    {
      "type" : {attributeType},
      "value" : "Test Attribute",
      "displayed" : true
    }

For example, to add a Description Attribute to the Email Address ``bad@example.com``, you would use the following query:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/attributes
    Content-type: application/json; charset=utf-8

    {
      "type" : "Description",
      "value" : "Test Description",
      "displayed" : true
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "attribute": {
          "id": "54321",
          "type": "Description",
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-07-13T17:50:17",
          "displayed": true,
          "value": "Test Description"
        }
      }
    }

To add a Security Label to an Attribute, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the Attribute on the Threat:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/attributes/54321/securityLabels/TLP%20Amber

.. note:: In order to add a Security Label to an Attribute, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Indicator Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a Security Label to an Indicator, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the Email Address ``bad@example.com``:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

.. note:: In order to add a Security Label to an Indicator, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Indicator Tags
^^^^^^^^^^^^^^^^^^^^^

To add a Tag to an Indicator, use the following format, where ``{tagName}`` is replaced with the name of the Tag you wish to add to the Indicator:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/tags/{tagName}

For example, the query below will add the ``Nation State`` Tag to the Email Address ``bad@example.com``:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

.. include:: ../_includes/tag_length.rst

Creating File Occurrences
^^^^^^^^^^^^^^^^^^^^^^^^^

To add a File Occurrence to a File Indicator, use a query in the following format:

.. code::

    POST /v2/indicators/files/{fileHash}/fileOccurrences
    Content-type: application/json; charset=utf-8

    {
      "fileName" : {fileName},
      "path" : {filePath},
      "date" : {date}
    }

When adding a File Occurrence, the following fields are available:

+--------------+----------+
| Valid Fields | Required |
+==============+==========+
| fileName     | FALSE\*  |
+--------------+----------+
| path         | FALSE\*  |
+--------------+----------+
| date         | FALSE\*  |
+--------------+----------+

\* While none of the fields are required, at least one of them must be populated to create a File Occurrence.

For example, the following query will add a File Occurrence to the File Indicator represented by the hash ``aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa``:

.. code::

    POST /v2/indicators/files/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/fileOccurrences
    Content-type: application/json; charset=utf-8

    {
      "fileName" : "win999301.dll",
      "path" : "C:\\\\Windows\\System",
      "date" : "2017-07-13T00:00:00-05:00"
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "fileOccurrence": {
          "id": 87534,
          "fileName": "win999301.dll",
          "path": "C:\\\\Windows\\System",
          "date": "2017-07-13T05:00:00Z"
        }
      }
    }

Create Indicator Associations
-----------------------------

Associate Group to Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To associate an Indicator with a Group, use a query in the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/groups/{associatedGroupType}/{associatedGroupId}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, the query below will associate the Email Address ``bad@example.com`` with an Incident with the ID 54321:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

Associate Indicator to Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The documentation for creating and retrieving Indicator-to-Indicator relationships has been moved `here <#indicator-to-indicator-associations>`_.

Associate Victim to Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To associate an Indicator with a Victim, use a query in the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/victims/{victimId}

For example, the query below will associate the Email Address ``bad@example.com`` with the Victim with ID 54321:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/victims/54321

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

.. include:: ../_includes/victim_asset_required_warning.rst
