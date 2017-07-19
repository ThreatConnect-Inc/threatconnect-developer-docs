Filtering Indicators
--------------------

The example below demonstrates usage of the modifiedSince parameter:

.. code::

    /v2/indicators?modifiedSince=2014-08-21T12:00:00Z

The example below demonstrates usage of the modifiedSince parameter and
an additional parameter:

.. code::

    /v2/indicators?modifiedSince=2014-08-21T12:00:00Z&owner=Common%20Community

The example below demonstrates usage of the summary parameter:

.. code::

    /v2/indicators?filters=summary%3Dexample.com

The example below demonstrates usage of the rating parameter:

.. code::

    /v2/indicators?filters=rating%3E3

The example below demonstrates usage of the threatAssessConfidence
parameter:

.. code::

    /v2/indicators/urls?filters=threatAssessConfidence%3E50

The example below demonstrates usage of the organization parameter:

.. code::

    /v2/indicators/addresses?filters=organization%3Dmosso%20hosting

The example below demonstrates usage of the whoisActive parameter:

.. code::

    /v2/indicators/hosts?filters=whoisActive%3Dtrue

The example below demonstrates usage of a Group name parameter:

.. code::

    /v2/groups?filters=name%5ETest

The example below demonstrates usage of a Group fileType parameter:

.. code::

    /v2/groups/documents?filters=fileType%3DPDF

The example below demonstrates usage of a securityLabels filter
parameter:

.. code::

    /v2/securityLabels?filters=name%3Ddictators

The example below demonstrates usage of a victim filter parameter:

.. code::

    /v2/victims?filters=name%5ETest

The example below demonstrates usage of a tag filter parameter:

.. code::

    /v2/tags?filters=weight%3E2

The example below demonstrates usage multiple parameters (with implicit
AND):

.. code::

    /v2/indicators?filters=summary%3Dexample.com,dateAdded%3C20151015

The example below demonstrates usage multiple parameters (with
parameters OR’ed):

.. code::

    /v2/indicators?filters=summary%3Dexample.com,dateAdded%3E20151015&orParams=true

To prevent the ThreatConnect API from returning an entire result-set, limit
the scope of the query based on the modifiedSince parameter. When a
query from the list below is issued with this parameter, it will only
return Indicators whose lastModified field contains a value on or after
the time specified by the included ISO 8601 time-stamp.

Use the modifiedSince parameter on the Indicators Service, e.g.,
``/v2/indicators``

Note that the ISO 8601 time-stamp is in the same format used to display
an Indicator’s lastModified value, and it can also be used in
conjunction with other parameters.

Note that an Indicator’s lastModified field is used to determine whether
or not it will be included with such a query. The following actions
update an Indicator’s lastModified field: - Creating the Indicator
manually - Importing the Indicator via structured or unstructured import
- Changing or resetting the Indicator’s "Threat" Rating - Changing the
Indicator’s Confidence value

**Filters**

+------------------------------------+------------+-----------+----------------------------------+
| Name                               | Data Type  | Operators | DB Field                         |
+====================================+============+===========+==================================+
| **Indicator Common Filters**       |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| summary                            | String     | ``= ^``   | indicator.summary                |
+------------------------------------+------------+-----------+----------------------------------+
| dateAdded                          | Date       | ``< >``   | indicator.dateAdded              |
+------------------------------------+------------+-----------+----------------------------------+
| rating                             | BigDecimal | ``<>``    | indicator.rating                 |
+------------------------------------+------------+-----------+----------------------------------+
| confidence                         | Short      | ``=<>``   | indicator.confidence             |
+------------------------------------+------------+-----------+----------------------------------+
| threatAssessRating                 | Double     | ``<>``    | commonIndicator.rating           |
+------------------------------------+------------+-----------+----------------------------------+
| threatAssessConfidence             | Double     | ``<>``    | commonIndicator.confidence       |
+------------------------------------+------------+-----------+----------------------------------+
| **Address Specific Filters**       |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| countryCode                        | String     | ``=``     | ipgeo.countryCode                |
+------------------------------------+------------+-----------+----------------------------------+
| organization                       | String     | ``=``     | ipgeo.registeringOrg             |
+------------------------------------+------------+-----------+----------------------------------+
| asn                                | Integer    | ``=``     | ipgeo.asn                        |
+------------------------------------+------------+-----------+----------------------------------+
| **Host Specific Filters**          |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| whoisActive                        | Boolean    | ``=``     | Indicator.flag2 on a host record |
+------------------------------------+------------+-----------+----------------------------------+
| dnsActive                          | Boolean    | ``=``     | Indicator.flag1 on a host record |
+------------------------------------+------------+-----------+----------------------------------+
| **Groups Type Filters**            |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| name                               | String     | ``= ^``   | bucket.name                      |
+------------------------------------+------------+-----------+----------------------------------+
| dateAdded                          | Date       | ``=<>``   | bucket.dateAdded                 |
+------------------------------------+------------+-----------+----------------------------------+
| **Groups Document Filter**         |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| fileType                           | String     | ``=``     | bucketDocument.type              |
+------------------------------------+------------+-----------+----------------------------------+
| **Security Label Specific Filter** |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| name                               | String     | ``= ^``   | securitylabel.name               |
+------------------------------------+------------+-----------+----------------------------------+
| **Tag Specific Filter**            |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| name                               | String     | ``= ^``   | tag.name                         |
+------------------------------------+------------+-----------+----------------------------------+
| weight                             | Integer    | ``=<>``   | tag.weight                       |
+------------------------------------+------------+-----------+----------------------------------+
| **Victim Specific Filter**         |            |           |                                  |
+------------------------------------+------------+-----------+----------------------------------+
| name                               | String     | ``=  ^``  | victim.name                      |
+------------------------------------+------------+-----------+----------------------------------+

.. note:: ``<``, ``>``, and ``^`` operators need to be escaped in the url as: ``< %3C``, ``> %3E``, ``^ %5E``.
