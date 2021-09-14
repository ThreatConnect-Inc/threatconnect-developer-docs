Groups
======

Groups represent a collection of related behavior and/or intelligence.

.. hint:: When working with Groups using the ThreatConnect REST API, it is often necessary to specify the ID corresponding to the Group with which you would like to work. While the ID of a Group can be retrieved from the API, it can also be found in the URL of each Group. If you navigate to the screen for a Group, the URL should look like: ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456`` or ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456&ow...``. The number after the <GROUP-TYPE> key is the ID for the Group. (In both of the previous examples, the ID of the Group is ``123456``.)

.. include:: retrieve.rst

.. include:: create.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: publish.rst

.. include:: create_report.rst
