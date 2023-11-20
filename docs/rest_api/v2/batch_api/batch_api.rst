=========
Batch API
=========

Overview
--------

The Batch API allows you to create and modify threat intelligence data in bulk. Currently, there are two versions of the Batch API: V1 and V2. The V1 Batch API supports Indicators only, whereas the V2 Batch API supports Indicators and Groups. Using the Batch API will improve performance when importing large amounts of data.

After you create a batch job, you can upload a JSON file containing the objects to be created or modified to the Batch API and trigger the batch job that will process the data in the file. The contents of the uploaded file must contain valid JSON and mimic the data structure of a `JSON bulk report file <https://docs.threatconnect.com/en/latest/rest_api/v2/indicators/indicators.html#json-bulk-reports>`_.

Prerequisites
-------------

To use the Batch API, the following prerequisites must be met:

* Batch API must be enabled on your ThreatConnect instance
* Document storage must be enabled on your ThreatConnect instance
* To create batch jobs in and upload data to an Organization, your API user account must have an Organization role of Standard User or higher
* To create batch jobs in and upload data to a Community or Source, your API user account must have a Community role of Editor or higher

.. include:: v2_batch_api.rst

.. include:: v1_batch_api.rst