Delete Tags
-----------

To delete a tag, use the query format below:

.. code::

    DELETE /v2/tags/{tagName}

For example, the following query will delete the ``Nation State`` tag:

.. code::

    DELETE /v2/tags/Nation State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

As you would likely expect, deleting a Tag via the API removes that Tag from all Groups, Indicators, and Victims which had the deleted Tag.
