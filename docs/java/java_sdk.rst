Java SDK
========

Getting Started with Java SDK
-----------------------------

-  Install `Java JDK
   7+ <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`__
-  Import `Java SDK for
   ThreatConnect <https://github.com/ThreatConnect-Inc/threatconnect-java>`__
-  Create an API User, refer to `REST API documentation <../rest_api/quick_start.html#creating-an-api-key>`__

Maven™ Configuration
~~~~~~~~~~~~~~~~~~~~

Add the following entries to your POM (project object model) file. This
is the preferred method to use the SDK:

.. code:: xml

       <properties>
            <threatconnect-sdk.version>2.7.3</threatconnect-sdk.version>
        </properties>


    <!-- sdk dependency -->
        <dependencies>
            <dependency>
                <groupId>com.threatconnect.sdk.core</groupId>
                <artifactId>threatconnect-sdk</artifactId>
                <version>${threatconnect-sdk.version}</version>
            </dependency>
        </dependencies>

Programmatic Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to the API using the SDK, create a Configuration object with
one of the following constructors:

.. code:: java

       public Configuration(String tcApiUrl, String tcApiAccessID, String tcApiUserSecretKey, String defaultOwner);
       public Configuration(String tcApiUrl, String tcApiAccessID, String tcApiUserSecretKey, String defaultOwner, Integer resultLimit);

Pass the ``Configuration`` object when creating a new ``Connection``.
(See examples in the Reader and Writer sections.)

Configuration using Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This property can be defined in two ways:

In the JVM (Java virtual machine), you can call your program with the
following -D property flag:

``threatconnect.api.config=<YOUR CONFIG FILE LOCATION>``

Or the system property can be directly set at runtime using the
following code:

.. code:: java

    System.getProperties().setProperty("threatconnect.api.config", "<YOUR CONFIG FILE LOCATION>");

Once the configuration has been set up, the examples in this document
should be executable, as long as the Java SDK for ThreatConnect is part
of the classpath. See the following examples for a typical start-up
script.

On Windows:

.. code:: shell

     java -cp ".;threatconnect-sdk-<version>.jar" -Dthreatconnect.api.config=myConfig.properties TestClass

On Linux:

.. code:: shell

    java -cp ".:./threatconnect-sdk-<version>.jar" -Dthreatconnect.api.config=myConfig.properties TestClass

The Java SDK will need to be configured with an Access ID and Secret
Key. When a no-arg ``Configuration`` constructor is called, the SDK
searches system properties for the "threatconnect.api.config" property.

The configuration file should contain the following lines at a minimum:

``connection.tcApiUrl=https://api.threatconnect.com``

``connection.tcApiAccessID=<YOUR API ACCESS ID>``

``connection.tcApiUserSecretKey=<YOUR API SECRET KEY>``

.. note:: If you are working with the ThreatConnect **sandbox**, the connection.tcApiUrl should be: ``https://sandbox.threatconnect.com/api``.

Third-Party Dependencies

The SDK utilizes these open-source libraries primarily for RESTful
communication and JSON (JavaScript Object Notation) parsing.

+----------------------+-----------+--------------------+
| Library              | Version   | Used by            |
+======================+===========+====================+
| HTTP Core            | 4.4.1     | SDK                |
+----------------------+-----------+--------------------+
| HTTP Client          | 4.4.1     | SDK                |
+----------------------+-----------+--------------------+
| Commons Logging      | 1.2       | HTTP Client        |
+----------------------+-----------+--------------------+
| Commons Codec        | 1.9       | HTTP Client        |
+----------------------+-----------+--------------------+
| Jackson Core         | 2.5.3     | SDK                |
+----------------------+-----------+--------------------+
| Jackson Databind     | 2.5.3     | SDK                |
+----------------------+-----------+--------------------+
| Jackson Annotation   | 2.5.0     | Jackson Databind   |
+----------------------+-----------+--------------------+

Technical Design

The Java SDK for ThreatConnect was designed with a focus on abstracting
the API REST calls while enabling the developer to use an
enterprise-level programming language. The abstraction layer is
relatively "thin" because it coincides directly with all of the REST API
calls. In fact, the entities themselves were ported directly from the
ThreatConnect API to enable consistent communication between the Java
SDK and the REST API.

.. figure:: ../_static/sdk-design.png
   :alt: SDK Technical Design

   SDK Design

The Java library was designed with common programming design patterns.
You’ll notice the "Adapter" pattern used to manage the interaction with
the API connection and REST calls. The Java SDK depends on the Apache
HTTP components open-source library to handle these calls. Because
instantiating an Adapter requires a low-level RequestExecutor, a
"Factory" design pattern was utilized to expose reading/writing
functionality in a simplified way.

Java generics are used to type many of the Adapters in an effort to
reuse code, as most readers share functional resources. Below is a
diagram that will help illustrate common interactions between different
classes (Note: Names are conceptual to illustrate interaction. Actual
class names and methods will be discussed later in this document) . All
interactions with the Java SDK will follow this programmatic idiom.

.. figure:: ../_static/sdk-arch.png
   :alt: SDK Architecture

   SDK Architecture

To facilitate interaction with the full set of Java SDK readers and
writers, the use of ReaderAdapterFactory and WriterAdapterFactory,
respectively, is highly recommended.

Example Java App
----------------

Once retrieved, the adversary objects will be printed to the console.

.. code-block:: java
    :linenos:
    :lineno-start: 1

    import com.threatconnect.sdk.client.reader.AbstractGroupReaderAdapter;
    import com.threatconnect.sdkb.client.reader.ReaderAdapterFactory;
    import com.threatconnect.sdk.conn.Connection;
    import com.threatconnect.sdkb.exception.FailedResponseException;
    import com.threatconnect.sdkb.server.entity.Adversary;
    import java.io.IOException;
    import java.util.List;
    
    public class GroupExample {
    
        public static void main(String[] args) {
        
            Connection conn = null;
            
            try {
                
                System.getProperties().setProperty("threatconnect.api.config", "/config.properties");
                conn = new Connection();
                
                AbstractGroupReaderAdapter<Adversary> reader = ReaderAdapterFactory.createAdversaryGroupReader(conn);
                List<Adversary> data = reader.getAll("System");
                for (Adversary g : data ) {
                    System.out.println( "Adversary: " + g.toString() );
                }   
                
            } catch (IOException | FailedResponseException ex) {
                System.err.println("Error: " + ex);
            } finally {
                if ( conn != null )     conn.disconnect();
            }   
            
        }   
        
    }   

To write the first program using the Java SDK for the ThreatConnect API,
an Adversary reader that pulls all adversaries belonging to the "System"
Organization must be created.

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 1-7          | Notable imports include: The                                |
|              | ``com.threatconnect.sdk.client.reader`` package holds all      |
|              | Adapter classes that read data from the API. The            |
|              | ``com.threatconnect.sdk.server.entity`` package holds all      |
|              | entities returned by the Java SDK.                          |
+--------------+-------------------------------------------------------------+
| 17-18        | The platform programmatically define the system property to |
|              | load the configuration file. This allows the developer to   |
|              | instantiate Connection objects (line 18) with a no-arg      |
|              | constructor. If the ``threatconnect.api.config`` property   |
|              | is not defined, the developer has the option of passing the |
|              | configuration file name string in the single-arg Connection |
|              | constructor.                                                |
+--------------+-------------------------------------------------------------+
| 20           | To create an AbstractGroupReaderAdapter object: Use the     |
|              | ReaderAdapterFactory pattern and generics to enforce        |
|              | compile-time type constraints on this abstract class. Then  |
|              | pass the connection object used by the Adapter to interact  |
|              | with the ThreatConnect API.                                 |
+--------------+-------------------------------------------------------------+
| 21           | Using the reader object, call ``getAll()`` method and pass  |
|              | it the Organization string name to return all Adversaries   |
|              | for the "System" Organization.                              |
+--------------+-------------------------------------------------------------+
| 22-24        | Iterate through the data collection to print the contents   |
|              | to the console.                                             |
+--------------+-------------------------------------------------------------+
| 26           | The IOException is potentially thrown if the Connection     |
|              | object cannot find the properties file. The                 |
|              | FailedResponseException is thrown if the API request is     |
|              | invalid.                                                    |
+--------------+-------------------------------------------------------------+
| 29           | In all cases when processing is complete, call              |
|              | ``disconnect()`` on the connection object to release        |
|              | resources.                                                  |
+--------------+-------------------------------------------------------------+

**Summary**

This section explained:

-  How to connect to the ThreatConnect API by passing the configuration
   file in system properties
-  How to get a list of adversaries for the "System" Organization
-  What types of exceptions a connection and read operation can
   potentially throw
-  How to close a ThreatConnect API connection

Deploying a Java App
--------------------

Apps must be packaged and deployed into ThreatConnect's application
runtime environment.

**Supported Version**

ThreatConnect Java integrations require Oracle JRE 7 or later. OpenJRE
is not supported.

**Third-Party Libraries**

These libraries are automatically included in the classpath of every
Java app. There is no need to include these libraries in the
installation zip file. There is also no need to include these libraries
in the ``configuration`` variable named ``java.classpath``.

+---------------------------------------------------------------------------------+---------+
| Library                                                                         | Version |
+=================================================================================+=========+
| `ThreatConnect SDK <https://github.com/ThreatConnect-Inc/threatconnect-java>`__ | 2.0.0   |
+---------------------------------------------------------------------------------+---------+
| `HTTP Core <https://hc.apache.org/httpcomponents-core-ga/>`__                   | 4.4.1   |
+---------------------------------------------------------------------------------+---------+
| `HTTP Client <https://hc.apache.org/httpcomponents-client-ga/>`__               | 4.4.1   |
+---------------------------------------------------------------------------------+---------+
| `Commons Logging <http://commons.apache.org/proper/commons-logging/>`__         | 1.2     |
+---------------------------------------------------------------------------------+---------+
| `Commons Codec <https://commons.apache.org/proper/commons-codec/>`__            | 1.9     |
+---------------------------------------------------------------------------------+---------+
| `Jackson Core <https://github.com/FasterXML/jackson-core>`__                    | 2.5.3   |
+---------------------------------------------------------------------------------+---------+
| `Jackson Databind <https://github.com/FasterXML/jackson-databind/>`__           | 2.5.3   |
+---------------------------------------------------------------------------------+---------+
| `Jackson Annotation <https://github.com/FasterXML/jackson-annotations>`__       | 2.5.0   |
+---------------------------------------------------------------------------------+---------+

Deployment Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

Apps use a deployment configuration file to define variables and execution environment. You can read more about the deployment configuration file `here <../deployment_config.html>`_.

Command-Line Parameters
-----------------------

The application runtime environment passes standard parameters to all
jobs as part of its standard sandbox container. There should be no
assumptions made on the naming or existence of paths passed in these
variables outside of the lifetime of the job execution. Because all job
executions are run in a sandboxed environment, app developers should
never hard-code ThreatConnect Parameters.

+----------------------+-------------------------------------------------------------+
| ThreatConnect        | Description                                                 |
| Parameter            |                                                             |
+======================+=============================================================+
| ``tc_log_path``      | Log path for the specific instance of the job execution.    |
|                      |                                                             |
+----------------------+-------------------------------------------------------------+
| ``tc_tmp_path``      | Temporary storage path for the specific instance of thejob  |
|                      | execution.                                                  |
+----------------------+-------------------------------------------------------------+
| ``tc_out_path``      | Output path for the specific instance of the job execution. |
|                      |                                                             |
+----------------------+-------------------------------------------------------------+
| ``tc_api_path``      | Path to the ThreatConnect API server.                       |
|                      |                                                             |
+----------------------+-------------------------------------------------------------+

Job Results
~~~~~~~~~~~

Job executions can use a special file called ``results.tc`` to write
results as a mechanism for updating parameters for subsequent runs. A
use case for this feature is an app that needs to know the last time it
completed successfully in order to process data since that completion.
The parameter definitions are quite flexible, with the only restriction
being that the parameters written to the ``results.tc`` file must exist
in the ``configuration`` file in order to be persisted.

Example ``results.tc`` file:

``param.last_completed_time = 1430619556``

Assuming there is a property with the same name in ``configuration``,
the job executor will update the new property value in the system for
the next run. The property will only be stored if the job execution is
successful. This file should be written to the ``tc_out_path`` passed as
one of the standard ThreatConnect parameters.

Exit Codes
~~~~~~~~~~

There are standard exit codes that the application runtime environment
uses to report whether a program completed successfully. The Java app is
responsible for calling ``System.exit(N)``, where 'N' is the appropriate
exit code highlighted below:

When ``System.exit()`` is not called by the app, an exit code of zero is
returned by default during normal code execution. System-critical errors
(e.g., file not found) return non-zero exit codes. The developer is
responsible for catching and handling program errors accordingly.

At times a program may want to report a partial failure (e.g., batch
process where X out of Y updates completed). In cases of partial
failure, the system administrator can retrieve the log file for that job
execution and view more detailed output from the program run.

The contents of message.tc are typically written any time the program
exits normally or through an error:

+-------------------+------------------------------------------------------------------+
| Status            | Description                                                      |
+===================+==================================================================+
| Success           | Exit code 0 - Process completed successfully.                    |
+-------------------+------------------------------------------------------------------+
| Partial Failure   | Exit code 3 - Process had a partial failure.                     |
+-------------------+------------------------------------------------------------------+
| Failure           | Any value not 0 or 3 (typically Exit code 1) - Process failed.   |
+-------------------+------------------------------------------------------------------+

Exit Message File
~~~~~~~~~~~~~~~~~

Exit codes provide a mechanism to report status at a high level. For
more granular control of the exit message displayed to the user, the app
can write a message to the ``tc_out_path`` directory under the file
named ``message.tc``. All content in this file should be limited to 255
characters or less. The job executor reads this file after execution
completes on each job and displays the contents in the Job table detail
tip.

.. figure:: ../_static/exit-message-tip.png
   :alt: Exit Message

   Exit Message

The Reader Package
------------------

The Reader package is the primary package to retrieve data from the
ThreatConnect API. It covers all available resources exposed through the
ThreatConnect API. The primary classes in the Reader Package, which
encompass all read functionality from the API, are listed below.

+---------------------------------------------------------+---------------------------------+
| Class                                                   | *Description*                   |
+=========================================================+=================================+
| ``ReaderAdapterFactory``                                | Primary entry point to          |
|                                                         | instantiate all readers in the  |
|                                                         | Reader Package.                 |
+---------------------------------------------------------+---------------------------------+
| ``AbstractGroupReaderAdapter<T extends Group>``         | Generic Group Reader Abstract   |
|                                                         | class. Concrete object          |
|                                                         | available in                    |
|                                                         | ReaderAdapterFactory.           |
+---------------------------------------------------------+---------------------------------+
| ``AbstractIndicatorReaderAdapter<T extends Indicator>`` | Generic Indicator Reader        |
|                                                         | Abstract class. Concrete object |
|                                                         | available in                    |
|                                                         | ReaderAdapterFactory.           |
+---------------------------------------------------------+---------------------------------+
| ``AbstractReaderAdapter``                               | Base Abstract Reader for all    |
|                                                         | Reader Adapters in the Reader   |
|                                                         | Package.                        |
+---------------------------------------------------------+---------------------------------+
| ``OwnerReaderAdapter``                                  | Concrete Reader for             |
|                                                         | Organization owner data.        |
|                                                         | Convenience object available in |
|                                                         | ReaderAdapterFactory.           |
+---------------------------------------------------------+---------------------------------+
| ``SecurityLabelReaderAdapter``                          | Concrete Reader for             |
|                                                         | SecurityLabel data. Convenience |
|                                                         | object available in             |
|                                                         | ReaderAdapterFactory.           |
+---------------------------------------------------------+---------------------------------+
| ``TagReaderAdapter``                                    | Concrete Reader for Tag data.   |
|                                                         | Convenience object available in |
|                                                         | ReaderAdapterFactory.           |
+---------------------------------------------------------+---------------------------------+
| ``TaskReaderAdapter``                                   | Concrete Reader for Task data.  |
|                                                         | Convenience object available in |
|                                                         | ReaderAdapterFactory.           |
+---------------------------------------------------------+---------------------------------+
| ``VictimReaderAdapter``                                 | Concrete Reader for Victim      |
|                                                         | data. Convenience object        |
|                                                         | available in                    |
|                                                         | ReaderAdapterFactory.           |
+---------------------------------------------------------+---------------------------------+

Reader Factory
~~~~~~~~~~~~~~

The ReaderAdapterFactory class is, effectively, the "hub" for reader
Adapters. It provides convenience objects for all the Adapters in the
Reader Package. Below is a list of the static methods and return types
of the ReaderAdapterFactory:


+---------------------------------------------------------+----------------------------------------------------+
| Type                                                    | Method                                             |
+=========================================================+====================================================+
| ``static AbstractGroupReaderAdapter<Adversary>``        | createAdversaryGroupReader(Connection conn)        |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Email>``            | createEmailGroupReader(Connection conn)            |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Incident>``         | createIncidentGroupReader(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Signature>``        | createSignatureGroupReader(Connection conn)        |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Threat>``           | createThreatGroupReader(Connection conn)           |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<Address>``      | createAddressIndicatorReader(Connection conn)      |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<EmailAddress>`` | createEmailAddressIndicatorReader(Connection conn) |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<File>``         | createFileIndicatorReader(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<Host>``         | createHostIndicatorReader(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<Url>``          | createUrlIndicatorReader(Connection conn)          |
+---------------------------------------------------------+----------------------------------------------------+
| ``static BatchReaderAdapter<Indicator>``                | createIndicatorBatchReader(Connection conn)        |
+---------------------------------------------------------+----------------------------------------------------+
| ``static DocumentReaderAdapter``                        | createDocumentReader(Connection conn)              |
+---------------------------------------------------------+----------------------------------------------------+
| ``static OwnerReaderAdapter``                           | createOwnerReader(Connection conn)                 |
+---------------------------------------------------------+----------------------------------------------------+
| ``static SecurityLabelReaderAdapter``                   | createSecurityLabelReader(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static TagReaderAdapter``                             | createTagReader(Connection conn)                   |
+---------------------------------------------------------+----------------------------------------------------+
| ``static TaskReaderAdapter``                            | createTaskReader(Connection conn)                  |
+---------------------------------------------------------+----------------------------------------------------+
| ``static VictimReaderAdapter``                          | createVictimReader(Connection conn)                |
+---------------------------------------------------------+----------------------------------------------------+

Reader Factory Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

      1 import com.threatconnect.sdk.client.reader.AbstractGroupReaderAdapter;
      2 import com.threatconnect.sdk.client.reader.ReaderAdapterFactory;
      3 import com.threatconnect.sdk.conn.Connection;
      4 import com.threatconnect.sdk.exception.FailedResponseException;
      5 import com.threatconnect.sdk.server.entity.Adversary;
      6 import com.threatconnect.sdk.server.entity.Email;
      7 import com.threatconnect.sdk.server.entity.Group;
      8 import com.threatconnect.sdk.server.entity.Incident;
      9 import com.threatconnect.sdk.server.entity.Signature;
     10 import com.threatconnect.sdk.server.entity.Threat;
     11 import java.io.IOException;
     13 
      
     53     private static void doGetById(Connection conn) throws IOException, FailedResponseException {
     54 
     55         AbstractGroupReaderAdapter reader = ReaderAdapterFactory.createAdversaryGroupReader(conn);
     56         IterableResponse<Group> data = reader.getAllGroups();
     57         for (Group group : data) {
     58             System.err.println("Checking group.class=" + group.getClass() + ", type=" + group.getType());
     59             Group result = null;
     60             switch( Group.Type.valueOf(group.getType()) ) {
     61                 case Adversary:
     62                     AbstractGroupReaderAdapter<Adversary> adversaryReader 
     63                         = ReaderAdapterFactory.createAdversaryGroupReader(conn);
     64                     // "result" is assigned an Adversary object
     65                     result = adversaryReader.getById(group.getId(),group.getOwnerName());
     66                     break;
     67                 case Email:
     68                     AbstractGroupReaderAdapter<Email> emailReader 
     69                         = ReaderAdapterFactory.createEmailGroupReader(conn);
     70                     // "result" is assigned an Email object
     71                     result = emailReader.getById(group.getId(), group.getOwnerName());  
     72                     break;
     73                 case Incident:
     74                     AbstractGroupReaderAdapter<Incident> incidentReader 
     75                         = ReaderAdapterFactory.createIncidentGroupReader(conn);
     76                     // "result" is assigned an Incident object
     77                     result = incidentReader.getById(group.getId(), group.getOwnerName()); 
     78                     break;
     79                 case Signature:
     80                     AbstractGroupReaderAdapter<Signature> sigReader 
     81                         = ReaderAdapterFactory.createSignatureGroupReader(conn);
     82                     // "result" is assigned a Signature object
     83                     result = sigReader.getById(group.getId(), group.getOwnerName() ); 
     84                     break;
     85                 case Threat:
     86                     AbstractGroupReaderAdapter<Threat> threatReader 
     87                         = ReaderAdapterFactory.createThreatGroupReader(conn);
     88                     // "result" is assigned a Threat object
     89                     result = threatReader.getById(group.getId(), group.getOwnerName() ); 
     90                     break;
     91                 default: 
     92                     System.err.println("Unknown Group Type: " + group.getType() );
     93                     break;
     94             }
     95 
     96             assert result.getId().equals(group.getId());
     97         }
     98 
     99     }

This example continues building from the first one and uses more
Adapters available in the Reader Package. The following example reads
all Groups available to the "System" Organization. It then proceeds to
iterate through each Group, printing and performing "getById()" lookups
to get the full Group object from the ThreatConnect API. (Note: An
ellipsis (...) has been substituted for code sections removed for
brevity.)

There are more concise ways of handling reading data and purely checking
its ID. This code is written in a more verbose form strictly to
illustrate the usage of different methods in the ReaderFactory.

+--------+-------------------------------------------------------------------+
| Line   | Description                                                       |
+========+===================================================================+
| 5-10   | Notice how all Group-level entities in the imports are added.     |
|        | Results from reader Adapters will return an entity or a           |
|        | collection of entities from the                                   |
|        | ``com.threatconnect.sdk.server.entity`` package.                  |
+--------+-------------------------------------------------------------------+
| 52-53  | Groups to which the current API user has access under the         |
|        | "System" Organization should be retrieved. All                    |
|        | AbstractGroupReaderAdapter’s have access to the                   |
|        | ``getAllGroups()`` method—it returns a collection of Group        |
|        | objects for the "System" Organization from the ThreatConnect API. |
+--------+-------------------------------------------------------------------+
| 60     | To illustrate the different instantiations, a switch statement on |
|        | the generic Group object is used.                                 |
+--------+-------------------------------------------------------------------+
| 61-63  | Based on the Group.Type enum value (in this section,              |
|        | "Adversary"), an AdversaryGroupReader object is created from the  |
|        | ReaderAdapterFactory. The assignment to the adversaryReader       |
|        | variable is typed using generics to enforce compile time checks   |
|        | on the data returned from this reader.                            |
+--------+-------------------------------------------------------------------+
| 65     | The ``getById()`` method to retrieve the proper Adversary Group   |
|        | data, based on the ID and Organization name, from the             |
|        | ThreatConnect API, is used here. The ``result`` variable is       |
|        | assigned an Adversary-type object.                                |
+--------+-------------------------------------------------------------------+
| 67-90  | The remaining case statement blocks will check for different      |
|        | Group types, but, effectively, does the same operation. Take some |
|        | time to review these blocks to understand how the ReaderFactory   |
|        | facilitates the creation of proper readers.                       |
+--------+-------------------------------------------------------------------+
| 96     | Here the Group ID is compared against the result ID returned by   |
|        | the ``getById`` method to assert that they are, in fact, the same |
|        | entity.                                                           |
+--------+-------------------------------------------------------------------+

IterableResponse Class
~~~~~~~~~~~~~~~~~~~~~~

Using this iterable, the developer can utilize traditional ``iterator()`` methods to iterate through the results, or, more concisely, the Java for each loop is as follows:

.. code:: java

        IterableResponse<Address> data = reader.getAll();
        for(Address a : data) {
           System.out.println("Address: " + a); 
        }

In the previous example, the ``IterableResponse`` class retrieves all
Groups for the default owner. The ``IterableResponse`` class is the
primary type returned by all collection-based reader operations.
Typically, a collection, like a ``List``, would be expected in this
scenario, but to resolve the paging limits of the ThreatConnect API, the
``IterableResponse`` was created.

All paging is performed behind the scenes, allowing the developer to
rely on an Iterable to fulfill its contract and return a ``hasNext()``
of false when there are no more results. The Iterable will make use of
the ``resultLimit`` value defined during the creation of the
``Configuration`` object.

Reader Class Overview
---------------------

While the main entry point to the Reader Package is the ReaderFactory,
getting familiar with the main Adapters helps developers understand how
to interact with the data returning from the ThreatConnect API. Although
there is extensive use of Java Generics, the method-naming conventions
will be familiar and self-explanatory. Parameter naming conventions have
been kept abstract to more accurately reflect the identifiers being
passed.

Parameter Naming Convention
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+------------------------------------+
| Type                 | Description                        |
+======================+====================================+
| ``uniqueId``         | Identifier for the reader/writer   |
|                      | Group or Incident Adapter type.    |
|                      | For Groups, this is an Integer     |
|                      | that requires an Adversary ID,     |
|                      | Email ID, Incident ID, Signature   |
|                      | ID, or Threat ID. This identifier  |
|                      | is system generated when the group |
|                      | is created in ThreatConnect. For   |
|                      | Indicators, this is a String that  |
|                      | requires an IP Address, Email      |
|                      | Address, File Hash, Host Name, or  |
|                      | URL text. This identifier is user  |
|                      | generated when the Indicator is    |
|                      | created in ThreatConnect.          |
+----------------------+------------------------------------+
| ``victimId``         | Identifier for the Victim Adapter  |
|                      | type. This identifier is an        |
|                      | Integer created by the system when |
|                      | the Victim entry is created in     |
|                      | ThreatConnect.                     |
+----------------------+------------------------------------+
| ``assetId``          | Identifier for the VictimAsset     |
|                      | Adapter type. This identifier is   |
|                      | an Integer created by the system   |
|                      | when the VictimAsset is created in |
|                      | ThreatConnect. This identifier     |
|                      | represents a VictimEmailAddress    |
|                      | ID, VictimNetworkAccount ID,       |
|                      | VictimPhone ID,                    |
|                      | VictimSocialNetwork ID, or         |
|                      | VictimWebsite ID.                  |
+----------------------+------------------------------------+
| ``securityLabel``    | Identifier for SecurityLabel       |
|                      | Adapter type. This is a            |
|                      | user-provided String that          |
|                      | represents the Security Label.     |
+----------------------+------------------------------------+
| ``tagName``          | Identifier for Iag Adapter type.   |
|                      | This is a user-provided String     |
|                      | that represents the Tag.           |
+----------------------+------------------------------------+

The AbstractGroupReaderAdapter is the object returned when GroupReader
is called from the ReaderFactory. These GroupReader instantiations were
reviewed in the last example.

The Java SDK library for ThreatConnect comes with JavaDocs in the
"apidocs" directory, which is an additional reference to the Java SDK.

Filtering
~~~~~~~~~

Example filter usage:

.. code:: java

    IterableResponse<Url> urls 
      = urlReader.getForFilters("System", // owners
                                 true,                              // OR filters 
                                 ApiFilterType.filterConfidence()   // filter:
                                              .greaterThan(50),     // confidence > 50
                                 ApiFilterType.filterRating()       // filter:
                                              .greaterThan(2.5));   // rating > 2.5

| ``ApiFilterType``\ exposes a builder pattern that can be used to build
  filters for indicators, groups, documents, tags, and victims.
| Filters can be passed to the ``getForFilters(...)`` method in the
  ``AbstractBaseReader`` class.

AbstractGroupReaderAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below get data for the Group type (T) linked to this
Adapter. The uniqueId (P) for Groups is an Integer.

+-------------------------+----------------------------------------------------------------------------+
| Type                    | Method                                                                     |
+=========================+============================================================================+
| ``T``                   | getById(P uniqueId)                                                        |
+-------------------------+----------------------------------------------------------------------------+
| ``T``                   | getById(P uniqueId, String ownerName)                                      |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getForFilters(String ownerName, boolean orParams, ApiFilterType...filters) |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll()                                                                   |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll(String ownerName)                                                   |
+-------------------------+----------------------------------------------------------------------------+

The methods below get generic Group objects associated to this Group
type (T).

+-----------------------------+--------------------------------+
| Type                        | Method                         |
+=============================+================================+
| ``IterableResponse<Group>`` | getAllGroups()                 |
+-----------------------------+--------------------------------+
| ``IterableResponse<Group>`` | getAllGroups(String ownerName) |
+-----------------------------+--------------------------------+
| ``String``                  | getAllGroupsAsText()           |
+-----------------------------+--------------------------------+

Associated Groups
~~~~~~~~~~~~~~~~~

The methods below get associated Group elements by distinct type.

+---------------------------------+--------------------------------------------------------------------------------------+
| Type                            | Method                                                                               |
+=================================+======================================================================================+
| ``IterableResponse<Group>``     | getAssociatedGroups(Integer uniqueId)                                                |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Group>``     | getAssociatedGroups(Integer uniqueId, String ownerName)                              |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Adversary>`` | getAssociatedGroupAdversaries(Integer uniqueId)                                      |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Adversary>`` | getAssociatedGroupAdversaries(Integer uniqueId, String ownerName)                    |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Adversary``                   | getAssociatedGroupAdversary(Integer uniqueId, Integer adversaryId)                   |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Adversary``                   | getAssociatedGroupAdversary(Integer uniqueId, Integer adversaryId, String ownerName) |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Email>``     | getAssociatedGroupEmails(Integer uniqueId)                                           |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Email>``     | getAssociatedGroupEmails(Integer uniqueId, String ownerName)                         |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Email``                       | getAssociatedGroupEmail(Integer uniqueId, Integer emailId)                           |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Email``                       | getAssociatedGroupEmail(Integer uniqueId, Integer emailId, String ownerName)         |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Incident>``  | getAssociatedGroupIncidents(Integer uniqueId)                                        |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Incident>``  | getAssociatedGroupIncidents(Integer uniqueId, String ownerName)                      |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Incident``                    | getAssociatedGroupIncident(Integer uniqueId, Integer incidentId)                     |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Incident``                    | getAssociatedGroupIncident(Integer uniqueId, Integer incidentId, String ownerName)   |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Signature>`` | getAssociatedGroupSignatures(Integer uniqueId)                                       |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Signature>`` | getAssociatedGroupSignatures(Integer uniqueId, String ownerName)                     |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Signature``                   | getAssociatedGroupSignature(Integer uniqueId, Integer signatureId)                   |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Signature``                   | getAssociatedGroupSignature(Integer uniqueId, Integer signatureId, String ownerName) |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Threat>``    | getAssociatedGroupThreats(Integer uniqueId)                                          |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Threat>``    | getAssociatedGroupThreats(Integer uniqueId, String ownerName)                        |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Threat``                      | getAssociatedGroupThreat(Integer uniqueId, Integer threatId)                         |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Threat``                      | getAssociatedGroupThreat(Integer uniqueId, Integer threatId, String ownerName)       |
+---------------------------------+--------------------------------------------------------------------------------------+

Associated Indicators
~~~~~~~~~~~~~~~~~~~~~

The methods below get associated Indicator elements by distinct types.

+---------------------------------+--------------------------------------------------------------------------------------+
| Type                            | Method                                                                               |
+=================================+======================================================================================+
| ``IterableResponse<Indicator>`` | getAssociatedIndicators(Integer uniqueId)                                            |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Indicator>`` | getAssociatedIndicators(Integer uniqueId, String ownerName)                          |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Address>``   | getAssociatedIndicatorAddresses(Integer uniqueId)                                    |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Address>``   | getAssociatedIndicatorAddresses(Integer uniqueId, String ownerName)                  |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Address``                     | getAssociatedIndicatorAddress(Integer uniqueId, String ipAddress)                    |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Address``                     | getAssociatedIndicatorAddress(Integer uniqueId, String ipAddress, String ownerName)  |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Email>``     | getAssociatedIndicatorEmails(Integer uniqueId)                                       |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Email>``     | getAssociatedIndicatorEmails(Integer uniqueId, String ownerName)                     |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Email``                       | getAssociatedIndicatorEmail(Integer uniqueId, String emailAddress)                   |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Email``                       | getAssociatedIndicatorEmail(Integer uniqueId, String emailAddress, String ownerName) |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<File>``      | getAssociatedIndicatorFiles(Integer uniqueId)                                        |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<File>``      | getAssociatedIndicatorFiles(Integer uniqueId, String ownerName)                      |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``File``                        | getAssociatedIndicatorFile(Integer uniqueId, String fileHash)                        |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Host>``      | getAssociatedIndicatorHosts(Integer uniqueId)                                        |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Host>``      | getAssociatedIndicatorHosts(Integer uniqueId, String ownerName)                      |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Host``                        | getAssociatedIndicatorHost(Integer uniqueId, String hostName)                        |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Host``                        | getAssociatedIndicatorHost(Integer uniqueId, String hostName, String ownerName)      |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Url>``       | getAssociatedIndicatorUrls(Integer uniqueId)                                         |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<Url>``       | getAssociatedIndicatorUrls(Integer uniqueId, String ownerName)                       |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Url``                         | getAssociatedIndicatorUrl(Integer uniqueId, String urlText)                          |
+---------------------------------+--------------------------------------------------------------------------------------+
| ``Url``                         | getAssociatedIndicatorUrl(Integer uniqueId, String urlText, String ownerName)        |
+---------------------------------+--------------------------------------------------------------------------------------+

Associated Security Labels
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below get associated SecurityLabel data elements.

+-------------------------------------+--------------------------------------------------------------------------------------+
| Type                                | Method                                                                               |
+=====================================+======================================================================================+
| ``IterableResponse<SecurityLabel>`` | getAssociatedSecurityLabels(Integer uniqueId)                                        |
+-------------------------------------+--------------------------------------------------------------------------------------+
| ``IterableResponse<SecurityLabel>`` | getAssociatedSecurityLabels(Integer uniqueId, String ownerName)                      |
+-------------------------------------+--------------------------------------------------------------------------------------+
| ``SecurityLabel``                   | getAssociatedSecurityLabel(Integer uniqueId, String securityLabel)                   |
+-------------------------------------+--------------------------------------------------------------------------------------+
| ``SecurityLabel``                   | getAssociatedSecurityLabel(Integer uniqueId, String securityLabel, String ownerName) |
+-------------------------------------+--------------------------------------------------------------------------------------+

Associated Tags
~~~~~~~~~~~~~~~

The methods below get associated Tag data elements.

+---------------------------+----------------------------------------------------------------------+
| Type                      | Method                                                               |
+===========================+======================================================================+
| ``IterableResponse<Tag>`` | getAssociatedTags(Integer uniqueId)                                  |
+---------------------------+----------------------------------------------------------------------+
| ``IterableResponse<Tag>`` | getAssociatedTags(Integer uniqueId, String ownerName)                |
+---------------------------+----------------------------------------------------------------------+
| ``Tag``                   | getAssociatedTag(Integer uniqueId, String tagName)                   |
+---------------------------+----------------------------------------------------------------------+
| ``Tag``                   | getAssociatedTag(Integer uniqueId, String tagName, String ownerName) |
+---------------------------+----------------------------------------------------------------------+

Associated VictimAssets
~~~~~~~~~~~~~~~~~~~~~~~

The methods below get associated VictimAsset data elements.

+--------------------------------------------+---------------------------------------------------------------------------------------------+
| Type                                       | Method                                                                                      |
+============================================+=============================================================================================+
| ``IterableResponse<VictimAsset>``          | getAssociatedVictimAssets(Integer uniqueId)                                                 |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimAsset>``          | getAssociatedVictimAssets(Integer uniqueId, String ownerName)                               |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimEmailAddress>``   | getAssociatedVictimAssetEmailAddresses(Integer uniqueId)                                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimEmailAddress>``   | getAssociatedVictimAssetEmailAddresses(Integer uniqueId, String ownerName)                  |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimEmailAddress``                     | getAssociatedVictimAssetEmailAddress(Integer uniqueId, Integer assetId)                     |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimEmailAddress``                     | getAssociatedVictimAssetEmailAddress(Integer uniqueId, Integer assetId, String ownerName)   |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimNetworkAccount>`` | getAssociatedVictimAssetNetworkAccounts(Integer uniqueId)                                   |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimNetworkAccount>`` | getAssociatedVictimAssetNetworkAccounts(Integer uniqueId, String ownerName)                 |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimNetworkAccount``                   | getAssociatedVictimAssetNetworkAccount(Integer uniqueId, Integer assetId)                   |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimNetworkAccount``                   | getAssociatedVictimAssetNetworkAccount(Integer uniqueId, Integer assetId, String ownerName) |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimPhone>``          | getAssociatedVictimAssetPhoneNumbers(Integer uniqueId)                                      |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimPhone>``          | getAssociatedVictimAssetPhoneNumbers(Integer uniqueId, String ownerName)                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimPhone``                            | getAssociatedVictimAssetPhoneNumber(Integer uniqueId, Integer assetId)                      |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimPhone``                            | getAssociatedVictimAssetPhoneNumber(Integer uniqueId, Integer assetId, String ownerName)    |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimSocialNetwork>``  | getAssociatedVictimAssetSocialNetworks(Integer uniqueId)                                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimSocialNetwork>``  | getAssociatedVictimAssetSocialNetworks(Integer uniqueId, String ownerName)                  |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimSocialNetwork``                    | getAssociatedVictimAssetSocialNetwork(Integer uniqueId, Integer assetId)                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimSocialNetwork``                    | getAssociatedVictimAssetSocialNetwork(Integer uniqueId, Integer assetId, String ownerName)  |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimWebSite>``        | getAssociatedVictimAssetWebsites(Integer uniqueId)                                          |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``IterableResponse<VictimWebSite>``        | getAssociatedVictimAssetWebsites(Integer uniqueId, String ownerName)                        |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimWebSite``                          | getAssociatedVictimAssetWebsite(Integer uniqueId, Integer assetId)                          |
+--------------------------------------------+---------------------------------------------------------------------------------------------+
| ``VictimWebSite``                          | getAssociatedVictimAssetWebsite(Integer uniqueId, Integer assetId, String ownerName)        |
+--------------------------------------------+---------------------------------------------------------------------------------------------+

Associated Attributes
~~~~~~~~~~~~~~~~~~~~~

The methods below get Attributes and Attribute SecurityLabels for this Group type.

+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| Type                                | Method                                                                                                   |
+=====================================+==========================================================================================================+
| ``IterableResponse<Attribute>``     | getAttributes(Integer uniqueId)                                                                          |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``IterableResponse<Attribute>``     | getAttributes(Integer uniqueId, String ownerName)                                                        |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``Attribute``                       | getAttribute(Integer uniqueId, Integer attributeId)                                                      |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``Attribute``                       | getAttribute(Integer uniqueId, Integer attributeId, String ownerName)                                    |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``IterableResponse<SecurityLabel>`` | getAttributeSecurityLabels(Integer uniqueId, Integer attributeId)                                        |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``IterableResponse<SecurityLabel>`` | getAttributeSecurityLabels(Integer uniqueId, Integer attributeId, String ownerName)                      |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``SecurityLabel``                   | getAttributeSecurityLabel(Integer uniqueId, Integer attributeId, String securityLabel)                   |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``SecurityLabel``                   | getAttributeSecurityLabel(Integer uniqueId, Integer attributeId, String securityLabel, String ownerName) |
+-------------------------------------+----------------------------------------------------------------------------------------------------------+

AbstractIndicatorReaderAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AbstractIndicatorReaderAdapter and AbstractGroupReaderAdapter share many
of the association actions. Indicators share the ability to associate
Groups, Indicators, SecurityLabels, Tags, VictimAssets, and Attributes.
The listings below are some distinctions or subtle differences.

All Indicators in the ThreatConnect API have a uniqueId data type of
"String". This identifier is provided by each Organization in the form
of an Email Address, IP Address, File Hash, Host Name, or URL text. To
understand this distinction, read the Indicator section in the
ThreatConnect API documentation.

The methods below get data for the Indicator type (T) linked to this
Adapter. The uniqueId (P) for Indicators is a String.

+-------------------------+----------------------------------------------------------------------------+
| Type                    | Method                                                                     |
+=========================+============================================================================+
| ``T``                   | getById(P uniqueId)                                                        |
+-------------------------+----------------------------------------------------------------------------+
| ``T``                   | getById(P uniqueId, String ownerName)                                      |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getForFilters(String ownerName, boolean orParams, ApiFilterType...filters) |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll()                                                                   |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll(String ownerName)                                                   |
+-------------------------+----------------------------------------------------------------------------+

The method below returns all the generic Indicators to which the current API user has access.

+---------------------------------+-----------------+
| Type                            | Method          |
+=================================+=================+
| ``IterableResponse<Indicator>`` | getIndicators() |
+---------------------------------+-----------------+

The methods below return owners who have created the Indicator under the uniqueId.

+-----------------------------+--------------------------------------------------------+
| Type                        | Method                                                 |
+=============================+========================================================+
| ``IterableResponse<Owner>`` | getAssociatedOwners(String uniqueId)                   |
+-----------------------------+--------------------------------------------------------+
| ``IterableResponse<Owner>`` | getAssociatedOwners(String uniqueId, String ownerName) |
+-----------------------------+--------------------------------------------------------+

The methods below return False Positive counts for the Indicator under the uniqueId.

+-------------------+-----------------------------------------------------+
| Type              | Method                                              |
+===================+=====================================================+
| ``FalsePositive`` | getFalsePositive(String uniqueId)                   |
+-------------------+-----------------------------------------------------+
| ``FalsePositive`` | getFalsePositive(String uniqueId, String ownerName) |
+-------------------+-----------------------------------------------------+

The methods below return Observations and Observation counts for the Indicator under the uniqueId.

+-----------------------------------+--------------------------------------------------------+
| Type                              | Method                                                 |
+===================================+========================================================+
| ``IterableResponse<Observation>`` | getObservations(String uniqueId)                       |
+-----------------------------------+--------------------------------------------------------+
| ``IterableResponse<Observation>`` | getObservations(String uniqueId, String ownerName)     |
+-----------------------------------+--------------------------------------------------------+
| ``ObservationCount``              | getObservationCount(String uniqueId)                   |
+-----------------------------------+--------------------------------------------------------+
| ``ObservationCount``              | getObservationCount(String uniqueId, String ownerName) |
+-----------------------------------+--------------------------------------------------------+

The AbstractIndicatorReaderAdapter class has a concrete subclass **FileIndicatorReaderAdapter** that exposes the methods
below.

+--------------------+-------------------------------------------------------------------------------+
| Type               | Method                                                                        |
+====================+===============================================================================+
| ``FileOccurrence`` | getFileOccurrence(String uniqueId, Integer fileOccurrencId)                   |
+--------------------+-------------------------------------------------------------------------------+
| ``FileOccurrence`` | getFileOccurrence(String uniqueId, Integer fileOccurrencId, String ownerName) |
+--------------------+-------------------------------------------------------------------------------+

BatchReaderAdapter
~~~~~~~~~~~~~~~~~~

The BatchReaderAdapter class allows the developer to poll for the status of a batch upload file using a batch id. Once a
batch is complete (either successfully or with errors), the developer can download errors (if any).

+-------------------------------------------------------------------+----------------------------------------------------------------+
| Type                                                              | Method                                                         |
+===================================================================+================================================================+
| ``ApiEntitySingleResponse<BatchStatus, BatchStatusResponseData>`` | getStatus(int batchId)                                         |
+-------------------------------------------------------------------+----------------------------------------------------------------+
| ``ApiEntitySingleResponse<BatchStatus, BatchStatusResponseData>`` | getStatus(int batchId, String ownerName)                       |
+-------------------------------------------------------------------+----------------------------------------------------------------+
| ``void``                                                          | downloadErrors(int batchId, Path outputPath)                   |
+-------------------------------------------------------------------+----------------------------------------------------------------+
| ``void``                                                          | downloadErrors(int batchId, String ownerName, Path outputPath) |
+-------------------------------------------------------------------+----------------------------------------------------------------+

DocumentReaderAdapter
~~~~~~~~~~~~~~~~~~~~~

The DocumentReaderAdapter class is a subclass of the AbstractGroupReader class. In addition to all GroupReader
functionality, the document reader has access to the following method.

+----------+---------------------------------------------------------------+
| Type     | Method                                                        |
+==========+===============================================================+
| ``void`` | downloadFile(int uniqueId, String ownerName, Path outputPath) |
+----------+---------------------------------------------------------------+

OwnerReaderAdapter
~~~~~~~~~~~~~~~~~~

The OwnerReaderAdapter is a simple Adapter that returns a list of Organizations to which the API user has access. There
is a second method called "getOwnerMine()" that returns the default Organization for the API user.

+-----------------------------+----------------+
| Type                        | Method         |
+=============================+================+
| ``Owner``                   | getOwnerMine() |
+-----------------------------+----------------+
| ``IterableResponse<Owner>`` | getOwners()    |
+-----------------------------+----------------+

SecurityLabelReaderAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SecurityLabelReaderAdapter class is a concrete class (available through the ReaderFactory) that returns
SecurityLabels to which the developer's API user has access, as well as by uniqueId (P). The uniqueId data type for
SecurityLabels is a String.

+-------------------------+---------------------------------------+
| Type                    | Method                                |
+=========================+=======================================+
| ``T``                   | getById(P uniqueId)                   |
+-------------------------+---------------------------------------+
| ``T``                   | getById(P uniqueId, String ownerName) |
+-------------------------+---------------------------------------+
| ``IterableResponse<T>`` | getAll()                              |
+-------------------------+---------------------------------------+
| ``IterableResponse<T>`` | getAll(String ownerName)              |
+-------------------------+---------------------------------------+

In addition to retrieving basic SecurityLabel data, associated `Groups <#associate-groups>`__ and
`Indicators <#associate-indicators>`__ can be retrieved. For more details on these methods, see the
`AbstractGroupReaderAdapter <#abstractgroupreaderadapter>`__ class.

TagReaderAdapter Class
~~~~~~~~~~~~~~~~~~~~~~

The TagReaderAdapter class is a concrete class (available through the ReaderFactory) that returns Tags to which the
developer's API user has access, as well as by uniqueId (P). The uniqueId data type for Tags is a String.

+-------------------------+----------------------------------------------------------------------------+
| Type                    | Method                                                                     |
+=========================+============================================================================+
| ``T``                   | getById(P uniqueId)                                                        |
+-------------------------+----------------------------------------------------------------------------+
| ``T``                   | getById(P uniqueId, String ownerName)                                      |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getForFilters(String ownerName, boolean orParams, ApiFilterType...filters) |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll()                                                                   |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll(String ownerName)                                                   |
+-------------------------+----------------------------------------------------------------------------+

In addition to retrieving basic Tag data, associated `Groups <#associate-groups>`__ and
`Indicators <#associate-indicators>`__ can be retrieved. For more details on these methods, review the
`AbstractGroupReaderAdapter <#abstractgroupreaderadapter>`__ class.

TaskReaderAdapter Class
~~~~~~~~~~~~~~~~~~~~~~~

The TaskReaderAdapter class is a concrete class (available through the ReaderFactory) that returns Tasks to which the
API user has access, as well as by uniqueId (P). The uniqueId data type for a Task is an Integer.

+-------------------------+----------------------------------------------------------------------------+
| Type                    | Method                                                                     |
+=========================+============================================================================+
| ``T``                   | getById(P uniqueId)                                                        |
+-------------------------+----------------------------------------------------------------------------+
| ``T``                   | getById(P uniqueId, String ownerName)                                      |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getForFilters(String ownerName, boolean orParams, ApiFilterType...filters) |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll()                                                                   |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll(String ownerName)                                                   |
+-------------------------+----------------------------------------------------------------------------+

In addition to retrieving basic Task data, associated Assignees and Escalatees can be retrieved.

The methods below return all Assignees or Escalatees associated with a given Task's id

+----------------------------+---------------------------+
| Type                       | Method                    |
+============================+===========================+
| ``IterableResponse<User>`` | getAssignees(P uniqueId)  |
+----------------------------+---------------------------+
| ``IterableResponse<User>`` | getEscalatees(P uniqueId) |
+----------------------------+---------------------------+

The methods below return an individual Assignee or Escalatees' information

+----------------------------+-------------------------------------------+
| Type                       | Method                                    |
+============================+===========================================+
| ``IterableResponse<User>`` | getAssignee(P uniqueId, String userName)  |
+----------------------------+-------------------------------------------+
| ``IterableResponse<User>`` | getEscalatee(P uniqueId, String userName) |
+----------------------------+-------------------------------------------+

VictimReaderAdapter Class
~~~~~~~~~~~~~~~~~~~~~~~~~

The VictimReaderAdapter class is a concrete class (available through the ReaderFactory) that returns Victims to which
the API user has access, as well as by uniqueId (P). The uniqueId data type for a Victim is an Integer.

+-------------------------+----------------------------------------------------------------------------+
| Type                    | Method                                                                     |
+=========================+============================================================================+
| ``T``                   | getById(P uniqueId)                                                        |
+-------------------------+----------------------------------------------------------------------------+
| ``T``                   | getById(P uniqueId, String ownerName)                                      |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getForFilters(String ownerName, boolean orParams, ApiFilterType...filters) |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll()                                                                   |
+-------------------------+----------------------------------------------------------------------------+
| ``IterableResponse<T>`` | getAll(String ownerName)                                                   |
+-------------------------+----------------------------------------------------------------------------+

In addition to retrieving basic Victim data, associated `Groups <#associate-groups>`__,
`Indicators <#associate-indicators>`__, and `VictimAssets <#associated-victimassets>`__ can be retrieved. For more
details on these methods, review the `AbstractGroupReaderAdapter <#abstractgroupreaderadapter>`__ class.

Reader IP Address and Tag Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example uses the Reader Package to retrieve associated
Tags from our IP address Indicators:

.. code-block:: java
    :linenos:
    :lineno-start: 1

    private static void doGetAssociatedTags(Connection conn) throws IOException, FailedResponseException {
        AbstractIndicatorReaderAdapter reader = ReaderAdapterFactory.createAddressIndicatorReader(conn);
        IterableResponse<Address> data = reader.getAll();
        for (Address address : data) {
            System.out.printf("IP Address: %20s", address.getIp() );

            IterableResponse<Tag> associatedTags = reader.getAssociatedTags( address.getIp() );
            System.out.printf("\tAssociated Tag:");
            for(Tag tag : associatedTags) {
                System.out.printf("%20s", tag.getName() );
            }
            System.out.println();
        }
    }


+-------+-------------------------------------------------------------------+
| Line  | Description                                                       |
+=======+===================================================================+
| 3-4   | An IndicatorReaderAdapter is created to read all the addresses to |
|       | which the API user has access. The ``getAll()`` method returns a  |
|       | collection of addresses from the ThreatConnect API.               |
+-------+-------------------------------------------------------------------+
| 5-6   | Each address is iterated through and its uniqueId is printed. As  |
|       | mentioned in the AbstractIndicatorReaderAdapter section, all      |
|       | uniqueIds for Indicators are Strings. In the case of address      |
|       | objects, it is the IP address or the ``getIp()`` getter method.   |
+-------+-------------------------------------------------------------------+
| 8     | To get a collection of associated Tags for the IP Address, the    |
|       | ``getAssociatedTags()`` method is called.                         |
+-------+-------------------------------------------------------------------+
| 10-11 | Each Tag returned from the ThreatConnect API for that specific IP |
|       | address is iterated through and printed to the console.           |
+-------+-------------------------------------------------------------------+

**Summary**

This example explained how to:

-  Get a collection of Indicators to which the API user has access
-  Retrieve associated data (in this case Tags) based on the uniqueId of
   the Indicator

The Writer Package
------------------

The Writer Package shares many of the concepts of the Reader Package
with the distinction of introducing the new functionality of version 2.0
of the ThreatConnect API. Note that the WriterAdapterFactory class is
effectively the "hub" for writer Adapters. It provides convenience
objects for all the Adapters in the Writer Package. Below is a list of
the static methods and return types of the WriterAdapterFactory.

+-------------+----------------------------------------------------------------+
| Class       | *Description*                                                  |
+=============+================================================================+
| ``WriterA   | Primary entry point to instantiate all writers in the Writer   |
| dapterFac   | Package.                                                       |
| tory``      |                                                                |
+-------------+----------------------------------------------------------------+
| ``Abstrac   | Generic Group writer abstract class. Concrete object available |
| tGroupWri   | in WriterAdapterFactory.                                       |
| terAdapte   |                                                                |
| r<T exten   |                                                                |
| ds Group>`` |                                                                |
+-------------+----------------------------------------------------------------+
| ``Abstrac   | Generic Indicator writer abstract class. Concrete object       |
| tIndicato   | available in WriterAdapterFactory.                             |
| rWriterAd   |                                                                |
| apter<T e   |                                                                |
| xtends In   |                                                                |
| dicator>``  |                                                                |
+-------------+----------------------------------------------------------------+
| ``Abstrac   | Base abstract writer for all reader Adapters in the Reader     |
| tWriterAd   | Package.                                                       |
| apter``     |                                                                |
+-------------+----------------------------------------------------------------+
| ``Securit   | Concrete writer for SecurityLabel data. Convenience object     |
| yLabelWri   | available in WriterAdapterFactory.                             |
| terAdapte   |                                                                |
| r``         |                                                                |
+-------------+----------------------------------------------------------------+
| ``TagWrit   | Concrete writer for Tag data. Convenience object available in  |
| erAdapter`` | WriterAdapterFactory.                                          |
+-------------+----------------------------------------------------------------+
| ``TaskWri   | Concrete writer for Task data. Convenience object available in |
| terAdapte   | WriterAdapterFactory.                                          |
| r``         |                                                                |
+-------------+----------------------------------------------------------------+
| ``VictimW   | Concrete writer for Victim data. Convenience object available  |
| riterAdap   | in WriterAdapterFactory.                                       |
| ter``       |                                                                |
+-------------+----------------------------------------------------------------+
| ``Abstrac   | Writer for batch indicator uploads. Concrete object available  |
| tBatchWri   | in WriterAdapterFactory.                                       |
| terAdapte   |                                                                |
| r<T>``      |                                                                |
+-------------+----------------------------------------------------------------+

Writer Factory
~~~~~~~~~~~~~~

The primary methods for the WriterFactory are listed below. They
encompass all write functionality for the ThreatConnect API.

+---------------------------------------------------------+----------------------------------------------------+
| Class                                                   | Method                                             |
+=========================================================+====================================================+
| ``static AbstractGroupWriterAdapter<Adversary>``        | createAdversaryGroupWriter(Connection conn)        |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupWriterAdapter<Email>``            | createEmailGroupWriter(Connection conn)            |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupWriterAdapter<Incident>``         | createIncidentGroupWriter(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupWriterAdapter<Signature>``        | createSignatureGroupWriter(Connection conn)        |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractGroupWriterAdapter<Threat>``           | createThreatGroupWriter(Connection conn)           |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorWriterAdapter<Address>``      | createAddressIndicatorWriter(Connection conn)      |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorWriterAdapter<EmailAddress>`` | createEmailAddressIndicatorWriter(Connection conn) |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorWriterAdapter<File>``         | createFileIndicatorWriter(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorWriterAdapter<Host>``         | createHostIndicatorWriter(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractIndicatorWriterAdapter<Url>``          | createUrlIndicatorWriter(Connection conn)          |
+---------------------------------------------------------+----------------------------------------------------+
| ``static AbstractBatchWriterAdapter<Indicator>``        | createBatchIndicatorWriter(Connection conn)        |
+---------------------------------------------------------+----------------------------------------------------+
| ``static DocumentWriterAdapter``                        | createDocumentWriter(Connection conn)              |
+---------------------------------------------------------+----------------------------------------------------+
| ``static SecurityLabelWriterAdapter``                   | createSecurityLabelWriter(Connection conn)         |
+---------------------------------------------------------+----------------------------------------------------+
| ``static TagWriterAdapter``                             | createTagWriter(Connection conn)                   |
+---------------------------------------------------------+----------------------------------------------------+
| ``static TaskWriterAdapter``                            | createTaskWriter(Connection conn)                  |
+---------------------------------------------------------+----------------------------------------------------+
| ``static VictimWriterAdapter``                          | createVictimWriter(Connection conn)                |
+---------------------------------------------------------+----------------------------------------------------+

Writer Responses
~~~~~~~~~~~~~~~~

This section details some conventions used in the writer API that will
help clarify how deletes, creates, and updates are handled by the Java
SDK, and what the developer should expect when a failure occurs.

When a single item is modified (create/delete/update) using the Java
SDK, the return type is an ApiEntitySingleResponse object. In an effort
to simplify write-operation response handling, the
ApiEntitySingleResponse object provides a single object for the
developer to validate the modify operation.

When a collection of items is modified (create/delete/update) using the
Java SDK, the return type is a WriteListResponse object. Likewise, in an
effort to simplify write-operation response handling, the
WriteListResponse object holds collections of failed/succeeded
ApiEntitySingleResponse objects. The following listing describes how
modify responses should be handled.

+-------------------------------------+--------------------+
| Type                                | *Method*           |
+=====================================+====================+
| ``List<ApiEntitySingleResponse>``   | getFailureList()   |
+-------------------------------------+--------------------+
| ``List<ApiEntitySingleResponse>``   | getSuccessList()   |
+-------------------------------------+--------------------+
| ``boolean``                         | isSuccess()        |
+-------------------------------------+--------------------+
| ``String``                          | getMessage()       |
+-------------------------------------+--------------------+
| ``T``                               | getItem()          |
+-------------------------------------+--------------------+

While the ApiEntitySingleResponse class manages failed write operations
to the ThreatConnect API, the developer is responsible for capturing any
runtime exceptions that may occur because of network, configuration, or
data-related issues.

Fluent Entities
~~~~~~~~~~~~~~~

The following is a simple Fluent Example:

.. code:: java


           Attribute attribute = new AttributeBuilder()
                    .withDisplayed(true)
                    .withType(type)
                    .withDateAdded(new Date())
                    .withLastModified(new Date())
                    .withValue(value)
                    .createAttribute();

There are entity classes available using a fluent style to simplify
object creation. These classes are part of the SDK and can be used in
place of creating a traditional new ThreatConnect entity with all
setters. Using the fluent entities in the
``com.threatconnect.sdk.client.fluent`` package are optional and a
matter of preference.

+---------------------------------+
| Fluent Types                    |
+=================================+
| ``AddressBuilder``              |
+---------------------------------+
| ``AdversaryBuilder``            |
+---------------------------------+
| ``AttributeBuilder``            |
+---------------------------------+
| ``CommunityBuilder``            |
+---------------------------------+
| ``DocumentBuilder``             |
+---------------------------------+
| ``EmailAddressBuilder``         |
+---------------------------------+
| ``EmailBuilder``                |
+---------------------------------+
| ``FileBuilder``                 |
+---------------------------------+
| ``FileOccurrenceBuilder``       |
+---------------------------------+
| ``GroupBuilder``                |
+---------------------------------+
| ``HostBuilder``                 |
+---------------------------------+
| ``IncidentBuilder``             |
+---------------------------------+
| ``IndicatorBuilder``            |
+---------------------------------+
| ``IndividualBuilder``           |
+---------------------------------+
| ``SecurityLabelBuilder``        |
+---------------------------------+
| ``SignatureBuilder``            |
+---------------------------------+
| ``SourceBuilder``               |
+---------------------------------+
| ``TagBuilder``                  |
+---------------------------------+
| ``TaskBuilder``                 |
+---------------------------------+
| ``ThreatBuilder``               |
+---------------------------------+
| ``UrlBuilder``                  |
+---------------------------------+
| ``UserBuilder``                 |
+---------------------------------+
| ``VictimAssetBuilder``          |
+---------------------------------+
| ``VictimBuilder``               |
+---------------------------------+
| ``VictimEmailAddressBuilder``   |
+---------------------------------+
| ``VictimNetworkAccountBuilder`` |
+---------------------------------+
| ``VictimPhoneBuilder``          |
+---------------------------------+
| ``VictimSocialNetworkBuilder``  |
+---------------------------------+
| ``VictimWebSiteBuilder``        |
+---------------------------------+

Writer Create Example
~~~~~~~~~~~~~~~~~~~~~

The following is a simple Writer Create Example:

.. code-block:: java

      3 import com.threatconnect.sdk.client.writer.AbstractGroupWriterAdapter;
      4 import com.threatconnect.sdk.client.writer.WriterAdapterFactory;
      5 import com.threatconnect.sdk.conn.Connection;
      6 import com.threatconnect.sdk.exception.FailedResponseException;
      7 import com.threatconnect.sdk.server.entity.Adversary;
      8 import com.threatconnect.sdk.server.response.entity.ApiEntitySingleResponse;
      9 import java.io.IOException;
     10 import java.util.List;
    103     private static void doCreate(Connection conn) {
    104         AbstractGroupWriterAdapter<Adversary> writer = WriterAdapterFactory.createAdversaryGroupWriter(conn);
    105 
    106         Adversary adversary = new Adversary();
    107         adversary.setName("Test Adversary");
    108         adversary.setOwnerName("System");
    109 
    110         try {
    111             ApiEntitySingleResponse<Adversary,?> response = writer.create(adversary);
    112             if ( response.isSuccess() ) {
    113                 Adversary savedAdversary = response.getItem();
    114                 System.out.println("Saved: " + savedAdversary.toString() );
    115             } else {
    116                 System.err.println("Error: " + response.getMessage() );
    117 
    118             }
    119 
    120         } catch (IOException | FailedResponseException ex) {
    121             System.err.println("Error: " + ex.toString());
    122         }
    123 
    124     }

Code Sample

+--------+-------------------------------------------------------------------+
| Line   | Description                                                       |
+========+===================================================================+
| 104    | An AbstractGroupWriterAdapter for the Adversary Group type is     |
|        | created. With this Adapter, Group data elements, Victim assets,   |
|        | Attributes, and associations can be written/updated/deleted.      |
+--------+-------------------------------------------------------------------+
| 106-10 | A simple Adversary with a name and owner (Organization) is        |
| 8      | created.                                                          |
+--------+-------------------------------------------------------------------+
| 111    | The writer is used to create an Adversary using the ThreatConnect |
|        | API. For single-item writes, an ApiEntitySingleResponse object is |
|        | always returned. This object allows for the appropriate           |
|        | inspection and handling of the response.                          |
+--------+-------------------------------------------------------------------+
| 112-11 | To see if the create was successful, ``isSuccess()`` is called.   |
| 4      | If the check passes, the item associated with the response is     |
|        | delivered using the ``getItem()`` method (Line 113). The          |
|        | successfully saved Adversary object returns from the              |
|        | ThreatConnect API with a valid ID value.                          |
+--------+-------------------------------------------------------------------+
| 116    | If the response is unsuccessful, the response message to the      |
|        | console is printed.                                               |
+--------+-------------------------------------------------------------------+
| 121    | Any potential runtime exceptions are caught and handled           |
|        | appropriately. In the case of this basic example, it is simply    |
|        | dumped to the console.                                            |
+--------+-------------------------------------------------------------------+

**Summary**

This example explained how to:

-  Create an Adapter using the WriterFactory
-  Create an Adversary, and verify if the save was successful
-  Handle errors from a write operation to the ThreatConnect API

Writer Class Overview
---------------------

Most of the conventions in the Reader Package are mirrored in the Writer
Package. Much like the Reader Package, the method-naming conventions
will be familiar and self-explanatory. `Parameter-naming
conventions <#parameter-naming-convention>`__ have been kept
abstract to allow for a better representation of the identifiers being
passed. Below is a listing of the classes in the Writer Package.

AbstractGroupWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below write data for the Group type (T) linked to this
Adapter.

-  The create methods require a Group type object as a collection or
   single object.
-  The delete methods require the key ID value as a collection or single
   object.
-  The update methods require a Group type object as a collection or
   single object.

+-----------------------------+------------------------------------------------------+
| Type                        | *Method*                                             |
+=============================+======================================================+
| ``WriteListResponse<T>``    | create(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``)                        |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``, ``String ownerName``)  |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``)                               |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``, ``String ownerName``)         |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``, ``String ownerName``) |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+

Associate Groups
~~~~~~~~~~~~~~~~

The methods below associate a Group type to another Group type. Groups
are associated by passing in the uniqueId (Integer) with the Group ID to
which it will be associated.

+--------------------------------+---------------------------------------------------------------------------------------------------------+
| Type                           | Method                                                                                                  |
+================================+=========================================================================================================+
| ``WriteListResponse<Integer>`` | associateGroupAdversaries(\ ``Integer uniqueId``, ``List<Integer> adversaryIds``)                       |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupAdversaries(\ ``Integer uniqueId``, ``List<Integer> adversaryIds``, ``String ownerName``) |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupAdversary(\ ``Integer uniqueId``, ``Integer adversaryId``)                                |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupAdversary(\ ``Integer uniqueId``, ``Integer adversaryId``, ``String ownerName``)          |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupEmails(\ ``Integer uniqueId``, ``List<Integer> emailIds``)                                |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupEmails(\ ``Integer uniqueId``, ``List<Integer> emailIds``, ``String ownerName``)          |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupEmail(\ ``Integer uniqueId``, ``Integer emailId``)                                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupEmail(\ ``Integer uniqueId``, ``Integer emailId``, ``String ownerName``)                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupIncidents(\ ``Integer uniqueId``, ``List<Integer> incidentIds``)                          |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupIncidents(\ ``Integer uniqueId``, ``List<Integer> incidentIds``, ``String ownerName``)    |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupIncident(\ ``Integer uniqueId``, ``Integer incidentId``)                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupIncident(\ ``Integer uniqueId``, ``Integer incidentId``, ``String ownerName``)            |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupSignatures(\ ``Integer uniqueId``, ``List<Integer> signatureIds``)                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupSignatures(\ ``Integer uniqueId``, ``List<Integer> signatureIds``, ``String ownerName``)  |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupSignature(\ ``Integer uniqueId``, ``Integer signatureId``)                                |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupSignature(\ ``Integer uniqueId``, ``Integer signatureId``, ``String ownerName``)          |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupThreats(\ ``Integer uniqueId``, ``List<Integer> threatIds``)                              |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateGroupThreats(\ ``Integer uniqueId``, ``List<Integer> threatIds``, ``String ownerName``)        |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupThreat(\ ``Integer uniqueId``, ``Integer threatId``)                                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateGroupThreat(\ ``Integer uniqueId``, ``Integer threatId``, ``String ownerName``)                |
+--------------------------------+---------------------------------------------------------------------------------------------------------+

Associate Indicators
~~~~~~~~~~~~~~~~~~~~

The methods below associate Indicators to a Group type.

+-------------------------------+---------------------------------------------------------------------------------+
| Type                          | Method                                                                          |
+===============================+=================================================================================+
| ``WriteListResponse<String>`` | associateIndicatorAddresses(\ ``Integer uniqueId``,                             |
|                               | ``List<String> ipAddresses``)                                                   |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorAddresses(\ ``Integer uniqueId``,                             |
|                               | ``List<String> ipAddresses``, ``String ownerName``)                             |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorAddress(\ ``Integer uniqueId``, ``String ipAddress``)         |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorAddress(\ ``Integer uniqueId``, ``String ipAddress``,         |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorEmailAddresses(\ ``Integer uniqueId``,                        |
|                               | ``List<String> emailAddresses``)                                                |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorEmailAddresses(\ ``Integer uniqueId``,                        |
|                               | ``List<String> emailAddresses``, ``String ownerName``)                          |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorEmailAddress(\ ``Integer uniqueId``, ``String emailAddress``) |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorEmailAddress(\ ``Integer uniqueId``, ``String emailAddress``, |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorFiles(\ ``Integer uniqueId``, ``List<String> fileHashes``)    |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorFiles(\ ``Integer uniqueId``, ``List<String> fileHashes``,    |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorFile(\ ``Integer uniqueId``, ``String fileHash``)             |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorFile(\ ``Integer uniqueId``, ``String fileHash``,             |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorHosts(\ ``Integer uniqueId``, ``List<String> hostNames``)     |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorHosts(\ ``Integer uniqueId``, ``List<String> hostNames``,     |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorHost(\ ``Integer uniqueId``, ``String hostName``)             |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorHost(\ ``Integer uniqueId``, ``String hostName``,             |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorUrls(\ ``Integer uniqueId``, ``List<String> urlTexts``)       |
+-------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateIndicatorUrls(\ ``Integer uniqueId``, ``List<String> urlTexts``,       |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorUrl(\ ``Integer uniqueId``, ``String urlText``)               |
+-------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateIndicatorUrl(\ ``Integer uniqueId``, ``String urlText``,               |
|                               | ``String ownerName``)                                                           |
+-------------------------------+---------------------------------------------------------------------------------+


Associate Security Labels
~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below associate Security Labels to a Group type.

+-------------------------------+--------------------------------------------------------------------------------------------------------+
| Type                          | Method                                                                                                 |
+===============================+========================================================================================================+
| ``WriteListResponse<String>`` | associateSecurityLabels(\ ``Integer uniqueId``, ``List<String> securityLabels``)                       |
+-------------------------------+--------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateSecurityLabels(\ ``Integer uniqueId``, ``List<String> securityLabels``, ``String ownerName``) |
+-------------------------------+--------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateSecurityLabel(\ ``Integer uniqueId``, ``String securityLabel``)                               |
+-------------------------------+--------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateSecurityLabel(\ ``Integer uniqueId``, ``String securityLabel``, ``String ownerName``)         |
+-------------------------------+--------------------------------------------------------------------------------------------------------+

Associate Tag
~~~~~~~~~~~~~

The methods below associate Tags to a Group type.

+-------------------------------+----------------------------------------------------------------------------------------+
| Type                          | Method                                                                                 |
+===============================+========================================================================================+
| ``WriteListResponse<String>`` | associateTags(\ ``Integer uniqueId``, ``List<String> tagNames``)                       |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | associateTags(\ ``Integer uniqueId``, ``List<String> tagNames``, ``String ownerName``) |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateTag(\ ``Integer uniqueId``, ``String tagName``)                               |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | associateTag(\ ``Integer uniqueId``, ``String tagName``, ``String ownerName``)         |
+-------------------------------+----------------------------------------------------------------------------------------+

Associate Victim
~~~~~~~~~~~~~~~~

The methods below associate Victims to a Group type.

+--------------------------------+---------------------------------------------------------------------------------------------+
| Type                           | Method                                                                                      |
+================================+=============================================================================================+
| ``WriteListResponse<Integer>`` | associateVictims(\ ``Integer uniqueId``, ``List<Integer> victimIds``)                       |
+--------------------------------+---------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictims(\ ``Integer uniqueId``, ``List<Integer> victimIds``, ``String ownerName``) |
+--------------------------------+---------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictim(\ ``Integer uniqueId``, ``Integer victimId``)                               |
+--------------------------------+---------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictim(\ ``Integer uniqueId``, ``Integer victimId``, ``String ownerName``)         |
+--------------------------------+---------------------------------------------------------------------------------------------+

Associate Victim Asset
~~~~~~~~~~~~~~~~~~~~~~

The methods below associate Victim Assets to a Group type.

+--------------------------------+---------------------------------------------------------------------------------+
| Type                           | Method                                                                          |
+================================+=================================================================================+
| ``WriteListResponse<Integer>`` | associateVictimAssetEmailAddresses(\ ``Integer uniqueId``,                      |
|                                | ``List<Integer> assetIds``)                                                     |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetEmailAddresses(\ ``Integer uniqueId``,                      |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                               |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetEmailAddress(\ ``Integer uniqueId``, ``Integer assetId``)   |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetEmailAddress(\ ``Integer uniqueId``, ``Integer assetId``,   |
|                                | ``String ownerName``)                                                           |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetNetworkAccounts(\ ``Integer uniqueId``,                     |
|                                | ``List<Integer> assetIds``)                                                     |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetNetworkAccounts(\ ``Integer uniqueId``,                     |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                               |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetNetworkAccount(\ ``Integer uniqueId``, ``Integer assetId``) |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetNetworkAccount(\ ``Integer uniqueId``, ``Integer assetId``, |
|                                | ``String ownerName``)                                                           |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetPhoneNumbers(\ ``Integer uniqueId``,                        |
|                                | ``List<Integer> assetIds``)                                                     |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetPhoneNumbers(\ ``Integer uniqueId``,                        |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                               |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetPhoneNumber(\ ``Integer uniqueId``, ``Integer assetId``)    |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetPhoneNumber(\ ``Integer uniqueId``, ``Integer assetId``,    |
|                                | ``String ownerName``)                                                           |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetSocialNetworks(\ ``Integer uniqueId``,                      |
|                                | ``List<Integer> assetIds``)                                                     |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetSocialNetworks(\ ``Integer uniqueId``,                      |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                               |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetSocialNetwork(\ ``Integer uniqueId``, ``Integer assetId``)  |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetSocialNetwork(\ ``Integer uniqueId``, ``Integer assetId``,  |
|                                | ``String ownerName``)                                                           |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetWebsites(\ ``Integer uniqueId``,                            |
|                                | ``List<Integer> assetIds``)                                                     |
+--------------------------------+---------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | associateVictimAssetWebsites(\ ``Integer uniqueId``,                            |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                               |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetWebsite(\ ``Integer uniqueId``, ``Integer assetId``)        |
+--------------------------------+---------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | associateVictimAssetWebsite(\ ``Integer uniqueId``, ``Integer assetId``,        |
|                                | ``String ownerName``)                                                           |
+--------------------------------+---------------------------------------------------------------------------------+

Add Attributes
~~~~~~~~~~~~~~

The methods below add Attribute types to a Group.

+----------------------------------+-----------------------------------------------------------------------------+
| Type                             | Method                                                                      |
+==================================+=============================================================================+
| ``WriteListResponse<Attribute>`` | addAttributes(\ ``Integer uniqueId``, ``List<Attribute> attributes``)       |
+----------------------------------+-----------------------------------------------------------------------------+
| ``WriteListResponse<Attribute>`` | addAttributes(\ ``Integer uniqueId``, ``List<Attribute> attribute``,        |
|                                  | ``String ownerName``)                                                       |
+----------------------------------+-----------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``      | addAttribute(\ ``Integer uniqueId``, ``Attribute attribute``)               |
+----------------------------------+-----------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``      | addAttribute(\ ``Integer uniqueId``, ``Attribute attribute``,               |
|                                  | ``String ownerName``)                                                       |
+----------------------------------+-----------------------------------------------------------------------------+
| ``WriteListResponse<String>``    | addAttributeSecurityLabels(\ ``Integer uniqueId``, ``Integer attributeId``, |
|                                  | ``List<String> securityLabels``)                                            |
+----------------------------------+-----------------------------------------------------------------------------+
| ``WriteListResponse<String>``    | addAttributeSecurityLabels(\ ``Integer uniqueId``, ``Integer attributeId``, |
|                                  | ``List<String> securityLabels``, ``String ownerName``)                      |
+----------------------------------+-----------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``      | addAttributeSecurityLabel(\ ``Integer uniqueId``, ``Integer attributeId``,  |
|                                  | ``String securityLabel``)                                                   |
+----------------------------------+-----------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``      | addAttributeSecurityLabel(\ ``Integer uniqueId``, ``Integer attributeId``,  |
|                                  | ``String securityLabel``, ``String ownerName``)                             |
+----------------------------------+-----------------------------------------------------------------------------+

Update Attribute
~~~~~~~~~~~~~~~~

The methods below **update** an Attribute added to a specific Indicator type.

+----------------------------------+-----------------------------------------------------------------------------------------------+
| Type                             | Method                                                                                        |
+==================================+===============================================================================================+
| ``WriteListResponse<Attribute>`` | updateAttributes(\ ``Integer uniqueId``, ``List<Attribute> attributes``)                      |
+----------------------------------+-----------------------------------------------------------------------------------------------+
| ``WriteListResponse<Attribute>`` | updateAttributes(\ ``Integer uniqueId``, ``List<Attribute> attribute``, ``String ownerName``) |
+----------------------------------+-----------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``      | updateAttribute(\ ``Integer uniqueId``, ``Attribute attribute``)                              |
+----------------------------------+-----------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``      | updateAttribute(\ ``Integer uniqueId``, ``Attribute attribute``, ``String ownerName``)        |
+----------------------------------+-----------------------------------------------------------------------------------------------+

Create Observation
~~~~~~~~~~~~~~~~~~

The methods below **create** an Observation on a specific Indicator type.

+-----------------------------+-----------------------------------------------------------------+
| Type                        | Method                                                          |
+=============================+=================================================================+
| ``ApiEntitySingleResponse`` | createObservation(\ ``Integer uniqueId``)                       |
+-----------------------------+-----------------------------------------------------------------+
| ``ApiEntitySingleResponse`` | createObservation(\ ``Integer uniqueId``, ``String ownerName``) |
+-----------------------------+-----------------------------------------------------------------+

Update False Positive
~~~~~~~~~~~~~~~~~~~~~

The methods below **update** the False Positive field on a specific Indicator type.

+-----------------------------+-------------------------------------------------------------------+
| Type                        | Method                                                            |
+=============================+===================================================================+
| ``ApiEntitySingleResponse`` | updateFalsePositive(\ ``Integer uniqueId``)                       |
+-----------------------------+-------------------------------------------------------------------+
| ``ApiEntitySingleResponse`` | updateFalsePositive(\ ``Integer uniqueId``, ``String ownerName``) |
+-----------------------------+-------------------------------------------------------------------+

Delete Group Association
~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Group associations to a specific Group type.

+--------------------------------+----------------------------------------------------------------------------------------------------------+
| Type                           | Method                                                                                                   |
+================================+==========================================================================================================+
| ``WriteListResponse<Integer>`` | dissociateGroupAdversaries(\ ``Integer uniqueId``, ``List<Integer> adversaryIds``)                       |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupAdversaries(\ ``Integer uniqueId``, ``List<Integer> adversaryIds``, ``String ownerName``) |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupAdversary(\ ``Integer uniqueId``, ``Integer adversaryId``)                                |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupAdversary(\ ``Integer uniqueId``, ``Integer adversaryId``, ``String ownerName``)          |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupEmails(\ ``Integer uniqueId``, ``List<Integer> emailIds``)                                |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupEmails(\ ``Integer uniqueId``, ``List<Integer> emailIds``, ``String ownerName``)          |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupEmail(\ ``Integer uniqueId``, ``Integer emailId``)                                        |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupEmail(\ ``Integer uniqueId``, ``Integer emailId``, ``String ownerName``)                  |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupIncidents(\ ``Integer uniqueId``, ``List<Integer> incidentIds``)                          |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupIncidents(\ ``Integer uniqueId``, ``List<Integer> incidentIds``, ``String ownerName``)    |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupIncident(\ ``Integer uniqueId``, ``Integer incidentId``)                                  |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupIncident(\ ``Integer uniqueId``, ``Integer incidentId``, ``String ownerName``)            |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupSignatures(\ ``Integer uniqueId``, ``List<Integer> signatureIds``)                        |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupSignatures(\ ``Integer uniqueId``, ``List<Integer> signatureIds``, ``String ownerName``)  |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupSignature(\ ``Integer uniqueId``, ``Integer signatureId``)                                |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupSignature(\ ``Integer uniqueId``, ``Integer signatureId``, ``String ownerName``)          |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupThreats(\ ``Integer uniqueId``, ``List<Integer> threatIds``)                              |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateGroupThreats(\ ``Integer uniqueId``, ``List<Integer> threatIds``, ``String ownerName``)        |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupThreat(\ ``Integer uniqueId``, ``Integer threatId``)                                      |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateGroupThreat(\ ``Integer uniqueId``, ``Integer threatId``, ``String ownerName``)                |
+--------------------------------+----------------------------------------------------------------------------------------------------------+

Delete Indicator Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Indicator associations to a specific Group type.

+-------------------------------+-------------------------------------------------------------------------------+
| Type                          | Method                                                                        |
+===============================+===============================================================================+
| ``WriteListResponse<String>`` | dissociateIndicatorAddresses(\ ``Integer uniqueId``,                          |
|                               | ``List<String> ipAddresses``)                                                 |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorAddresses(\ ``Integer uniqueId``,                          |
|                               | ``List<String> ipAddresses``, ``String ownerName``)                           |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorAddress(\ ``Integer uniqueId``, ``String ipAddress``)      |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorAddress(\ ``Integer uniqueId``, ``String ipAddress``,      |
|                               | ``String ownerName``)                                                         |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorEmailAddresses(\ ``Integer uniqueId``,                     |
|                               | ``List<String> emailAddresses``)                                              |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorEmailAddresses(\ ``Integer uniqueId``,                     |
|                               | ``List<String> emailAddresses``, ``String ownerName``)                        |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorEmailAddress(\ ``Integer uniqueId``,                       |
|                               | ``String emailAddress``)                                                      |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorEmailAddress(\ ``Integer uniqueId``,                       |
|                               | ``String emailAddress``, ``String ownerName``)                                |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorFiles(\ ``Integer uniqueId``, ``List<String> fileHashes``) |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorFiles(\ ``Integer uniqueId``, ``List<String> fileHashes``, |
|                               | ``String ownerName``)                                                         |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorFile(\ ``Integer uniqueId``, ``String fileHash``)          |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorFile(\ ``Integer uniqueId``, ``String fileHash``,          |
|                               | ``String ownerName``)                                                         |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorHosts(\ ``Integer uniqueId``, ``List<String> hostNames``)  |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorHosts(\ ``Integer uniqueId``, ``List<String> hostNames``,  |
|                               | ``String ownerName``)                                                         |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorHost(\ ``Integer uniqueId``, ``String hostName``)          |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorHost(\ ``Integer uniqueId``, ``String hostName``,          |
|                               | ``String ownerName``)                                                         |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorUrls(\ ``Integer uniqueId``, ``List<String> urlTexts``)    |
+-------------------------------+-------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateIndicatorUrls(\ ``Integer uniqueId``, ``List<String> urlTexts``,    |
|                               | ``String ownerName``)                                                         |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorUrl(\ ``Integer uniqueId``, ``String urlText``)            |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateIndicatorUrl(\ ``Integer uniqueId``, ``String urlText``,            |
|                               | ``String ownerName``)                                                         |
+-------------------------------+-------------------------------------------------------------------------------+

Delete Security Label Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** SecurityLabel associations to a specific Group type.

+-------------------------------+--------------------------------------------------------------------------------------------------------+
| Type                          | Method                                                                                                 |
+===============================+========================================================================================================+
| ``WriteListResponse<String>`` | dissociateSecurityLabel(\ ``Integer uniqueId``, ``List<String> securityLabels``)                       |
+-------------------------------+--------------------------------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateSecurityLabel(\ ``Integer uniqueId``, ``List<String> securityLabels``, ``String ownerName``) |
+-------------------------------+--------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateSecurityLabel(\ ``Integer uniqueId``, ``String securityLabel``)                              |
+-------------------------------+--------------------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateSecurityLabel(\ ``Integer uniqueId``, ``String securityLabel``, ``String ownerName``)        |
+-------------------------------+--------------------------------------------------------------------------------------------------------+

Delete Tag Associations
~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Tag associations to a specific Group type.

+-------------------------------+-----------------------------------------------------------------------------------------+
| Type                          | Method                                                                                  |
+===============================+=========================================================================================+
| ``WriteListResponse<String>`` | dissociateTags(\ ``Integer uniqueId``, ``List<String> tagNames``)                       |
+-------------------------------+-----------------------------------------------------------------------------------------+
| ``WriteListResponse<String>`` | dissociateTags(\ ``Integer uniqueId``, ``List<String> tagNames``, ``String ownerName``) |
+-------------------------------+-----------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateTag(\ ``Integer uniqueId``, ``String tagName``)                               |
+-------------------------------+-----------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``   | dissociateTag(\ ``Integer uniqueId``, ``String tagName``, ``String ownerName``)         |
+-------------------------------+-----------------------------------------------------------------------------------------+

Delete Victim Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Victim associations to a specific Group type.

+--------------------------------+----------------------------------------------------------------------------------------------+
| Type                           | Method                                                                                       |
+================================+==============================================================================================+
| ``WriteListResponse<Integer>`` | dissociateVictims(\ ``Integer uniqueId``, ``List<Integer> victimIds``)                       |
+--------------------------------+----------------------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictims(\ ``Integer uniqueId``, ``List<Integer> victimIds``, ``String ownerName``) |
+--------------------------------+----------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictim(\ ``Integer uniqueId``, ``Integer victimId``)                               |
+--------------------------------+----------------------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictim(\ ``Integer uniqueId``, ``Integer victimId``, ``String ownerName``)         |
+--------------------------------+----------------------------------------------------------------------------------------------+

Delete VictimAsset Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** VictimAsset associations to a specific Group type.

+--------------------------------+--------------------------------------------------------------------------------+
| Type                           | Method                                                                         |
+================================+================================================================================+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetEmailAddresses(\ ``Integer uniqueId``,                    |
|                                | ``List<Integer> assetIds``)                                                    |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetEmailAddresses(\ ``Integer uniqueId``,                    |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                              |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetEmailAddress(\ ``Integer uniqueId``, ``Integer assetId``) |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetEmailAddress(\ ``Integer uniqueId``, ``Integer assetId``, |
|                                | ``String ownerName``)                                                          |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetNetworkAccounts(\ ``Integer uniqueId``,                   |
|                                | ``List<Integer> assetIds``)                                                    |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetNetworkAccounts(\ ``Integer uniqueId``,                   |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                              |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetNetworkAccount(\ ``Integer uniqueId``,                    |
|                                | ``Integer assetId``)                                                           |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetNetworkAccount(\ ``Integer uniqueId``,                    |
|                                | ``Integer assetId``, ``String ownerName``)                                     |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetPhoneNumbers(\ ``Integer uniqueId``,                      |
|                                | ``List<Integer> assetIds``)                                                    |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetPhoneNumbers(\ ``Integer uniqueId``,                      |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                              |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetPhoneNumber(\ ``Integer uniqueId``, ``Integer assetId``)  |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetPhoneNumber(\ ``Integer uniqueId``, ``Integer assetId``,  |
|                                | ``String ownerName``)                                                          |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetSocialNetworks(\ ``Integer uniqueId``,                    |
|                                | ``List<Integer> assetIds``)                                                    |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetSocialNetworks(\ ``Integer uniqueId``,                    |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                              |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetSocialNetwork(\ ``Integer uniqueId``,                     |
|                                | ``Integer assetId``)                                                           |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetSocialNetwork(\ ``Integer uniqueId``,                     |
|                                | ``Integer assetId``, ``String ownerName``)                                     |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetWebsites(\ ``Integer uniqueId``,                          |
|                                | ``List<Integer> assetIds``)                                                    |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | dissociateVictimAssetWebsites(\ ``Integer uniqueId``,                          |
|                                | ``List<Integer> assetIds``, ``String ownerName``)                              |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetWebsite(\ ``Integer uniqueId``, ``Integer assetId``)      |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | dissociateVictimAssetWebsite(\ ``Integer uniqueId``, ``Integer assetId``,      |
|                                | ``String ownerName``)                                                          |
+--------------------------------+--------------------------------------------------------------------------------+

Delete Attribute
~~~~~~~~~~~~~~~~

The methods below **delete** Attributes from a specific Group type.

+--------------------------------+--------------------------------------------------------------------------------+
| Type                           | Method                                                                         |
+================================+================================================================================+
| ``WriteListResponse<Integer>`` | deleteAttributes(\ ``Integer uniqueId``, ``List<Integer> attributes``)         |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<Integer>`` | deleteAttributes(\ ``Integer uniqueId``, ``List<Integer> attribute``,          |
|                                | ``String ownerName``)                                                          |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | deleteAttribute(\ ``Integer uniqueId``, ``Integer attribute``)                 |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | deleteAttribute(\ ``Integer uniqueId``, ``Integer attribute``,                 |
|                                | ``String ownerName``)                                                          |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<String>``  | deleteAttributeSecurityLabels(\ ``Integer uniqueId``, ``Integer attributeId``, |
|                                | ``List<String> securityLabels``)                                               |
+--------------------------------+--------------------------------------------------------------------------------+
| ``WriteListResponse<String>``  | deleteAttributeSecurityLabels(\ ``Integer uniqueId``, ``Integer attributeId``, |
|                                | ``List<String> securityLabels``, ``String ownerName``)                         |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | deleteAttributeSecurityLabel(\ ``Integer uniqueId``, ``Integer attributeId``,  |
|                                | ``String securityLabel``)                                                      |
+--------------------------------+--------------------------------------------------------------------------------+
| ``ApiEntitySingleResponse``    | deleteAttributeSecurityLabel(\ ``Integer uniqueId``, ``Integer attributeId``,  |
|                                | ``String securityLabel``, ``String ownerName``)                                |
+--------------------------------+--------------------------------------------------------------------------------+

AbstractIndicatorWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AbstractIndicatorWriterAdapter shares most of the write
functionality with the AbstractGroupWriterAdapter. In fact, they both
implement the following writer interfaces:

Interface \| ----------------------------------------- \|
``AttributeAssociateWritable<T>`` \| ``GroupAssociateWritable<T>`` \|
``IndicatorAssociateWritable<T>`` \|
``SecurityLabelAssociateWritable<T>`` \| ``TagAssociateWritable<T>`` \|
``VictimAssetAssociateWritable<T>`` \|

These interfaces allow the AbstractIndicatorWriterAdapter to run all of
the same methods as the AbstractGroupWriterAdapter.

The key parameter-level distinction between the
AbstractIndicatorWriterAdapter and the AbstractGroupWriterAdapter is the
type (T) for the ``uniqueId`` parameter. As mentioned in previous
sections, Indicator ``uniqueId`` types are all Strings. The
method-naming conventions are the same.

FileIndicatorWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

FileIndicatorWriterAdapter, which all the functionality of the AbstractIndicatorWriterAdapter with the addition of the
following write methods:

+---------------------------------------+-----------------------------------------------------------------+
| Type                                  | Method                                                          |
+=======================================+=================================================================+
| ``WriteListResponse<FileOccurrence>`` | updateFileOccurrences(\ ``String fileHash``,                    |
|                                       | ``List<FileOccurrence> fileOccurrences``)                       |
+---------------------------------------+-----------------------------------------------------------------+
| ``WriteListResponse<FileOccurrence>`` | updateFileOccurrences(\ ``String fileHash``,                    |
|                                       | ``List<FileOccurrence> fileOccurrences``, ``String ownerName``) |
+---------------------------------------+-----------------------------------------------------------------+
| ``FileOccurrence``                    | updateFileOccurrence(\ ``String fileHash``,                     |
|                                       | ``FileOccurrence fileOccurrence``)                              |
+---------------------------------------+-----------------------------------------------------------------+
| ``FileOccurrence``                    | updateFileOccurrence(\ ``String fileHash``,                     |
|                                       | ``FileOccurrence fileOccurrence``, ``String ownerName``)        |
+---------------------------------------+-----------------------------------------------------------------+

DocumentWriterAdapter
~~~~~~~~~~~~~~~~~~~~~

DocumentWriterAdapter has all the functionality of the AbstractGroupWriterAdapter with the addition of the following
write methods:

+-----------------------------+---------------------------------------------------------------------+
| Type                        | Method                                                              |
+=============================+=====================================================================+
| ``ApiEntitySingleResponse`` | uploadFile(\ ``int uniqueId``, ``File file``)                       |
+-----------------------------+---------------------------------------------------------------------+
| ``ApiEntitySingleResponse`` | uploadFile(\ ``int uniqueId``, ``File file``, ``String ownerName``) |
+-----------------------------+---------------------------------------------------------------------+

AbstractBatchWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The AbstractBatchWriterAdapter class allows batch writing of indicators
to the API. The adapter facilitates the initial creation and upload of
the batch file using the following write methods:

+-------------------------------+--------------------------------------------------------+
| Type                          | *Method*                                               |
+===============================+========================================================+
| ``ApiEntitySingleResponse``   | create(\ ``BatchConfig item`` )                        |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``BatchConfig item``, ``String ownerName``)   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | uploadFile(\ ``int batchId``, ``File file``)           |
+-------------------------------+--------------------------------------------------------+

Once a batch configuration is created, the ApiEntitySingleResponse
object returns BatchResponseData with a batchId if successful. This
batchId is used to upload the batch file using the ``uploadFile``
method. At this point, a successfully response to the upload will trigger
the batch. Use the BatchReaderAdapter to poll for the status of the
batch.

SecurityLabelWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SecurityLabelWriterAdapter class allows
`Group <#associate-groups>`__ and `Indicator <#associate-indicators>`__
associations. Much like the Indicator Adapters, the ``uniqueId`` is a
user-created Security Label String. In addition to creating
associations, the SecurityLabelWriterAdapter allows deleting
associations from `Group <#delete-group-association>`__ and
`Indicator <#delete-indicator-associations>`__ types.

Below is the standard create methods available to all WriterAdapter’s.
Note that the deletes require the Security Label as the ``uniqueId``
String (P). The create and update requires the full SecurityLabel object
(T).

+-----------------------------+------------------------------------------------------+
| Type                        | *Method*                                             |
+=============================+======================================================+
| ``WriteListResponse<T>``    | create(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``)                        |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``, ``String ownerName``)  |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``)                               |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``, ``String ownerName``)         |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``, ``String ownerName``) |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+

TagWriterAdapter
~~~~~~~~~~~~~~~~

The TagWriterAdapter class allows `Group <#associate-groups>`__ and
`Indicator <#associate-indicators>`__ associations. Much like the
Indicator Adapters, the uniqueId is a user-created Tag name String. In
addition to creating associations, the TagWriterAdapter allows deleting
associations from `Group <#delete-group-association>`__ and
`Indicator <#delete-indicator-associations>`__ types.

Below is the standard create methods available to all WriterAdapters.
Note that the deletes require the Tag Name as the ``uniqueId`` String
(P). The create and update requires the full Tag object (T).

+-----------------------------+------------------------------------------------------+
| Type                        | *Method*                                             |
+=============================+======================================================+
| ``WriteListResponse<T>``    | create(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``)                        |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``, ``String ownerName``)  |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``)                               |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``, ``String ownerName``)         |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``, ``String ownerName``) |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+

TaskWriterAdapter
~~~~~~~~~~~~~~~~~

The TaskWriterAdapter allows

Below is the standard create methods available to all WriterAdapters.

+-----------------------------+------------------------------------------------------+
| Type                        | Method                                               |
+=============================+======================================================+
| ``WriteListResponse<T>``    | create(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``)                        |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``, ``String ownerName``)  |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``)                               |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``, ``String ownerName``)         |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``, ``String ownerName``) |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+

In addition to the User-specific methods below. Note the delete methods
require the username while the create methods require the entire User
object.

+------------------+----------------------------------------------+
| Type             | *Method*                                     |
+==================+==============================================+
| ``UserResponse`` | createAssignee(P uniqueId, User assignee)    |
+------------------+----------------------------------------------+
| ``UserResponse`` | createEscalatee(P uniqueId, User escalatee)  |
+------------------+----------------------------------------------+
| ``UserResponse`` | deleteAssignee(P uniqueId, String userName)  |
+------------------+----------------------------------------------+
| ``UserResponse`` | deleteEscalatee(P uniqueId, String userName) |
+------------------+----------------------------------------------+

VictimWriterAdapter
~~~~~~~~~~~~~~~~~~~

The TagWriterAdapter class allows `Group <#associate-groups>`__,
`Indicator <#associate-indicators>`__, and VictimAsset associations.
Much like the Group Adapters, the uniqueId is a user-created Security
Label String. In addition to creating associations, the
VictimAssetWriterAdapter can remove associations for
`Group <#delete-group-association>`__, `Indicator <#delete-indicator-associations>`__,
and `VictimAssets <#delete-victimasset-associations>`__.

Below is the standard create methods available to all WriterAdapters.
Note that the deletes require the system-generated VictimAsset ID as the
``uniqueId`` Integer (P). The create and update requires the full
VictimAsset object (T).

+-----------------------------+------------------------------------------------------+
| Type                        | *Method*                                             |
+=============================+======================================================+
| ``WriteListResponse<T>``    | create(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | create(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``)                        |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<P>``    | delete(\ ``List<P> itemIds``, ``String ownerName``)  |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``)                               |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | delete(\ ``P itemId``, ``String ownerName``)         |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``)                       |
+-----------------------------+------------------------------------------------------+
| ``WriteListResponse<T>``    | update(\ ``List<T> itemList``, ``String ownerName``) |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``)                                 |
+-----------------------------+------------------------------------------------------+
| ``ApiEntitySingleResponse`` | update(\ ``T item``, ``String ownerName``)           |
+-----------------------------+------------------------------------------------------+

Writer Examples
~~~~~~~~~~~~~~~

Writer Delete Example:

.. code-block:: java

      2 
      3 import com.threatconnect.sdk.client.reader.AbstractGroupReaderAdapter;
      4 import com.threatconnect.sdk.client.reader.ReaderAdapterFactory;
      5 
      6 import com.threatconnect.sdk.client.writer.AbstractGroupWriterAdapter;
      7 import com.threatconnect.sdk.client.writer.WriterAdapterFactory;
      8 import com.threatconnect.sdk.server.response.entity.ApiEntitySingleResponse;
      9 
     10 import com.threatconnect.sdk.server.entity.Adversary;
     11 import com.threatconnect.sdk.conn.Connection;
     12 import java.io.IOException;
     13 
     
    130     private static void doDelete(Connection conn) {
    131         AbstractGroupWriterAdapter<Adversary> writer = WriterAdapterFactory.createAdversaryGroupWriter(conn);
    132 
    133         Adversary adversary = new Adversary();
    134         adversary.setName("Test Adversary");
    135         adversary.setOwnerName("System");
    136 
    137         try {
    138             ApiEntitySingleResponse<Adversary,?> createResponse = writer.create(adversary);
    139             if ( createResponse.isSuccess() ) {
    140                 System.out.println("Saved: " + createResponse.getItem() );
    141                 ApiEntitySingleResponse<Adversary,?> deleteResponse 
    142                    = writer.delete( createResponse.getItem().getId() );
    143                 if ( deleteResponse.isSuccess() ) {
    144                     System.out.println("Deleted: " + createResponse.getItem() );
    145                 } else {
    146                     System.err.println("Delete Failed. Cause: " + deleteResponse.getMessage() );
    147                 }
    148             } else {
    149                 System.err.println("Create Failed. Cause: " + createResponse.getMessage() );
    150             }
    151             
    152         } catch (IOException | FailedResponseException ex) {
    153             System.err.println("Error: " + ex.toString());
    154         }
    155     
    156     }
     

This section offers examples on how to create, delete, and update data
using the Java SDK for ThreatConnect.

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 131          | Since Adversary objects from the ThreatConnect API will be  |
|              | created and deleted, an AbstractGroupWriterAdapter with the |
|              | Adversary parameterized type applied is instantiated.       |
+--------------+-------------------------------------------------------------+
| 138-139      | An Adversary object with the ThreatConnect API is created,  |
|              | the response is captured, and ``isSuccess()`` is called to  |
|              | check if the save was successful.                           |
+--------------+-------------------------------------------------------------+
| 140          | The response Adversary object returned from the             |
|              | ThreatConnect API is printed. The ``getItem()``\ method     |
|              | will return this object with the ID field populated. This   |
|              | method will always hold the saved item on a successful      |
|              | response.                                                   |
+--------------+-------------------------------------------------------------+
| 141-142      | The ID from the successful create is used to delete the     |
|              | same Adversary object. Note that the call to the            |
|              | ``delete()`` method requires the system-generated Adversary |
|              | ID.                                                         |
+--------------+-------------------------------------------------------------+
| 143-144      | The delete response is verified as successful, and the      |
|              | original response is dumped.                                |
+--------------+-------------------------------------------------------------+
| 146          | With a failed delete, the error message is printed by       |
|              | calling the ``getMessage()`` method on the response object. |
+--------------+-------------------------------------------------------------+
| 149          | If the original create failed, the ``getMessage()`` method  |
|              | is also called to find the cause.                           |
+--------------+-------------------------------------------------------------+

Writer Update Example
~~~~~~~~~~~~~~~~~~~~~

Writer Update Example:

.. code-block:: java

      2 
      3 import com.threatconnect.sdk.client.reader.AbstractGroupReaderAdapter;
      4 import com.threatconnect.sdk.client.reader.ReaderAdapterFactory;
      5 import com.threatconnect.sdk.client.writer.AbstractGroupWriterAdapter;
      6 import com.threatconnect.sdk.client.writer.WriterAdapterFactory;
      7 import com.threatconnect.sdk.conn.Connection;
      8 import com.threatconnect.sdk.exception.FailedResponseException;
      9 import com.threatconnect.sdk.server.entity.Adversary;

     15 import com.threatconnect.sdk.server.response.entity.ApiEntitySingleResponse;
     16 import java.io.IOException;
     17 import java.util.List;
     18 

    153 
    154     private static void doUpdate(Connection conn) {
    155         AbstractGroupWriterAdapter<Adversary> writer = WriterAdapterFactory.createAdversaryGroupWriter(conn);
    156 
    157         Adversary adversary = new Adversary();
    158         adversary.setName("Test Adversary");
    159         adversary.setOwnerName("System");
    160 
    161         try {
    162             ApiEntitySingleResponse<Adversary,?> createResponse = writer.create(adversary);
    163             if ( createResponse.isSuccess() ) {
    164                 System.out.println("Created Adversary: " + createResponse.getItem() );
    165 
    166                 Adversary updatedAdversary = createResponse.getItem();
    167                 updatedAdversary.setName("UPDATED: " + createResponse.getItem().getName());
    168                 System.out.println("Saving Updated Adversary: " + updatedAdversary );
    169 
    170                 ApiEntitySingleResponse<Adversary,?> updateResponse = writer.update( updatedAdversary );
    171                 if ( updateResponse.isSuccess() ) {
    172                     System.out.println("Updated Adversary: " + updateResponse.getItem());
    173                 } else {
    174                     System.err.println("Failed to Update Adversary: " + updateResponse.getMessage() );
    175                 }   
    176             } else {
    177                 System.err.println("Failed to Create Adversary: " + createResponse.getMessage() );
    178             }   
    179             
    180         } catch (IOException | FailedResponseException ex) {
    181             System.err.println("Error: " + ex.toString()); 
    182         }   
    183         
    184     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 155-164      | A test Adversary is created and saved to the ThreatConnect  |
|              | API.                                                        |
+--------------+-------------------------------------------------------------+
| 166-168      | The created Adversary is assigned to a variable called      |
|              | "updatedAdversary()" so that the Adversary name can be      |
|              | changed (line 167). Before updating the Adversary in        |
|              | ThreatConnect, it is printed to the console. The output     |
|              | should have an ID value populated and the name should read: |
|              | "UPDATED: Test Adversary".                                  |
+--------------+-------------------------------------------------------------+
| 170-172      | The "update()" method is called to save the changes to      |
|              | ThreatConnect. The argument to this method is the actual    |
|              | Adversary object. Just like the delete, the response        |
|              | success is verified and written to the console.             |
+--------------+-------------------------------------------------------------+

Writer Add Attribute Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Add Attribute Example

.. code-block:: java

      1 
      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 
     15     private static Attribute createTestAttribute() {
     16         Attribute attribute = new Attribute();
     17         attribute.setSource("Test Source");
     18         attribute.setDisplayed(true);
     19         attribute.setType("Description");
     20         attribute.setValue("Test Attribute Description");
     21 
     22         return attribute;
     23     }

     69     private static void doAddAttribute(Connection conn) {
     70         AbstractGroupWriterAdapter<Email> writer = WriterAdapterFactory.createEmailGroupWriter(conn);
     71 
     72         Email email = createTestEmail();
     73         Attribute attribute = createTestAttribute();
     74 
     75         try {
     76             // ------------------------------------------------------------------
     77             // Create Email
     78             // ------------------------------------------------------------------
     79             ApiEntitySingleResponse<Email, ?> createResponse = writer.create(email);
     80             if (createResponse.isSuccess()) {
     81                 System.out.println("Created Email: " + createResponse.getItem());
     82 
     83                 // -------------------------------------------------------------------
     84                 // Add Attribute
     85                 // -------------------------------------------------------------------
     86                 ApiEntitySingleResponse<Attribute, ?> attribResponse
     87                     = writer.addAttribute( createResponse.getItem().getId(), attribute );
     88 
     89                 if ( attribResponse.isSuccess() ) {
     90                     System.out.println("\tAdded Attribute: " + attribResponse.getItem());
     91                 } else {
     92                     System.err.println("Failed to Add Attribute: " + attribResponse.getMessage());
     93                 }
     94 
     95             } else {
     96                 System.err.println("Failed to Create Email: " + createResponse.getMessage());
     97             }
     98 
     99         } catch (IOException | FailedResponseException ex) {
    100             System.err.println("Error: " + ex.toString());
    101         }
    102 
    103     }
    104

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 72-73        | The test email object and the Attribute to be added are     |
|              | created.                                                    |
+--------------+-------------------------------------------------------------+
| 79-81        | The email in ThreatConnect is created and checked that it   |
|              | is successful.                                              |
+--------------+-------------------------------------------------------------+
| 86-87        | The ``addAttribute()`` method takes the Email Group ID and  |
|              | the Attribute object to be added.                           |
+--------------+-------------------------------------------------------------+
| 89-90        | To confirm that the Attribute was added successfully, the   |
|              | response is checked.                                        |
+--------------+-------------------------------------------------------------+

Writer Associate Indicator Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Indicator Example

.. code-block:: java

      1 
      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 

     25     private static Host createTestHost() {
     26         Host host = new Host();
     27         host.setOwnerName("System");
     28         host.setDescription("Test Host");
     29         host.setHostName("www.bad-hostname.com");
     30         host.setRating( 5.0 );
     31         host.setConfidence(98.0);
     32 
     33         return host;
     34     }

    104 
    105     private static void doAssociateIndicator(Connection conn) {
    106         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    107         AbstractIndicatorWriterAdapter<Host> hWriter = WriterAdapterFactory.createHostIndicatorWriter(conn);
    108 
    109         Email email = createTestEmail();
    110         Host host = createTestHost();
    111 
    112         try {
    113 
    114             // ----------------------------------------
    115             // Create Email and Host
    116             // ----------------------------------------
    117             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
    118             ApiEntitySingleResponse<Host,?> createResponseHost = hWriter.create(host);
    119             if (createResponseEmail.isSuccess() && createResponseHost.isSuccess() ) {
    120                 System.out.println("Created Email: " + createResponseEmail.getItem());
    121                 System.out.println("Created Host: " + createResponseHost.getItem());
    122 
    123                 // -----------------------------------------
    124                 // Associate Host
    125                 // -----------------------------------------
    126                 ApiEntitySingleResponse assocResponse
    127                      gWriter.associateIndicatorHost(createResponseEmail.getItem().getId()
    128                                                   , createResponseHost.getItem().getHostName() );
    129 
    130                 if ( assocResponse.isSuccess() ) {
    131                     System.out.println("\tAssociated Host: " + createResponseHost.getItem().getHostName() );
    132                 } else {
    133                     System.err.println("Failed to Add Attribute: " + assocResponse.getMessage());
    134                 }
    135 
    136             } else {
    137                 if ( !createResponseEmail.isSuccess() ) {
    138                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    139                 }
    140                 if ( !createResponseHost.isSuccess() ) {
    141                     System.err.println("Failed to Create Host: " + createResponseHost.getMessage());
    142                 }
    143             }
    144 
    145         } catch (IOException | FailedResponseException ex) {
    146             System.err.println("Error: " + ex.toString());
    147         }
    148 
    149     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 106-107      | Two writers are created: one for the new email and the      |
|              | other for the host to be associated.                        |
+--------------+-------------------------------------------------------------+
| 109-110      | The test email object is crated, as well as the host to be  |
|              | associated.                                                 |
+--------------+-------------------------------------------------------------+
| 117-121      | To set up the example, both email and host are created in   |
|              | ThreatConnect. The create is verified as successful and the |
|              | items are printed to the console.                           |
+--------------+-------------------------------------------------------------+
| 126-128      | The host is associated to the Email Group by using the      |
|              | Email ID and the Host Name (the unique ID for the Host      |
|              | Indicator).                                                 |
+--------------+-------------------------------------------------------------+
| 130-133      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Associate Group Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Group Example

.. code-block:: java

      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 

     36     private static Threat createTestThreat() {
     37         Threat threat = new Threat();
     38         threat.setOwnerName("System");
     39         threat.setName("Test Threat");
     40 
     41         return threat;
     42     }

    151 
    152     private static void doAssociateGroup(Connection conn) {
    153         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    154         AbstractGroupWriterAdapter<Threat> tWriter = WriterAdapterFactory.createThreatGroupWriter(conn);
    155 
    156         Email email = createTestEmail();
    157         Threat threat = createTestThreat();
    158 
    159         try {
    160             // ---------------------------------
    161             // Create Email and Threat
    162             // ---------------------------------
    163             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
    164             ApiEntitySingleResponse<Threat,?> createResponseThreat = tWriter.create(threat);
    165             if (createResponseEmail.isSuccess() && createResponseThreat.isSuccess() ) {
    166                 System.out.println("Created Email: " + createResponseEmail.getItem());
    167                 System.out.println("Created Threat: " + createResponseThreat.getItem());
    168 
    169                 // ----------------------------------
    170                 // Associate Threat
    171                 // ----------------------------------
    172                 ApiEntitySingleResponse assocResponse
    173                     = gWriter.associateGroupThreat(createResponseEmail.getItem().getId(), 
    174                                                 createResponseThreat.getItem().getId());
    175                 
    176                 if ( assocResponse.isSuccess() ) {
    177                     System.out.println("\tAssociated Threat: " + createResponseThreat.getItem().getId() );
    178                 } else {
    179                     System.err.println("Failed to Associate Threat: " + assocResponse.getMessage());
    180                 }
    181             
    182             } else { 
    183                 if ( !createResponseEmail.isSuccess() ) {
    184                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    185                 }
    186                 if ( !createResponseThreat.isSuccess() ) {
    187                     System.err.println("Failed to Create Threat: " + createResponseThreat.getMessage());
    188                 }
    189             }
    190         
    191         } catch (IOException | FailedResponseException ex) {
    192             System.err.println("Error: " + ex.toString());
    193         }
    194 
    195     }
    196 

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 153-154      | Two writers are created: one for the new email and the      |
|              | other for the Threat to be associated.                      |
+--------------+-------------------------------------------------------------+
| 156-157      | The test email object is created, as well as the Threat to  |
|              | be associated.                                              |
+--------------+-------------------------------------------------------------+
| 163-167      | To set up the example, both email and Threat are created in |
|              | ThreatConnect, the create is verified as successful, and    |
|              | the items are printed to the console.                       |
+--------------+-------------------------------------------------------------+
| 172-174      | The Threat is associated to the Email Group by using the    |
|              | Email ID and the Threat ID.                                 |
+--------------+-------------------------------------------------------------+
| 176-179      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Associate Tag Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Tag Example

.. code-block:: java

      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 

     44     private static Tag createTestTag() {
     45         Tag tag = new Tag();
     46         tag.setName("Test-Tag");
     47         tag.setDescription("Test Tag Description");
     48 
     49         return tag;
     50     }

    196 
    197     private static void doAssociateTag(Connection conn) {
    198         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    199         TagWriterAdapter tWriter = WriterAdapterFactory.createTagWriter(conn);
    200 
    201         Email email = createTestEmail();
    202         Tag tag = createTestTag();
    203 
    204         try {
    205             // -------------------------------------------
    206             // Create Email and Tag 
    207             // -------------------------------------------
    208             ApiEntitySingleResponse<Email, ?> createResponseEmail = gWriter.create(email);
    209             tWriter.delete(tag.getName()); // delete if it exists
    210             ApiEntitySingleResponse<Tag, ?> createResponseTag = tWriter.create(tag);
    211 
    212             if (createResponseEmail.isSuccess() && createResponseTag.isSuccess() ) {
    213                 System.out.println("Created Email: " + createResponseEmail.getItem());
    214                 System.out.println("Created Tag: " + createResponseTag.getItem());
    215 
    216                 // ---------------------------------------------
    217                 // Associate Tag
    218                 // ---------------------------------------------
    219                 ApiEntitySingleResponse assocResponse
    220                     = gWriter.associateTag(createResponseEmail.getItem().getId()
    221                                          , createResponseTag.getItem().getName() );
    222 
    223                 if ( assocResponse.isSuccess() ) {
    224                     System.out.println("\tAssociated Tag: " + createResponseTag.getItem().getName() );
    225                 } else {
    226                     System.err.println("Failed to Associate Tag: " + assocResponse.getMessage());
    227                 }
    228 
    229             } else {
    230                 if ( !createResponseEmail.isSuccess() ) {
    231                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    232                 }
    233                 if ( !createResponseTag.isSuccess() ) {
    234                     System.err.println("Failed to Create Tag: " + createResponseTag.getMessage());
    235                 }
    236             }
    237         
    238         } catch (IOException | FailedResponseException ex) {
    239             System.err.println("Error: " + ex.toString());
    240         }
    241     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 198-199      | Two writers are created: one for the new email and the      |
|              | other for the Tag to associate.                             |
+--------------+-------------------------------------------------------------+
| 201-202      | The test email object, and the Tag to associate, are        |
|              | created.                                                    |
+--------------+-------------------------------------------------------------+
| 208-214      | To set up the example, both email and Tag are created in    |
|              | ThreatConnect. The create is verified as successful, and    |
|              | the items are printed to the console.                       |
+--------------+-------------------------------------------------------------+
| 219-221      | The Tag is associated to the Email Group by using the Email |
|              | ID and the Tag name (the ``uniqueID`` for the Tag).         |
+--------------+-------------------------------------------------------------+
| 223-226      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Associate Victim Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Victim Example

.. code-block:: java

     59 
     60     private static Victim createTestVictim() {
     61         Victim victim = new Victim();
     62         victim.setOrg("System");
     63         victim.setName("Test API Victim");
     64         victim.setDescription("Test API Victim Description");
     65 
     66         return victim;
     67     }

    304     private static void doAssociateVictim(Connection conn) {
    305         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    306         VictimWriterAdapter vWriter = WriterAdapterFactory.createVictimWriter(conn);
    307         
    308         Email email = createTestEmail();
    309         Victim victim = createTestVictim();
    310         
    311         try {
    312             // --------------------------------
    313             // Create Email and Victim
    314             // --------------------------------
    315             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
    316             ApiEntitySingleResponse<Victim,?> createResponseVictim = vWriter.create(victim);
    317             if (createResponseEmail.isSuccess() && createResponseVictim.isSuccess() ) {
    318                 System.out.println("Created Email: " + createResponseEmail.getItem());
    319                 System.out.println("Created Victim: " + createResponseVictim.getItem());
    320 
    321                 // --------------------------------
    322                 // Associate Victim
    323                 // --------------------------------
    324                 ApiEntitySingleResponse assocResponse
    325                     = gWriter.associateVictim(createResponseEmail.getItem().getId()
    326                                             , createResponseVictim.getItem().getId());
    327 
    328                 if ( assocResponse.isSuccess() ) {
    329                     System.out.println("\tAssociated Victim: " + createResponseVictim.getItem().getId() );
    330                 } else {
    331                     System.err.println("Failed to Associate Victim: " + assocResponse.getMessage());
    332                 }
    333 
    334             } else {
    335                 if ( !createResponseEmail.isSuccess() ) {
    336                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    337                 }
    338                 if ( !createResponseVictim.isSuccess() ) {
    339                     System.err.println("Failed to Create Victim: " + createResponseVictim.getMessage());
    340                 }
    341             }
    342 
    343         } catch (IOException | FailedResponseException ex) {
    344             System.err.println("Error: " + ex.toString());
    345         }
    346 
    347     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 305-306      | Two writers are created: one for the new email and the      |
|              | other for the Victim to associate.                          |
+--------------+-------------------------------------------------------------+
| 308-309      | The test email object, and the Victim to associate, are     |
|              | created.                                                    |
+--------------+-------------------------------------------------------------+
| 315-319      | To set up the example, both email and Victim are created in |
|              | ThreatConnect. The create is verified as successful, and    |
|              | the items are printed to the console.                       |
+--------------+-------------------------------------------------------------+
| 324-326      | The Victim is associated to the Email Group by using the    |
|              | Email ID and the Victim ID.                                 |
+--------------+-------------------------------------------------------------+
| 328-331      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Remove Association Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Remove Association Example

.. code-block:: java
    :linenos:
    :lineno-start: 243

    private static void doRemoveAssociatedTag(Connection conn) {

        AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
        TagWriterAdapter tWriter = WriterAdapterFactory.createTagWriter(conn);

        Email email = createTestEmail();
        Tag tag = createTestTag();

        try {
            // -----------------------------------------
            // Create Email and Tag 
            // -----------------------------------------
            ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
            tWriter.delete(tag.getName()); // delete if it exists
            ApiEntitySingleResponse<Tag, ?> createResponseTag = tWriter.create(tag);

            if (createResponseEmail.isSuccess() && createResponseTag.isSuccess() ) {
                System.out.println("Created Email: " + createResponseEmail.getItem());
                System.out.println("Created Tag: " + createResponseTag.getItem());

                // -----------------------------------------
                // Associate Tag
                // -----------------------------------------
                ApiEntitySingleResponse assocResponse
                    = gWriter.associateTag(createResponseEmail.getItem().getId()
                                         , createResponseTag.getItem().getName() );

                if ( assocResponse.isSuccess() ) {
                    System.out.println("\tAssociated Tag: " + createResponseTag.getItem().getName() );

                    // -----------------------------------------
                    // Delete Association
                    // -----------------------------------------
                    ApiEntitySingleResponse dissociateResponse
                        = gWriter.dissociateTag(createResponseEmail.getItem()
                                      .getId(), createResponseTag.getItem().getName() );

                    if ( dissociateResponse.isSuccess() ) {
                        System.out.println("\tDeleted Associated Tag: " + createResponseTag.getItem().getName() );
                    } else {
                        System.err.println("Failed to delete Associated Tag: "+ dissociateResponse.getMessage());
                    }

                } else {
                    System.err.println("Failed to Associate Tag: " + assocResponse.getMessage());
                }

            } else {
                if ( !createResponseEmail.isSuccess() ) {
                    System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
                }
                if ( !createResponseTag.isSuccess() ) {
                    System.err.println("Failed to Create Tag: " + createResponseTag.getMessage());
                }
            }

        } catch (IOException | FailedResponseException ex) {
            System.err.println("Error: " + ex.toString());
        }
    }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 245-271      | The Email Group is created and associated with the Tag      |
|              | item.                                                       |
+--------------+-------------------------------------------------------------+
| 276-278      | The ``dissociateTag()`` method is called using the same     |
|              | parameters as the associate method. The email item ID value |
|              | is used with the Tag name.                                  |
+--------------+-------------------------------------------------------------+
| 280-281      | The deleting is verified as successful, and the message is  |
|              | dumped to the console.                                      |
+--------------+-------------------------------------------------------------+

**Summary**

The previous two examples explained how to:

-  Delete and update an Adversary and verify that the action was
   successfully applied to ThreatConnect
-  Add an Attribute to a Group item
-  Associate Indicators, Groups, Tags, and Victims
-  Remove Association from a Group item
