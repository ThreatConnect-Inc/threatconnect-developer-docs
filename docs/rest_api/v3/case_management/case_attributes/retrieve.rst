Retrieve Case Attributes
------------------------

Retrieve All Case Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Case Attributes, use the following query:

.. code::

    GET /v3/caseAttributes/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "type": "Detection Percentage",
        "value": "50",
        "source": "Hybrid analysis"
      }, {
        "id": 2,
        "type": "Phishing Open Rate",
        "value": "20",
      }],
      "count": 2,
      "status": "Success"
    }

Retrieve a Single Case Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Case Attribute, use a query in the following format:

.. code::

    GET /v3/caseAttributes/{caseAttributeId}

For example, the following query will return information about the Case Attribute with ID 1:

.. code::

    GET /v3/notes/1

JSON Response:

.. code:: json

    {
      "data": {
        "id": 1,
        "type": "Detection Percentage",
        "value": "50",
        "source": "Hybrid analysis"
      },
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned Case Attribute, refer to the `Request Additional Fields for Returned Objects <../../additional_fields.html>`__ section in this documentation.

Filter Results
^^^^^^^^^^^^^^

To filter returned Case Attribute using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../../filter_results.html>`__ section in this documentation.
