Retrieve a PDF Report for Groups
--------------------------------

To retrieve a PDF report for a Group, use a query in the following format:

.. code::

    GET /v3/groups/{groupId}/pdf

PDF reports can only be retrieved for the following Group types:

- ``Adversary``
- ``Attack Pattern``
- ``Campaign``
- ``Course of Action``
- ``Event``
- ``Incident``
- ``Intrusion Set``
- ``Malware``
- ``Report``
- ``Tactic``
- ``Threat``
- ``Tool``
- ``Vulnerability``