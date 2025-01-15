Delete Indicator Exclusion Lists
--------------------------------

.. code:: http

   DELETE /v3/security/exclusionLists/{id}

Delete a specific custom Indicator Exclusion List.

.. attention::
   You cannot delete default Indicator Exclusion Lists (that is, Indicator Exclusion Lists for which ``managed`` is ``true``).

Requirements
^^^^^^^^^^^^

-  To delete custom Indicator Exclusion Lists in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer.
-  To delete custom Indicator Exclusion Lists in a Community or Source, your API user account must have a Community role of Editor or Director for that Community or Source.
-  To delete custom Indicator Exclusion Lists at the System, Community, or Source level, your API user account's ID number must be entered into the **systemExclusionListApiAccess** system setting on the **System Settings** screen in the ThreatConnect UI (must be a System Administrator to perform this action). For instruction on retrieving an API user account's ID number, see `Users Overview <https://docs.threatconnect.com/en/latest/rest_api/v3/users/users.html>`__.

Example Request
^^^^^^^^^^^^^^^

.. note::
   You must include the required authentication headers for the method you are using to `authenticate your API request <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#id1>`__.

**Request**

.. code:: http

   DELETE /v3/security/exclusionLists/30

**Response**

.. code:: json

   {
       "message": "Deleted",
       "status": "Success"
   }