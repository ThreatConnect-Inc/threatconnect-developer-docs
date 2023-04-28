Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/security/users`` endpoint:

.. code::

    OPTIONS /v3/security/users?show=readonly

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/security/users`` endpoint:

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - customTqlTimeout
     - The maximum amount of time, in milliseconds, that ThreatConnect Query Language (TQL) queries made by the user will be allowed to run before timing out
     - Integer
     - FALSE
     - TRUE
   * - disabled
     - Determines whether the user's account is disabled
     - Boolean
     - FALSE
     - TRUE
   * - firstName
     - The user's first name
     - String
     - TRUE
     - TRUE
   * - lastName
     - The user's last name
     - String
     - TRUE
     - TRUE
   * - locked
     - Determines whether the user's account is locked
     - Boolean
     - FALSE
     - TRUE
   * - logoutIntervalMinutes
     - The amount of time, in minutes, after which the user will be logged out of ThreatConnect
     - Integer
     - FALSE
     - TRUE
   * - owner
     - The Organization to which the user belongs
     - String
     - TRUE
     - FALSE
   * - ownerRoles
     - The user's `role within each Organization, Community, or Source <https://docs.threatconnect.com/en/latest/rest_api/v3/owner_roles/owner_roles.html>`_ to which they have access
     - String
     - TRUE
     - FALSE
   * - password
     - The password for the user's account
     - String
     - TRUE
     - TRUE
   * - passwordResetRequired
     - Determines whether the user needs to reset their password the next time they log into ThreatConnect
     - Boolean
     - FALSE
     - TRUE
   * - pseudonym
     - The user's pseudonym
     - String
     - FALSE
     - TRUE
   * - systemRole [1]_
     - The user's `System role <https://docs.threatconnect.com/en/latest/rest_api/v3/system_roles/system_roles.html>`_
     - String
     - TRUE
     - TRUE
   * - termsAccepted
     - Determines whether to present the user with ThreatConnect's terms of service the next time they log into ThreatConnect
     - Boolean
     - FALSE
     - TRUE
   * - twoFactorResetRequired
     - Determines whether to require the user to configure multi-factor authentication (MFA) for their account (or to reset MFA if the user already has it configured)
     - Boolean
     - FALSE
     - TRUE
   * - uiTheme [2]_
     - Specifies whether to set the ThreatConnect user interface to a light or dark theme for the user (accepted values include "Light" and "Dark")
     - String
     - FALSE
     - TRUE
   * - userName
     - The username for the user's account
     - String
     - TRUE
     - TRUE

.. [1] All System roles except **API User** may be assigned to a user.

.. [2] The following are accepted values for the ``uiTheme`` field:

    - ``Light``
    - ``Dark``

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/security/users`` endpoint:

.. code::

    OPTIONS /v3/security/users/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/security/users`` endpoint:

.. code::

    OPTIONS /v3/security/users/tql