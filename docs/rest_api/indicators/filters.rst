Filtering Indicators
^^^^^^^^^^^^^^^^^^^^

Filters Parameter
"""""""""""""""""

When retrieving Indicators from ThreatConnect, it is possible to filter the results. Results can be filtered on the following data points:

+------------------------------+------------+---------------------+
| Name                         | Data Type  | Operator(s)         |
+==============================+============+=====================+
| **Indicator Common Filters** |            |                     |
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
| threatAssessRating           | double     | ``<``, ``>``        |
+------------------------------+------------+---------------------+
| threatAssessConfidence       | double     | ``<``, ``>``        |
+------------------------------+------------+---------------------+
| falsePositive                | integer    | ``=``, ``<``, ``>`` |
+------------------------------+------------+---------------------+
| **Address Specific Filters** |            |                     |
+------------------------------+------------+---------------------+
| countryCode                  | string     | ``=``               |
+------------------------------+------------+---------------------+
| organization                 | string     | ``=``               |
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

The example below demonstrates usage multiple parameters (with implicit
AND):

.. code::

    /v2/indicators?filters=summary%3Dexample.com,dateAdded%3C20151015

The example below demonstrates usage multiple parameters (with
parameters OR’ed):

.. code::

    /v2/indicators?filters=summary%3Dexample.com,dateAdded%3E20151015&orParams=true

The example below demonstrates how to filter based on the number of times an Indicator has been voted a False Positive:

.. code::

    GET /v2/indicators?filters=falsePositive%3E10

Modified Since Parameter
""""""""""""""""""""""""

To prevent the ThreatConnect API from returning an entire result-set, limit the scope of the query based on the ``modifiedSince`` parameter. This query requires an ISO 8601 date-stamp (as shown in the examples below) and will only return Indicators whose lastModified field contains a value on or after the date specified.

The following actions update an Indicator’s lastModified field:

* Creating the Indicator manually
* Importing the Indicator via structured or unstructured import
* Changing the Indicator’s threat rating
* Changing the Indicator’s confidence rating.

The example below demonstrates usage of the modifiedSince parameter:

.. code::

    GET /v2/indicators?modifiedSince=2017-08-21T12:00:00Z

The example below demonstrates usage of the modifiedSince parameter and
an additional parameter:

.. code::

    GET /v2/indicators?modifiedSince=2017-08-21T12:00:00Z&owner=Common%20Community

Owner Parameter
"""""""""""""""

By default, all API calls will operate in the API user account's default organization. To specify a different owner, use the ``owner`` URL parameter like ``?owner={ownerName}``. For example, the following query will return all Host Indicators in the Common Community:

.. code::

    GET /v2/indicators/hosts/?owner=Common%20Community
