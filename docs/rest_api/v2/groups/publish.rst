Publish Groups
--------------

As of ThreatConnect version 5.2, it is possible to publish intelligence for a specific Group. The general format for this request is as follows:

.. code::

    POST v2/groups/{groupType}/{groupId}/publish
    Content-type: application/json; charset=utf-8

    {
      "securityLabelList": [],
      "excludeUnlabeled": false
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

The ``securityLabelList`` key of the request body allows you to provide the name(s) of the Security Label(s) that, if an item has this Label, you would like to exclude when publishing. The following example-request body would *not* publish any items (Groups or Indicators) that have the ``TLP Green`` or ``TLP Amber`` Labels:

.. code:: json

    {
      "securityLabelList": [
        "TLP Green",
        "TLP Amber"
      ],
      "excludeUnlabeled": false
    }

The ``excludeUnlabeled`` key gives you the option to exclude all items that do not have a Security Label. The following example-request body would *not* publish any items that have the ``TLP Green`` or ``TLP Amber`` Labels or any items that do not have a Security Label:

.. code:: json

    {
      "securityLabelList": [
        "TLP Green",
        "TLP Amber"
      ],
      "excludeUnlabeled": true
    }

The JSON response to any of these queries, assuming the query is successful, is as follows:

.. code:: json

    {
      "status": "Success"
    }
