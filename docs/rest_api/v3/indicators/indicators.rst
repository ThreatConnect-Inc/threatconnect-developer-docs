==========
Indicators
==========

An Indicator represents an atomic piece of information that has some intelligence value. Indicators are guaranteed to be unique within an owner. For example, an Organization can have only one copy of the ``badguy@bad.com`` Email Address Indicator.

Endpoint: ``/api/v3/indicators``

.. note::
    When retrieving, updating, and deleting Indicators, you can target a specific Indicator using its ID or summary. If targeting an Indicator by its summary, the API request will search for the Indicator in your Organization. To target an Indicator in one of your Communities or Sources by its summary, use the ``owner`` `query parameter <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ in your API request.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: associations.rst

.. include:: fileOccurrences.rst

.. include:: mergeFileHashes.rst

.. include:: falsePositivesObservations.rst

----

*MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation.*