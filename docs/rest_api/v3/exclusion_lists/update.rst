Update Indicator Exclusion Lists
--------------------------------

.. code:: http

   PUT /v3/security/exclusionLists/{id}

Update the contents of a specific custom Indicator Exclusion List.

Requirements
^^^^^^^^^^^^

-  To update custom Indicator Exclusion Lists in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer.
-  To update custom Indicator Exclusion Lists in a Community or Source, your API user account must have a Community role of Editor or Director for that Community or Source.
-  To update custom Indicator Exclusion Lists at the System, Community, or Source level, your API user account's ID number must be entered into the **systemExclusionListApiAccess** system setting on the **System Settings** screen in the ThreatConnect UI (must be a System Administrator to perform this action). For instruction on retrieving an API user account's ID number, see `Users Overview <https://docs.threatconnect.com/en/latest/rest_api/v3/users/users.html>`__.

Query Parameters
^^^^^^^^^^^^^^^^

The following table outlines **optional** query parameter(s) that may be used when sending a PUT request to the ``/v3/security/exclusionLists`` endpoint.

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

Example Request
^^^^^^^^^^^^^^^

.. note::
   In addition to the required ``Content-Type`` header, you must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`__.

**Request**

.. code:: http

   PUT /v3/security/exclusionLists/30
   Content-Type: application/json

   {
       "fixedValues": {
           "data": [
               {
                   "value": "2001:500:1::53"
               }
           ],
           "mode": "append"
       },
       "variableValues": {
           "data": [
               {
                   "value": "100::/64"
               }
           ],
           "mode": "delete"
       }
   }

**Response**

.. code:: json

   {
       "data": {
           "id": 30,
           "owner": "Demo Organization",
           "ownerId": 1,
           "name": "Indicator-Address-IPv6",
           "description": "2 fixed",
           "active": true,
           "managed": false
       },
       "message": "Updated",
       "status": "Success"
   }