Retrieve Owner Metrics
----------------------

To get some metrics for an Owner, you can use the Metrics Branch as formatted below:

.. code::

    GET /v2/owners/{ownerId}/metrics

Here is an example query:

.. code::

    GET /v2/owners/1/metrics

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "ownerMetric": [
          {
            "metricDate": "2017-06-19",
            "totalIndicator": 4,
            "totalHost": 0,
            "totalAddress": 1,
            "totalEmailAddress": 1,
            "totalFile": 1,
            "totalUrl": 1,
            "totalGroup": 8,
            "totalThreat": 2,
            "totalIncident": 2,
            "totalEmail": 0,
            "totalCampaign": 1,
            "totalAdversary": 1,
            "totalSignature": 1,
            "totalTask": 30,
            "totalDocument": 1,
            "totalTag": 7,
            "totalTrack": 0,
            "totalResult": 0,
            "totalIndicatorAttribute": 18,
            "totalGroupAttribute": 54,
            "averageIndicatorRating": 2.5,
            "averageIndicatorConfidence": 75.0,
            "totalEnrichedIndicator": 9,
            "totalGroupIndicator": 6,
            "totalObservationDaily": 0,
            "totalObservationIndicator": 0,
            "totalObservationAddress": 0,
            "totalObservationEmailAddress": 0,
            "totalObservationFile": 0,
            "totalObservationHost": 0,
            "totalObservationUrl": 0,
            "totalFalsePositiveDaily": 0,
            "totalFalsePositive": 2
          },
          {
            "metricDate": "2017-06-20",
            "totalIndicator": 4,
            "totalHost": 0,
            "totalAddress": 1,
            "totalEmailAddress": 1,
            "totalFile": 1,
            "totalUrl": 1,
            "totalGroup": 8,
            "totalThreat": 2,
            "totalIncident": 2,
            "totalEmail": 0,
            "totalCampaign": 1,
            "totalAdversary": 1,
            "totalSignature": 1,
            "totalTask": 30,
            "totalDocument": 1,
            "totalTag": 7,
            "totalTrack": 0,
            "totalResult": 0,
            "totalIndicatorAttribute": 18,
            "totalGroupAttribute": 54,
            "averageIndicatorRating": 2.5,
            "averageIndicatorConfidence": 75.0,
            "totalEnrichedIndicator": 9,
            "totalGroupIndicator": 6,
            "totalObservationDaily": 0,
            "totalObservationIndicator": 0,
            "totalObservationAddress": 0,
            "totalObservationEmailAddress": 0,
            "totalObservationFile": 0,
            "totalObservationHost": 0,
            "totalObservationUrl": 0,
            "totalFalsePositiveDaily": 0,
            "totalFalsePositive": 2
          },
          ...
          # Data for 2017-06-21 through 2017-07-16
          ...
          {
            "metricDate": "2017-07-17",
            "totalIndicator": 1,
            "totalHost": 0,
            "totalAddress": 0,
            "totalEmailAddress": 0,
            "totalFile": 1,
            "totalUrl": 0,
            "totalGroup": 5,
            "totalThreat": 0,
            "totalIncident": 2,
            "totalEmail": 0,
            "totalCampaign": 0,
            "totalAdversary": 2,
            "totalSignature": 0,
            "totalTask": 7,
            "totalDocument": 1,
            "totalTag": 8,
            "totalTrack": 0,
            "totalResult": 0,
            "totalIndicatorAttribute": 2,
            "totalGroupAttribute": 10,
            "averageIndicatorRating": 2.5,
            "averageIndicatorConfidence": 75.0,
            "totalEnrichedIndicator": 1,
            "totalGroupIndicator": 1,
            "totalObservationDaily": 0,
            "totalObservationIndicator": 0,
            "totalObservationAddress": 0,
            "totalObservationEmailAddress": 0,
            "totalObservationFile": 0,
            "totalObservationHost": 0,
            "totalObservationUrl": 0,
            "totalFalsePositiveDaily": 0,
            "totalFalsePositive": 0
          },
          {
            "metricDate": "2017-07-18",
            "totalIndicator": 1,
            "totalHost": 0,
            "totalAddress": 0,
            "totalEmailAddress": 0,
            "totalFile": 1,
            "totalUrl": 0,
            "totalGroup": 5,
            "totalThreat": 0,
            "totalIncident": 2,
            "totalEmail": 0,
            "totalCampaign": 0,
            "totalAdversary": 2,
            "totalSignature": 0,
            "totalTask": 7,
            "totalDocument": 1,
            "totalTag": 8,
            "totalTrack": 0,
            "totalResult": 0,
            "totalIndicatorAttribute": 2,
            "totalGroupAttribute": 10,
            "averageIndicatorRating": 2.5,
            "averageIndicatorConfidence": 75.0,
            "totalEnrichedIndicator": 1,
            "totalGroupIndicator": 1,
            "totalObservationDaily": 0,
            "totalObservationIndicator": 0,
            "totalObservationAddress": 0,
            "totalObservationEmailAddress": 0,
            "totalObservationFile": 0,
            "totalObservationHost": 0,
            "totalObservationUrl": 0,
            "totalFalsePositiveDaily": 0,
            "totalFalsePositive": 0
          }
        ]
      }
    }

The Metrics Branch returns data for every day for the past 30 days.
