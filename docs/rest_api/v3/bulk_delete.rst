Delete Case Objects in Bulk
---------------------------

If your System Administrator enabled bulk deletion operations for ThreatConnect v3 API, you can delete Artifacts, Cases, Notes, Workflow Tasks, and Workflow Events (i.e., Timeline Events) in bulk by sending a request in the following format:

.. code::

    DELETE /v3/{caseObjectType}

If desired, you can filter objects to be deleted by appending ``?tql=`` followed by a `ThreatConnect Query Language (TQL) <https://knowledge.threatconnect.com/docs/threatconnect-query-language-tql>`__ string to your request. For example, the following request will delete all Notes created between January 1 and 8, 2023, inclusive. Note that the TQL string included in the request URL for this example **is not encoded**.

.. code::

    DELETE /v3/notes?tql=dateAdded GEQ "2023-01-01" and dateAdded LEQ "2023-01-08"

.. note::
    Depending on the tool you are using to interact with the ThreatConnect API, it may be necessary to encode the URL in your request manually if it includes query parameters. For example, some tools may accept ``/v3/notes?tql=dateAdded GEQ "2023-01-01" and dateAdded LEQ "2023-01-08"`` as a valid request URL and encode it automatically, while others may require you to encode the request's URL manually. If you send a request with query parameters and a 401 Unauthorized error is returned, verify whether the URL in your request is encoded properly for the API tool you are using.