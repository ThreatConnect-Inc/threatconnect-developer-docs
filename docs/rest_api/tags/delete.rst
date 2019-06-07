Delete Tags
-----------

To delete a Tag, use the query format below:

.. code::

    DELETE /v2/tags/{tagName}

For example, the following query will delete the ``Nation State`` Tag:

.. code::

    DELETE /v2/tags/Nation State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Deleting a Tag via the API removes that Tag from all Groups, Indicators, and Victims that had the deleted Tag.
