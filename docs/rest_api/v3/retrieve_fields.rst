Retrieve a List of Available Fields for an Object
-------------------------------------------------

Send a request in the following format to retrieve a list of available fields, including the field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the specified object's endpoint:

.. code::

    OPTIONS /v3/{objectType}

By default, the API response will not include read-only fields for the object's endpoint. To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

.. code::
    
    OPTIONS /v3/{objectType}?show=readonly
