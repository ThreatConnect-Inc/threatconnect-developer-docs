Custom Metrics
==============

Custom metrics allow you to track data not available through other functionality in ThreatConnect. For example, you may want to know the number of times a particular Playbook was run. Data collected for custom metrics can be visualized on a `dashboard <https://knowledge.threatconnect.com/docs/dashboard>`_ with a User Metrics dashboard card.

Retrieving Custom Metrics
-------------------------

Retrieving All Custom Metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all custom metrics created in your Organization:

.. code::

    GET /v2/customMetrics

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "customMetricConfig": [
          {
            "id": 1,
            "name": "playbookRuns",
            "dataType": "Sum",
            "interval": "Hourly",
            "keyedValues": true,
            "description": "Monitor Playbook runs"
          },
          {
            "id": 2,
            "name": "tasksCompleted",
            "dataType": "Sum",
            "interval": "Daily",
            "keyedValues": false,
            "description": "Track the number of completed Tasks"
          }
        ]
      }
    }

Retrieving a Specific Custom Metric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific custom metric created in your Organization:

.. code::

    GET /v2/customMetrics/{metricName or metricId}

Creating a Custom Metric
------------------------

Send a request in the following format to create a custom metric:

.. code::

    POST /v2/customMetrics
    {
      "name": "<string>",
      "dataType": "<string>",
      "interval": "<string>",
      "keyedValues": <boolean>,
      "description": "<string>"
    }

- ``name``: <*String*> **REQUIRED** The metric's name. (Minimum value: **1**; Maximum value: **45**)
- ``dataType``: <*String*> **REQUIRED** The metric's data type. (Acceptable values: **Average**, **Count**, **First**, **Last**, **Max**, **Min**, **Sum**)
- ``interval``: <*String*> **REQUIRED** The time interval before the metric is reset, which starts on midnight of the day created for **Daily**, midnight of the first of the month for **Monthly**, and so forth. (Acceptable values: **Hourly**, **Daily**, **Weekly**, **Monthly**, **Yearly**)
- ``keyedValues``: <*Boolean*> Specifies whether the metric is a keyed metric. If this field is not included in the request body, a default value of **false** will be assigned to it, and the metric will be a non-keyed metric.
- ``description``: <*String*> The metric's description. (Minimum value: **1**; Maximum value: **500**)

For example, the following request will create a non-keyed metric named ``dailyOccurrenceCount``:

.. code::

  POST /v2/customMetrics
  {
    "name": "dailyOccurrenceCount",
    "description": "A daily count of occurrences",
    "dataType": "Sum",
    "interval": "Daily",
    "keyedValues": false
  }

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "customMetricConfig": {
          "id": 3,
          "name": "dailyOccurrenceCount",
          "dataType": "Sum",
          "interval": "Daily",
          "keyedValues": false,
          "description": "A daily count of occurrences"
        }
      }
    }

Creating Content in a Custom Metric
-----------------------------------

.. note::
    When passing a DateTime field into a request, use a timestamp in `ISO 8601 format <https://en.wikipedia.org/wiki/ISO_8601>`_ (e.g. ``2024-04-01T14:44:00Z``).

Creating Content in a Keyed Metric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to add content to a keyed metric:

.. code::

    POST /v2/customMetrics/{metricName}/data
    {
      "name": "<string>",
      "value": <int>,
      "date": "<datetime>",
      "weight": <int>
    }

- ``name``: <*String*> **REQUIRED** The name of the key associated with the metric.
- ``value``: <*Integer*> **REQUIRED** The value to add to the specified key. If the metric's data type is **Count**, then this field is not required.
- ``date``: <*DateTime*> The date and time when the provided value was added to the metric. If this field is not included in the request body, the default value will be today's date.
- ``weight``: <*Integer*> The weight of the provided value.


For example, the following request will add one to the value stored in the ``app1`` key in a ``playbookRuns`` metric:

.. code::

    POST /v2/customMetrics/playbookRuns/data
    {
      "name": "app1",
      "value": 1
    }

Creating Content in a Non-Keyed Metric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to 

.. code::

    POST /v2/customMetrics/{metricName}/data
    {
      "value": <int>,
      "date": "<datetime>",
      "weight": <int>
    }

- ``value``: <*Integer*> **REQUIRED** The value to add to the non-keyed metric. If the metric's data type is **Count**, then this field is not required.
- ``date``: <*DateTime*> The date and time when the provided value was added to the metric. If this field is not included in the request body, the default value will be today's date.
- ``weight``: <*Integer*> The weight of the provided value.

For example, the following request will add two to the count of a ``tasksCompleted`` metric and set the date that the value was added to April 9, 2024:

.. code::

    POST /v2/customMetrics/tasksCompleted/data
    {
      "value": 2,
      "date": "2024-04-09T14:44:00Z"
    }

Custom Metrics Return Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When content is successfully added to a custom metric, the API returns a 204 HTTP status code. To have the API return a 200 HTTP status code with the current value of the custom metric instead, use the ``returnValue`` query parameter and assign it a value of ``true``.

For example, the following query will increment the value of the ``tasksCompleted`` metric by two and return the current value of the metric in the API response:

.. code::

    POST /v2/customMetrics/tasksCompleted/data?returnValue=true
    {
      "value": 2
    }

JSON Response:

.. code-block:: json

    {
      "value": 4.0,
      "date": "2024-04-09T17:00:00Z"
    }

.. note::
    When the ``date`` field is included in a response, the minutes and seconds in the timestamp will be set to ``00``.

Deleting a Custom Metric
------------------------

Send a request in the following format to delete a custom metric:

.. code::

    DELETE /v2/customMetrics/{metricName or metricId}