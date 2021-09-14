Playbooks
=========

The Playbooks feature allows ThreatConnect users to automate cyberdefense tasks via a drag-and-drop interface. The interface uses Triggers (e.g., a new IP address Indicator or a phishing email sent to an inbox) to pass data to Apps, which perform a variety of functions, including data enrichment, malware analysis, and blocking actions. Once enabled, Playbooks run in real time and provide users with detailed logs of each execution. Playbooks may also be saved for use as Components (i.e., modules) within other Playbooks.

Retrieving Playbooks
^^^^^^^^^^^^^^^^^^^^

Filter Parameters
"""""""""""""""""

When retrieving Playbooks from ThreatConnect, it is possible to filter the results by using specified data points:

**Examples**

The following query returns a list of available Playbooks:

.. code::

    GET /v2/playbooks

The following query executes a search:

.. code::

   GET /v2/playbooks/search  
 
The following are optional URL search parameters:

- ``resultStart``: The first result to return

- ``resultLimit``: The number of results to return

- ``name``: Searches for Playbooks by including a specified name

- ``triggerType``: Filters results based on the Playbook's type

- ``status``: Filters results based on the status of the Playbook. Possible values are ``Active``, ``Inactive``, ``Draft``, and ``Archive``

- ``sortOn``: Determines the field to sort by. Possible values are ``name`` and ``triggerType``

- ``sortAscending``: Filters by ``true/false``

- ``labels``: A comma-delimited list of labels by which to filter

To search for a specific playbook by name:

.. code:: 

    /v2/playbooks/search?name=Playbook%20Name

or to return only active Playbooks: 

.. code::

    /v2/playbooks/search?status=Active




The following query uploads and installs a new Playbook with the playbook file submitted as an JSON payload in the request:

.. code::

    POST /v2/playbooks

The following query uploads a Playbook as a new, major version to an existing Playbook, with the playbook file submitted as an JSON payload in the request:


.. code::

    POST /v2/playbooks/{id}

The following query returns information about the specified Playbook by the given ID. If the Playbook does not exist, a 404 error is returned:

.. code::

    GET /v2/playbooks/{id}

The following query deletes the specified Playbook:

.. code::

    DELETE /v2/playbooks/{id}

The following query activates the specified Playbook:

.. code::

    POST /v2/playbooks/{id}/activate

The following query deactivates the specified Playbook:

.. code::

    POST /v2/playbooks/{id}/deactivate
