File Occurrences
----------------

Create a File Occurrence
^^^^^^^^^^^^^^^^^^^^^^^^

The following table outlines the fields available when creating File Occurrences for a File Indicator.

.. list-table::
   :widths: 20 35 20 25
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
   * - date
     - The date and time of the File Occurrence
     - Date
     - FALSE*
   * - fileName
     - The name of the file corresponding to the File Occurrence
     - String
     - FALSE*
   * - path
     - The run path for the file corresponding to the File Occurrence
     - String
     - FALSE*

.. note::
    \*While none of these fields are required, you must include at least one of them to create a File Occurrence.

In the following example, the query will add a File Occurrence to the existing File Indicator with ID ``20``:

.. code::

    PUT /v3/indicators/20

    {
        "fileOccurrences": {
            "data": [
                {
                    "fileName": "win999301.dll",
                    "path": "C:\\\\Windows\\System",
                    "date": "2022-06-14T10:00:00Z"
                }
            ]
        }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 20,
            "ownerName": "Demo Organization",
            "dateAdded": "2022-06-14T13:59:54Z",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=9D67E81C18101FC266057CD7851604B8",
            "tags": {},
            "securityLabels": {},
            "type": "File",
            "lastModified": "2022-06-14T14:00:11Z",
            "summary": "9D67E81C18101FC266057CD7851604B8",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {},
            "associatedIndicators": {},
            "fileActions": {
                "count": 0
            },
            "attributes": {},
            "associatedCases": {},
            "associatedArtifacts": {},
            "md5": "9D67E81C18101FC266057CD7851604B8"
        },
        "message": "Updated",
        "status": "Success"
    }

By default, the fileOccurrences field is not included in the response that is returned when retrieving, creating, and updating Indicators. To include this field in responses returned by the API, include the ``?fields=fileOccurrences`` `query parameter <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_ in your request.

For comparison, the following example uses the same request in the preceding example with the ``?fields=fileOccurrences`` query parameter added to it:

.. code::

    PUT /v3/indicators/20?fields=fileOccurrences

    {
        "fileOccurrences": {
            "data": [
                {
                    "fileName": "win999301.dll",
                    "path": "C:\\\\Windows\\System",
                    "date": "2022-06-14T10:00:00Z"
                }
            ]
        }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 20,
            "ownerName": "Demo Organization",
            "dateAdded": "2022-06-14T13:59:54Z",
            "webLink": "https://appthreatconnect.com/auth/indicators/details/file.xhtml?file=9D67E81C18101FC266057CD7851604B8",
            "type": "File",
            "lastModified": "2022-06-14T14:00:11Z",
            "summary": "9D67E81C18101FC266057CD7851604B8",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "fileOccurrences": {
                "data": [
                    {
                        "id": 5,
                        "fileName": "win999301.dll",
                        "path": "C:\\\\Windows\\System",
                        "date": "2022-06-14T10:00:00Z"
                    }
                ],
                "count": 1
            },
            "md5": "9D67E81C18101FC266057CD7851604B8"
        },
        "message": "Updated",
        "status": "Success"
    }


Manage an Indicator's File Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can append, replace, and delete File Occurrences via the ``mode`` field. If deleting a File Occurrence, use the File Occurrence's ID when constructing your query. For example, the following query will delete the File Occurrence with ID ``5`` added to the File Indicator with ``20``:

.. code::

    PUT /v3/indicators/20

    {
        "fileOccurrences": {
            "data": [
                {
                    "id": 5
                }
            ],
            "mode": "delete"
        }
    }

For more information on using the ``mode`` field, see `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_.

.. hint::
    You can retrieve a File Occurrence's ID by submitting a request in the following format:

    ``GET v3/indicators/{fileIndicatorId or fileIndicatorSummary}?fields=fileOccurrences``