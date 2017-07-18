Groups
======

Groups represent a collection of related behavior and/or intelligence.

.. hint:: When working with groups using the ThreatConnect REST API, it is often necessary to specify the ID corresponding to the group you would like to work with. While the ID of a group can be retrieved from the API, it can also be found in the URL of each group. If you navigate to the page for a group, the URL should look something like: ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456`` or ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456&ow...``. The number after the <GROUP-TYPE> key is the ID for the group (in both of the previous examples, the ID of the group is ``123456``).

.. include:: groups/filters.rst

.. include:: groups/generic_group_retrieve.rst

.. include:: groups/adversaries/adversaries.rst

.. include:: groups/campaigns/campaigns.rst

.. include:: groups/documents/documents.rst

.. include:: groups/emails/emails.rst

.. include:: groups/incidents/incidents.rst

.. include:: groups/signatures/signatures.rst

.. include:: groups/threats/threats.rst

.. include:: groups/_metadata/metadata.rst
