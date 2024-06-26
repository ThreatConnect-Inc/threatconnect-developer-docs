Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ that may be included in responses returned from the ``/v3/playbook/executions`` endpoint, which is a **read-only** endpoint:

.. code::

    OPTIONS /v3/playbook/executions?show=readonly

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/playbook/executions`` endpoint:

.. code::

    OPTIONS /v3/playbook/executions/tql

.. hint::
    See the `"Retrieve Playbook Executions Completed During a Specific Time Range" <#id1>`_ and `"Retrieve Executions for a Specific Playbook" <#id2>`_ sections for example use cases of the ``tql`` query parameter.