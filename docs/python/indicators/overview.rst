Indicators Overview
-------------------

An Indicator represents an atomic piece of information that has some intelligence value (see the article on the `ThreatConnect data model <http://kb.threatconnect.com/customer/en/portal/articles/2092925-the-threatconnect-data-model>`_ for more details). Indicators are guaranteed to be unique within an Owner. For example, a single Organization can have only one instance of the email address Indicator ``badguy@bad.com``.

In the ThreatConnect Python SDK, there is one Indicator class to handle all types of indicators. An object of the Indicator class can be instantiated as demonstrated below:

.. code-block:: python

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate an Indicators object
    indicators = tc.indicators()

The following, high-level actions can be performed on Indicator objects:

* ``retrieve()`` - retrieve Indicator/Indicators from ThreatConnect
* ``commit()`` - commit a new or updated Indicator to ThreatConnect
* ``delete()`` - delete an Indicator from ThreatConnect

When retrieving Indicators from ThreatConnect, there are various `filters <https://docs.threatconnect.com/en/latest/python/python_sdk.html#filtering-indicators>`__ which can be used to refine the Indicators returned by the ``retrieve()`` call.

There are also functions which enable the creation of `Indicator metadata <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-metadata>`_ such as `associations <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-associations>`__ , `attributes <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-attributes>`__ , `security labels <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-security-labels>`__ , `tags <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-tags>`__ , `threat and confidence ratings <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-threat-and-confidence-ratings>`_ , `false positives <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-false-positives>`_ , and `observations <https://docs.threatconnect.com/en/latest/python/python_sdk.html#indicator-observations>`_ .
