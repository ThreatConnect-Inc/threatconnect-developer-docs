Common Errors
=============

Here are some common errors that may be encountered while using the API or SDKs. If you run into an error that is not listed here and you are unable to debug it, contact support@threatconnect.com.

You may also find the list of `HTTP Responses <https://docs.threatconnect.com/en/latest/rest_api/overview.html#http-responses>`__ helpful in troubleshooting.

General Errors
--------------

Signature data did not match expected result
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This error occurs when something is wrong with the signature used in the `Authorization Section <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#authorization>`__. Make sure you are using the ``HMAC-SHA256`` algorithm and base-64 encoding to create the signature. Refer to the `Authorization Section <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#authorization>`__ for steps to fix this error.

Timestamp out of acceptable time range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every API call to ThreatConnect requires a ``Timestamp`` header that is within five minutes of the ThreatConnect server's system time. If you get this error, you are passing in a Timestamp that does not line up with ThreatConnect system time. Refer to the `Timestamp Section <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#timestamp>`__ for steps to fix this error.

Access Denied
^^^^^^^^^^^^^

This error occurs when one of the values in the `Authorization Header <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#authorization>`__ is incorrect, or when you are making a request to an owner to which the API account you are using does not have access.

Creating Indicators
-------------------

There are a few details to keep in mind when creating certain Indicator types.

ASN Indicators
^^^^^^^^^^^^^^

When `creating an ASN Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-a-custom-indicator>`__ in ThreatConnect, the AS Number must be **prefixed with "ASN"** and should not include a space between the prefix ("ASN") and the AS Number. There are some examples of correct and incorrect indicator formats below.

.. code-block:: text

    ASN12345 # CORRECT

    12345 # INCORRECT
    AS12345 # INCORRECT
    AS 12345 # INCORRECT
    ASN 12345 # INCORRECT

Host Indicators
^^^^^^^^^^^^^^^

When `creating a Host Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-host-indicators>`__ in ThreatConnect, the host must be in [ASCII](https://en.wikipedia.org/wiki/ASCII). This means that Unicode Host Indicators (e.g. [internationalized domain names](https://en.wikipedia.org/wiki/Internationalized_domain_name)), must be represented as [Punycode](https://en.wikipedia.org/wiki/Punycode).

.. code-block:: text

    xn--sterreich-z7a.icom.museum # CORRECT

    österreich.icom.museum # INCORRECT

Registry Key Indicators
^^^^^^^^^^^^^^^^^^^^^^^

When `creating a Registry Key Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-a-custom-indicator>`__ in ThreatConnect, the **Key Name** for the Registry Key must start with one of the following values:

* HKEY_CLASSES_ROOT
* HKEY_CURRENT_CONFIG
* HKEY_CURRENT_USER
* HKEY_CURRENT_USER_LOCAL_SETTINGS
* HKEY_LOCAL_MACHINE
* HKEY_PERFORMANCE_DATA
* HKEY_PERFORMANCE_NLSTEXT
* HKEY_PERFORMANCE_TEXT
* HKEY_USERS

.. note:: If a Registry Key starts with ``HKLM\``, this must be changed to ``HKEY_LOCAL_MACHINE\`` before the Key can be created in ThreatConnect.

.. code-block:: text

    HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\WbemPerf\001 # CORRECT

    HKLM\Software\Microsoft\Windows NT\CurrentVersion\WbemPerf\001 # INCORRECT

URL Indicators
^^^^^^^^^^^^^^

When `creating a URL Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-url-indicators>`__ in ThreatConnect, the domain name of the URL must be **lowercase**. There are some examples of correct and incorrect indicator formats below.

.. code-block:: text

    http://example.com # CORRECT

    http://EXAMPLE.com # INCORRECT
