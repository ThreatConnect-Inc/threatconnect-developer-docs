Available Fields
----------------

You can retrieve a list of fields for the ``v3/security/users`` endpoint using the following query:

.. code::

    OPTIONS /v3/security/users?show=readonly

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request for the ``users`` object:

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
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
   * - systemRole
     - The user's `System role <https://docs.threatconnect.com/en/latest/rest_api/v3/system_roles/system_roles.html>`_ (all System roles except API User may be used)
     - String
     - FALSE
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
   * - uiTheme
     - Specifies whether to set the ThreatConnect user interface to a light or dark theme for the user (accepted values include "Light" and "Dark")
     - String
     - FALSE
     - TRUE
   * - userName
     - The username for the user's account
     - String
     - TRUE
     - TRUE