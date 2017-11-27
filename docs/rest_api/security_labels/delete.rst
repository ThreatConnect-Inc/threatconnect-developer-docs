Delete Security Labels
----------------------

To delete a Security Label, use the query format below:

.. code::

    DELETE /v2/securityLabels/{securityLabel}

For example, the following query will delete the ``TLP:Amber`` Security Label:

.. code::

    DELETE /v2/securityLabels/TLP:Amber

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

As you would likely expect, deleting a Security Label via the API removes that Security Label from all Groups, Indicators, and Victims which had the deleted Security Label.
