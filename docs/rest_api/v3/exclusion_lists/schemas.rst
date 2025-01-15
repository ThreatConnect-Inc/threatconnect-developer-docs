Schemas
-------

Request Body (POST)
~~~~~~~~~~~~~~~~~~~

The following is the request body schema for a POST request to the ``/v3/security/exclusionLists`` endpoint:

-  ``name``: <*String*> **REQUIRED** The Indicator Exclusion List's name. The name must be of the format ``Indicator-{exclusionListType}``, where ``{exclusionListType}`` is the type of Exclusion List you are creating. For owner-level Exclusion Lists, you can obtain a list of Exclusion List types by navigating to **Indicator Exclusions** tab on the **Organization Config** (for Organization-level Exclusion Lists), **Community Config** (for Community-level Exclusion Lists), or **Source Config** (for Source-level Exclusion Lists) screen in the ThreatConnect UI. For System-level Exclusion Lists, you can obtain a list of Exclusion List types by navigating to the **Indicators** tab on the **System Settings** screen in the ThreatConnect UI and selecting **Exclusion Rules** in the menu on this tab.
-  ``fixedValues``: <*Object*> **REQUIRED** The fixed Indicator values to add to the Indicator Exclusion List.
   -  ``data``: <*Array of Objects*> An array of fixed Indicator value objects.
      -  ``value``: <*String*> The fixed Indicator value (e.g., ``badguy@bad.com`` ).
-  ``variableValues``: <*Object*> **REQUIRED** The variable Indicator values to add to the Indicator Exclusion List.
   -  ``data``: <*Array of Objects*> An array of variable Indicator value objects.
      -  ``value``: <*String*> The variable Indicator value (e.g., ``*@bad.com``).
-  ``ownerId``: <*Integer*> The ID number of the owner to which the Indicator Exclusion List. If creating a System-level Indicator Exclusion List, do not include this field in the request body.

.. note::
   Include both the ``fixedValues`` and ``variableValues`` fields in the request body, regardless of whether each one contains Indicator values. Otherwise, the API may return a **500 - Internal Server Error** status code.

**Example**

.. code:: json

   {
       "name": "<string>",
       "fixedValues": {
           "data": [
               {
                   "value": "<string>"
               }
           ]
       },
       "variableValues": {
           "data": [
               {
                   "value": "<string>"
               }
           ]
       },
       "ownerId": 0,
   }

Request Body (PUT)
~~~~~~~~~~~~~~~~~~

The following is the request body schema for a PUT request to the ``/v3/security/exclusionLists`` endpoint:

-  ``fixedValues``: <*Object*> **REQUIRED** The fixed Indicator values to add to or remove from the Indicator Exclusion List.
   -  ``data``: <*Array of Objects*> An array of fixed Indicator value objects.
      -  ``value``: <*String*> The fixed Indicator value (e.g., ``badguy@bad.com`` ).
   -  ``mode``: <*String*> Specifies how to `update <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`__ the fixed Indicator values. (Acceptable values: **append**, **delete**, **replace**; Default value: **replace**)
-  ``variableValues``: <*Object*> **REQUIRED** The variable Indicator values to add to or remove from the Indicator Exclusion List.
   -  ``data``: <*Array of Objects*> An array of variable Indicator value objects.
      -  ``value``: <*String*> The variable Indicator value (e.g., ``*@bad.com``).
   -  ``mode``: <*String*> Specifies how to `update <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`__ the variable Indicator values. (Acceptable values: **append**, **delete**, **replace**; Default value: **replace**)

.. note::
   Include both the ``fixedValues`` and ``variableValues`` fields in the request body, regardless of whether each one contains Indicator values. Otherwise, the API may return a **500 - Internal Server Error** status code.

**Example**

.. code:: json

   {
       "fixedValues": {
           "data": [
               {
                   "value": "<string>"
               }
           ],
           "mode": "<string>"
       },
       "variableValues": {
           "data": [
               {
                   "value": "<string>"
               }
           ],
           "mode": "<string>"
       }
   }

Response Body
~~~~~~~~~~~~~

The default response returned for successful GET, POST, and PUT requests to the ``/v3/security/exclusionLists`` endpoint may include one or more objects with the following fields:

-  ``id``: <*Integer*> The Indicator Exclusion List's ID number.
-  ``owner``: <*String*> The name of the owner to which the Indicator Exclusion List applies. This field will be included only for owner-level Indicator Exclusion List objects.
-  ``ownerId``: <*Integer*> The ID number of the owner to which the Indicator Exclusion List applies. This field will be included only for owner-level Indicator Exclusion List objects.
-  ``name``: <*String*> The Indicator Exclusion List's name.
-  ``description``: <*String*> The Indicator Exclusion List's description.
-  ``active``: <*Boolean*> Specifies whether the Indicator Exclusion list is active.
-  ``managed``: <*Boolean*> Specifies whether the Indicator Exclusion List is a non-custom, default Exclusion List managed at the System level.

**Example**

.. code:: json

   {
       "id": 0,
       "owner": "<string>",
       "ownerId": 0,
       "name": "<string>",
       "description": "<string>",
       "active": true,
       "managed": true
   }