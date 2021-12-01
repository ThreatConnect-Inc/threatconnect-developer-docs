Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/artifacts`` endpoint, including the field’s name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/artifacts

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.