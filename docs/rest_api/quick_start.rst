Quick Start
===========

Creating an API Key
-------------------

To access the ThreatConnect API, you must `create an API user account <https://knowledge.threatconnect.com/docs/creating-user-accounts#creating-an-api-user>`_. If you are not able to create an API user account, please send an email to sales@threatconnect.com to discuss pricing.

Using the API
-------------

If using an API user account on ThreatConnect's Public Cloud instance, the ThreatConnect API is accessible at ``https://app.threatconnect.com/api``. If using an API user account on a Dedicated Cloud or On-Premises ThreatConnect instance, the ThreatConnect API is accessible at the base URL of your instance followed by ``/api`` (e.g., ``https://companyabc.threatconnect.com/api``).

Throughout this documentation, the base API URL will not be included in any of the endpoints (e.g., the branch for the v2 API owners endpoint will be described as ``/v2/owners`` rather than ``https://app.threatconnect.com/api/v2/owners``). When sending requests to the ThreatConnect API, you will be responsible for adding the correct base URL to the URL in the request.

Each API response is formatted with a status. If a ``"Success"`` status is returned, each response will include a data field with the appropriate response type. If an ``"Error"`` status is returned, an appropriate error message as to why the request failed will be provided. For a list of HTTP status codes returned by the API, see `HTTP Status Codes <https://docs.threatconnect.com/en/latest/rest_api/overview.html#http-status-codes>`__.

.. attention::

    Requests to ThreatConnect API endpoints must be made over HTTPS with a supported authentication method, as described in the `"Authentication" <#authentication>`_ section. Otherwise, a 403 error will be returned.

API Versioning
--------------

The API will be versioned, as needed, to support continued development of ThreatConnect, and existing API versions will be deprecated appropriately .

Version 1 (/v1)
^^^^^^^^^^^^^^^

The ThreatConnect v1 API has been deprecated for several years now and, as of ThreatConnect version 6.0, is no longer available.

Version 2 (/v2)
^^^^^^^^^^^^^^^

The ThreatConnect v2 API can be used to interact with threat intelligence data, custom metrics, notifications, and Playbooks. Write capabilities are supported via HTTP POST and PUT methods. The HTTP GET method is used for read access to resources. To better understand the implementation and usage of the v2 API, refer to the individual sections within this documentation that describe the methods and data formats available at each endpoint.

Version 3 (/v3)
^^^^^^^^^^^^^^^

The ThreatConnect v3 API was introduced in ThreatConnect version 6.0 and is the current active version for Case management features within the platform. As of ThreatConnect version 6.4, it supports many of the threat intelligence features currently available in the ThreatConnect v2 API.

The v3 API was designed to leverage a few "lessons learned" identified within the design and deployment of the v2 API. Of particular note, the number of calls needed to make relatively complex setting/getting operations has been greatly reduced and simplified. TQL filtering is also now supported, allowing the user to format, filter, and sort data in a nearly infinite number of ways. The path structure has been simplified as well, having eliminated the need for many levels of nested paths within a given primary endpoint. Finally, error messaging has also been improved in order to better assist the user in identifying and repairing malformed requests.

To understand the implementation and usage of the v3 API, consider the HTTP methods below supported by each v3 endpoint. Take special note of the OPTIONS methods, which now carry the main responsibility of describing data formats and filtering options available to the user. Once familiarized with this design pattern, users may wish to visit the individual sections within this document that describe the different endpoints currently available within the v3 API, with some examples specific to those respective endpoints.

**OPTIONS /**
    - Returns an object descriptor for a given endpoint, which contains names, data types, and text descriptions of each field within an object
    - The response here can be used as a "template" of sorts to construct a body to use in a POST or PUT request; or it can be used to better understand what fields users can expect to see in a GET request.
    - ``?show=readOnly`` will also include read-only (non-settable) parameters for the object

**OPTIONS /fields**
    - Returns a list of names and descriptions of available options to set in the ``?fields=`` query parameter (See GET sections below.)
    
**OPTIONS /tql**
    - Returns available tql filter options to use in the ``?tql=`` query parameter
    
**GET /**
    - Retrieves a list of objects
    - ``?tql= tql`` query to filter results
    - ``?fields=`` requests additional fields not automatically included with each returned object
    - ``?resultStart=`` starting result index, for pagination
    - ``?resultLimit=`` maximum number of results, for pagination
    - ``?sorting=`` query parameter to specify sorting order
    - ``?owner=`` query parameter to specify the owner of the data being requested
    
**GET /{id}**
    - Retrieves a single object specified by the given ID
    - ``?fields=`` requests additional fields not automatically included with each returned object
    - ``?owner=`` query parameter to specify the owner of the data being requested
    
**POST /**
    - Saves a new object of the given data type
    - May include nested objects, where applicable, to save multiple items at once (e.g., a Case with nested Task(s))
    - ``?owner=`` query parameter to specify the owner of the data being set
    
**PUT /{id}**
    - Updates the object specified by the given ID
    - Typically, only necessary to provide the data fields being modified
    - Similar to POST, may include nested objects where applicable
    - ``?owner=`` query parameter to specify the owner of the data being set
    
**DELETE /**
    - Performs bulk deletion of objects (**Note**: This feature must be enabled in the system settings for your ThreatConnect instance.)
    - ``?tql= tql`` query to filter items to be deleted
    - ``?owner=`` query parameter to specify the owner of the data being set
    
**DELETE /{id}**
    - Deletes the single object specified by the given ID
    - ``?owner=`` query parameter to specify the owner of the data being set

Authentication
--------------

As of ThreatConnect 7.7, there are two ways to authenticate an API request to ThreatConnect:

- API token
- Access ID and Secret Key

API Token
^^^^^^^^^

.. note::

    Authenticating an API request to ThreatConnect with an API token requires a ThreatConnect instance with version 7.7 or newer installed.

To authenticate an API request to ThreatConnect with your API token, you must include the *required* ``Authorization`` header in your request. The value of the ``Authorization`` header must be in the format ``TC-Token $API_TOKEN``, where ``$API_TOKEN`` is the value of your API token.

The following example illustrates how a complete API request should look when authenticating with your API token:

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/v3/indicators' \
    --header 'Authorization: TC-Token APIV2:430:c8mTcH:1234567890123:7mbiy0OnuSIq0ujNbkrqEB3RlpplzNL3CcQsYGso8ZQ=' \
    --header 'Accept: application/json'

Generate an API Token
"""""""""""""""""""""
**New API User**

Follow these steps to generate an API token for a new API user account in ThreatConnect:

1.	Log into ThreatConnect with an Organization Administrator account.

2.	Hover over **Settings** |gear| on the top navigation bar and select **Org Settings**.

3.	On the **Membership** tab of the **Organization Settings** screen, click **Create API User**.

4.	On the **API User Administration** window, fill out all required fields for the API user, enter the number of days until the API token will expire in the **Token Expiration (days)** field, and click **SAVE USER AND GENERATE TOKEN**. (See the `"Creating an API User" section of Creating User Accounts <https://knowledge.threatconnect.com/docs/creating-user-accounts#creating-an-api-user>`_ for more information on creating API users.)
    
**Existing API User**

Follow these steps to generate an API token for an existing API user account in ThreatConnect:

1.	Log into ThreatConnect with an Organization Administrator account.

2.	Hover over **Settings** |gear| on the top navigation bar and select **Org Settings**.

3.	On the **Membership** tab of the **Organization Settings** screen, click **Edit** |pencil| in the **Options** column for an API user account.

4.	On the **API User Administration** window, enter the number of days until the API token will expire in the **Token Expiration (days)** field, and then click **GENERATE TOKEN**.

.. |gear| image:: https://cdn.document360.io/dfc206c8-1c9f-4725-b74d-a66f83432320/Images/Documentation/Settings%20icon.png
    :height: 25px

.. |pencil| image:: https://cdn.document360.io/dfc206c8-1c9f-4725-b74d-a66f83432320/Images/Documentation/Pencil%20icon_Black.png
    :height: 25px

Access ID and Secret Key
^^^^^^^^^^^^^^^^^^^^^^^^

To authenticate an API request to ThreatConnect with your Access ID and Secret Key, you must include the following *required* headers in your request: ``Timestamp`` and ``Authorization``. Both headers are detailed in the following subsections.

The following example illustrates how a complete API request should look when authenticating with your Access ID and Secret Key:

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/v2/indicators?owner=Common%20Community' \
    --header 'Timestamp: 1513703787' \
    --header 'Authorization: TC 12345678901234567890:PthSlXIA7rNMow1h8wShfvOnTOhxHd+7njUe4MT4ZSs=' \
    --header 'Accept: application/json'

Timestamp
"""""""""

The required ``Timestamp`` header is a nonce in Unix epoch time (generated by Unix shell with the command: ``date +%s``). The value of the ``Timestamp`` header should look something like ``1513703787``.

.. note::

    If the nonce is not within five minutes of the ThreatConnect server's system time, a `Timestamp error <../common_errors.html#timestamp-out-of-acceptable-time-range>`__  will be returned.

Authorization
"""""""""""""

The required ``Authorization`` header's value has the format: ``TC $ACCESS_ID:$SIGNATURE``:

- ``$ACCESS_ID``: This is the Access ID of your API user account. If you do know this value, contact your System Administrator.
- ``$SIGNATURE``: This value is created by concatenating the API path and query strings, HTTP method, and value of the Timestamp header as follows: ``/api/v2/indicators/hosts/example.com?Owner=Common%20Community:GET:1513703787``. The result is signed with your Secret Key using SHA256 to calculate a hash-based message authentication code (HMAC) and then base-64 encoded.

The following example illustrates how the value of the ``Authorization`` header should look:

.. code::

    TC 12345678901234567890:PthSlXIA7rNMow1h8wShfvOnTOhxHd+7njUe4MT4ZSs=

Testing API Connectivity
------------------------

To test API connectivity, start with a request to the ``/v2/owners`` branch to return all Organizations and Communities to which the API credentials have access. An example Bash script for performing this test is available on `GitHub <https://github.com/ThreatConnect-Inc/threatconnect-bash>`_. In this example, you will first update the fields in the ``config.sh`` file, and then execute the ``threatconnect.sh`` file to make the request to the ``/v2/owners`` branch. 

.. note::
    If you receive an error while using the script above, make sure that the ``API_HOST`` variable in the ``config.sh`` file is pointed to the correct API for the instance of ThreatConnect you wish to use.

Send the following request to retrieve a list of all owners to which your API user account has access:

.. code::

    GET /v2/owners

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "owner": [
          {
            "id": 0,
            "name": "Exemplary Organization",
            "type": "Organization"
          },
          {
            "id": 1,
            "name": "Common Community",
            "type": "Community"
          },
        ]
      }
    }

XML Response:

.. code:: xml

    <ownersResponse>
     <Status>Success</Status>
     <Data xsi:type="ownerListResponseData" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <Owner xsi:type="organization">
       <Id>0</Id>
       <Name>Exemplary Organization</Name>
       <Type>Organization</Type>
      </Owner>
      <Owner xsi:type="community">
       <Id>1</Id>
       <Name>Common Community</Name>
       <Type>Community</Type>
      </Owner>
     </Data>
    </ownersResponse>

Next Steps
----------

From here, find a topic that interests you and dig in! If you don't know where to start, retrieving Indicators is a good place to begin.

.. hint::
    When using this documentation, it is helpful to have a basic understanding of the `ThreatConnect Data Model <https://knowledge.threatconnect.com/docs/the-threatconnect-data-model>`_.