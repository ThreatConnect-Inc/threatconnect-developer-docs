Create Tags
-----------

To create a new Tag via API, simply add a Tag to a Group, Indicator, Task, or Victim and the new Tag will be created.

Tag descriptions can be written with the following request:

.. code::

   POST /v2/tags

   {
      "name": "Ransomware",
      "description": "Apply this Tag to objects related to ransomware attacks."
   }
   
Response:

.. code::

   {
       "status": "Success",
           "data": {
                "tag": {
                   "name": "Ransomware",
                   "description": "Apply this Tag to objects related to ransomware attacks.",
                   "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=12346&owner=Example+Organization"
               }
           }
   }
   
A Tag's name and description can be edited as follows:

.. code::

   PUT /v2/tags/Ransomware

   {
      "name": "Ransomware Attack",
      "description": "Apply this Tag to Indicators and Groups related to ransomware attacks. Do not apply it to Victims."
   }


For more details, see:

* `Adding Tags to Groups <https://docs.threatconnect.com/en/latest/rest_api/v2/groups/groups.html#create-group-tags>`_ 
* `Adding Tags to Indicators <https://docs.threatconnect.com/en/latest/rest_api/v2/indicators/indicators.html#create-indicator-tags>`_ 
* `Adding Tags to Tasks <https://docs.threatconnect.com/en/latest/rest_api/v2/tasks/tasks.html#create-task-tags>`_ 
* `Adding Tags to Victims <https://docs.threatconnect.com/en/latest/rest_api/v2/victims/victims.html#create-victim-tags>`_ 

.. include:: ../_includes/apply_attack_tags.rst