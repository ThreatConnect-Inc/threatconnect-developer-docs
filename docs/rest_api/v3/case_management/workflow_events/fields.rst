Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/workflowEvents`` endpoint, including the field’s name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/workflowEvents

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``workflowEvents`` object.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example value(s)
   * - caseId
     - The ID of the Case that contains the Event
     - Integer
     - TRUE*
     - FALSE
     - 1, 2, 3
   * - caseXid
     - The XID of the Case that contains the Event
     - String
     - TRUE*
     - FALSE
     - "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"
   * - eventDate
     - The date and time when the Event took place
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - notes
     - A list of Notes corresponding to the Event
     - `Note Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/notes/notes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"text": "Note for New Workflow Event"}]}
   * - summary
     - A summary of the Event
     - String
     - TRUE
     - TRUE
     - "badguy.com"