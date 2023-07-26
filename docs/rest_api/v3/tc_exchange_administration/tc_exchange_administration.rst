==========================
TC Exchange Administration
==========================

As of ThreatConnect version 7.2, you can use the ThreatConnect v3 API endpoints to upload and install Apps on TC Exchange™ and generate API and Service tokens in order to run Service Apps locally for testing purposes:

- ``/v3/apps/exchange/install``
- ``/v3/token/api``
- ``/v3/token/svc``

.. attention::
    Your API user account must have a `system role <https://docs.threatconnect.com/en/latest/rest_api/v3/system_roles/system_roles.html>`_ of **Exchange Admin** to use these API endpoints.

Upload and Install Apps on TC Exchange
--------------------------------------

To upload an App to TC Exchange and install it on your ThreatConnect instance, you must send a multipart/form-data request. Refer to the following table for the key-value pairs that may be included in the request.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Key Name
     - Description
     - Required?
   * - allowAllOrgs
     - | Specifies whether to grant all Organizations on the ThreatConnect instance access to the App after it is installed.
       |
       | **Accepted values**:
       |
       | - true
       | - false (default)
     - Optional
   * - allowAppDistribution
     - urlscan.io
     - | Specifies whether to allow the App to be downloaded by App Catalog clients.
       |
       | **Accepted values**:
       |
       | - true
       | - false (default)
    - Optional
   * - fileData
     - The .tcx (App zip) file to be uploaded.
     - Required

For example, the following request will upload the Vault.tcx file to TC Exchange and install the corresponding App with permissions to be used by all Organizations on the ThreatConnect instance:

.. code::
    curl --location --request POST 'https://companyabc.threatconnect.com/api/v3/apps/exchange/install' \
    --header 'Timestamp: $UNIX_EPOCH_TIMESTAMP' \
    --header 'Authorization: TC $ACCESS_ID:$SIGNATURE' \
    --header 'Content-Type: multipart/form-data' \
    --form 'fileData=@"/Users/jsmith/Downloads/Vault.tcx"' \
    --form 'allowAllOrgs="true"'

JSON Response

.. code:: json
    [
        {
            "id": 500,
            "programName": "TCPB - Vault v1",
            "displayName": "Vault",
            "displayPath": null,
            "programVersion": "1.0.0",
            "parent": null
        }
    ]

.. hint::
    For more information about the values used for the ``Timestamp`` and ``Authorization`` headers, refer to the `"Authentication" section of Quick Start <https://docs.threatconnect.com/en/latest/rest_api/quick_start.html#authentication>`_.

Generate API Tokens
-------------------

API tokens may be used to run Service Apps locally for testing. Note that these tokens expire after 4 hours.

Send a request in the following format to generate an API token:

.. code::
    curl --location --request POST 'https://companyabc.threatconnect.com/api/v3/token/api' \
    --header 'Timestamp: $UNIX_EPOCH_TIMESTAMP' \
    --header 'Authorization: TC $ACCESS_ID:$SIGNATURE' \
    --header 'Content-Type: application/json'

JSON Response

.. code:: json
    {
        "status": "Success",
        "data": "API:5:5Aca6d:1687297679443:BxTn+qxRV3p5YzYg+/oIKhbU2QuW2u6C8f06YaRd9Cg="
    }

Generate Service Tokens
-----------------------

Service tokens may be used to run Service Apps locally for testing. To create a Service token, you must provide the ID of the Service to which the token will correspond. Note that these tokens expire after 4 hours.

Step 1: Obtain the Service ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the following database command to obtain the ID of the desired Service:

.. code::
    select * from appcatalogitem where programname like '%TCVC%';

Step 2: Generate a Service Token for the Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After you obtain the ID of the Service you want to test, send a request in the following format to generate a Service token:

.. code::
    curl --location 'https://companyabc.threatconnect.com/api/v3/token/svc' \
    --header 'Timestamp: $UNIX_EPOCH_TIMESTAMP' \
    --header 'Authorization: TC $ACCESS_ID:$SIGNATURE' \
    --header 'Content-Type: application/json' \
    --data '{
        "serviceId": 12345
    }'

.. code:: json
    {
        "status": "Success",
        "data": "SVC:5:savejX:1687291192791:da39a780af56bc0b4521e6cf75b09f1a:357:SJWhTy0R6LgUx0ZI7hDW16/bTL9uJq+lmH68VLMtIHE="
    }

---

*TC Exchange™ is a trademark of ThreatConnect, Inc.*