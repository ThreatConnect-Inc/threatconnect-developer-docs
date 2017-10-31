Groups Overview
---------------

In ThreatConnect, Groups represent a collection of related behavior and/or intelligence (refer to the article on the `ThreatConnect data model <http://kb.threatconnect.com/customer/en/portal/articles/2092925-the-threatconnect-data-model>`_ for more details).

The following group objects are available via the ThreatConnect SDK:

.. code-block:: python

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate a generic Groups object
    groups = tc.groups()

    # instantiate an object for a specific Group type
    adversaries = tc.adversaries()
    campaigns = tc.campaigns()
    documents = tc.documents()
    emails = tc.emails()
    incidents = tc.incidents()
    signatures = tc.signatures()
    threats = tc.threats()

The following, high-level actions can be performed on Group objects:

* ``retrieve()`` - retrieve Group/Groups from ThreatConnect
* ``commit()`` - commit a new or updated Group to ThreatConnect
* ``delete()`` - delete a Group from ThreatConnect

When retrieving Groups from ThreatConnect, there are various `filters <https://docs.threatconnect.com/en/latest/python/python_sdk.html#filtering-groups>`__ which can be used to refine the Groups returned by the ``retrieve()`` call.

There are also functions which enable the creation of `Group metadata <https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-metadata>`_ such as `associations <https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-associations>`__ , `attributes <https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-attributes>`__ , `security labels <https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-security-labels>`__ , and `tags <https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-tags>`__.

.. hint:: When working with groups using the ThreatConnect Python SDK, it is often necessary to specify the ID corresponding to the Group you would like to work with. While the ID of a Group can be retrieved from the SDK, it can also be found in the URL of each Group. If you navigate to the page for a Group, the URL should look something like: ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456`` or ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456&ow...``. The number after the <GROUP-TYPE> key is the ID for the Group (in both of the previous examples, the ID of the Group is ``123456``).
