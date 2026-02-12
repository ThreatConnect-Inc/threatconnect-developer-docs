Endpoint Options
----------------

Available Request Body Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available request body fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that you can use in a POST or PUT request to the ``/v3/posts`` endpoint:

**Request**

.. code:: http

   OPTIONS /v3/posts

.. hint::

   To include read-only fields in the API response, use the ``show`` query parameter and assign it a value of ``readonly``.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/posts`` endpoint:

.. code::

    OPTIONS /v3/posts/fields

Filter Results With TQL
^^^^^^^^^^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can assign to the ``tql`` query parameter when using it in a request to the ``/v3/posts`` endpoint:

**Request**

.. code:: http

   OPTIONS /v3/posts/tql