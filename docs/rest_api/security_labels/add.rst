 Add Security Labels to Data Imported Via Batch API
 ----------------------

The platform supports adding Security Labels via Batch API.

Users can specify this JSON Response inside their Indicator or Group:

.. code:: json

    `"securityLabel": [{
            "name": "TLP:GREEN",
        }],

The name can be any Security Label that already exists in the user's system. Users who wish to create a new Security Label (and have permission to do so), can provide the entire label definition as follows:

.. code::

    `"securityLabel": [{`
               `"name": "MyCustomLabel",`
               `"description": "A security label I just made up.",`
               `"color": "33FF00"`
           `}],`
