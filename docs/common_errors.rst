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

CIDR Range Indicators with IPv6 Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When `creating a CIDR Range Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-a-custom-indicator>`__ that is based on an IPv6 Address, the CIDR Range must be formatted very specifically. There can be no leading zeros in any of the sections unless that section contains only a zero. CIDR Ranges based on compressed IPv6 Addresses (e.g. ``2001:db8:1234::/48``) are **not** accepted. CIDR Ranges based on expanded/exploded IPv6 Addresses (e.g. ``2001:0DB8:1234:0000:0000:0000:0000:0000``) are also **not** accepted. Any section with ``0000`` must be replaced with a single zero (``0``). There are some examples below which demonstrate acceptable and unacceptable forms.

.. code-block:: text

    abc:def:10:0:0:0:0:0/48 # CORRECT

    abc:def:10::/48 # INCORRECT - compressed IPv6 addresses not accepted
    0abc:def:10:0:0:0:0:0/48 # INCORRECT - leading zero on first section
    abc:0def:10:0:0:0:0:0/48 # INCORRECT - leading zero on second section
    abc:def:0010:0:0:0:0:0/48 # INCORRECT - leading zeros on third section
    abc:def:10:0000:0000:0000:0000:0000/48 # INCORRECT - expanded/exploded IPv6 addresses not accepted

The Python3 script below will format a CIDR Range (as the ``incoming_cidr_range`` variable) into the desired format:

.. code-block:: python

    import ipaddress

    incoming_cidr_range = "2001:db8:1234::/48"
    desired_cidr_range = "2001:db8:1234:0:0:0:0:0/48"

    address_sections =[section.replace("0000", "xxxx").lstrip("0") for section in ipaddress.IPv6Network(incoming_cidr_range).exploded.split(":")]

    formatted_cidr_range = ":".join(address_sections)
    formatted_cidr_range = formatted_cidr_range.replace("xxxx", "0")

    assert formatted_cidr_range == desired_cidr_range
    print(formatted_cidr_range)

.. note:: The script above only works with Python3.

Host Indicators
^^^^^^^^^^^^^^^

When `creating a Host Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-host-indicators>`__ in ThreatConnect, the host must be in `ASCII <https://en.wikipedia.org/wiki/ASCII>`__. This means that Unicode Host Indicators (e.g. `internationalized domain names <https://en.wikipedia.org/wiki/Internationalized_domain_name>`__), must be represented as `Punycode <https://en.wikipedia.org/wiki/Punycode>`__.

.. code-block:: text

    xn--sterreich-z7a.icom.museum # CORRECT

    österreich.icom.museum # INCORRECT

Registry Key Indicators
^^^^^^^^^^^^^^^^^^^^^^^

Key Name
""""""""

When `creating a Registry Key Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-a-custom-indicator>`__ in ThreatConnect, the **Key Name** for the Registry Key must start with one of the following values:

* ``HKEY_CLASSES_ROOT``
* ``HKEY_CURRENT_CONFIG``
* ``HKEY_CURRENT_USER``
* ``HKEY_CURRENT_USER_LOCAL_SETTINGS``
* ``HKEY_LOCAL_MACHINE``
* ``HKEY_PERFORMANCE_DATA``
* ``HKEY_PERFORMANCE_NLSTEXT``
* ``HKEY_PERFORMANCE_TEXT``
* ``HKEY_USERS``

.. note:: If a Registry Key starts with ``HKLM\``, this must be changed to ``HKEY_LOCAL_MACHINE\`` before the Key can be created in ThreatConnect.

.. code-block:: text

    HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\WbemPerf\001 # CORRECT

    HKLM\Software\Microsoft\Windows NT\CurrentVersion\WbemPerf\001 # INCORRECT

Value Name
""""""""""

When `creating a Registry Key Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-a-custom-indicator>`__ in ThreatConnect via the API, the **Value Name** for the Registry Key is required, although you do not need to specify a value. For example, to create a Registry Key with an empty value name, use the following request:

.. code-block::

    POST /v2/indicators/registryKeys
    Content-type: application/json; charset=utf-8

    {
      "Key Name": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\DRM\\{cd704ff3-cd05-479e-acf7-6474908031dd}",
      "Value Name": " ",
      "Value Type": "REG_NONE"
    }

.. note:: The space in the value for the **Value Name** field is important. Without it, the API will return an error. The API will handle this request as though no value name was given.

URL Indicators
^^^^^^^^^^^^^^

When `creating a URL Indicator <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-url-indicators>`__ in ThreatConnect, the domain name of the URL must be **lowercase**. There are some examples of correct and incorrect indicator formats below.

.. code-block:: text

    http://example.com # CORRECT

    http://EXAMPLE.com # INCORRECT

Additionally, the domain name of a URL must be in ASCII (if it is `internationalized <https://en.wikipedia.org/wiki/Internationalized_domain_name>`_ , it must be represented as Punycode as described `here <https://docs.threatconnect.com/en/latest/common_errors.html#host-indicators>`__).

TCEX Errors
-----------

Can't find '__main__' module in '.'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``can't find '__main__' module in '.'`` error means that you are trying to run the tcex script or app without the ``__main__.py`` file available `here <https://github.com/ThreatConnect-Inc/tcex/blob/master/app_init/__main__.py>`__. Download ``__main__.py`` into the base directory or your app and try running it again.
