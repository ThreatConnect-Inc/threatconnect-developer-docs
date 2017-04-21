Filtering Groups
----------------

This section provides the available filters which can be used when retrieving Groups from ThreatConnect.

**Supported API Filters**

API filters use the API filtering feature to limit the result set returned from the API.

+--------------------------+-------------+-------------------------------------------+
| Filter                   | Value Type  | Description                               |
+==========================+=============+===========================================+
| ``add_id()``             | int         | Filter Groups by ID.                      |
+--------------------------+-------------+-------------------------------------------+
| ``add_adversary_id()``   | int         | Filter Groups on associated Adversary ID. |
+--------------------------+-------------+-------------------------------------------+
| ``add_campaign_id()``    | int         | Filter Groups on associated Campaign ID.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_document_id()``    | int         | Filter Groups on associated Document ID.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_email_id()``       | int         | Filter Groups on associated Email ID.     |
+--------------------------+-------------+-------------------------------------------+
| ``add_incident_id()``    | int         | Filter Groups on associated Incident ID.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_indicator()``      | str         | Filter Groups on associated Indicator.    |
+--------------------------+-------------+-------------------------------------------+
| ``add_owner()``          | list or str | Filter Groups on Owner.                   |
+--------------------------+-------------+-------------------------------------------+
| ``add_security_label()`` | str         | Filter Groups on applied Security Label.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_signature_id()``   | int         | Filter Groups on associated Signature ID. |
+--------------------------+-------------+-------------------------------------------+
| ``add_tag()``            | str         | Filter Groups on applied Tag.             |
+--------------------------+-------------+-------------------------------------------+
| ``add_task_id()``        | int         | Filter Groups on associated Task ID.      |
+--------------------------+-------------+-------------------------------------------+
| ``add_threat_id()``      | int         | Filter Groups on associated Threat ID.    |
+--------------------------+-------------+-------------------------------------------+
| ``add_victim_id()``      | int         | Filter Groups on associated Victim ID.    |
+--------------------------+-------------+-------------------------------------------+

**Supported Post Filters**

Post filters are applied on the results returned by the API request.

+-------------------------+------------+------------------------------+
| Filter                  | Value Type | Description                  |
+=========================+============+==============================+
| ``add_pf_name()``       | str        | Filter Groups on name.       |
+-------------------------+------------+------------------------------+
| ``add_pf_date_added()`` | str        | Filter Groups on date added. |
+-------------------------+------------+------------------------------+

The example below demonstrates how to use the ``add_pf_name()`` filter to find a group with the name "Example Group".

.. code-block:: python
    :linenos:
    :emphasize-lines: 13-15

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # create a Groups object
    groups = tc.groups()

    owner = 'Example Community'
    filter1 = groups.add_filter()
    # only retrieve groups from the given owner
    filter1.add_owner(owner)

    desired_group_name = 'Example Group'
    # add a filter for groups whose name matches the desired_group_name
    filter1.add_pf_name(desired_group_name)

    try:
        # retrieve Groups
        groups.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for group in groups:
        print(group.id)
        print(group.name)
        print(group.date_added)
        print(group.weblink)

        # Group specific property
        print(group.type)
        print("")

The example below demonstrates how to use the ``add_pf_date_added()`` filter to find all groups added within the past seven days.

.. code-block:: python
    :linenos:
    :emphasize-lines: 20,22-23

    import datetime

    from threatconnect.Config.FilterOperator import FilterOperator

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # create a Groups object
    groups = tc.groups()

    owner = 'Example Community'
    filter1 = groups.add_filter()
    # only retrieve groups from the given owner
    filter1.add_owner(owner)

    # get a datestamp for the past week
    today = datetime.datetime.today()
    delta = datetime.timedelta(days = 7)
    datestamp = (today - delta).isoformat() + "Z"

    # add a filter to see all groups with a date added datestamp greater than (thus, more recent) than the datestamp
    filter1.add_pf_date_added(datestamp, FilterOperator.GE)

    try:
        # retrieve Groups
        groups.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for group in groups:
        print(group.id)
        print(group.name)
        print(group.date_added)
        print(group.weblink)

        # Group specific property
        print(group.type)
        print("")

.. note:: Both of the examples above will first retrieve *all* of the groups from the owner and will then apply the post filter.
