Create Tags
-----------

To create a new Tag via API, simply add a Tag to a Group, Indicator, Task, or Victim and the new Tag will be created.

Tag descriptions can be written with the following request:

.. code::

   POST /api/v2/tags

   { "name": "myTag", "description": "my description" }
   
Response:

.. code::

   {
       "status": "Success",
           "data": {
                "tag": {
                   "name": "myTag",
                   "description": "my description",
                   "webLink": "https://....com/auth/tags/tag.xhtml?tag=myTag\u0026owner=System"
               }
           }
   }
   
Tag descriptions can be edited as follows:

.. code::

   PUT /api/v2/tags/myTag

   { "name": "myTag", "description": "new desc" }


For more details, see:

* `Adding Tags to Groups <https://docs.threatconnect.com/en/latest/rest_api/groups/groups.html#create-group-tags>`_ 
* `Adding Tags to Indicators <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-indicator-tags>`_ 
* `Adding Tags to Tasks <https://docs.threatconnect.com/en/latest/rest_api/tasks/tasks.html#create-task-tags>`_ 
* `Adding Tags to Victims <https://docs.threatconnect.com/en/latest/rest_api/victims/victims.html#create-victim-tags>`_ 
