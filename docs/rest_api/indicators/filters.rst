Filtering Indicators
^^^^^^^^^^^^^^^^^^^^

Filter Parameters
"""""""""""""""""

When retrieving Indicators from ThreatConnect, it is possible to filter the results. Results can be filtered on the following data points:

+------------------------------+------------+---------------------+
| Name                         | Data Type  | Operator(s)         |
+==============================+============+=====================+
| **Indicator Common Filters** |            |                     |
+------------------------------+------------+---------------------+
| active                       | boolean    | ``=``               |
+------------------------------+------------+---------------------+
| summary                      | string     | ``=``, ``^``        |
+------------------------------+------------+---------------------+
| modifiedSince                | string     | ``=``, ``^``        |
+------------------------------+------------+---------------------+
| dateAdded                    | date       | ``<``, ``>``        |
+------------------------------+------------+---------------------+
| rating                       | bigdecimal | ``<``, ``>``        |
+------------------------------+------------+---------------------+
| confidence                   | integer    | ``=``, ``<``, ``>`` |
+------------------------------+------------+---------------------+
| threatAssessScore            | integer    | ``=``, ``<``, ``>`` |
+------------------------------+------------+---------------------+
| threatAssessRating           | double     | ``<``, ``>``        |
+------------------------------+------------+---------------------+
| threatAssessConfidence       | double     | ``<``, ``>``        |
+------------------------------+------------+---------------------+
| falsePositive                | integer    | ``=``, ``<``, ``>`` |
+------------------------------+------------+---------------------+
| **Address Specific Filters** |            |                     |
+------------------------------+------------+---------------------+
| city                         | string     | ``=``               |
+------------------------------+------------+---------------------+
| countryCode                  | string     | ``=``               |
+------------------------------+------------+---------------------+
| countryName                  | string     | ``=``               |
+------------------------------+------------+---------------------+
| organization                 | string     | ``=``               |
+------------------------------+------------+---------------------+
| state                        | string     | ``=``               |
+------------------------------+------------+---------------------+
| timezone                     | string     | ``=``               |
+------------------------------+------------+---------------------+
| asn                          | integer    | ``=``               |
+------------------------------+------------+---------------------+
| **Host Specific Filters**    |            |                     |
+------------------------------+------------+---------------------+
| whoisActive                  | boolean    | ``=``               |
+------------------------------+------------+---------------------+
| dnsActive                    | boolean    | ``=``               |
+------------------------------+------------+---------------------+

.. include:: ../_includes/filter_symbol_encoding_note.rst

**Examples**

The example below demonstrates the use of the ``active`` parameter, to retrieve both active and inactive indicators (with
parameters OR'ed):

.. code::

    GET /v2/indicators?filters=active%3Dtrue,active%3Dfalse&orParams=true

The example below demonstrates usage of the summary parameter:

.. code::

    GET /v2/indicators?filters=summary%3Dexample.com

The example below demonstrates usage of the rating parameter:

.. code::

    GET /v2/indicators?filters=rating%3E3

The example below demonstrates usage of the threatAssessScore
parameter:

.. code::

    GET /v2/indicators/?filters=threatAssessScore%3E450

The example below demonstrates usage of the threatAssessConfidence
parameter:

.. code::

    GET /v2/indicators/urls?filters=threatAssessConfidence%3E50

The example below demonstrates usage of the organization parameter:

.. code::

    GET /v2/indicators/addresses?filters=organization%3Dmosso%20hosting

The example below demonstrates usage of the whoisActive parameter:

.. code::

    GET /v2/indicators/hosts?filters=whoisActive%3Dtrue

The example below demonstrates the use of multiple parameters (with implicit
AND):

.. code::

    GET /v2/indicators?filters=summary%3Dexample.com,dateAdded%3C2015-10-15

The example below demonstrates the use of multiple parameters (with
parameters OR’ed):

.. code::

    GET /v2/indicators?filters=summary%3Dexample.com,dateAdded%3E2015-10-15&orParams=true

The example below demonstrates how to filter based on the number of times an Indicator has been voted a False Positive:

.. code::

    GET /v2/indicators?filters=falsePositive%3E10

Owner Parameter
"""""""""""""""

By default, all API calls will operate in the API user account's default Organization. To specify a different Owner, use the ``owner`` URL parameter as in ``?owner={ownerName}``. For example, the following query will return all Host Indicators in the Common Community:

.. code::

    GET /v2/indicators/hosts/?owner=Common%20Community

Modified Since Parameter
""""""""""""""""""""""""

To prevent the ThreatConnect API from returning an entire result set, limit the scope of the query based on the ``modifiedSince`` parameter. This query requires an ISO 8601 date-stamp (as shown in the examples below) and will only return Indicators whose lastModified field contains a value on or after the date specified.

The following actions update an Indicator’s lastModified field:

* Creating the Indicator manually
* Importing the Indicator via structured or unstructured import
* Changing the Indicator’s threat rating
* Changing the Indicator’s confidence rating.

The example below demonstrates the use of the modifiedSince parameter:

.. code::

    GET /v2/indicators?modifiedSince=2017-08-21T12:00:00Z

The example below demonstrates the use of the modifiedSince parameter and
an additional parameter:

.. code::

    GET /v2/indicators?modifiedSince=2017-08-21T12:00:00Z&owner=Common%20Community


