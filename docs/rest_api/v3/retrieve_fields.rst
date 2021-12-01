Retrieve a List of Available Fields for an Object
-------------------------------------------------

To retrieve a list of available fields for an object, including the field's name, description, and accepted data type, use a query in the following format:

.. code::

    OPTIONS /v3/{objectType}

By default, this request will return a list of fields that can be included in a POST and/or PUT request. To retrieve a list of all fields for an object, including read-only fields, include the ``?show=readonly`` query parameter in your query.

.. code::
    
    OPTIONS/v3/{objectType}?show=readonly