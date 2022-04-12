Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/notes`` endpoint, including each field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/notes

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request for the ``notes`` object.

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - artifactId
     - The ID of the Artifact to which the Note will be applied
     - Integer
     - FALSE
     - FALSE
   * - caseId
     - The ID of the Case to which the Note will be applied
     - Integer
     - TRUE*
     - FALSE
   * - caseXid
     - The XID of the Case to which the Note will be applied
     - String
     - TRUE*
     - FALSE
   * - taskId
     - The ID of the Task to which the Note will be applied
     - Integer
     - FALSE
     - FALSE
   * - taskXid
     - The XID of the Task to which the Note will be applied
     - String
     - FALSE
     - FALSE
   * - text
     - The contents of the Note
     - String
     - TRUE
     - TRUE
   * - workflowEventId
     - The ID of the Workflow Event to which the Note will be applied
     - Integer
     - FALSE
     - FALSE

.. note::
    \*When creating a Note, either ``caseId`` or ``caseXid`` must be included in the body of the POST request. Only one needs to be included in the body of the POST request, but both can be included, if desired.