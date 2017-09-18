Groups Overview
---------------

In ThreatConnect, Groups represent a collection of related behavior and/or intelligence (see the article on the `ThreatConnect data model <http://kb.threatconnect.com/customer/en/portal/articles/2092925-the-threatconnect-data-model>`_ for more details).

The available group types are:



.. code-block:: python

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    adversaries = tc.adversaries()
    campaigns = tc.campaigns()
    documents = tc.documents()
    emails = tc.emails()
    incidents = tc.incidents()
    signatures = tc.signatures()
    threats = tc.threats()

.. hint:: When working with groups using the ThreatConnect Python SDK, it is often necessary to specify the ID corresponding to the group you would like to work with. While the ID of a group can be retrieved from the SDK, it can also be found in the URL of each group. If you navigate to the page for a group, the URL should look something like: ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456`` or ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456&ow...``. The number after the <GROUP-TYPE> key is the ID for the group (in both of the previous examples, the ID of the group is ``123456``).
