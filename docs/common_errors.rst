Common Errors
=============

Here are some common errors that may be encountered while using the API or SDKs. If you run into an error that is not listed here and you are unable to debug it, contact support@threatconnect.com.

You may also find the list of `HTTP Responses <https://docs.threatconnect.com/en/latest/rest_api/overview.html#http-responses>`_ helpful in troubleshooting.

General Errors
--------------

Signature data did not match expected result
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This error occurs when something is wrong with the signature used in the `Authorization header <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#authorization>`_. Make sure you are using the ``HMAC-SHA256`` algorithm and base-64 encoding to create the signature. Refer to the `Authorization header section <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#authorization>`_ for steps to fix this error.

Timestamp out of acceptable time range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every API call to ThreatConnect requires a ``Timestamp`` header that is within five minutes of the ThreatConnect server's system time. If you get this error, you are passing in a Timestamp that does not line up with ThreatConnect system time. Refer to the `Timestamp header section <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#timestamp>`_ for steps to fix this error.

Access Denied
^^^^^^^^^^^^^

This likely means that either one of the values in the `Authorization header <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#authorization>`_ is incorrect or you are making a request to an owner to which the API account you are using does not have access.

Creating Indicators
-------------------

There are a few details to keep in mind when creating certain Indicator types.

URL Indicators
^^^^^^^^^^^^^^

When creating a URL Indicator in ThreatConnect, the domain name of the URL must be **lower-cased**.

.. code-block:: text

    http://EXAMPLE.com # INCORRECT
    http://example.com # CORRECT

ASN Indicators
^^^^^^^^^^^^^^

When creating an ASN Indicator in ThreatConnect, the AS Number must be prefixed with "ASN".

For example, trying to create an ASN Indicator for the AS Number ``12345`` in the following formats will return an error:

.. code-block:: text

    12345 # INCORRECT
    AS12345 # INCORRECT
    AS 12345 # INCORRECT
    ASN 12345 # INCORRECT

The correct format of the ASN Indicator for the AS Number ``12345`` is:

.. code-block:: text

    ASN12345 # CORRECT
