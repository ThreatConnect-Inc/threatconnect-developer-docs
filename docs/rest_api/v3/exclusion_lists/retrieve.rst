Retrieve Indicator Exclusion Lists
----------------------------------

Requirements
^^^^^^^^^^^^

-  To view Indicator Exclusion Lists in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer.
-  To view Indicator Exclusion Lists in a Community or Source, your API user account must have a Community role of Editor or Director for that Community or Source.

Query Parameters
^^^^^^^^^^^^^^^^

The following table outlines **optional** query parameter(s) that may be used when sending a GET request to the ``/v3/security/exclusionLists`` endpoint.

.. list-table::
   :widths: 20 40 20 20
   :header-rows: 1

   * - Parameter
     - Description
     - Data Type
     - Default Value
   * - ``fields``
     - `Returns additional fields <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_ in the API response based on the specified value(s).
     - String
     - N/A
   * - ``owner``
     - Filters custom Indicator Exclusion Lists by `owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_. Note that default Indicator Exclusion Lists managed at the System-level will still be included in the response.
     - String
     - N/A
   * - ``resultLimit``
     - The maximum number of objects to include each `result set <https://docs.threatconnect.com/en/latest/rest_api/v3/enable_pagination.html>`_ within the API response.
     - Integer
     - 100
   * - ``resultStart``
     - The starting index of the `result set <https://docs.threatconnect.com/en/latest/rest_api/v3/enable_pagination.html>`_ within the API response.
     - Integer
     - 0
   * - ``sorting``
     - The order and field by which to `sort results <https://docs.threatconnect.com/en/latest/rest_api/v3/sort_results.html>`_ in the API response.
     - String
     - N/A
   * - ``tql``
     - `Filters results <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_ based on the provided ThreatConnect Query Language (TQL) query.
     - String
     - N/A

Retrieve All Indicator Exclusion Lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: http

   GET /v3/security/exclusionLists

Retrieve details about all Indicator Exclusion Lists in your owners and at the System level.

Example Request
"""""""""""""""

.. note::
   You must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`_.

**Request**

.. code:: http

   GET /v3/security/exclusionLists

**Response**

.. code:: json

   {
       "data": [
           {
               "id": 1,
               "name": "Indicator-ASN-AS Number",
               "description": "1058 fixed",
               "active": true,
               "managed": true
           },
           {
               "id": 2,
               "name": "Indicator-Address-IPv4",
               "description": "106 fixed, 42 variable",
               "active": true,
               "managed": true
           },
           ...
           {
               "id": 32,
               "owner": "CAL Automated Threat Library",
               "ownerId": 22,
               "name": "Indicator-Host",
               "description": "1 fixed",
               "active": true,
               "managed": false
           },
           {
               "id": 33,
               "name": "Indicator-File-SHA256",
               "description": "1 fixed",
               "active": true,
               "managed": false
           }
       ],
       "status": "Success"
   }

Retrieve a Specific Indicator Exclusion List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: http

   GET /v3/security/exclusionLists/{id}

Retrieve details about a specific Indicator Exclusion List.

Example Request
"""""""""""""""

.. note::
   You must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`_.

**Request**

.. code:: http

   GET /v3/security/exclusionLists/30

**Response**

.. code:: json

   {
       "data": {
           "id": 30,
           "owner": "Demo Organization",
           "ownerId": 1,
           "name": "Address-IPv6",
           "description": "1 fixed, 1 variable",
           "active": true,
           "managed": false
       },
       "status": "Success"
   }

To include the Indicator values on an Indicator Exclusion List, use the ``fields`` query parameter in the request and assign it a value of ``values``:

**Request**

.. code:: http

   GET /v3/security/exclusionLists/30?fields=values

**Response**

.. code:: json

   {
       "data": {
           "id": 30,
           "owner": "Demo Organization",
           "ownerId": 1,
           "name": "Address-IPv6",
           "description": "1 fixed, 1 variable",
           "fixedValues": {
               "data": [
                   {
                       "value": "2001:500:12::d0d"
                   }
               ],
               "count": 1
           },
           "variableValues": {
               "data": [
                   {
                       "value": "100::/64"
                   }
               ],
               "count": 1
           },
           "active": true,
           "managed": false
       },
       "status": "Success"
   }