Custom Metrics
==============

As of ThreatConnect 5.4, it is possible to create Custom Metrics which can be used to monitor and track important data points. A card for Custom Metrics can be created on the `ThreatConnect dashboard <http://kb.threatconnect.com/customer/en/portal/articles/2092053-dashboard>`_ to show the value(s) of a metric. This documentation will detail how to retrieve, create, and delete Custom Metrics via the API.

Retrieving Custom Metrics
-------------------------

In order to view the Custom Metrics available to an Organization in ThreatConnect, use the following query:

.. code::

    GET /v2/customMetrics/

JSON Response:

.. code::

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "customMetricConfig": [
          {
            "id": 7,
            "name": "playbookRuns",
            "dataType": "Sum",
            "interval": "Hourly",
            "keyedValues": true,
            "description": "Monitor playbook runs."
          },
          {
            "id": 11,
            "name": "tasksCompleted",
            "dataType": "Sum",
            "interval": "Daily",
            "keyedValues": false,
            "description": "Track the number of tasks closed."
          }
        ]
      }
    }

To view a specific metric, add the metric’s name to the end of the query as shown below:

.. code::

    GET /v2/customMetrics/{metricName}

Or, alternatively, you can use the ID of the metric to get the same result:

.. code::

    GET /v2/customMetrics/{metricId}

Creating a Custom Metric
------------------------

To create a new Custom Metric, use a query in the following format:

.. code::

    POST /v2/customMetrics
    {
      "name" : "newMetric",
      "dataType" : "Sum",
      "interval" : "Daily",
      "keyedValues" : false,
      "description" : "Testing API Updates"
    }

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "customMetricConfig": {
          "id": 1234567,
          "name": "newMetric",
          "dataType": "Sum",
          "interval": "Daily",
          "keyedValues": false,
          "description": "Testing API Updates"
        }
      }
    }

The following values are the available values for the ``dataType`` field in the body of the query above:

* Sum
* Count
* Min
* Max
* First
* Last
* Average

The following values are the available values for the ``interval`` field in the body of the query above:

* Hourly
* Daily
* Weekly
* Monthly
* Yearly

Creating Content in a Custom Metric
-----------------------------------

.. note:: When passing a "date" field into a request, use a timestamp in `ISO format <https://en.wikipedia.org/wiki/ISO_8601>`__ (e.g. ``2018-10-19T14:44:00Z``).

Creating Content in a Keyed Metric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add content to a keyed metric, use a query in the following format:

.. code::

    POST /v2/customMetrics/{metricName}/data
    {
      "name": "{metricKeyName}",
      "value": "{incrementValue}",
      "date": "{date}", //optional
      "weight": "{weight}" //optional and only needed for average
    }

For example, the query below will add one to the value stored in the ``app1`` key in a ``playbookRuns`` metric:

.. code::

    POST /v2/customMetrics/playbookRuns/data
    {
      "name": "app1",
      "value": "1"
    }

Creating Content in a Non-Keyed Metric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add content to a non-keyed metric, use a query in the following format:

.. code::

    POST /v2/customMetrics/{metricName}/data
    {
      "value": "{incrementValue}",
      "date": "{date}", //optional
      "weight": "{weight}" //optional and only needed for average
    }

For example, the query below will add two to the count of a ``tasksCompleted`` metric:

.. code::

    POST /v2/customMetrics/tasksCompleted/data
    {
      "value": "2",
      "date": "2018-01-19T14:44:00Z"
    }

Custom Metrics Return Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating a new entry in a metric, it is possible to view the current value by adding the ``?returnValue=true`` flag to the query. For example, the query format below will increment the value of a non-keyed metric by two and return the current value of the metric:

.. code::

    POST /v2/customMetrics/{metricName}/data?returnValue=true
    {
      "value": "{incrementValue}",
      "date": "{date}", //optional
      "weight": "{weight}" //optional and only needed for average
    }

THe following is a notional example that keeps track of how many tasks have been closed. The query below will add two to the ``tasksCompleted`` metric *and* will return the updated value of the metric:

.. code::

    POST /v2/customMetrics/tasksCompleted/data?returnValue=true
    {
      "value": "2"
    }

JSON Response:

.. code-block:: json

    {
      "value": 2.0,
      "date": "2017-07-13T00:00:00Z"
    }

Deleting a Custom Metric
------------------------

To delete a custom metric, use a query in the following format:

.. code::

    DELETE /v2/customMetrics/{metricName}

Or, alternatively, you can use the ID of the metric to get the same result:

.. code::

    DELETE /v2/customMetrics/{metricId}
