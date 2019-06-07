Add Security Labels to Data Imported Via Batch API
-------------------------------------------------- 

The platform supports adding Security Labels via Batch API.

Users can specify this JSON Response inside their Indicator or Group:

.. code:: json

    "securityLabel": [{
            "name": "TLP:GREEN",
        }],
The name can be any Security Label that already exists in the user's system. Users who wish to create a new Security Label (and have permission to do so), can provide the entire Label definition as follows:

.. code::

    "securityLabel": [{
               "name": "MyCustomLabel",
               "description": "A security label I just made up.",
               "color": "33FF00"
           }],

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

Deleting a Security Label via the API removes that Security Label from all Groups, Indicators, and Victims which had the deleted Security Label.
