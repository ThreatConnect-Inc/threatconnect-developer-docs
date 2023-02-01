Delete Indicators
-----------------

Send a request in the following format to delete an Indicator:

.. code::

    DELETE /v3/indicators/{indicatorId or indicatorSummary}

For example, the following request will delete the Indicator whose ID is 3:

.. code::

    DELETE /v3/indicators/3

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

The same response will be returned for the following request, where the Indicator's ID is replaced with its summary:

.. code::

    DELETE /v3/indicators/badguy.com

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }