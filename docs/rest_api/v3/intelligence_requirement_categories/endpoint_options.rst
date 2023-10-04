Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to retrieve a complete list of fields that may be included in responses returned from the ``/v3/intelRequirements/categories`` endpoint, which is a **read-only endpoint**:

.. code::

    OPTIONS /v3/intelRequirements/categories?show=readonly

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/intelRequirements/categories`` endpoint:

.. code::

    OPTIONS /v3/intelRequirements/categories/tql