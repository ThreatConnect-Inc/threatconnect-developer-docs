HTTP Status Codes
-----------------

The API will return appropriate HTTP response codes to indicate the success or failure of a request. For failed API requests, refer to the ``message`` field included in the response for an explanation as to why the request failed.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - HTTP Status Code
     - Description
   * - 200 - Success
     - The request succeeded.
   * - 201 - Created
     - The request succeeded and created the specified entity.
   * - 400 - Bad Request
     - The request was not formatted properly. The response will include a message with details explaining the formatting issue.
   * - 401 - Unauthorized
     - The API user does not have access to the specified resource or permissions to perform the operation attempted on a resource.
   * - 403 - Forbidden
     - The API user specified an owner that does not exist or to which they do not have access.
   * - 404 - Not Found
     - The requested resource does not exist.
   * - 500 - Internal Server Error
     - An unknown internal error prevented the server from fulfilling the request.
   * - 503 - Service Unavailable
     - The ThreatConnect instance is not licensed to enable the API.