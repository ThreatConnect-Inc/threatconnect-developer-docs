Endpoint Options
----------------

Available Request Body Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available request body fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that you can use in a POST or PUT request to the ``/v3/security/exclusionLists`` endpoint:

**Request**

.. code:: http

   OPTIONS /v3/security/exclusionLists

.. hint::

   To include read-only fields in the API response, use the ``show`` query parameter and assign it a value of ``readonly``.

Filter Results With TQL
^^^^^^^^^^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can assign to the ``tql`` query parameter when using it in a request to the ``/v3/security/exclusionLists`` endpoint:

**Request**

.. code:: http

   OPTIONS /v3/security/exclusionLists/tql