Quick Start
===========

Creating an API Key
-------------------

To create an API user account, please refer to the `Creating User Accounts <https://knowledge.threatconnect.com/docs/creating-user-accounts>`__ knowledge base article. If you are not able to create an API key using instructions provided in this article, please contact sales@threatconnect.com to discuss pricing.

Using the API
-------------

If using an API user account on ThreatConnect's Public Cloud instance, the ThreatConnect API is accessible at ``https://app.threatconnect.com/api``. If using an API user account on a Dedicated Cloud or On-Premises ThreatConnect instance, the ThreatConnect API is accessible at the base URL of your instance followed by ``/api`` (e.g., ``https://companyabc.threatconnect.com/api``).

For the rest of this document, the base API URL will not be included in any of the endpoints (e.g., the branch for the v2 API owners endpoint will be described as ``/v2/owners`` rather than ``https://app.threatconnect.com/api/v2/owners``). When sending requests to the ThreatConnect API, you will be responsible for adding the correct base URL to the URL in the request.

Requests to ThreatConnect API endpoints must be made over HTTPS with a valid signature (as described in the next "Authentication" section), or a 403 error will be returned. Each API response is formatted with a status. If a ``"Success"`` status is returned, each response will include a ``data`` field with the appropriate response type. If a ``"Failure"`` status is returned, an appropriate error message indicating why the request failed will be provided.

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

To authenticate an API request to ThreatConnect, there are two required headers—`Authorization <#authorization>`_ and `Timestamp <#timestamp>`_. The following example illustrates how a complete API request should look:

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/v2/indicators?owner=Common%20Community' \
    --header 'Timestamp: 1513703787' \
    --header 'Authorization: TC 12345678901234567890:PthSlXIA7rNMow1h8wShfvOnTOhxHd+7njUe4MT4ZSs=' \
    --header 'Accept: application/json'

Timestamp
^^^^^^^^^

The required ``Timestamp`` header is a nonce in Unix epoch time (generated by Unix shell with the command: ``date +%s``). The value of the ``Timestamp`` header should look something like ``1513703787``.

.. note::
    If the nonce is not within five minutes of the ThreatConnect server's system time, a `Timestamp error <../common_errors.html#timestamp-out-of-acceptable-time-range>`__  will be returned.

Authorization
^^^^^^^^^^^^^

The required ``Authorization`` header has the format: ``TC $ACCESS_ID:$SIGNATURE``.

- ``$ACCESS_ID``: This is the Access ID of your API user account. If you do know this value, contact your System Administrator.
- ``$SIGNATURE``: This value is created by concatenating the API path and query strings, HTTP method, and value of the Timestamp header as follows: ``/api/v2/indicators/hosts/example.com?Owner=Common%20Community:GET:1513703787``. The result is signed with your API user account's Secret Key using SHA256 to calculate a hash-based message authentication code (HMAC) and then base-64 encoded.

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