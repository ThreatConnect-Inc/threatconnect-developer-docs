Update Groups
-------------

To update a Group, the basic format is:

.. code::

    PUT /v2/groups/{groupType}/{groupId}
    {
      {updatedField}: {updatedValue}
    }

The ``{groupType}`` can be any one of the available group types:

- ``adversaries``
- ``campaigns``
- ``documents``
- ``emails``
- ``incidents``
- ``signatures``
- ``threats``

When updating the fields on a Group itself, you can change any of the fields available for the type of Group you are updating. Below is a table of available fields for each Group type:

+-------------+--------------+----------+
| Group Type  | Valid Fields | Required |
+=============+==============+==========+
| adversaries | name         | TRUE     |
+-------------+--------------+----------+
| campaigns   | name         | TRUE     |
+-------------+--------------+----------+
|             | firstSeen    | FALSE    |
+-------------+--------------+----------+
| documents   | fileName     | TRUE     |
+-------------+--------------+----------+
|             | name         | TRUE     |
+-------------+--------------+----------+
|             | malware      | FALSE    |
+-------------+--------------+----------+
|             | password     | FALSE    |
+-------------+--------------+----------+
| emails      | name         | TRUE     |
+-------------+--------------+----------+
|             | to           | FALSE    |
+-------------+--------------+----------+
|             | from         | FALSE    |
+-------------+--------------+----------+
|             | subject      | TRUE     |
+-------------+--------------+----------+
|             | header       | TRUE     |
+-------------+--------------+----------+
|             | body         | TRUE     |
+-------------+--------------+----------+
| incidents   | name         | TRUE     |
+-------------+--------------+----------+
|             | eventDate    | TRUE     |
+-------------+--------------+----------+
| threats     | name         | TRUE     |
+-------------+--------------+----------+
| signatures  | name         | TRUE     |
+-------------+--------------+----------+
|             | fileName     | TRUE     |
+-------------+--------------+----------+
|             | fileType\*   | TRUE     |
+-------------+--------------+----------+
|             | fileText\*\* | TRUE     |
+-------------+--------------+----------+

\*The valid values for a Signature’s fileType field are: {Snort ® , Suricata, YARA, ClamAV ® , OpenIOC, CybOX™, Bro, Regex}.

\*\*A Signature’s fileText field contains the Signature itself, which must be properly escaped and encoded when submitting for creation or updating.
  
By way of example, the query below will update the name of an Incident with ID 12345:

.. code::

    PUT /v2/groups/incidents/12345
    {
      "name": "New Incident Name",
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

Update Group Metadata
---------------------

Update Group Attributes
^^^^^^^^^^^^^^^^^^^^^^^

To update a Group's attribute, use the following format:

.. code::

    PUT /v2/groups/{groupType}/{groupId}/attributes/{attributeId}
    {
      {updatedField}: {updatedValue}
    }

When updating attributes, you can change the following fields:

+----------------------------+----------+
| Updatable Attribute Fields | Required |
+============================+==========+
| value                      | TRUE     |
+----------------------------+----------+
| displayed                  | FALSE    |
+----------------------------+----------+
| source                     | FALSE    |
+----------------------------+----------+

For example, if you wanted to update the value of an attribute with ID 54321 on the threat with ID 12345, you would use the following query:

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
