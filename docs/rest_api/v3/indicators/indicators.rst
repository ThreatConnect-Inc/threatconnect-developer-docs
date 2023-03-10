==========
Indicators
==========

An Indicator represents an atomic piece of information that has some intelligence value. Indicators are guaranteed to be unique within an Owner. For example, a single Organization can have only one copy of the Indicator **badguy@bad.com**.

Endpoint: ``/api/v3/indicators``

.. note::
    You can retrieve, update, or delete a specific Indicator using its ID or summary. If using an Indicator's summary, the API request will search for the Indicator in the Organization in which your API user account resides. To search for an Indicator by summary in a Community or Source to which your API user account has access, use the ``owner`` `query parameter <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: indicatorToIndicatorAssociations.rst

.. include:: fileActions.rst

.. include:: fileOccurrences.rst

.. include:: mergeFileHashes.rst