Delete Indicators
-----------------

The basic format for deleting an Indicator is:

.. code::

    DELETE /v3/indicators/{indicatorId or indicatorSummary}

For example, the following query will delete the Indicator with ID 3:

.. code::

    DELETE /v3/indicators/3

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

The same response would be returned if we used the following request, where the Indicator ID is replaced with the Indicator’s summary:

.. code::

    DELETE /v3/indicators/badguy.com