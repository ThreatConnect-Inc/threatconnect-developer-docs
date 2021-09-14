Retrieving File Occurrences
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the File Occurrences of a File Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/files/{fileHash}/fileOccurrences

For example, the query below will return all of the File Occurrences for the File Indicator represented by the hash ``aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa``:

.. code::

    GET /v2/indicators/files/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/fileOccurrences

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "fileOccurrence": {
          "id": 87534,
          "fileName": "win999301.dll",
          "path": "C:\\\\Windows\\System",
          "date": "2017-07-13T05:00:00Z"
        }
      }
    }

To retrieve a specific File Occurrence, you can add the ID of the File Occurrence to the end of the query:

.. code::

    GET /v2/indicators/files/{fileHash}/fileOccurrences/{fileOccurrenceId}
