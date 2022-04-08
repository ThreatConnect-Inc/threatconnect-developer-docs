Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/artifacts`` endpoint, including the field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/artifacts

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``artifacts`` object.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example value(s)
   * - associatedGroups
     - A list of Groups associated to the Artifact
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - {"data": [{"id": 12345}]}, {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - associatedIndicators
     - A list of Indicators associated to the Artifact
     - `Indicator Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_
     - FALSE
     - TRUE
     - {"data": [{"id": 12345}]}, {"data": [{"hostName":"badguy.com", "type": "Host"}]}
   * - caseId
     - The ID of the Case that contains the Artifact
     - Integer
     - TRUE*
     - FALSE
     - 1, 2, 3
   * - caseXid
     - The XID of the Case that contains the Artifact
     - String
     - TRUE*
     - FALSE
     - "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"
   * - derivedLink
     - Specifies whether the Artifact should be used to potentially associate Cases
     - Boolean
     - FALSE
     - TRUE
     - true, false
   * - fieldName
     - The name of the Artifact Field within a corresponding Task
     - String
     - FALSE
     - TRUE
     - "Sender Address"
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
     - A list of Notes corresponding to the Artifact
     - `Note Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/notes/notes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"text": "Note about malware case"}]}
   * - source
     - The name of the user who added the Artifact to the Case
     - String
     - FALSE
     - TRUE
     - "jsmith"
   * - summary
     - The data contained in the Artifact
     - String
     - TRUE
     - TRUE
     - "badguy.com"
   * - taskId
     - The ID of the Task corresponding to the Artifact
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3
   * - taskXid
     - The XID of the Task corresponding to the Artifact
     - String
     - FALSE
     - FALSE
     - "d7dafb59-bf74-46fe-bf18-8da14cc59219"
   * - type
     - The Artifact's data type
     - String
     - TRUE
     - FALSE
     - "URL"

.. note::
    \*When creating an Artifact, either ``caseId`` or ``caseXid`` must be included in the body of the POST request. Only one needs to be included in the body of the POST request, but both can be included, if desired.

.. note::
    To view a list of available Artifact data types, use the following query and refer to the ``type`` field:
    
    ``OPTIONS /v3/artifacts/``
    
    Alternatively, refer to `Artifact Types <../artifact_types/artifact_types.html>`_ for instructions on retrieving available Artifact types.

.. note::
    To **associate an existing Group** to an Artifact, use the Group's ID when setting the ``associatedGroups`` field (e.g., ``{"data": [{"id": 12345}]}``). To **associate an existing Indicator** to an Artifact, use either the Indicator's ID, or the Indicator's type and summary (e.g., for a Host Indicator, use its ``hostName``), when setting the ``associatedIndicators`` field.