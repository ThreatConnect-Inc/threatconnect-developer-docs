Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_that may be included in responses returned from the ``/v3/job/executions`` endpoint, which is a **read-only** endpoint:

.. code::

    OPTIONS /v3/job/executions?show=readonly

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/job/executions`` endpoint:

.. code::

    OPTIONS /v3/job/executions/tql

.. hint::
    See the `"Retrieve Job Executions Completed During a Specific Time Range" <#retrieve-job-executions-completed-during-a-specific-time-range>`_ and `"Retrieve Executions for a Specific Job" <#retrieve-executions-for-a-specific-job>`_ sections for example use cases of the ``tql`` query parameter.