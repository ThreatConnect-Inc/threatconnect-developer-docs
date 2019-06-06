Private Indicators
------------------

.. warning:: In order to mark an Indicator as private, the ThreatConnect instance of ThreatConnect needs to have the ``privateIndicatorsEnabled`` configuration selected. This can be modified under System Settings.

.. note:: Custom Indicators cannot be marked as private. Only Address, Email Address, File, Host, and URL Indicators can be marked as private.

Retrieving Private Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When retrieving an Indicator, it is possible to see if the Indicator is private by appending the ``includeAdditional=true`` parameter to the query, as demonstrated below:

.. code::

    GET /v2/indicators/hosts/example.org?includeAdditional=true

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "host": {
          "id": 123456,
          "owner": {
            "id": 2,
            "name": "Example Org",
            "type": "Organization"
          },
          "dateAdded": "2017-10-31T16:55:44Z",
          "lastModified": "2017-11-06T13:23:13Z",
          "rating": 4.00,
          "confidence": 85,
          "threatAssessRating": 4.37,
          "threatAssessConfidence": 72.91,
          "threatAssessScore": 650,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=example.org&owner=Example+Org",
          "source": "ThreatConnect Enrichment",
          "description": "Malicious domain.",
          "observationCount": 0,
          "falsePositiveCount": 0,
          "privateFlag": true,
          "hostName": "example.org",
          "dnsActive": "true",
          "whoisActive": "true"
        }
      }
    }

Creating Private Indicators 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To mark an Indicator as private when creating it, add the following key-value pair to the body of the POST query used to create the Indicator:

.. code::

    "privateFlag": "true"

For example, the following query will create a host Indicator that is marked as private:

.. code::

    POST /v2/indicators/hosts
    {
        "hostName": "example.org",
        "privateFlag": "true"
    }
