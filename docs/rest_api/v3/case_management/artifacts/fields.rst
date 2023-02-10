Available Fields
----------------

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including the field's name, description, and accepted data type, for the ``/v3/artifacts`` endpoint:

.. code::

    OPTIONS /v3/artifacts

.. hint::
    To include read-only fields in the response, append the ``?show=readonly`` query parameter to the OPTIONS request.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/artifacts`` endpoint.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - associatedGroups
     - A list of Groups associated to the Artifact
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - associatedIndicators
     - A list of Indicators associated to the Artifact
     - `Indicator Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"hostName":"badguy.com", "type": "Host"}]}
   * - caseId
     - The ID of the Case to which the Artifact belongs
     - Integer
     - TRUE [1]_
     - FALSE
     - 1, 2, 3
   * - caseXid
     - The XID of the Case to which the Artifact belongs
     - String
     - TRUE [1]_
     - FALSE
     - "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"
   * - derivedLink
     - Specifies whether the Artifact should be used to potentially associate Cases
     - Boolean
     - FALSE
     - TRUE
     - true, false
   * - fieldName [2]_
     - The name of the Task Artifact Field to which the Artifact corresponds
     - String
     - FALSE
     - TRUE
     - "senderAddress"
   * - fileData
     - Base64-encoded file attachment (required only for certain Artifact types)
     - String
     - FALSE
     - TRUE
     -  "UEsDBBQABgAIAA..."
   * - hashCode
     - The hash code of File-type Artifacts
     - String
     - FALSE
     - TRUE
     - "C254ZZjosDoUA2B..."
   * - notes
     - A list of Notes added to the Artifact
     - `Note Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/notes/notes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"text": "This IP address is malicious."}]}
   * - source
     - The name of the user who added the Artifact to the Case
     - String
     - FALSE
     - TRUE
     - "jsmith"
   * - summary
     - The summary (i.e., name) of the Artifact
     - String
     - TRUE
     - TRUE
     - "badguy.com"
   * - taskId
     - The ID of the Task to which the Artifact belongs
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3
   * - taskXid
     - The XID of the Task to which the Artifact belongs
     - String
     - FALSE
     - FALSE
     - "d7dafb59-bf74-46fe-bf18-8da14cc59219"
   * - type [3]_
     - The Artifact's type
     - String
     - TRUE
     - FALSE
     - "URL"

.. [1] When adding an Artifact to a Case, you must include either the ``caseId`` or ``caseXid`` field in the body of the POST request. Only one needs to be included in the body of the POST request, but both can be included, if desired.

.. [2] To retrieve the name of a Task's Artifact Field(s), send a request in the following format and review the ``name`` field for each Artifact Field contained within the ``configTask`` object in the response: ``GET /v3/tasks/{taskId}``.

.. [3] To retrieve a list of available Artifact types, send the following request and review the ``type`` field in the response: ``OPTIONS /v3/artifacts``. You can also retrieve a list of available Artifact types by sending the following request: ``GET /v3/artifactTypes``.

.. note::
    If adding an Artifact to a Task, you do not need to specify the ID of the Case to which the Task belongs in your request. You only need to specify the ID or XID of the Task to which the Artifact will be added.