Playbooks
---------

The Playbooks feature allows ThreatConnect users to automate cyberdefense tasks via a drag-and-drop interface. The interface uses Triggers (tools that create an event that initiates the actions defined within a Playbook, such as creating a new IP address Indicator or sending a phishing email an inbox) to pass data to Apps, which perform a variety of functions, including data enrichment, malware analysis, and blocking actions. Once enabled, Playbooks run in real time and provide users with detailed logs of each execution. Playbooks may also be saved for use as Components (i.e., modules) within other Playbooks.

Retrieve Playbooks
^^^^^^^^^^^^^^^^^^

Retrieve All Playbooks
======================

The following query returns a list of available Playbooks:

.. code::

    GET /v2/playbooks

Retrieve a Specific Playbook
============================

The following query returns information about the specified Playbook by the given ``id`` or ``groupXid``, each of which can be retrieved from the response body of a successful ``GET /v2/playbooks`` request. . If the Playbook does not exist, a 404 error is returned:

.. code::

    GET /v2/playbooks/{id or groupXid}

Search for Playbooks
====================

The following query executes a search:

.. code::

   GET /v2/playbooks/search  
 
The following are optional URL search parameters:

- ``resultStart``: The first result to return
- ``resultLimit``: The number of results to return
- ``name``: Searches for Playbooks by including a specified name
- ``triggerType``: Filters results based on the Playbook's type
- ``status``: Filters results based on the status of the Playbook (accepted values include ``Active``, ``Inactive``, ``Draft``, and ``Archive``)
- ``sortOn``: Specifies the field to sort by (accepted values include ``name`` and ``triggerType``)
- ``sortAscending``: Specifies whether to sort Playbooks in ascending order (accepted values include ``true`` and ``false``)
- ``labels``: A comma-delimited list of labels by which to filter

For example, the following query will search for a specific Playbook by name:

.. code:: 

    /v2/playbooks/search?name=Playbook%20Name

In this second example, the query will search for only active Playbooks:

.. code::

    /v2/playbooks/search?status=Active


Export Playbooks
================

The following query exports the specified Playbook as a Playbook (**.pbx**) file:

.. code::

    GET /v2/playbooks/{id or groupXid}/export

The following query exports the specified Playbook as a Content Pack (**.tcxp**) file:

.. code::

    GET /v2/playbooks/{id or groupXid}/export?format=tcxp

Import Playbooks
================

The following query uploads and installs a new Playbook with the Playbook (**.pbx**) file submitted as a JSON payload in the request:

.. code::

    POST /v2/playbooks

Create New Playbook Versions
============================

The following query uploads a Playbook as a new, major version to an existing Playbook, with the Playbook (**.pbx**) file submitted as a JSON payload in the request:

.. code::

    POST /v2/playbooks/{id or groupXid}

Activate and Deactivate Playbooks
=================================

The following query activates the specified Playbook:

.. code::

    POST /v2/playbooks/{id or groupXid}/activate

The following query deactivates the specified Playbook:

.. code::

    POST /v2/playbooks/{id or groupXid}/deactivate

Delete Playbooks
=================

The following query deletes the specified Playbook:

.. code::

    DELETE /v2/playbooks/{id or groupXid}