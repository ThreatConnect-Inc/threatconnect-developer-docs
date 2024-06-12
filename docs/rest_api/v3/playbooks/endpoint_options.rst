Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_that may be included in responses returned from the ``/v3/playbooks`` endpoint, which is a **read-only** endpoint:

.. code::

    OPTIONS /v3/playbooks?show=readonly

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/playbooks`` endpoint:

.. code::

    OPTIONS /v3/playbooks/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/playbooks`` endpoint:

.. code::

    OPTIONS /v3/playbooks/tql

.. hint::
    See the `"Retrieve a Specific Playbook" <#retrieve-a-specific-playbook>`_ section for example use cases of the ``tql`` query parameter.