Batch Commit
------------

Python SDK Batch Commit Code Sample:

.. code-block:: python
    :linenos:

    ...

    dst_tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    #
    # populate 'indicators' list of dictionaries
    #

    batch_job_ids = []
    batch_jobs = dst_tc.batch_jobs()
    batch_job = batch_jobs.add()

    batch_job.set_halt_on_error(False)             # If True, abort processing after first error
    batch_job.set_attribute_write_type('Replace')  # Replace attributes (can also be Append)
    batch_job.set_action('Create')                 # Create indicators (can also be Delete) 
    batch_job.set_owner(dst_owner)                 # Owner to write indicators to

    batch_job.upload(json.dumps(indicators))

    try:
        batch_job.commit()
        print("Created batchjob %s" % batch_job.id)
        batch_job_ids.append(batch_job.id)
    except RuntimeError as re:
        print("Encountered problem creating batchJob")
        traceback.print_exc(file=sys.stderr)

    finished_batches = []
    total_time = 0 
    while len(batch_job_ids) > 0:
        time.sleep(args.poll_time)
        total_time += args.poll_time
        print("polling (total wait time {0} minutes)".format(int(total_time / 60)))
                     
        batch_jobs = dst_tc.batch_jobs()
        for batchId in batch_job_ids:
            filter = batch_jobs.add_filter()
            filter.add_id(batchId)
            batch_jobs.retrieve()

            for batch_job in batch_jobs:
                if batch_job.status == 'Completed':
                    finished_batches.append(batch_job)
                    batch_job_ids.remove(batchId)
                    print("Finished batch job {0}: succeeded: {1}, "
                          "failed: {2}, unprocessed: {3}".format(batchId, batch_job.success_count, batch_job.error_count, batch_job.unprocess_count))

    success_total = 0
    error_total = 0
    unprocess_total = 0
    for batch_job in finished_batches:
        if batch_job.unprocess_count:
            success_total += batch_job.success_count
        if batch_job.unprocess_count:
            unprocess_total += batch_job.unprocess_count
        if batch_job.unprocess_count:
            error_total += batch_job.error_count
            batch_job.download_errors()
            for error in batch_job.errors:
                print("Batch Job {0} errors: {1}".format(batch_job.id, batch_job.errors))
    print("All batch jobs completed, totals:  "
          "succeeded: {0}, failed: {1}, unprocessed: {2}".format(success_total, error_total, unprocess_total))

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

The ThreatConnect platform supports adding indicators in bulk using the
API. The Python SDK features an easy-to-use interface to assist in rapid
development of software to manage this data.

These API calls assume that indicator data is formatted in `JSON, specifically a list of dictionaries <../rest_api/rest_api_docs.html#batch-indicator-input-file-format>`_.

Adding Batch Resources
^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to use a Batch Resource in the
ThreatConnect platform. The Batch Resource has a few methods to support
batch configuration before uploading a batch Indicator file to the
platform. For more information on the purpose of each line of code, see
the **Code Highlights** section below.

**Supported Functions and Properties**

+--------------------------+-------------------------------+------------+-------------------------+
| Property Name            | Method                        | Required   | Allowable Values        |
+==========================+===============================+============+=========================+
| halt\_on\_error          | set\_halt\_on\_error          | True       | True, False             |
+--------------------------+-------------------------------+------------+-------------------------+
| attribute\_write\_type   | set\_attribute\_write\_type   | True       | Replace, Append         |
+--------------------------+-------------------------------+------------+-------------------------+
| action                   | set\_action                   | True       | Create, Delete          |
+--------------------------+-------------------------------+------------+-------------------------+
| owner                    | set\_owner                    | True       | Any Owner               |
+--------------------------+-------------------------------+------------+-------------------------+
| --                       | upload                        | True       | Indicator JSON String   |
+--------------------------+-------------------------------+------------+-------------------------+

**Code Highlights**

+----------------------------------------------+---------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                     |
+==============================================+=================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                           |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_jobs = dst_tc.batch_jobs()``         | Instantiate a Batch Job container object.                                       |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``for batch in indicators:``                 | Iterator through an array of arrays of indicator objects.                       |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_job.set_...``                        | Configure batch job to process as many indicators as possible without aborting. |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_job.upload(json.dumps(batch))``      | Upload job with indicator chunk as JSON data.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_job.commit()``                       | Start batch job with configuration and data defined.                            |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``while len(batch_ids) > 0:``                | Begin polling for batch status until all pending batches are complete.          |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``filter.add_id(batchId)``                   | Add current batchId to filter.                                                  |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``for batch_job in batch_jobs:``             | Get job for filtered batch ID.                                                  |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``if batch_job.status == 'Completed':``      | Check job status completion.                                                    |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``for batch_job in finished_batches:``       | Iterate through the finished batches for status print.                          |
+----------------------------------------------+---------------------------------------------------------------------------------+
