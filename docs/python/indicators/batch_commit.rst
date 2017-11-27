Batch Commit
------------

As demonstrated by the code snippet below, the ThreatConnect Python SDK supports adding indicators in bulk to the ThreatConnect platform.

The code snippet below assumes that indicator data is formatted in the same way as the JSON `used by the API <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#batch-indicator-input-file-format>`_ .

.. code-block:: python

    import json
    import time

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    # define the owner where you would like to put the data
    dst_owner = 'Example Community'

    dst_tc = ThreatConnect(api_access_id, api_secret_key, dst_owner, api_base_url)

    #
    # populate 'indicators' list of dictionaries as formatted here:
    # https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#batch-indicator-input-file-format
    #
    indicators = [
        {
            'rating': 3,
            'confidence': 75,
            'description': 'Malicious domain',
            'summary': 'example.com',
            'type': 'Host',
            'associatedGroup': [12345, 54321],
            'attribute': [
                {
                    'type': 'Source',
                    'value': 'SEIM log - 13/01/2017"
                }
            ],
            'tag': [
                {
                    'name': 'MyTag"
                }
            ]
        }
    ]

    # time (in seconds) to wait before checking the status of a batch job
    poll_time = 5

    batch_job_ids = []

    # instantiate a Batch Jobs Object
    batch_jobs = dst_tc.batch_jobs()

    # add a new Batch Job
    batch_job = batch_jobs.add()

    # configure the Batch Job
    batch_job.set_halt_on_error(False)             # if True, abort processing after first error
    batch_job.set_attribute_write_type('Replace')  # replace attributes (can also be Append)
    batch_job.set_action('Create')                 # create indicators (can also be Delete) 
    batch_job.set_owner(dst_owner)                 # owner to write indicators to

    # set the indicators to be uploaded in this Batch Job
    batch_job.upload(json.dumps(indicators))

    try:
        # commit the Batch Job
        batch_job.commit()
        print('Created batchjob %s' % batch_job.id)
        batch_job_ids.append(batch_job.id)
    except RuntimeError as e:
        print('Error creating Batch Job: {}'.format(e))
        sys.exit(1)

    finished_batches = []
    total_time = 0

    # iterate through the Batch Jobs that have been started and see if they have finished
    while len(batch_job_ids) > 0:
        # sleep for the poll_time
        time.sleep(poll_time)
        total_time += poll_time
        print('polling (total wait time {0} seconds)'.format(int(total_time)))

        # retrieve all of the Batch Jobs
        batch_jobs = dst_tc.batch_jobs()

        for batchId in batch_job_ids:
            # create a filter to find only the Batch Job that we are monitoring
            filter = batch_jobs.add_filter()
            filter.add_id(batchId)

            # retrieve the desired Batch Job that we are monitoring
            batch_jobs.retrieve()

            # iterate through the Batch Jobs (there will only be one)
            for batch_job in batch_jobs:
                # if the Batch Job is done, print the details of the Batch Job
                if batch_job.status == 'Completed':
                    finished_batches.append(batch_job)
                    batch_job_ids.remove(batchId)
                    print('Finished batch job {0}: succeeded: {1}, "
                          'failed: {2}, unprocessed: {3}'.format(batchId, batch_job.success_count, batch_job.error_count, batch_job.unprocess_count))

    # now that all of the Batch Jobs have finished, get some statistics on them
    success_total = 0
    error_total = 0
    unprocess_total = 0

    # record statistics based on the Batch Jobs
    for batch_job in finished_batches:
        # record success count
        if batch_job.success_count:
            success_total += batch_job.success_count

        # record unprocessed count
        if batch_job.unprocess_count:
            unprocess_total += batch_job.unprocess_count

        # record error count
        if batch_job.error_count:
            error_total += batch_job.error_count

            # print some more details about the errors
            batch_job.download_errors()
            for error in batch_job.errors:
                print('Batch Job {0} errors: {1}'.format(batch_job.id, batch_job.errors))

    # print the final statistics of the Batch Jobs
    print('All batch jobs completed, totals:  "
          'succeeded: {0}, failed: {1}, unprocessed: {2}'.format(success_total, error_total, unprocess_total))

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
