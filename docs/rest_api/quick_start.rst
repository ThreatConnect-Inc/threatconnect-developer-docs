Quick Start
===========

Creating an API Key
-------------------

To create an API User, please refer to the `Creating User Accounts <https://training.threatconnect.com/learn/article/creating-user-accounts-kb-article>`__ Knowledge Base article.

If you are not able to create an API key using instructions provided in the KB article above, please contact sales@threatconnect.com to discuss pricing.

Using the API
-------------

For those with a ThreatConnect Public Cloud API user account, the ThreatConnect API is accessible at ``https://app.threatconnect.com/api``.

For the rest of this document, the base API URL will not be included in any of the endpoints (e.g., the branch for owners will be described as ``/v2/owners`` rather than ``https://app.threatconnect.com/api/v2/owners``). You will be responsible for adding the correct base API URL.

Requests to ThreatConnect API endpoints must be made over HTTPS with a valid Signature (as described in the next section), or a 403 error will be returned.

Each API response is formatted with a status. If the status is "Success," each response includes a ``data`` field with the appropriate response type. If the status is "Failure," an appropriate error message is provided as to why the request failed.

API Versioning
--------------

The API will be versioned, as needed, to support continued development of the ThreatConnect platform, and existing API versions will be appropriately deprecated.

Version 1 (/v1)
^^^^^^^^^^^^^^^

v1 of the ThreatConnect API has been deprecated for several years now and, as of v6.0, is no longer available.

Version 2 (/v2)
^^^^^^^^^^^^^^^

v2 of the ThreatConnect API remains the current active version for Threat Intelligence features within the platform. Write capabilities are supported via HTTP POST and PUT methods. The HTTP GET method is used for read access to resources. To better understand the implementation and usage of the v2 API, refer to the individual sections within this document that describe the methods and data formats available at each endpoint.

Version 3 (/v3)
^^^^^^^^^^^^^^^

v3 of the ThreatConnect API begins with the release of v6.0 and is the current active version for Case Management features within the platform. In future versions, users can expect to see many of the Threat Intelligence features currently available within v2 to be made available in v3 format; however, this is still currently not supported.

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
    - ``?fields=`` requests additional fields not automatically provided with each returned object
    - ``?resultStart=`` starting result index, for pagination
    - ``?resultLimit=`` maximum number of results, for pagination
    - ``?sorting=`` query parameter to specify sorting order
    - ``?owner=`` query parameter to specify the owner of the data being requested
    
**GET /{id}**
    - Retrieves a single object specified by the given ID
    - ``?fields=`` requests additional fields not automatically provided with each returned object
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
    - Performs bulk deletion of objects (Note: System Configuration option v3ApiBulkDeleteAllowed must be enabled.)
    - ``?tql= tql`` query to filter items to be deleted
    - ``?owner=`` query parameter to specify the owner of the data being set
    
**DELETE /{id}**
    - Deletes the single object specified by the given ID
    - ``?owner=`` query parameter to specify the owner of the data being set

Authentication
--------------

To authenticate an API call to ThreatConnect, there are two required headers—`Authorization <#authorization>`__ and `Timestamp <#timestamp>`__—which are detailed below:

A complete request should look like:

.. code::

    GET https://app.threatconnect.com/api/v2/indicators?owner=Common%20Community HTTP/1.1
     Timestamp: 1513703787
     Authorization: TC 12345678901234567890:PthSlXIA7rNMow1h8wShfvOnTOhxHd+7njUe4MT4ZSs=

Timestamp
^^^^^^^^^

The required ``Timestamp`` header is a nonce in Unix epoch time (generated by Unix shell with the command: ``date +%s``). The value of the ``Timestamp`` header should look something like ``1513703787``.

.. note:: If the nonce is not within five minutes of the ThreatConnect server's system time, a `Timestamp error <../common_errors.html#timestamp-out-of-acceptable-time-range>`__  will be returned.

Authorization
^^^^^^^^^^^^^

The required ``Authorization`` header has the format: ``TC $ACCESS_ID:$SIGNATURE``.

The ``$ACCESS_ID`` is the ID of the API user you are using to make requests. If you do not have or do not know the API_ID, ask your System Administrator.

The ``$SIGNATURE`` is created by concatenating the API path and query strings, HTTP method, and Timestamp (dicsussed in the previous section) as follows:

``/v2/indicators/hosts/example.com?Owner=Common%20Community:GET:1513703787``

The result is then signed with the user's ``Secret Key`` using SHA256 to calculate an HMAC (a.k.a. ``HMAC-SHA256``) and base-64 encoded.

The value of the final ``Authorization`` header should look like:

.. code::

    TC 12345678901234567890:PthSlXIA7rNMow1h8wShfvOnTOhxHd+7njUe4MT4ZSs=

.. hint:: For Python users, you can view how our `Python SDK <https://docs.threatconnect.com/en/latest/python/python_sdk.html>`__  handles authentication `here <https://github.com/ThreatConnect-Inc/threatconnect-python/blob/fbf428cfff839a5fb5eb19720d23478e563914dc/threatconnect/ThreatConnect.py#L187>`__.

Testing API Connectivity
------------------------

To test API connectivity, start with a request to the ``/v2/owners`` branch to return all Organizations and Communities to which the API credentials have access. An example Bash script for performing this test is available on `GitHub <https://github.com/ThreatConnect-Inc/threatconnect-bash>`_. In this example, you will first update the fields in the ``config.sh`` file, and then execute the ``threatconnect.sh`` file to make the request to the ``/v2/owners`` branch. 

.. note:: If you receive an error while using the script above, make sure that the ``API_HOST`` variable in the ``config.sh`` file is pointed to the correct API for the instance of ThreatConnect you wish to use.

Get a list of all Owners visible to this user:

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

.. hint:: When using this documentation, it will be helpful to have a basic understanding of the `ThreatConnect Data Model <http://kb.threatconnect.com/customer/en/portal/articles/2092925-the-threatconnect-data-model>`_.

