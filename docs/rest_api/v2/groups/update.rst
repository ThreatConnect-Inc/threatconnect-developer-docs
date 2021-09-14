Update Groups
-------------

To update a Group, the basic format is:

.. code::

    PUT /v2/groups/{groupType}/{groupId}
    {
      {updatedField}: {updatedValue}
    }

The ``{groupType}`` can be any one of the available Group types:

- ``adversaries``
- ``attackPatterns``
- ``campaigns``
- ``coursesOfAction``
- ``documents``
- ``emails``
- ``events``
- ``incidents``
- ``intrusionSets``
- ``malware``
- ``reports``
- ``signatures``
- ``tactics``
- ``threats``
- ``tools``
- ``vulnerabilities``

When updating the fields on a Group, you can change any of the fields available for the type of Group you are updating. Below is a table of available fields for each Group type:

.. include:: group_fields.rst

By way of example, the query below will update the name of an Incident with ID 12345:

.. code::

    PUT /v2/groups/incidents/12345
    {
      "name": "New Incident Name"
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "incident": {
          "id": "12345",
          "name": "New Incident Name",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=12345",
          "eventDate": "2017-7-13T00:00:00-04:00"
        }
      }
    }

Uploading/Updating Document Contents
^^^^^^^^^^^^^^^^^^^^^^^^

To update the contents of a Document in ThreatConnect, use a query in the following format:

.. note:: If you’re uploading a file larger than 5GB, contact your System Administrator about increasing the allowed file size for uploads.

.. note:: To upload the initial document, rather than updating the existing document, replace PUT with POST

.. code::

    PUT /v2/groups/documents/{documentId}/upload
    Content-Type: application/octet-stream

    <raw document contents>

The ``Content-Type`` header must be set to ``application/octet-stream`` for this query to work properly. The query below demonstrates how to upload some text into the Document with ID 12345:

.. code::

    PUT /v2/groups/documents/12345/upload
    Content-Type: application/octet-stream

    New Document contents here.

JSON Response:

.. code:: json

    {
      "status": "Success",
    }

Uploading/Updating Report Contents
^^^^^^^^^^^^^^^^^^^^^^^^

To update the contents of a Report in ThreatConnect, use a query in the following format:

.. note:: If you’re uploading a file larger than 5GB, contact your System Administrator about increasing the allowed file size for uploads.

.. note:: To upload the initial report, rather than updating the existing report, replace PUT with POST

.. code::

    PUT /v2/groups/reports/{documentId}/upload
    Content-Type: application/octet-stream

    <raw report contents>

The ``Content-Type`` header must be set to ``application/octet-stream`` for this query to work properly. The query below demonstrates how to upload some text into the Document with ID 12345:

.. code::

    PUT /v2/groups/reports/12345/upload
    Content-Type: application/octet-stream

    New report contents here.

JSON Response:

.. code:: json

    {
      "status": "Success",
    }

Update Group Metadata
---------------------

Update Group Attributes
^^^^^^^^^^^^^^^^^^^^^^^

To update a Group's Attribute, use the following format:

.. code::

    PUT /v2/groups/{groupType}/{groupId}/attributes/{attributeId}
    {
      {updatedField}: {updatedValue}
    }

When updating Attributes, you can change the following fields:

+----------------------------+----------+
| Updatable Attribute Fields | Required |
+============================+==========+
| value                      | TRUE     |
+----------------------------+----------+
| displayed                  | FALSE    |
+----------------------------+----------+
| source                     | FALSE    |
+----------------------------+----------+

For example, if you wanted to update the value of an Attribute with ID 54321 on the Threat with ID 12345, you would use the following query:

.. code::

    PUT /v2/groups/threats/12345/attributes/54321
    {
      "value": "Bad... Very bad."
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
          "lastModified": "2017-07-19T15:54:12Z",
          "displayed": true,
          "value": "Bad... Very bad."
        }
      }
    }

Update Adversary Assets
^^^^^^^^^^^^^^^^^^^^^^^

To update an Adversary's Asset, use the following format:

.. code::

    PUT /v2/groups/adversaries/{adversaryId}/adversaryAssets/{assetType}/{assetId}
    {
      {updatedField}: {updatedValue}
    }

``{assetType}`` can be replaced with the following Asset types:

* handles
* phoneNumbers
* urls

When updating an Adversary Asset, you can change the following field:

+----------------------------+----------+
| Updatable Attribute Fields | Required |
+============================+==========+
| handle\*                   | FALSE    |
+----------------------------+----------+
| phoneNumber\*\*            | FALSE    |
+----------------------------+----------+
| url\*\*\*                  | FALSE    |
+----------------------------+----------+

\* The ``handle`` field can only be updated for Adversary Assets of the handles type

\*\* The ``phoneNumber`` field can only be updated for Adversary Assets of the phoneNumbers type

\*\*\* The ``url`` field can only be updated for Adversary Assets of the urls type

For example, if you wanted to update the URL of the Adversary Asset with ID 1 on the Adversary with ID 12345, you would use the following request:

.. code::

    PUT /v2/groups/adversaries/12345/adversaryAssets/urls/1
    {
      "url": "https://newsite.com/"
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "adversaryUrl": {
          "id": 1,
          "type": "URL",
          "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=12345",
          "url": "https://newsite.com/"
        }
      }
    }
