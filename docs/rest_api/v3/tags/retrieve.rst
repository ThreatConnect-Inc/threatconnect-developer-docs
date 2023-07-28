Retrieve Tags
-------------

Retrieve All Tags
^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Tags:

.. code::

    GET /v3/tags

JSON Response

.. code:: json

    {
        "next": "https://app.threatconnect.com/api/v3/tags?resultStart=100&resultLimit=100",
        "data": [
            {
                "id": 1,
                "name": "Ransomware",
                "owner": "Demo Organization",
                "description": "Apply this Tag to objects related to ransomware attacks.",
                "lastUsed": "2021-11-08T18:01:36Z"
            },
            {
                "id": 2,
                "name": "Malicious Host",
                "owner": "Demo Organization",
                "lastUsed": "2021-11-14T13:54:20Z"
            },
            {
                "id": 3,
                "name": "Robbery",
                "owner": "Demo Organization",
                "lastUsed": "2021-11-14T18:52:38Z"
            },
            {...},
            {
                "id": 100,
                "name": "Process Injection: Thread Local Storage",
                "description": "Adversaries may inject malicious code into processes via thread local storage (TLS) callbacks in order to evade process-based defenses as well as possibly elevate privileges. TLS callback injection is a method of executing arbitrary code in the address space of a separate live process. \n\nTLS callback injection involves manipulating pointers inside a portable executable (PE) to redirect a process to malicious code before reaching the code's legitimate entry point. TLS callbacks are normally used by the OS to setup and/or cleanup data used by threads. Manipulating TLS callbacks may be performed by allocating and writing to specific offsets within a process’ memory space using other [Process Injection](https://attack.mitre.org/techniques/T1055) techniques such as [Process Hollowing](https://attack.mitre.org/techniques/T1055/012).(Citation: FireEye TLS Nov 2017)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via TLS callback injection may also evade detection from security products since the execution is masked under a legitimate process. ",
                "lastUsed": "2023-06-05T19:39:45Z",
                "techniqueId": "T1055.005",
                "platforms": {
                    "data": [
                        "Windows"
                    ],
                    "count": 1
                }
            }
        ],
        "status": "Success"
    }

Retrieve a Specific Tag
^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Tag:

.. code::

    GET /v3/tags/{tagId}

For example, the following request will retrieve data for the Tag whose ID is 2:

.. code::

    GET /v3/tags/2

JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "name": "Malicious Host",
            "owner": "Demo Organization",
            "lastUsed": "2021-11-14T13:54:20Z"
        },
        "status": "Success"
    }

Retrieve Tags by Type
^^^^^^^^^^^^^^^^^^^^^

Retrieve Standard Tags
======================

As of ThreatConnect version 7.2, the API response for a GET request to the ``/v3/tags`` endpoint will include standard Tags and system-generated ATT&CK® Tags (i.e., Tag objects that include the ``techniqueId`` field). A standard Tag is any Tag that is not an ATT&CK Tag.

To retrieve only standard Tags, send the following request:

Request (Decoded URL)

.. code::

    GET /v3/tags?tql=techniqueId is null

Request (Encoded URL)

.. code::

    GET /v3/tags?tql=techniqueId%20is%20null

Retrieve ATT&CK Tags
====================

As of ThreatConnect version 7.2, the API response for a GET request to the ``/v3/tags`` endpoint will include standard Tags and system-generated ATT&CK® Tags (i.e., Tag objects that include the ``techniqueId`` field). An ATT&CK Tag is a system-generated Tag representing a MITRE ATT&CK® Enterprise technique or sub-technique.

To retrieve only ATT&CK Tags, send the following request:

Request (Decoded URL)

.. code::

    GET /v3/tags?tql=techniqueId is not null

Request (Encoded URL)

.. code::

    GET /v3/tags?tql=techniqueId%20is%20not%20null

Retrieve Main Tags
==================

As of ThreatConnect version 7.2, System Administrators can create Tag normalization rules that define one or more synonymous Tags that will be converted to a main Tag whenever they are applied to an object. To retrieve only main Tags, send the following request:

Request (Decoded URL)

.. code::

    GET v3/tags?tql=normalized EQ true

Request (Encoded URL)

.. code::
    
    GET /v3/tags?tql=normalized%20EQ%20true

.. note::
    This request will not return all main Tags defined within Tag normalization rules on your ThreatConnect instance; rather, it will only return those main Tags that have been created in one of your owners.