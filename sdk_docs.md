<b>About This Document</b>

This section explains the process of coding Python applications, and the implementation of the Python SDK, using the ThreatConnect API. The Python SDK offers coverage of all features in version 2.0 of the ThreatConnect API—including the ability to write data to ThreatConnect.

The goal of this Python SDK library is to provide a programmatic abstraction layer around the ThreatConnect API without losing functional coverage over the available API resources. This abstraction layer enables developers to focus on writing enterprise functionality without worrying about low-level RESTful calls and authentication management.

> This document is not a replacement for the official ThreatConnect API documentation. This document serves as a companion to the official documentation for the REST API. Read the official documentation to gain a further understanding of the functional aspects of using the ThreatConnect API.

<b>How to Use This Document</b>

This document explains how to create Groups, Indicators, Associations, Tags, Security Labels, and Victims. Along with creating data elements, a developer will learn how to create, update, delete, and request data from the API using Python. This document assumes the reader knows the Python programming language.

All code examples will be to the right in the code column in a separate box with a monospaced font to facilitate explanation of code functionality. 

## Getting Started

> Python SDK Installation:

```shell
unzip threatconnect-python.zip
cd threatconnect-python
python setup.py install
```

> Example of using ConfigParser to read API configuration values:

```python
read configuration file
config = ConfigParser.RawConfigParser()
config.read('threatconnect.conf')

try:
    api_access_id = config.get('threatconnect', 'api_access_id')
    api_secret_key = config.get('threatconnect', 'api_secret_key')
    api_default_org = config.get('threatconnect', 'api_default_org')
    api_base_url = config.get('threatconnect', 'api_base_url')
except ConfigParser.NoOptionError:
    print('Could not read configuration file.')
    sys.exit(1)
```

> The configuration file should contain the following lines at a minimum:

```
 1 [threatconnect]
 2 api_access_id = 12345678900987654321
 3 api_default_org = Acme Corp
 4 api_secret_key = aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=
 5 api_base_url = https://api.threatconnect.com
```

> The following examples illustrates a typical initialization of the ThreatConnect Class:

```python
tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)
```

Installation of Python 2.7+, along with the Python SDK, is a prerequisite. Typically, Python comes pre-installed on Linux/OS X/Unix systems, so additional steps to install Python are not required. This section will also highlight the basic configuration to connect to the ThreatConnect API. While an IDE will facilitate development of larger-scale systems, it is not required to follow the examples in this document.

To use the RESTful API for ThreatConnect, an API user must be provisioned. See the official ThreatConnect API documentation for details on how to create an API user as it is out of scope for this document.

The Python SDK will need to be configured with an Access ID and Secret Key. One way to achieve this is to use the `ConfigParser` module, which is part of the Python Standard Library. Another option is to use `ArgParse` and pass the configuration items via CLI (command-line interface) arguments. For this example, ConfigParser is used.

Once the configuration has been set up, the developer should be able to run the examples in this document as long as the Python SDK has been installed. 

<b>Third-Party Dependencies</b>

Name          | Version       | Link
------------- | ------------- | ----------------------
requests      | 2.7.0         | [Python Requests](http://docs.python-requests.org/en/latest/)
enum34        | 1.0.4         | [Python Enum34](https://pypi.python.org/pypi/enum34)

<b>Technical Design</b>

The Python SDK for ThreatConnect was designed with a focus on abstracting the API REST calls while enabling the developer to use an enterprise-level programming language. The abstraction layer provides a platform that makes cumbersome API requests simple and provides a powerful filtering feature that minimizes the results returned from the API, when possible, and otherwise utilizes post-API filters.

<b>Supported Resource Types</b>

The Python SDK supports the Resource Types listed below. There is also a mechanism to do manual API requests to cover any API calls that are not provided with the core functionality.

Object                | Description                     
--------------------- | -----------                     
`adversaries()`       | Adversary container object      
`bulk_indicators()`   | Bulk Indicator container object 
`documents()`         | Document container object       
`emails()`            | Email container object          
`groups()`            | Group container object          
`incidents()`         | Incident container object       
`indicators()`        | Indicator container object      
`owners()`            | Owner container object          
`signatures()`        | Signature container object      
`tasks()`             | Task container object           
`threats()`           | Threat container object         
`victims()`           | Victim container object         

## Example Python App

> Example of Python SDK writing to the ThreatConnect API:

```python
import ConfigParser
from threatconnect import ThreatConnect

config = ConfigParser.RawConfigParser()
config.read(config_file)

try:
    api_access_id = config.get('threatconnect', 'api_access_id')
    api_secret_key = config.get('threatconnect', 'api_secret_key')
    api_default_org = config.get('threatconnect', 'api_default_org')
    api_base_url = config.get('threatconnect', 'api_base_url')
except ConfigParser.NoOptionError:
    print('Could not read configuration file.')
    sys.exit(1)

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

owners = tc.owners()

try:
    owners.retrieve()
except RunTimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for owner in owners:
    print(owner.id)
    print(owner.name)
    print(owner.type)
```

The example illustrates how to write a program using the Python SDK for the ThreatConnect API. An Owner's object will be created in order to pull a collection of all Owners to which the API account being used has access. Once retrieved, the Owners objects will be printed to the console.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`import ConfigParser`                     | Import the ConfigParser module used to read <br> the configuration file. 
`from threatconnect import ThreatConnect` | Import the ThreatConnect Python SDK module. 
`config = ConfigParser.RawConfigParser()` | Get an instance of ConfigParser. 
`config.read(config_file)`                | Parse the configuration file containing the <br> API settings. 
`api_access_id = config.get('threatco...` | Get the configuration items from the config <br> instance. 
`tc = ThreatConnect(api_access_id, ap...` | Instantiate an instance of the ThreatConnect <br> Class. 
`owners = tc.owners()`                    | Create an Owner's container object. 
`owners.retrieve()`                       | Trigger an API request to retrieve Owners.  
`for owner in owners:`                    | Iterate through Owner's generator. 
`print(owner.id)`                         | Display the **'id'** property of the Owner. 

### Logging

> Example of Python SDK calling log-file and debug level:

```python
    tc.set_tcl_file('log/tc.log', 'debug')
    tc.set_tcl_console_level('critical')
```

The Python SDK allows for the setting of the log-file location and debug level. The level on the console logging can be set as well. The default logging level for each is *critical*.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc.set_tcl_file('log/tc.log', 'debug')`  | Set the destination log path and logging level. 
`tc.set_tcl_console_level('info')`        | Set the console logging level. 

<b>Summary</b>

This section explained how to:

* Connect to the ThreatConnect API by passing reading the configuration file
* Get a list of Owners
* Iterate through an object container

## Developing a Python App

This section provides an overview of the Python app development process and how to package an app for deployment to the ThreatConnect platform.

<b>Supported Version</b>

The current supported version for Cloud deployment Python apps is 2.7. This Python version is typically pre-installed on Linux®/Mac® OS/Unix systems. On-Premise clients do not have this restriction. They simply need to ensure that the Python runtime is available in their PATH environment variable.

<b>Third-Party Libraries</b>

Third-party libraries are restricted to the list below at this point in time. Cloud deployments will need to contact <support@threatconnect.com> to request installation of additional third-party libraries not on this list.

Name          | Version       | Link
------------- | ------------- | ----------------------
threatconnect | 2.0.0         | [ThreatConnect python libraries](https://github.com/ThreatConnect-Inc/threatconnect-python)
requests      | 2.6.0         | [Python Requests](http://docs.python-requests.org/en/latest/)
enum34        | 1.0.4         | [Python Enum34](https://pypi.python.org/pypi/enum34)

### Deployment Configuration
[Apps use a deployment configuration file to define variables and execution environment](#deployment-configuration-file)

##Command-Line Parameters

> Suppose `opendns.py` uses the following syntax:

```python
python opendns.py \
    --tc_log_path log \
    --tc_temp_path tmp \
    --tc_out_path out \
    --tc_api_path https://api.threatconnect.com \
    --api_access_id 1234567890 \
    --api_default_org Test & Org \
    --api_max_results 300 \
    --api_secret_key qwertyuiopasdfghjklzxcvbnm \
    --confidences >=,75 \
    --delete \
    --logging debug \
    --opendns_key x000000x-x0x0-0x00-x000-xx000x00000x \
    --owners Subscriber Community \
    --owners Test & Org \
    --queue_sleep 30 \
    --ratings >=,3.0 
```

> These command line options can be implemented using `argparse`:

```python
import argparse

#
# Parse Args
#
parser = argparse.ArgumentParser()

# Api Args
parser.add_argument('--api_access_id', help='API Access ID', required=True)
parser.add_argument('--api_secret_key', help='API Secret Key', required=True)
parser.add_argument('--api_default_org', help='API Default Org', required=True)
parser.add_argument('--api_max_results', help='API Max Results', type=int)
parser.add_argument('--opendns_key', help='OpenDNS API Key')

# Custom Args
parser.add_argument('--logging', help='Logging Level', default='critical', choices=list(log_level.keys()))
parser.add_argument('--queue_sleep', help='Seconds to Sleep', default=60, type=int)
parser.add_argument('--delete', help='Delete deprecated entries from OpenDNS', action='store_true', default=False)

# API Filter Args
parser.add_argument('--modified_since', help='Modified Since Filter')
parser.add_argument('--owners', help='Owner Names', action='append')
parser.add_argument('--tags', help='Tag Filter', action='append')

# Post Filters
parser.add_argument('--date_added', help='Date Added Filter', action='append')
parser.add_argument('--last_modified', help='Last Modified Filter', action='append')
parser.add_argument('--ratings', help='Rating Filter', action='append')
parser.add_argument('--confidences', help='Confidence Filter', action='append')

# Standard Args
parser.add_argument('--tc_log_path', help='ThreatConnect log path', default='/tmp')
parser.add_argument('--tc_temp_path', help='ThreatConnect temp path', default='/tmp')
parser.add_argument('--tc_api_path', help='ThreatConnect api path', default='https://api.threatconnect.com')

# Parse
args, unknown = parser.parse_known_args()
```

The developer is strongly advised to use a standard library like [argparse](https://docs.python.org/3/library/argparse.html) to simplify command line parsing. 

##Optional Properties

There are some optional flags that may be used by the app to:

 * Restrict intervals for repeating jobs
 * Handle list parsing for parameter arrays
 * Handle Boolean flags to turn features on/off
 * Encrypt parameters like API Keys

<b>Repeating Job Intervals</b>

This optional property controls which interval (in minutes) the job-creation dialogue can use when creating a repeating job. 

A repeating job is a job that runs every day on an interval (e.g., every 30 minutes).

The following property `repeating.minutes = 5,10,15,30,60,120,240,360` displays the following intervals in the repeating schedule picklist:

![Repeating Interval](images/repeating-interval.png "Repeating Interval") 

Multiple values should be separated by a comma. All minutes greater than 60 will be discarded unless they are divisible by 60. If this property is not provided, the following repeating intervals are defaulted during job creation: `60, 120, 240, 360, 720`.

<b>Parsing Argument Lists</b>

There is logic in place for parsing a list of values configured by the job-creation dialogue. In order to allow list parsing for a Python app, the configuration file must include the `list.delimiter` property.  

Delimiters may be a single character or a multi-character String:

`list.delimiter = |`

A parameter that accepts lists must have `<param-name>.list` property set. This enables the job executor to pass this parameter in list form by tokenizing the String using the designated list delimiter. 

No equal sign or property value is required for this flag:

`param.<param-name>.list`

Once these two properties are in place, the Python code must include the option below when the argument is added to the parser. 

This option allows argparse to convert duplicate parameters into a single list:

`action='append'`

<b>Parsing Argument Flags</b>

Apps can also use Boolean flags to designate whether to turn on a specific feature. In the parsing code noted earlier, there is an example of an argument flag (`--delete`) configurable by the job-creation dialogue within ThreatConnect. 

The configuration file must have the following flag present for a Boolean parameter:

`param.<param-name>.flag`

This property will direct the ThreatConnect application to show a checkbox to the job-creation dialogue. Once the job is created, the flag will be passed to each job execution without a parameter value. If the flag is left unchecked during job creation, then no flag is passed on each job execution.

<b>Encrypted Parameters</b>

This property should be used to encrypt private passwords used by the app (e.g., API keys). This added level of security will allow the application to persist the password in encrypted form when at rest. The input field during job creation will be "password" text, and the key will not be visible when typed. 

![Encrypted Field](images/encrypted-field.png "Encrypted Field") 

Use encrypted parameters by setting the following flag:

`param.<param-name>.encrypt`

At runtime, the application runtime environment  will call the app with the decrypted key. At no point in time is the password persisted in decrypted form.

The encrypt flag won't encrypt `.encrypted` parameters until the Keychain feature is enabled on the server. 

##ThreatConnect Parameters

ThreatConnect passes standard parameters to all jobs within its standard sandbox container. There should be no assumptions made on the naming or existence of paths passed in these variables outside of the lifetime of the job execution. 

Since all job executions are run in a sandboxed environment, app developers should never hard-code ThreatConnect Parameters:

ThreatConnect Parameter  | Description                                                                 | 
-------------- | ---------------------------------------------------------------------
`tc_log_path`  | Log path for the specific instance of the job execution.              
`tc_tmp_path`  | Temporary storage path for the specific instance of the job execution.
`tc_out_path`  | Output path for the specific instance of the job execution.           
`tc_api_path`  | Path to the ThreatConnect API server.                                 

##Results ThreatConnect File

Job executions can use a special file called `results.tc` to write results as a mechanism for updating parameters for subsequent runs. A use case for this feature is an app that needs to know the last time it completed successfully in order to process data since that completion. The parameter definitions are quite flexible, with the only restriction that the parameters written to the `results.tc` file must exist in the `configuration` file in order to be persisted.

Example `results.tc` file:

`param.last_completed_time = 1430619556`

Assuming there is a property with the same name in `configuration`, the job executor will update the new property value in the system for the next run. The property will only be stored if the job execution is successful. 

This file should be written to the `tc_out_path` passed as one of the standard TC parameters.

##Exit Codes

There are standard exit codes that ThreatConnect uses to report if a program completed successfully. The Python app is responsible for calling `sys.exit(N)`, where 'N' is the appropriate exit code highlighted below.

When `sys.exit()` is not called by an app, an exit code of zero is returned by default during normal code execution. System-critical errors (e.g., file not found) return non-zero exit codes. The developer is responsible for catching and handling program errors accordingly.

At times a program may want to report a partial failure (e.g.,  batch process where X out of Y updates completed). In cases of partial failure, the system administrator can retrieve the log file for that job execution and view more detailed output from the program run.  

Status          | Description                                                   
--------------- | --------------------------------------------------------------
Success         | Exit code 0 - Process completed successfully.                  
Partial Failure | Exit code 3 - Process had a partial failure.                   
Failure         | Any value not 0 or 3 (typically Exit code 1) - Process failed. 

##Wrapper-Testing Utility

> Command line argument script example:

```python
# Config file for tc-wrapper.py to call any ThreatConnect integration script
# with these properties as command line arguments:
#
#   Example:
#
#       python tc-wrapper.py <my-script.py>
[threatconnect]
tc_log_path = /tmp
tc_out_path = /tmp
tc_temp_path = /tmp
tc_api_path = https://api.threatconnect.com


```

> Calling the wrapper:

```python

    python tc-wrapper.py <my-script.py>

```

> The wrapper calls the developer's program with the parameters as ThreatConnect would:

```python
python <my-script.py> \
    --tc_log_path /tmp \
    --tc_temp_path /tmp \
    --tc_out_path /tmp \
    --tc_api_path https://api.threatconnect.com \


```

The command line parameters can be extensive. To facilitate app development, there is a Python wrapper utility that takes a `tc.conf` file and calls a Python script with the properties from the configuration file as command-line parameters. This simulates the way ThreatConnect would call the app in a production environment.

The configuration file should be in the same location as the developer's main Python script, then call the wrapper.

### Python Examples

 * [SDK Examples Directory](https://github.com/ThreatConnect-Inc/threatconnect-python/tree/master/examples)

## Python Retrieve

<b>Adversaries Retrieve</b>

This section explains how to work with ThreatConnect Adversary Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                 
---------------------| ------------ | ------------------------------------------------------------
`add_id()`             | int          | Filter Adversary by ID 
`add_document_id()`    | int          | Filter Adversary on associated Document ID 
`add_email_id()`       | int          | Filter Adversary on associated Email ID 
`add_incident_id()`    | int          | Filter Adversary on associated Incident ID 
`add_indicator()`      | str          | Filter Adversary on associated Indicator 
`add_owner()`          | list or str  | Filter Adversary on associated Owner 
`add_security_label()` | str          | Filter Adversary on associated Security Label 
`add_signature_id()`   | int          | Filter Adversary on associated Signature ID 
`add_tag()`            | str          | Filter Adversary on applied Tag 
`add_threat_id()`      | int          | Filter Adversary on associated Threat ID 
`add_victim_id()`      | int          | Filter Adversary on associated Victim ID 

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                 
---------------------| ------------ | ------------------------------------------------------------
`add_pf_name()`        | str          | Filter Adversary on name 
`add_pf_date_added()`  | str          | Filter Adversary on date added 

###Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python
tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

adversaries = tc.adversaries()

try:
    owner = 'Example Community'
    filter1 = adversaries.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    adversaries.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for adversary in adversaries:
    print(adversary.id)
    print(adversary.name)
    print(adversary.date_added)
    print(adversary.weblink)
```

This example will demonstrate how to retrieve Adversaries while applying filters. Two filters will be added: one for the Owner and another for a Tag. The result set returned from this example will contain any Adversaries in the "Example Community" Owner that has a Tag of ***EXAMPLE***.

Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters, see the [Advanced Filter Tutorial](#filtering).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`adversaries = tc.adversaries()`          | Instantiate an Adversaries container object. 
`filter1 = adversaries.add_filter()`      | Add a filter object to the Adversaries container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Adversaries with the 'Example' tag. 
`adversaries.retrieve()`                  | Trigger the API request and retrieve the Adversaries <br> intelligence data. 
`for adversary in adversaries:`           | Iterate over the Adversaries container object generator. 
`print(adversary.id)`                     | Display the **'id'** property of the Adversary object. 

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

## Bulk Indicator Download

This section explains how to work with ThreatConnect Bulk Indicators.

<b>Supported API Filters</b>

The Bulk Download feature of the ThreatConnect API does not support any API filters.

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter                             | Value Type   | Description                                                  
---------------------------------- | ------------ | ------------------------------------------------------------ 
`add_pf_attribute()`                 | str          | Filter Indicators on Attribute type. 
`add_pf_confidence()`                | int          | Filter Indicators on Confidence value. 
`add_pf_date_added()`                | str          | Filter Indicators on date added. 
`add_pf_last_modified()`             | str          | Filter Indicators on last modified date. 
`add_pf_rating()`                    | str          | Filter Indicators on Rating. 
`add_pf_tag()`                       | str          | Filter Indicators on Tag. 
`add_pf_threat_assess_confidence()`  | int          | Filter Indicators on Threat Assess Confidence. 
`add_pf_threat_assess_rating()`      | str          | Filter Indicators on Threat Assess Rating.
`add_pf_type()`                      | str         | Filter Indicators on Indicator type.

###Bulk Download Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python
tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

# indicator object
indicators = tc.bulk_indicators()
owner = 'Example Community'
 
# Add Post Filters
try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_pf_confidence(75, FilterOperator.GE)
    filter1.add_pf_rating('2.5', FilterOperator.GT)
except AttributeError as e:
    print(e)
    sys.exit(1)

# Retrieve Indicators and Apply Filters
try:
    indicators.retrieve()
except RuntimeError as e:
    print(e)
    sys.exit(1)

# Iterate Through Results
for indicator in indicators:
    if isinstance(indicator.indicator, dict):
        for indicator_type, indicator_value in indicator.indicator.items():
            print('{0}: {1}'.format(indicator_type, indicator_value))
    else:
        print(indicator.indicator)
    print(indicator.id)
    print(indicator.owner_name)
    print(indicator.date_added)
    print(indicator.last_modified)
    print(indicator.rating)
    print(indicator.threat_assess_rating)
    print(indicator.confidence)
    print(indicator.threat_assess_confidence)
    print(indicator.type)
    print(indicator.weblink)
    
```

This example will demonstrate how to retrieve Indicators while applying filters. In this example, three filters will be added, one for the Owner, one for the Confidence, and one for the Rating. The result set returned from this example will contain any Indicators in the **"Example Community"** Owner that has a Confidence greater than or equal to 75 and a Rating greater than 2.5.

Note: The `filter1` object contains a `filters` property which provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters, see the [Advanced Filter Tutorial](#filtering).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicators = tc.indicators()`            | Instantiate an Indicators container object. 
`filter1 = indicator.add_filter()`        | Add a filter object to the Indicators container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Indicators with the 'Example' tag. 
`indicator.retrieve()`                    | Trigger the API request and retrieve the Indicators <br> intelligence data. 
`for indicator in indicators:`            | Iterate over the Indicators container object generator. 
`print(indicator.indicator)`              | Display the **'indicator'** property of the Indicator object. 

###Loading Attributes Example

> Example of Python SDK iterating through a container of indicator objects:

```python
 
    for attribute in indicator.attributes:
        print(attribute.type)
        print(attribute.value)
        print(attribute.date_added)
        print(attribute.last_modified)
        print(attribute.displayed)
```

The example continues from the previous [Bulk Download Example](#bulk-download-example). Iterating through the **'indicators'** container provides `indicator` objects. The `load_attribute()` method does not need to be called for Bulk Indicator downloads, since the Attribute data is packaged with the Indicator data.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for attribute in indicator.attributes:`  | Iterate over the Attribute property object generator. 
`print(attribute.type)`                   | Display the **'type'** property of the Attribute object.

###Loading Security Label Example

> Example of Python SDK loading the Indicator Security Label:

```python
    indicator.load_security_label()
    if indicator.security_label is not None:
        print(indicator.security_label.name)
        print(indicator.security_label.description)
        print(indicator.security_label.date_added)
```

The example continues from the previous [Loading Attributes Example](#loading-attributes-example). While still in the indicator's loop, the Indicator Security Label can be loaded by calling the `load_security_label()` method of the Indicator object. By calling this method, another API request will be triggered, and the resulting data will be stored as a Security Label object in the Indicator object. This object can then be directly accessed from the `security_label` property.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`indicator.load_security_label()`         | Trigger API call to load the Security Label into the <br> Indicator object. 
`if indicator.security_label is not ...`  | Ensure the object has been loaded before <br> displaying properties. 
`print(indicator.security_label.name)`    | Display the **'name'** property of the <br> Security Label object. 

###Loading Tags Example

> Example of Python SDK:

```python
    for tag in indicator.tags:
        print(tag.name)
        print(tag.weblink)
```

The example continues from the previous [Loading Security Label Example](#loading-security-label-example). The `load_tags()` method of the Indicator object does not need to be called for Bulk Indicator downloads, since the Tag is packaged with the Indicator data. By calling this method, another API request will be triggered, and the resulting data will be stored as a Tag objects in the Indicator object. This object can then be directly accessed from the `tags` property.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for tag in indicator.tags:`              | Iterate over the Attribute property object generator. 
`print(tag.name)`                         | Display the **'name'** property of the Attribute object. 

##Group Associations

> Example of Python SDK pulling Groups from the API:

```python
    for g_association in indicator.group_associations:
        print(g_association.id)
        print(g_association.name)
        if hasattr(g_association, 'type'):
            print(g_association.type)
        print(g_association.owner_name)
        print(g_association.date_added)
        print(g_association.weblink)
```

Iterate through all Groups associated with this Indicator. These Groups are pulled directly from the API and are not stored in the Indicator object.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for g_associations in indicator.grou...` | Trigger API call to retrieve all Groups associated <br> with this Indicator. 
`print(g_association.id)`                 | Display the **'id'** property of the associated <br> Group object. 

###Indicator Associations

> Example Python SDK iterating through all Indicators associated with an Indicator:

```python
    for i_association in indicator.indicator_associations:
        print(i_association.id)
        print(i_association.indicator)
        print(i_association.type)
        print(i_association.description)
        print(i_association.owner_name)
        print(i_association.rating)
        print(i_association.confidence)
        print(i_association.date_added)
        print(i_association.last_modified)
        print(i_association.weblink)
```

Iterate through all Indicators associated with this Indicator. These Indicators are pulled directly from the API and are not stored in the Indicator object.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for i_association in indicator.ind_...` | Trigger API call to retrieve all Indicators associated <br>  with this Indicator. 
`print(i_association.id)`                 | Display the **'id'** property of the associated <br> Indicator object. 

###Victim Associations

> Python SDK example of iterating through all Victims associated with this Indicator:

```python
    for v_associations in indicator.victim_associations:
        print(v_associations.id)
        print(v_associations.name)
        print(v_associations.description)
        print(v_associations.owner_name)
        print(v_associations.nationality)
        print(v_associations.org)
        print(v_associations.suborg)
        print(v_associations.work_location)
        print(v_associations.weblink)
```

Iterate through all Victims associated with this Indicator. These Victims are pulled directly from the API and are not stored in the Indicator object.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for v_associations in indicator.vic_...` | Trigger API call to retrieve all Victims associated <br> with this Indicator. 
`print(v_association.id)`                 | Display the **'id'** property of the associated <br> Victim object.

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Documents Retrieve

This document explains how to work with ThreatConnect Document Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------  
`add_id()`             | int          | Filter Document by ID.
`add_document_id()`    | int          | Filter Document on associated Document ID.
`add_email_id()`       | int          | Filter Document on associated Email ID.
`add_incident_id()`    | int          | Filter Document on associated Incident ID.
`add_indicator()`      | str          | Filter Document on associated Indicator.
`add_owner()`          | list or str  | Filter Document on associated Owner.
`add_security_label()` | str          | Filter Document on associated Security Label.
`add_signature_id()`   | int          | Filter Document on associated Signature ID.
`add_tag()`            | str          | Filter Document on applied Tag.
`add_threat_id()`      | int          | Filter Document on associated Threat ID.
`add_victim_id()`      | int          | Filter Document on associated Victim ID.

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_pf_name()`        | str          | Filter Document on name.
`add_pf_date_added()`  | str          | Filter Document on date added.

###Documents Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

documents = tc.documents()
owner = 'Example Community'

try:
    filter1 = documents.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    documents.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

for document in documents:
    print(document.id)
    print(document.name)
    print(document.date_added)
    print(document.owner_name)
    print(document.weblink)
    
    # document specific property
    print(document.file_name)
```

This example will demonstrate how to retrieve documents while applying filters. In this example, two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any documents in the **Example Community** Owner that has a Tag of **EXAMPLE**.

Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters see the [Advanced Filter Tutorial](/python/advanced/filtering/).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`documents = tc.documents()`              | Instantiate a Documents container object. 
`filter1 = documents.add_filter()`        | Add a filter object to the Documents container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Documents with the 'Example' tag 
`documents.retrieve()`                    | Trigger the API request and retrieve the Documents <br> intelligence data. 
`for document in documents:`              | Iterate over the Documents container object generator. 
`print(document.id)`                      | Display the **'id'** property of the Document object. 

###Download Document Contents Example

> Python SDK example of downloading the contents of the document stored with the Document Resource:

```python
    document.download()
    if document.contents is not None:
        print(document.contents)
```

Continuing from the [Filter Example](#filter-example), the example will download the contents of the document stored with the Document Resource.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`document.download()`                     | Trigger API request to download the Document contents. 
`if document.contents is not None:`       | Validate the Document has downloaded before displaying. 
`print(document.contents)`                | Display the contents of the Document. <br> (This should only be done for ASCII contents.)

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Emails Retrieve

This section explains how to work with ThreatConnect Email Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_id()`             | int          | Filter Email by ID.
`add_document_id()`    | int          | Filter Email on associated Document ID.
`add_email_id()`       | int          | Filter Email on associated Email ID.
`add_incident_id()`    | int          | Filter Email on associated Incident ID.
`add_indicator()`      | str          | Filter Email on associated Indicator.
`add_owner()`          | list or str  | Filter Email on associated Owner.
`add_security_label()` | str          | Filter Email on associated Security Label.
`add_signature_id()`   | int          | Filter Email on associated Signature ID.
`add_tag()`            | str          | Filter Email on applied Tag.
`add_threat_id()`      | int          | Filter Email on associated Threat ID.
`add_victim_id()`      | int          | Filter Email on associated Victim ID.

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------
`add_pf_name()`        | str          | Filter Email on name. 
`add_pf_date_added()`  | str          | Filter Email on date added. 

###Emails Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

emails = tc.emails()
owner = 'Example Community'

try:
    filter1 = emails.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    emails.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

for email in emails:
    print(email.id)
    print(email.name)
    print(email.date_added)
    print(email.weblink)
    
    # email specific properties
    print(email.header)
    print(email.subject)
    print(email.from_address)
    print(email.to)
    print(email.body)
    print(email.score)
```

This example will demonstrate how to retrieve emails while applying filters. In this example, two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any emails in the **Example Community** Owner that has a Tag of ***EXAMPLE***.

> To retrieve the headers and body for a single email, include a filter for its ID. (Make an individual query for each email.)

`filter1.add_id($email_id)`

Note: The `filter1` object contains a `filters` property which provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters, see the [Advanced Filter Tutorial](#filtering).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`emails = tc.emails()`                    | Instantiate an Emails container object. 
`filter1 = emails.add_filter()`           | Add a Filter object to the Emails container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API Filter to be applied to the API request. 
`emails.retrieve()`                       | Trigger the API request and retrieve the Emails <br> intelligence data. 
`for email in emails:`                    | Iterate over the Emails container object generator. 
`print(email.id)`                         | Display the **'id'** property of the Email object. 

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Groups Retrieve

This section explains how to work with the ThreatConnect Group Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------  
`add_document_id()`    | int          | Filter Group on associated Document ID.
`add_email_id()`       | int          | Filter Group on associated Email ID.
`add_incident_id()`    | int          | Filter Group on associated Incident ID.
`add_indicator()`      | str          | Filter Group on associated Indicator. 
`add_owner()`          | list or str  | Filter Group on associated Owner. 
`add_security_label()` | str          | Filter Group on associated Security Label. 
`add_signature_id()`   | int          | Filter Group on associated Signature ID. 
`add_tag()`            | str          | Filter Group on applied Tag. 
`add_threat_id()`      | int          | Filter Group on associated Threat ID. 
`add_victim_id()`      | int          | Filter Group on associated Victim ID. 

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_pf_name()`        | str          | Filter Group on name.
`add_pf_date_added()`  | str          | Filter Group on date added.

###Groups Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

groups = tc.groups()
owner = 'Example Community'

try:
    filter1 = groups.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    groups.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

for group in groups:
    print(group.id)
    print(group.name)
    print(group.date_added)
    print(group.weblink)
    
    # group specific property
    print(group.type)
```

This example will demonstrate how to retrieve Groups while applying filters. In this example two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any Groups in the **Example Community** Owner that has a Tag of ***EXAMPLE***.

Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters see the [Advanced Filter Tutorial](#filtering).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`groups = tc.groups()`                    | Instantiate a Groups container object. 
`filter1 = groups.add_filter()`           | Add a filter object to the Groups container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Groups with the 'Example' tag. 
`groups.retrieve()`                       | Trigger the API request and retrieve the Groups <br> intelligence data. 
`for group in groups:`                    | Iterate over the Groups container object generator. 
`print(group.id)`                         | Display the **'id'** property of the Group object. 

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Incidents Retrieve

This section explains how to work with ThreatConnect Incident Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_id()`             | int          | Filter Incident by ID. 
`add_document_id()`    | int          | Filter Incident on associated Document ID. 
`add_email_id()`       | int          | Filter Incident on associated Email ID. 
`add_incident_id()`    | int          | Filter Incident on associated Incident ID. 
`add_indicator()`      | str          | Filter Incident on associated Indicator. 
`add_owner()`          | list or str  | Filter Incident on associated Owner. 
`add_security_label()` | str          | Filter Incident on associated Security Label. 
`add_signature_id()`   | int          | Filter Incident on associated Signature ID. 
`add_tag()`            | str          | Filter Incident on applied Tag. 
`add_threat_id()`      | int          | Filter Incident on associated Threat ID. 
`add_victim_id()`      | int          | Filter Incident on associated Victim ID. 

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_pf_name()`        | str          | Filter Incident on name. 
`add_pf_date_added()`  | str          | Filter Incident on date added. 

###Incidents Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python
tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

incidents = tc.incidents()
owner = 'Example Community'

try:
    filter1 = incidents.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    incidents.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

for incident in incidents:
    print(incident.id)
    print(incident.name)
    print(incident.date_added)
    print(incident.weblink)
    print(incident.event_date)
        
```

This example will demonstrate how to retrieve Incidents while applying filters. In this example, two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any Incidents in the **Example Community** Owner that has a Tag of ***EXAMPLE***.

Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters see the [Advanced Filter Tutorial](/python/advanced/filtering/).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`incidents = tc.incidents()`              | Instantiate an Incidents container object. 
`filter1 = incidents.add_filter()`        | Add a filter object to the Incidents container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Incidents with the 'Example' tag. 
`incidents.retrieve()`                    | Trigger the API request and retrieve the Incidents <br> intelligence data. 
`for incident in incidents:`              | Iterate over the Incidents container object generator. 
`print(incident.id)`                      | Display the **'id'** property of the Incidents object. 

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Indicators Retrieve

This section explains how to work with ThreatConnect Indicator Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------  
`add_adversary_id()`   | int          | Filter Indicator on associated Adversary ID. 
`add_document_id()`   | int          | Filter Indicator on associated Document ID. 
`add_email_id()`       | int          | Filter Indicator on associated Email ID. 
`add_incident_id()`    | int          | Filter Indicator on associated Incident ID. 
`add_indicator()`      | str          | Filter Indicator by Indicator value. 
`add_owner()`          | list or str  | Filter Indicator on associated Owner. 
`add_security_label()` | str          | Filter Indicator on associated Security Label. 
`add_signature_id()`   | int          | Filter Indicator on associated Signature ID. 
`add_tag()`            | str          | Filter Indicator on applied Tag. 
`add_threat_id()`      | int          | Filter Indicator on associated Threat ID. 
`add_victim_id()`      | int          | Filter Indicator on associated Victim ID. 

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter                             | Value Type   | Description                                                  
---------------------------------- | ------------ | ------------------------------------------------------------ 
`add_pf_attribute()`                 | str          | Filter Indicators on Attribute type. 
`add_pf_confidence()`                | int          | Filter Indicators on Confidence value. 
`add_pf_date_added()`                | str          | Filter Indicators on date added. 
`add_pf_last_modified()`             | str          | Filter Indicators on last modified date. 
`add_pf_rating()`                    | str          | Filter Indicators on Rating. 
`add_pf_tag()`                       | str          | Filter Indicators on Tag. 
`add_pf_threat_assess_confidence()`  | int          | Filter Indicators on Threat Assess Confidence. 
`add_pf_threat_assess_rating()`      | str          | Filter Indicators on Threat Assess Rating. 
`add_pf_type()`                      | str          | Filter Indicators on Indicator type. 

###Indicators Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python
tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

# indicator object
indicators = tc.indicators()
owner = 'Example Community'
 
# Add API/Post Filters
try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)

# Retrieve Indicators and Apply Filters
try:
    indicators.retrieve()
except RuntimeError as e:
    print(e)
    sys.exit(1)

# Iterate Through Results
for indicator in indicators:
    if isinstance(indicator.indicator, dict):
        for indicator_type, indicator_value in indicator.indicator.items():
            print('{0}: {1}'.format(indicator_type, indicator_value))
    else:
        print(indicator.indicator)
    print(indicator.id)
    print(indicator.owner_name)
    print(indicator.date_added)
    print(indicator.last_modified)
    print(indicator.rating)
    print(indicator.confidence)
    print(indicator.threat_assess_rating)
    print(indicator.threat_assess_confidence)
    print(indicator.source)
    print(indicator.description)
    print(indicator.dns_active)
    print(indicator.weblink)

```

This example will demonstrate how to retrieve Indicators while applying filters. In this example, two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any Indicators in the **Example Community** Owner that has a Tag of ***EXAMPLE***.

Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters see the [Advanced Filter Tutorial](#filtering).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicators = tc.indicators()`            | Instantiate an Indicators container object. 
`filter1 = indicator.add_filter()`        | Add a filter object to the Indicators container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Indicators with the 'Example' tag. 
`indicator.retrieve()`                    | Trigger the API request and retrieve the Indicators <br> intelligence data. 
`for indicator in indicators:`            | Iterate over the Indicators container object generator. 
`print(indicator.indicator)`              | Display the **'indicator'** property of the Indicator object. 

###Loading Attributes Example

> Example Python SDK iterating through the `indicators` container provides `indicator` objects

```python
 
    indicator.load_attributes()
    for attribute in indicator.attributes:
        print(attribute.type)
        print(attribute.value)
        print(attribute.date_added)
        print(attribute.last_modified)
        print(attribute.displayed)
```

The example continues from the previous [Filter Example](#filter-example). Iterating through the `indicators` container provides `indicator` objects. By calling the `load_attribute()` method of the Indicator object, an API request is triggered and the resulting data is stored as Attribute objects in the parent Indicator object. These Attribute objects can be retrieved by iterating over the `attributes` property generator, which will return the individual Attribute objects.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`indicator.load_attributes()`             | Trigger API call to load Attributes into the <br> Indicator object. 
`for attribute in indicator.attributes:`  | Iterate over the Attribute property object generator. 
`print(attribute.type)`                   | Display the **'type'** property of the Attribute object. 

###Loading Security Label Example

> Example Python SDK loading the Indicator Security Label by calling the `load_security_label()` method of the Indicator object:

```python

    indicator.load_security_label()
    if indicator.security_label is not None:
        print(indicator.security_label.name)
        print(indicator.security_label.description)
        print(indicator.security_label.date_added)
```

The example continues from the previous [Loading Attributes Example](#loading-attributes-example). While still in the `indicators` loop, the Indicator Security Label can be loaded by calling the `load_security_label()` method of the Indicator object. By calling this method, another API request will be triggered and the resulting data will be stored as a Security Label object in the Indicator object. This object can then be directly accessed from the `security_label` property.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`indicator.load_security_label()`         | Trigger API call to load the Security Label into the <br> Indicator object. 
`if indicator.security_label is not ...`  | Ensure the object has been loaded before displaying properties. 
`print(indicator.security_label.name)`    | Display the **'name'** property of the Security Label object. 

###Loading Tags Example

> Example of Python SDK loading the Indicator Tags by calling the `load_tags()` method of the Indicator object:

```python
    indicator.load_tags()
    for tag in indicator.tags:
        print(tag.name)
        print(tag.weblink)
```

The example continues from the previous [Loading Security Label Example](#loading-security-label-example). While still in the `indicators` loop, the Indicator Tags can be loaded by calling the `load_tags()` method of the Indicator object. By calling this method, another API request will be triggered and the resulting data will be stored as a Tag object in the Indicator object. This object can then be directly accessed from the `tags` property.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`indicator.load_tags()`                   | Trigger API call to load Tags into the Indicator object. 
`for tag in indicator.tags:`              | Iterate over the Attribute property object generator. 
`print(tag.name)`                         | Display the **'name'** property of the Attribute object. 

###Group Associations

> Example of Python SDK iterating through all Groups associated with this Indicator:

```python
    for g_association in indicator.group_associations:
        print(g_association.id)
        print(g_association.name)
        if hasattr(g_association, 'type'):
            print(g_association.type)
        print(g_association.owner_name)
        print(g_association.date_added)
        print(g_association.weblink)
```

Iterate through all Groups associated with this Indicator. These Groups are pulled directly from the API and are not stored in the Indicator object.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for g_associations in indicator.grou...` | Trigger API call to retrieve all Groups associated with <br> this Indicator. 
`print(g_association.id)`                 | Display the **'id'** property of the associated Group object. 

###Indicator Associations

> Example Python SDK iterating through all Indicators associated with an Indicator:

```python
    for i_association in indicator.indicator_associations:
        print(i_association.id)
        print(i_association.indicator)
        print(i_association.type)
        print(i_association.description)
        print(i_association.owner_name)
        print(i_association.rating)
        print(i_association.confidence)
        print(i_association.date_added)
        print(i_association.last_modified)
        print(i_association.weblink)
```

Iterate through all Indicators associated with this Indicator. These Indicators are pulled directly from the API and are not stored in the Indicator object.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for i_association in indicator.ind_...` | Trigger API call to retrieve all Indicators associated with <br> this Indicator. 
`print(i_association.id)`                 | Display the **'id'** property of the associated Indicator object. 

###Victim Associations

> Example Python SDK iterating through all Victims associated with this Indicator:

```python

    for v_associations in indicator.victim_associations:
        print(v_associations.id)
        print(v_associations.name)
        print(v_associations.description)
        print(v_associations.owner_name)
        print(v_associations.nationality)
        print(v_associations.org)
        print(v_associations.suborg)
        print(v_associations.work_location)
        print(v_associations.weblink)
```

Iterate through all Victims associated with this Indicator. These Groups are pulled directly from the API and are not stored in the Indicator object.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`for v_associations in indicator.vic_...` | Trigger API call to retrieve all Victims associated with <br> this Indicator. 
`print(v_association.id)`                 | Display the **'id'** property of the associated Victim object. 

### DNS Resolution

> Example Python SDK DNS Resolution:

```python

indicator.load_dns_resolutions()
for dns in indicator.dns_resolutions:
    print(dns.ip)
    print(dns.owner_name)
    print(dns.resolution_date)
    print(dns.weblink)
```

DNS Resolution is only supported for the Host Indicator Type.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`indicator.load_dns_resolutions()`        | Trigger API call to load DNS Resolutions into the Indicator object. 
`for dns in indicator.dns_resolutions:`   | Iterate over the DNS Resolutions property object generator.
`print(dns.ip)`                           | Display the **'ip'** property of the Attribute object.

<b>Output Formats</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Signatures Retrieve

This section explains how to work with ThreatConnect Signature Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------  
`add_id()`             | int          | Filter Signature by ID.
`add_document_id()`    | int          | Filter Signature on associated Document ID.
`add_email_id()`       | int          | Filter Signature on associated Email ID.
`add_incident_id()`    | int          | Filter Signature on associated Incident ID.
`add_indicator()`      | str          | Filter Signature on associated Indicator.
`add_owner()`          | list or str  | Filter Signature on associated Owner.
`add_security_label()` | str          | Filter Signature on associated Security Label.
`add_signature_id()`   | int          | Filter Signature on associated Signature ID.
`add_tag()`            | str          | Filter Signature on applied Tag.
`add_threat_id()`      | int          | Filter Signature on associated Threat ID.
`add_victim_id()`      | int          | Filter Signature on associated Victim ID.

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_pf_name()`        | str          | Filter Signature on name.
`add_pf_date_added()`  | str          | Filter Signature on date added.

###Signatures Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

signatures = tc.signatures()
owner = 'Example Community'

try:
    filter1 = signatures.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    signatures.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

for signature in signatures:
    print(signature.id)
    print(signature.name)
    print(signature.date_added)
    print(signature.weblink)
```

This example will demonstrate how to retrieve Signatures while applying filters. In this example, two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any Signatures in the **Example Community** Owner that has a Tag of ***EXAMPLE***.

Note: The `filter1` object contains a `filters` property which provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters, see the [Advanced Filter Tutorial](#filtering).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`signatures = tc.signatures()`            | Instantiate an Signatures container object. 
`filter1 = signatures.add_filter()`       | Add a filter object to the Signatures container object <br> (support multiple filter objects).
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Signatures with the 'Example' tag.
`signatures.retrieve()`                   | Trigger the API request and retrieve the Signatures <br> intelligence data.
`for signature in signatures:`            | Iterate over the Signatures container object generator.
`print(signature.id)`                     | Display the **'id'** property of the Signature object.

###Signature Download

> Example Python SDK downloading the Signature contents for the Signature Resource:

```python

    signature.download()
    if signature.contents is not None:
        print(signature.contents)
```

Download the Signature contents for the Signature Resource.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`signature.download()`                    | Trigger API request to download the Signature contents. 
`if signature.contents is not None:`      | Validate that the Signature has downloaded before displaying. 
`print(signature.contents)`               | Display the contents of the Signature.

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

## Tasks Retrieve
This section explains how to work with ThreatConnect Task Resources.

## Supported API Filters
API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  |
---------------------| ------------ | ------------------------------------------------------------ |  
add_id()             | int          | Filter Task by ID. |
add_document_id()    | int          | Filter Task on associated Document ID. |
add_email_id()       | int          | Filter Task on associated Email ID. |
add_incident_id()    | int          | Filter Task on associated Incident ID. |
add_indicator()      | int          | Filter Task on associated Indicator. |
add_owner()          | list or str  | Filter Task on associated Owner. |
add_security_label() | str          | Filter Task on associated Security Label. |
add_signature_id()   | int          | Filter Task on associated Signature ID. |
add_tag()            | str          | Filter Task on applied Tag. |
add_threat_id()      | int          | Filter Task on associated Task ID. |
add_victim_id()      | int          | Filter Task on associated Victim ID. |

## Supported Post Filters
Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  |
---------------------| ------------ | ------------------------------------------------------------ |
add_pf_name()        | str          | Filter Task on name. |
add_pf_date_added()  | str          | Filter Task on date added. |

## Filter Example

This example will demonstrate how to retrieve Tasks while applying filters. In this example, one filters will be added for a Tag. The result set returned from this example will contain any Tasks that has a Tag of ***EXAMPLE***.

> The import statement and reading of the configuration files have been replaced with `...` for brevity.
<br/>

```python
...

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

tasks = tc.tasks()

try:
    filter1 = tasks.add_filter()
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    tasks.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

for task in tasks:
    print(task.id)
    print(task.name)
    print(task.date_added)
    print(task.weblink)
```

> Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more information on using filters, see the [Advanced Filter Tutorial](/python/advanced/filtering/).

* Code Highlights*

Snippet                                   | Description                                                                       |
----------------------------------------- | --------------------------------------------------------------------------------- |
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. |
`Tasks = tc.Tasks()`                      | Instantiate a Tasks container object. |
`filter1 = Tasks.add_filter()`            | Add a filter object to the Tasks container object (support multiple filter objects). |
`filter1.add_tag('EXAMPLE')`              | Add an API filter to be applied to the API request. |
`Tasks.retrieve()`                        | Trigger the API request and retrieve the Tasks-intelligence data. |
`for task in Tasks:`                      | Iterate over the Tasks container object generator. |
`print(task.id)`                          | Display the **id** property of the Task object. |

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Threats Retrieve

This section explains how to work with ThreatConnect Threat Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_id()`             | int          | Filter Threat by ID.
`add_document_id()`    | int          | Filter Threat on associated Document ID.
`add_email_id()`       | int          | Filter Threat on associated Email ID.
`add_incident_id()`    | int          | Filter Threat on associated Incident ID.
`add_indicator()`      | str          | Filter Threat on associated Indicator.
`add_owner()`          | list or str  | Filter Threat on associated Owner.
`add_security_label()` | str          | Filter Threat on associated Security Label.
`add_signature_id()`   | int          | Filter Threat on associated Signature ID.
`add_tag()`            | str          | Filter Threat on applied Tag.
`add_threat_id()`      | int          | Filter Threat on associated Threat ID.
`add_victim_id()`      | int          | Filter Threat on associated Victim ID.

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_pf_name()`        | str          | Filter Threat on name. 
`add_pf_date_added()`  | str          | Filter Threat on date added. 

###Threats Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

threats = tc.threats()
owner = 'Example Community'

try:
    filter1 = threats.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    threats.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

for threat in threats:
    print(threat.id)
    print(threat.name)
    print(threat.date_added)
    print(threat.weblink)
```

This example will demonstrate how to retrieve Threats while applying filters. In this example, two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any Threats in the **Example Community** Owner that has a Tag of ***EXAMPLE***.

Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters, see the [Advanced Filter Tutorial](/python/advanced/filtering/).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`threats = tc.threats()`                  | Instantiate a Threats container object. 
`filter1 = threats.add_filter()`          | Add a filter object to the Threats container object <br> (support multiple filter objects). 
`filter1.add_tag('EXAMPLE')`              | Add API filter to retrieve Threats with the 'Example' tag. 
`threats.retrieve()`                      | Trigger the API request and retrieve the Threats <br> intelligence data. 
`for threat in threats:`                  | Iterate over the Threats container object generator. 
`print(threat.id)`                        | Display the **id** property of the Threat object. 

##Victims Retrieve

This section explains how to work with ThreatConnect Victims Resources.

<b>Supported API Filters</b>

API filters use the API filtering feature to limit the result set returned from the API.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_id()`             | int          | Filter Victim by ID. 
`add_adversary_id()`   | int          | Filter Victim on associated Adversary ID. 
`add_document_id()`    | int          | Filter Victim on associated Document ID. 
`add_email_id()`       | int          | Filter Victim on associated Email ID. 
`add_incident_id()`    | int          | Filter Victim on associated Incident ID. 
`add_indicator()`      | str          | Filter Victim on associated Indicator. 
`add_owner()`          | list or str  | Filter Victim on associated Owner. 
`add_signature_id()`   | int          | Filter Victim on associated Signature ID. 
`add_threat_id()`      | int          | Filter Victim on associated Threat ID. 

<b>Supported Post Filters</b>

Post filters are applied on the results returned by the API request.

Filter               | Value Type   | Description                                                  
---------------------| ------------ | ------------------------------------------------------------ 
`add_pf_name()`        | str          | Filter Victim on name.
`add_pf_date_added()`  | str          | Filter Victim on date added. 

###Victims Retrieve Filter Example

> The import statement and reading of the configuration files have been replaced with `...` for brevity.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

victims = tc.victims()
owner = 'Example Community'

try:
    filter1 = victims.add_filter()
    filter1.add_owner(owner)
    filter1.add_adversary_id(531)
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

try:
    victims.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
    
for victim in victims:
    print(obj.id)
    print(obj.name)
    print(obj.nationality)
    print(obj.org)
    print(obj.suborg)
    print(obj.work_location)
    print(obj.weblink)
```

This example will demonstrate how to retrieve Victims while applying filters. In this example two filters will be added, one for the Owner and another for an Adversary ID. The result set returned from this example would contain any Victim in the "Example Community" Owner that has associations with the Adversary having the supplied ID.

Note: The `filter1` object contains a `filters` property that provides a list of supported filters for the resource type being retrieved. To display this list, `print(filter1.filters)` can be used. For more on using filters, see the [Advanced Filter Tutorial](#filtering).

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`victims = tc.victims()`                  | Instantiate a Victims container object. 
`filter1 = victims.add_filter()`          | Add a filter object to the Victims container object <br> (support multiple filter objects). 
`filter1.add_adversary_id(531)`           | Add API filter to retrieve Victims associated with the given Adversary. 
`victims.retrieve()`                      | Trigger the API request and retrieve the Victims <br> intelligence data. 
`for victim in victims:`                  | Iterate over the Victims container object generator. 
`print(victim.id)`                        | Display the **id** property of the Victim object. 

###Load Victim Assets

> This Python SDK example will pull all Assets for the current Victim Resource:

```python
    victim.load_assets()
    for asset in victim.assets:
        print(asset.id)
        print(asset.name)
        print(asset.type)
        print(asset.weblink)
```

Continuing from the [Filter Example](#filter-example), the following example will pull all Assets for the current Victim Resource.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`victim.load_assets()`                    | Trigger API call to load Assets into the Resource object. 
`for asset in victim.assets:`             | Iterate over the Assets object generator. 
`print(asset.id)`                         | Display the **id** property of the Asset object. 

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

##Associations

> Python SDK example demonstrating how to use the `Group_Associations` method on an Adversary Resource:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()

try:
    resources.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for resource in resources:
    print(resource.id)
    print(resource.name)
    print(resource.date_added)
    print(resource.weblink)

    for g_associations in resource.group_associations:
        print(g_associations.id)
        print(g_associations.name)
        print(g_associations.type)
        print(g_associations.owner_name)
        print(g_associations.date_added)
        print(g_associations.weblink)
```

<b>Group Associations</b>

The Python SDK provides the `group_associations` method to retrieve Group Associations for a Resource. Group Associations are supported on Indicators as well as [Group](#groups-commit) Resources (e.g., [Adversaries](#resources-commit), [Documents](#documents-commit), [Emails](#emails-commit), [Incidents](#incidents-commit), [Signatures](#signatures-commit), and [Threats](#threats-commit)) and [Indicators](#indicators-commit). An example of the [Retrieving Group Associations](#associations) method, as well as an explanation of the code, is provided in the following section.

Resource Groups of the same type cannot be directly associated (e.g., Adversaries cannot be associated with other Adversaries).

<b>Retrieving Group Associations</b>

The following example demonstrates how to use the `Group_Associations` method on an Adversary Resource. For other Resource Groups and Indicators, the same method should be used. These Associations are pulled directly from the API and are not stored in the Resource object.

<b>Group Associations Properties</b>

Property Name            | Type
------------------------ | ----
id                       | int
name                     | str
type                     | str
owner_name               | str
date_added               | str
weblink                  | str

For more information on the properties of an Attribute, read the ThreatConnect API documentation.

When the `Group_Associations` method is called, an API request is invoked immediately.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate an Resources container object. 
`resources.retrieve()`                    | Trigger API calls to retrieve the Resources. 
`for resource in resources:`              | Iterate over the Resources container object generator. 
`print(resource.id)`                      | Display the **id** property of the Resource object. 
`for g_associations in resource.group_...`| Trigger an API call to retrieve all Groups associated <br> with this Resource. 
`print(g_association.id)`                 | Display the **id** property of the associated Group object. 

##Indicator Associations

> Python SDK example demonstrating how to use the `indicator_associations` method on an Adversary Resource:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()

try:
    resources.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for resource in resources:
    print(resource.id)
    print(resource.name)
    print(resource.date_added)
    print(resource.weblink)

    for associations in resource.indicator_associations:
        print(associations.id)
        print(associations.indicator)
        print(associations.type)
        print(associations.description)
        print(associations.owner_name)
        print(associations.rating)
        print(associations.confidence)
        print(associations.date_added)
        print(associations.last_modified)
        print(associations.weblink)
```

The Python SDK provides the `indicator_associations` method to retrieve Indicators Associations for a resource. Indicator Associations are supported on Indicators as well as [Group](#groups-commit) Resources (e.g., [Adversaries](#resources-commit), [Documents](#documents-commit), [Emails](#emails-commit), [Incidents](#incidents-commit), [Signatures](#signatures-commit), and [Threats](#threats-commit)) and [Indicators](#indicators-commit). An example of the [Retrieving Indicator Associations](#retrieving-indicator-associations) method, as well as explanations of the code, is provided in the following section.

<b>Retrieving Indicator Associations</b>

The following example demonstrates how to use the `indicator_associations` method on an Adversary Resource. For other Resource Groups and Indicators, the same method should be used. These Associations are pulled directly from the API and are not stored in the Resource object.

<b>Indicator Associations Properties</b>

Property Name            | Type
------------------------ | ----
id                       | int
indicator                | str
type                     | str
description              | str
owner_name               | str
rating                   | str
confidence               | str
date_added               | str
last_modified            | str
weblink                  | str

For more information on the properties of an Attribute, read the ThreatConnect API documentation.

When the `indicator_associations` method is called, an API request is invoked immediately.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate an Resources container object. 
`resources.retrieve()`                    | Trigger API calls to retrieve the Resources. 
`for resource in resources:`              | Iterate over the Resources container object generator. 
`print(resource.id)`                      | Display the **id** property of the Resource object. 
`for associations in resource.indicat_...`| Trigger API call to retrieve all Indicators associated <br> with this Resource. 
`print(association.id)`                   | Display the **'id'** property of the associated <br> Indicator object. 

##Victim Associations Retrieve

> Python SDK example demonstrating how to use the `victim_associations` method on an Adversary Resource:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()

try:
    resources.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for resource in resources:
    print(resource.id)
    print(resource.name)
    print(resource.date_added)
    print(resource.weblink)

    for associations in resource.victim_associations:
        print(associations.id)
        print(associations.name)
        print(associations.description)
        print(associations.owner_name)
        print(associations.nationality)
        print(associations.org)
        print(associations.suborg)
        print(associations.work_location)
        print(associations.weblink)
```

The Python SDK provides the `victim_associations` method to retrieve Victim Associations for a resource. Victim Associations are supported on all [Group](#groups_commit) Resources (e.g., [Adversaries](#resources-commit), [Documents](#documents-commit), [Emails](#emails-commit), [Incidents](#incidents-commit), [Signatures](#signatures-commit), and [Threats](#threats-commit)) and [Indicators](#indicators-commit). An example of the [Retrieving Victim Associations](#victim-associations-retrieve) method, as well as explanations of the code, is provided in the following section.

The following example demonstrates how to use the `victim_associations` method on an Adversary Resource. For other Resource Groups and Indicators, the same method should be used. These associations are pulled directly from the API and are not stored in the Resource object.

<b>Victim Associations Properties</b>

Property Name            | Type
------------------------ | ----
id                       | int
name                     | str
date_added               | str
weblink                  | str

For more information on the properties of an Attribute, read the ThreatConnect API documentation.

When the `victim_associations` method is called, an API request is invoked immediately.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | ---------------------------------------------------------------------------------
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate an Resources container object. 
`resources.retrieve()`                    | Trigger API calls to retrieve the Resources. 
`for resource in resources:`              | Iterate over the Resources container object generator. 
`print(resource.id)`                      | Display the **id** property of the Resource object. 
`for associations in resource.victim_...` | Trigger API call to retrieve all Victims associated <br> with this Resource. 
`print(v_association.id)`                 | Display the **id** property of the associated <br> Victim object. 

##Loading Attributes

> Python SDK example on how to Load Attributes on an Adversary Resource:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()

try:
    resources.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for resource in resources:
    print(resource.id)
    print(resource.name)
    print(resource.date_added)
    print(resource.weblink)

    resource.load_attributes()
    for attribute in resource.attributes:
        print(attribute.type)
        print(attribute.value)
        print(attribute.date_added)
        print(attribute.last_modified)
        print(attribute.displayed)
```

The Python SDK provides the `load_attributes()` method to load a Resources Attribute. Attributes are supported on all [Group](#groups-commit) Resources (e.g., [Adversaries](#resources-commit), [Documents](#documents-commit), [Emails](#emails-commit), [Incidents](#incidents-commit), [Signatures](#signatures-commit), and [Threats](#threats-commit)) and [Indicators](#indicators-commit).   

The following example demonstrates how to [Load Attributes](#loading-attributes) on an Adversary Resource. For other Resource Groups and Indicators, the same method should be used.

<b>Attribute Properties</b>

Property Name            | Type
------------------------ | ----
type                     | str
value                    | str
date_added               | str
last_modified            | str
displayed                | bool

For more information on the properties of an Attribute read, the ThreatConnect API documentation.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resources.retrieve()`                    | Trigger the API request and retrieve the Resources <br> intelligence data. 
`for resource in resources:`              | Iterate over the Resources container object generator. 
`print(resource.id)`                      | Display the **id** property of the Resource object. 
`resource.load_attributes()`              | Trigger API call to load Attributes into the Resource object. 
`for attribute in resource.attributes:`   | Iterate over the Attribute property object generator. 
`print(attribute.type)`                   | Display the **'type'** property of the Attribute object. 

##Loading a Security Label

> Python SDK example demonstrating how to **Load a Security Label** on an Adversary Resource:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()

try:
    resources.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for resource in resources:
    print(resource.id)
    print(resource.name)
    print(resource.date_added)
    print(resource.weblink)

    resource.load_security_label()
    if resource.security_label is not None:
        print(resource.security_label.name)
        print(resource.security_label.description)
        print(resource.security_label.date_added)
```

The Python SDK provides the `load_security_label()` method to load the Security Label for a resource. Attributes are supported on all [Group](#groups-commit) Resources (e.g., [Adversaries](#resources-commit), [Documents](#documents-commit), [Emails](#emails-commit), [Incidents](#incidents-commit), [Signatures](#signatures-commit), and [Threats](#threats-commit)) and [Indicators](#indicators-commit). An example of the [Loading Security Label](#loading-security-label) method, as well as explanations of the code, is provided in the following section.

The following example demonstrates how to **Load a Security Label** on an Adversary Resource. For other Resource Groups and Indicator,s the same method should be used.

<b>Attribute Properties</b>

Property Name            | Type
------------------------ | ----
name                     | str
description              | str
date_added               | str

For more information on the properties of a Security Label, read the ThreatConnect API documentation.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate an Resources container object. 
`resources.retrieve()`                    | Trigger the API request and retrieve the Resources <br> intelligence data. 
`for resource in resources:`              | Iterate over the Resources container object generator. 
`print(resource.id)`                      | Display the **id** property of the Resource object. 
`resource.load_security_label()`          | Trigger API call to load the Security Label into the <br> Resource object. 
`if resource.security_label is not None:` | Ensure the object has been loaded before displaying <br> properties. 
`print(resource.security_label.name)`     | Display the **'name'** property of the Security Label object. 

##Loading Tags

> Python SDK example demonstrating how to use the `load_tags()` method on an Adversary Resource:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()

try:
    resources.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

for resource in resources:
    print(resource.id)
    print(resource.name)
    print(resource.date_added)
    print(resource.weblink)

    resource.load_tags()
    for tag in resource.tags:
        print(tag.name)
        print(tag.weblink)
```

The Python SDK provides the `load_tags()` method to load a Resources Tag. Tags are supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats). An example of the [Loading Tags](#loading-tags) method,  as well as explanations of the code, is provided in the following section.

The following example demonstrates how to use the `load_tags()` method on an Adversary Resource. For other Resource Groups and Indicators, the same method should be used.

<b>Tag Properties</b>

Property Name            | Type
------------------------ | ----
name                     | str
weblink                  | str

For more information on the properties of an Attribute, read the ThreatConnect API documentation.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate an Resources container object. 
`resources.retrieve()`                    | Trigger API calls to retrieve the Resources. 
`for resource in resources:`              | Iterate over the Resources container object generator. 
`print(resource.id)`                      | Display the **id** property of the Resource object. 
`resource.load_tags()`                    | Trigger API call to load Tags into the Resource object. 
`for tag in resource.tags:`               | Iterate over the Tag property object generator. 
`print(tag.name)`                         | Display the **'name'** property of the Tag object. 

##Python Commit

> Example Python SDK creating an adversary resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

adversaries = tc.adversaries()
    
owner = 'Example Community'
adversary = adversaries.add('New Adversary', owner)
adversary.add_attribute('Description', 'Description Example')
adversary.add_tag('EXAMPLE')
adversary.set_security_label('TLP Green')
try:
    adversary.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

<b>Adversaries Commit</b>

The ThreatConnect platform supports [adding](#add-an-adversary-resource), [deleting](#delete-an-adversary-resource), and [updating](#update-an-adversary-resource) of threat-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Adding Adversary Resources</b>

The example demonstrates how to create an Adversary Resource in the ThreatConnect platform. For more information on the purpose of each line of code see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`adversaries = tc.adversaries()`          | Instantiate an Adversaries container object. 
`adversary = adversaries.add('New Adve...`| Add a resource object setting the name and Owner. 
`adversary.add_attribute('Description'...`| Add an Attribute of type **Description** to the Resource. 
`adversary.add_tag('EXAMPLE')`            | Add a Tag to the Adversary. 
`adversary.set_security_label('TLP Gre...`| Add a Security Label to the Adversary. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Updating Adversary Resources

> The example below demonstrates how to update an Adversary Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

adversaries = tc.adversaries()

owner = 'Example Community'
adversary = adversaries.add('Updated Adversary', owner)
adversary.set_id(20)

adversary.load_attributes()
for attribute in adversary.attributes:
    if attribute.type == 'Description':
        adversary.delete_attribute(attribute.id)

adversary.add_attribute('Description', 'Updated Description')

adversary.load_tags()
for tag in adversary.tags:
    adversary.delete_tag(tag.name)

adversary.add_tag('EXAMPLE')

try:
    adversary.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to update an Adversary Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`adversaries = tc.adversaries()`          | Instantiate an Adversaries container object. 
`adversary = adversaries.add('Updated ...`| Add a resource object setting the name and Owner. 
`adversary.set_id(20)`                  | Set the ID of the Adversary to the ***EXISTING*** <br> Adversary ID to update. 
`adversary.load_attributes()`             | Load existing Attributes into the Adversary object. 
`adversary.delete_attribute(attribute.id)`| Add a delete flag on the Attribute with type **Description**. 
`adversary.add_attribute('Description'...`| Add an Attribute of type **Description** to the Resource. 
`adversary.load_tags()`                   | Load existing Tags into the Adversary object. 
`adversary.delete_tag(tag.name)`          | Add a delete flag to all Tags. 
`adversary.add_tag('EXAMPLE')`            | Add a Tag to the Resource. 
`adversary.commit()`                       | Trigger API calls to write all added, deleted, or <br> modified data. 

##Deleting Adversary Resources

> The example below demonstrates how to delete an Adversary Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

adversaries = tc.adversaries()

adversary = adversaries.add('', owner)
adversary.set_id(20)

try:
    adversary.delete()
except RuntimeError as e:
    print(e)
    sys.exit(1)
```

The example demonstrates how to delete an Adversary Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`adversaries = tc.adversaries()`          | Instantiate an Adversaries container object. 
`adversary = adversaries.add('', owner)`  | Add a resource object setting the name and Owner. 
`adversary.set_id(20)`                  | Set the ID of the Adversary to the **EXISTING** <br> Adversary ID to delete. 
`adversary.delete()`                       | Trigger API calls to write all added, deleted, or <br> modified data. 

##Batch Commit

> Python SDK Batch Commit Code Sample:

```python

dst_tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

#
# ... populate 'indicators' list of dictionaries...
#

batch_job_ids = []
batch_jobs = dst_tc.batch_jobs()
batch_job = batch_jobs.add()

batch_job.set_halt_on_error(False)             # If True, abort processing after first error
batch_job.set_attribute_write_type('Replace')  # Replace attributes (can also be Append)
batch_job.set_action('Create')                 # Create indicators (can also be Delete) 
batch_job.set_owner(dst_owner)                 # Owner to write indicators to

batch_job.upload(json.dumps(indicators))

try:
    batch_job.commit()
    print("Created batchjob %s" % batch_job.id)
    batch_job_ids.append(batch_job.id)
except RuntimeError as re:
    print("Encountered problem creating batchJob")
    traceback.print_exc(file=sys.stderr)

finished_batches = []
total_time = 0 
while len(batch_job_ids) > 0:
    time.sleep(args.poll_time)
    total_time += args.poll_time
    print("polling (total wait time {0} minutes)...".format(int(total_time / 60)))
                 
    batch_jobs = dst_tc.batch_jobs()
    for batchId in batch_job_ids:
        filter = batch_jobs.add_filter()
        filter.add_id(batchId)
        batch_jobs.retrieve()

        for batch_job in batch_jobs:
            if batch_job.status == 'Completed':
                finished_batches.append(batch_job)
                batch_job_ids.remove(batchId)
                print("Finished batch job {0}: succeeded: {1}, "
                      "failed: {2}, unprocessed: {3}".format(batchId, batch_job.success_count, batch_job.error_count, batch_job.unprocess_count))

success_total = 0
error_total = 0
unprocess_total = 0
for batch_job in finished_batches:
    if batch_job.unprocess_count:
        success_total += batch_job.success_count
    if batch_job.unprocess_count:
        unprocess_total += batch_job.unprocess_count
    if batch_job.unprocess_count:
        error_total += batch_job.error_count
        batch_job.download_errors()
        for error in batch_job.errors:
            print("Batch Job {0} errors: {1}".format(batch_job.id, batch_job.errors))
print("All batch jobs completed, totals:  "
      "succeeded: {0}, failed: {1}, unprocessed: {2}".format(success_total, error_total, unprocess_total))
      

```

The ThreatConnect platform supports adding indicators in bulk using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

These API calls assume that indicator data is [formatted in JSON, specifically a list of dictionaries](#batch-indicator-input-file-format)

### Adding Batch Resources

The example below demonstrates how to use a Batch Resource in the ThreatConnect platform. The Batch Resource has a few methods to support batch configuration before uploading a batch Indicator file to the platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Supported Functions and Properties</b>

Property Name            | Method                  | Required              | Allowable Values 
------------------------ | ----------------------- | --------------------- | ---------------- 
halt_on_error            | set_halt_on_error       | True                  | True, False       
attribute_write_type     | set_attribute_write_type| True                  | Replace, Append   
action                   | set_action              | True                  | Create, Delete    
owner                    | set_owner               | True                  | Any Owner        
 --                      | upload                  | True                  | Indicator JSON String       

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`batch_jobs = dst_tc.batch_jobs()`        | Instantiate a Batch Job container object. 
`for batch in indicators:`                | Iterator through an array of arrays of indicator objects. 
`batch_job.set_...`                       | Configure batch job to process as many indicators as <br> possible without aborting. 
`batch_job.upload(json.dumps(batch))`     | Upload job with indicator chunk as JSON data. 
`batch_job.commit()`                      | Start batch job with configuration and data defined. 
`while len(batch_ids) > 0:`               | Begin polling for batch status until all pending batches <br> are complete. 
`filter.add_id(batchId)`                  | Add current batchId to filter. 
`for batch_job in batch_jobs:`            | Get job for filtered batch ID. 
`if batch_job.status == 'Completed':`     | Check job status completion. 
`for batch_job in finished_batches:`      | Iterate through the finished batches for status print. 

##Documents Commit

> The example below demonstrates how to a Document Resource in the ThreatConnect platform.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

documents = tc.documents()
    
owner = 'Example Community'
document = documents.add('New Document', owner)
document.set_file_name('New File.txt')

fh = open('./sample1.zip', 'rb')
contents = fh.read()
document.upload(contents)

document.add_attribute('Description', 'Description Example')
document.add_tag('EXAMPLE')
document.set_security_label('TLP Green')
try:
    document.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
The ThreatConnect platform supports [adding](#add-an-document-resource), [deleting](#delete-an-document-resource), and [updating](#update-an-document-resource) of threat-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Adding Document Resources</b>

The example demonstrates how to a Document Resource in the ThreatConnect platform. The Document Resource has a special method `upload()` that allows for uploading files to the platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Supported Properties</b>

Property Name            | Method                  | Required              
------------------------ | ----------------------- | --------------------- 
file_name                | set_file_name           | True                  

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`documents = tc.documents()`              | Instantiate a Documents container object. 
`document = documents.add('New Documen...`| Add a resource object setting the name and Owner. 
`document.set_file_name('New File.txt')`  | **(REQUIRED)** Set the Document file name. 
`fh = open('./sample1.zip', 'rb')`        | Open the file handle. 
`contents = fh.read()`                    | Read contents of file from file handle. 
`document.upload(contents)`               | **Upload** file contents. 
`document.add_attribute('Description',...`| Add an Attribute of type **Description** to the <br> Resource. 
`document.add_tag('EXAMPLE')`             | Add a Tag to the Document. 
`document.set_security_label('TLP Green')`| Add a Security Label to the Document. 
`document.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Updating Document Resources

> The example below demonstrates how to update a Document Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

documents = tc.documents()

owner = 'Example Community'
document = documents.add('Updated Document', owner)
document.set_id(20)

document.load_attributes()
for attribute in document.attributes:
    if attribute.type == 'Description':
        document.delete_attribute(attribute.id)

document.add_attribute('Description', 'Updated Description')

document.load_tags()
for tag in document.tags:
    document.delete_tag(tag.name)

document.add_tag('EXAMPLE')

try:
    document.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to update a Document Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`documents = tc.documents()`              | Instantiate a Documents container object. 
`document = documents.add('Updated Doc...`| Add a Resource object setting the name and Owner. 
`document.set_id(20)`                   | Set the ID of the Document to the ***EXISTING*** <br> Document ID to update. 
`document.load_attributes()`              | Load existing Attributes into the Document object. 
`document.delete_attribute(attribute.id)` | Add a delete flag on the Attribute with <br> type **Description**. 
`document.add_attribute('Description',...`| Add an Attribute of type **Description** to <br> the Resource. 
`document.load_tags()`                    | Load existing Tags into the Document object. 
`document.delete_tag(tag.name)`           | Add a delete flag to all Tags. 
`document.add_tag('EXAMPLE')`             | Add a Tag to the Resource. 
`document.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Deleting Document Resources

> The example below demonstrates how to delete a Document Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

documents = tc.documents()

document = documents.add('', owner)
document.set_id(20)

try:
    document.delete()
except RuntimeError as e:
    print(e)

```

The example demonstrates how to delete a Document Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`documents = tc.documents()`              | Instantiate a Documents container object. 
`document = documents.add('', owner)`     | Add a Resource object setting the name and Owner. 
`document.set_id(20)`                   | Set the ID of the Document to the **EXISTING** <br> Document ID to delete. 
`document.delete()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Emails Commit

> The example below demonstrates how to create an Email Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

emails = tc.emails()
    
owner = 'Example Community'
email = emails.add('New Email', owner)

email.set_body('This is an email body.')
email.set_from_address('bad_guy@badguys.com')
email.set_header('This is an improper email header.')
email.set_subject('This is an email subject.')
email.set_to('victim@goodguys.com')

email.add_attribute('Description', 'Description Example')
email.add_tag('EXAMPLE')
email.set_security_label('TLP Green')
try:
    email.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
The ThreatConnect platform supports [adding](#add-an-email-resource), [deleting](#delete-an-email-resource), and [updating](#update-an-email-resource) of threat-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Adding Email Resources</b>

The example demonstrates how to create an Email Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Supported Properties</b>

Property Name            | Method                  | Required              
------------------------ | ----------------------- | --------------------- 
body                     | set_body                | True                  
from_address             | set_from_address        | False                 
header                   | set_header              | True                  
score                    | set_score               | False                 
subject                  | set_subject             | True                  
to                       | set_to                  | False                 

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`emails = tc.emails()`          | Instantiate an Emails container object. 
`email = emails.add('New Email', ...`| Add a Resource object setting the name and Owner. 
`email.set_body('This is an email body...`| **(REQUIRED)** Set the Email body. 
`email.set_from_address('bad_guy@badgu...`| **(OPTIONAL)** Set the Email from address. 
`email.set_header('This is an improper...`| **(REQUIRED)** Set the Email header. 
`email.set_subject('This is an email s...`| **(REQUIRED)** Set the Email subject. 
`email.set_to('victim@goodguys.com')`     | **(OPTIONAL)** Set the Email to address. 
`email.add_attribute('Description', 'D...`| Add an Attribute of type **Description** to the Resource. 
`email.add_tag('EXAMPLE')`                | Add a Tag to the Email. 
`email.set_security_label('TLP Green')`   |Add a Security Label to the Email. 
`email.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Updating Email Resources

> The example below demonstrates how to update an Email Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

emails = tc.emails()

owner = 'Example Community'
email = emails.add('Updated Email', owner)
email.set_id(20)

email.load_attributes()
for attribute in email.attributes:
    if attribute.type == 'Description':
        email.delete_attribute(attribute.id)

email.add_attribute('Description', 'Updated Description')

email.load_tags()
for tag in email.tags:
    email.delete_tag(tag.name)

email.add_tag('EXAMPLE')

try:
    email.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to update an Email Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`emails = tc.emails()`                    | Instantiate an Emails container object. 
`email = emails.add('Updated Email', o...`| Add a Resource object setting the name and Owner. 
`email.set_id(20)`                      | Set the ID of the Email to the ***EXISTING*** <br> Email ID to update. 
`email.load_attributes()`                 | Load existing Attributes into the Email object. 
`email.delete_attribute(attribute.id)`    | Add a delete flag on the Attribute with <br> type **Description**. 
`email.add_attribute('Description', 'U...`| Add an Attribute of type **Description** to <br> the Resource. 
`email.load_tags()`                       | Load existing Tags into the Email object. 
`email.delete_tag(tag.name)`              | Add a delete flag to all Tags. 
`email.add_tag('EXAMPLE')`                | Add a Tag to the Resource. 
`email.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Deleting Email Resources

> The example below demonstrates how to delete an Email Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

emails = tc.emails()

email = emails.add('', owner)
email.set_id(20)

try:
    email.delete()
except RuntimeError as e:
    print(e)
    sys.exit(1)
```

The example demonstrates how to delete an Email Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`emails = tc.emails()`                    | Instantiate an Emails container object. 
`email = emails.add('', owner)`           | Add a Resource object setting the name <br> and Owner. 
`email.set_id(20)`                      | Set the ID of the Email to the **EXISTING** <Br> Email ID to delete. 
`email.delete()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Incidents Commit

> The example below demonstrates how to create an Incident Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

incidents = tc.incidents()
    
owner = 'Example Community'
incident = incidents.add('New Incident', owner)

incident.set_event_date('2015-03-01T00:00:00Z')
    
incident.add_attribute('Description', 'Description Example')
incident.add_tag('EXAMPLE')
incident.set_security_label('TLP Green')
try:
    incident.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The ThreatConnect platform supports [adding](#add-an-incident-resource), [deleting](#delete-an-incident-resource), and [updating](#update-an-incident-resource) of threat-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Adding Incident Resources</b>

The example demonstrates how to create an Incident Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Supported Properties</b>

Property Name            | Method                  | Required              
------------------------ | ----------------------- | --------------------- 
event_date               | set_event_date          | True                  

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`incidents = tc.incidents()`              | Instantiate an Incidents container object. 
`incident = incidents.add('New Incident')`| Add a Resource object setting the name and Owner. 
`incident.set_event_date('2015-03-01T0...`| **(REQUIRED)** Set event date of Incident. 
`incident.add_attribute('Description' ...`| Add an Attribute of type **Description** to <br> the Resource. 
`incident.add_tag('EXAMPLE')`             | Add a Tag to the Incident. 
`incident.set_security_label('TLP Green')`| Add a Security Label to the Incident. 
`incident.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Updating Incident Resources

> The example below demonstrates how to update an Incident Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

incidents = tc.incidents()

owner = 'Example Community'
incident = incidents.add('Updated Incident', owner)
incident.set_id(20)

incident.load_attributes()
for attribute in incident.attributes:
    if attribute.type == 'Description':
        incident.delete_attribute(attribute.id)

incident.add_attribute('Description', 'Updated Description')

incident.load_tags()
for tag in incident.tags:
    incident.delete_tag(tag.name)

incident.add_tag('EXAMPLE')

try:
    incident.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to update an Incident Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example ,no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`incidents = tc.incidents()`              | Instantiate an Incidents container object. 
`incident = incidents.add('Updated Inc...`| Add a Resource object setting the name and Owner. 
`incident.set_id(20)`                   | Set the ID of the Incident to the ***EXISTING*** <br> Incident ID to update. 
`incident.load_attributes()`              | Load existing Attributes into the Incident object. 
`incident.delete_attribute(attribute.id)` | Add a delete flag to the Attribute with <br> type **Description**. 
`incident.add_attribute('Description' ...`| Add an Attribute of type **Description** to <Bb> the Resource. 
`incident.load_tags()`                    | Load existing Tags into the Incident object. 
`incident.delete_tag(tag.name)`           | Add a delete flag to all Tags. 
`incident.add_tag('EXAMPLE')`             | Add a Tag to the Resource. 
`incident.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Deleting Incident Resources

> The example below demonstrates how to delete an Incident Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

incidents = tc.incidents()

incident = incidents.add('', owner)
incident.set_id(20)

try:
    incident.delete()
except RuntimeError as e:
    print(e)
    sys.exit(1)
```

The example demonstrates how to delete an Incident Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `delete()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`incidents = tc.incidents()`              | Instantiate an Incidents container object. 
`incident = incidents.add('', owner)`     | Add a Resource object setting the name and Owner. 
`incident.set_id(20)`                   | Set the ID of the Incident to the **EXISTING** <br> Incident ID to delete. 
`incident.delete()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Indicators Commit

> The example below demonstrates how to create an Address Indicator resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
    
owner = 'Example Community'
indicator = indicators.add('4.3.254.1', owner)
indicator.set_confidence(75)
indicator.set_rating(2.5)

indicator.add_attribute('Description', 'Example Attribute')
indicator.add_tag('EXAMPLE')
indicator.set_security_label('TLP Green')

try:
    indicator.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
The ThreatConnect platform supports the committing of Indicators of Compromise programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Indicator Type Override</b>

The `add()` method on the `indicators()` object allows the user to bypass the automatic Indicator identification and validation check by specifying the IndicatorType (e.g. `indicator = indicators.add('<indicator>', owner, IndicatorType.ADDRESSES)`).

<b>Adding Address Indicators</b>

The example demonstrates how to create an Address Indicator resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicators = tc.indicators()`            | Instantiate an Indicator container object. 
`indicator = indicators.add('4.3.254....` | Add a Resource object setting the value and Owner. 
`indicator.set_confidence(75)`            | Set the Confidence value for this Indicator. 
`indicator.set_rating(2.5)`               | Set the Rating value for this Indicator. 
`indicator.add_attribute('Description...` | Add an Attribute of type **Description** to the Resource. 
`indicator.add_tag('EXAMPLE')`            | Add a Tag to the Resource. 
`indicator.set_security_label('TLP Gre..` | Add a Security Label to the Resource. 
`indicator.commit()`                      | Trigger multiple API calls to write Resource, <br> Attributes, Security Labels, and Tags. 

##Adding Email Address Indicators

> The example below demonstrates how to create an Email Address Indicator Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
    
owner = 'Example Community'
indicator = indicators.add('badguy@badguysareus.com', owner)
indicator.set_confidence(75)
indicator.set_rating(2.5)

indicator.add_attribute('Description', 'Example Attribute')
indicator.add_tag('EXAMPLE')
indicator.set_security_label('TLP Green')

try:
    indicator.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to create an Email Address Indicator Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicators = tc.indicators()`            | Instantiate an Indicator container object. 
`indicator = indicators.add('badguy@....` | Add a Resource object setting the value and Owner. 
`indicator.set_confidence(75)`            | Set the Confidence value for this Indicator. 
`indicator.set_rating(2.5)`               | Set the Rating value for this Indicator. 
`indicator.add_attribute('Description...` | Add an Attribute of type **Description** to the Resource. 
`indicator.add_tag('EXAMPLE')`            | Add a Tag to the Resource. 
`indicator.set_security_label('TLP Gre..` | Add a Security Label to the Resource. 
`indicator.commit()`                      | Trigger multiple API calls to write Resource, <br> Attributes, Security Labels, and Tags. 

##Adding File Hash Indicators

> The example below demonstrates how to create a File Hash Indicator Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
    
owner = 'Example Community'
indicator = indicators.add('8743b52063cd84097a65d1633f5c74f5', owner) # MD5 hash of string `hashcat`
indicator.set_indicator('b89eaac7e61417341b710b727768294d0e6a277b') #SHA1 hash of same string
indicator.set_indicator('127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935') # SHA256 hash of same string
indicator.set_confidence(75)
indicator.set_rating(2.5)
indicator.set_size(112)

indicator.add_attribute('Description', 'Example Attribute')
indicator.add_tag('EXAMPLE')
indicator.set_security_label('TLP Green')

try:
    indicator.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to create a File Hash Indicator Resource in the ThreatConnect platform. File Indicators support MD5, SHA1, and SHA256 hashes, added in the above order to the same Indicator with the `set_indicator()` method. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicator = indicators.add('8743b520...` | Add an Indicator object setting the value and Owner. 
`indicator.set_indicator('b89eaac7e61...` | Add File addition File Hashes for this Indicator. 
`indicator.set_indicator('127e6fbfe24...` | Add File addition File Hashes for this Indicator. 
`indicator.set_confidence(75)`            | Set the Confidence value for this Indicator. 
`indicator.set_rating(2.5)`               | Set the Rating value for this Indicator. 
`indicator.set_size(112)`                 | Set the File size property of the Indicator. 
`indicator.add_attribute('Description...` | Add an Attribute of type **Description** to the Resource. 
`indicator.add_tag('EXAMPLE')`            | Add a Tag to the Indicator. 
`indicator.set_security_label('TLP Gre..` | Add a Security Label to the Indicator. 
`indicator.commit()`                      | Trigger multiple API calls to write Indicator, <br> Attributes, Security Labels, and Tags. 

##Adding File Occurrences

> A File occurrence can be added to File Indicators by inserting the example code before the `indicator.commit()` method is called:

```python

fo_date = (datetime.isoformat(datetime(2015, 3, 29))) + 'Z'
indicator.add_file_occurrence('badfile.exe', 'C:\windows', fo_date)
```

A File occurrence can be added to File Indicators by inserting the example code before the `indicator.commit()` method is called.

##Adding Host Indicators

> The example below demonstrates how to create a Host Indicator Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
    
owner = 'Example Community'
indicator = indicators.add('badguy.com', owner)
indicator.set_confidence(75)
indicator.set_rating(2.5)

indicator.add_attribute('Description', 'Example Attribute')
indicator.add_tag('EXAMPLE')
indicator.set_security_label('TLP Green')

try:
    indicator.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

> Automatically enrich indicator with DNS resolution or ownership information from a third-party service

```python
# Query PTR record for a given domain, or {A, AAAA} record for a given IP
indicator.set_dns_active(True)

# Look up IP or domain ownership information 
indicator.set_whois_active(True) 
```

The example demonstrates how to create a Host Indicator Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicators = tc.indicators()`            | Instantiate an Indicator container object. 
`indicator = indicators.add('badguy.....` | Add a Resource object setting the value and Owner. 
`indicator.set_confidence(75)`            | Set the Confidence value for this Indicator. 
`indicator.set_rating(2.5)`               | Set the Rating value for this Indicator. 
`indicator.add_attribute('Description...` | Add an Attribute of type **Description** to the Resource. 
`indicator.add_tag('EXAMPLE')`            | Add a Tag to the Resource. 
`indicator.set_security_label('TLP Gre..` | Add a Security Label to the Resource. 
`indicator.commit()`                      | Trigger multiple API calls to write Resource, <br> Attributes, Security Labels, and Tags. 

##Adding URL Indicators

> The example below demonstrates how to create a URL Indicator Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
    
owner = 'Example Community'
indicator = indicators.add('badguy.com/clickme.html', owner)
indicator.set_confidence(75)
indicator.set_rating(2.5)

indicator.add_attribute('Description', 'Example Attribute')
indicator.add_tag('EXAMPLE')
indicator.set_security_label('TLP Green')

try:
    indicator.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to create a URL Indicator Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicators = tc.indicators()`            | Instantiate an Indicator container object. 
`indicator = indicators.add('badguy.....` | Add a Resource object setting the value and Owner. 
`indicator.set_confidence(75)`            | Set the Confidence value for this Indicator. 
`indicator.set_rating(2.5)`               | Set the Rating value for this Indicator. 
`indicator.add_attribute('Description...` | Add an Attribute of type **Description** to the Resource. 
`indicator.add_tag('EXAMPLE')`            | Add a Tag to the Resource. 
`indicator.set_security_label('TLP Gre..` | Add a Security Label to the Resource. 
`indicator.commit()`                      | Trigger multiple API calls to write Resource, <br> Attributes, Security Labels, and Tags. 

##Deleting Indicator Resources

> Python SDK deleting Indicator Resources:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()

indicator = indicators.add('4.3.2.1', owner)

try:
    indicator.delete()
except RuntimeError as e:
    print(e)

```

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`indicators = tc.indicators()`              | Instantiate an Indicator container object. 
`indicator = indicators.add('4.3.2.1...`  | Add a Resource object setting the value and Owner. 
`indicator.delete()`                      | Trigger API calls to delete the Resource. 

##Signatures Commit

> The example below demonstrates how to create a Signature Resource in the ThreatConnect platform.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

signatures = tc.signatures()
    
owner = 'Example Community'
signature = signatures.add('New Signature', owner)

file_text = '"rule example_sig : example\n{\n'
file_text += 'meta:\n        description = "This '
file_text += 'is just an example"\n\n '
file_text += 'strings:\n        $a = {6A 40 68 00 '
file_text += '30 00 00 6A 14 8D 91}\n        $b = '
file_text += '{8D 4D B0 2B C1 83 C0 27 99 6A 4E '
file_text += '59 F7 F9}\n    condition:\n '
file_text += '$a or $b or $c\n}"'

signature.set_file_name('bad_file.txt')
signature.set_file_type('YARA')
signature.set_file_text(file_text)
    
signature.add_attribute('Description', 'Description Example')
signature.add_tag('EXAMPLE')
signature.set_security_label('TLP Green')
try:
    signature.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
The ThreatConnect platform supports [adding](#add-an-signature-resource), [deleting](#delete-an-signature-resource), and [updating](#update-an-signature-resource) of threat-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Adding Signature Resources</b>

The example demonstrates how to create a Signature Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

<b>Supported Properties</b>

Property Name            | Method                  | Required              
------------------------ | ----------------------- | --------------------- 
file_name                | set_file_name           | True                  
file_text                | set_file_text           | False                 
file_type                | set_file_type           | True                  

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`signatures = tc.signatures()`            | Instantiate a Signatures container object. 
`signature = signatures.add('New Signa...`| Add a Resource object setting the name and Owner. 
`signature.set_file_name('bad_file.txt')` | **(REQUIRED)** Set file name for Signature. 
`signature.set_file_type('YARA')`         | **(REQUIRED)** Set file type for Signature. 
`signature.set_file_text(file_text)`      | **(OPTIONAL)** Set file contents for Signature. 
`signature.add_attribute('Description'...`| Add an Attribute of type **Description** to the Resource. 
`signature.add_tag('EXAMPLE')`            | Add a Tag to the Signature. 
`signature.set_security_label('TLP Gre...`| Add a Security Label to the Signature. 
`signature.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Updating Signature Resources

> The example below demonstrates how to update a Signature Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

signatures = tc.signatures()

owner = 'Example Community'
signature = signatures.add('Updated Signature', owner)
signature.set_id(20)

signature.load_attributes()
for attribute in signature.attributes:
    if attribute.type == 'Description':
        signature.delete_attribute(attribute.id)

signature.add_attribute('Description', 'Updated Description')

signature.load_tags()
for tag in signature.tags:
    signature.delete_tag(tag.name)

signature.add_tag('EXAMPLE')

try:
    signature.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to update a Signature Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`signatures = tc.signatures()`            | Instantiate a Signatures container object. 
`signature = signatures.add('Updated D...`| Add a Resource object setting the name and Owner. 
`signature.set_id(20)`                  | Set the ID of the Signature to the ***EXISTING*** <br> Signature ID to update. 
`signature.load_attributes()`             | Load existing Attributes into the Signature object. 
`signature.delete_attribute(attribute.id)`| Add a delete flag to the Attribute with <br> type **Description**. 
`signature.add_attribute('Description'...`| Add an Attribute of type **Description** to <br> the Resource. 
`signature.load_tags()`                   | Load existing Tags into the Signature object. 
`signature.delete_tag(tag.name)`          | Add a delete flag to all Tags. 
`signature.add_tag('EXAMPLE')`            | Add a Tag to the Resource. 
`signature.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Deleting Signature Resources

> The example below demonstrates how to delete a Signature Resource in the ThreatConnect platform.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

signatures = tc.signatures()

signature = signatures.add('', owner)
signature.set_id(20)

try:
    signature.delete()
except RuntimeError as e:
    print(e)
    sys.exit(1)
```

The example demonstrates how to delete a Signature Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`signatures = tc.signatures()`            | Instantiate a Signatures container object. 
`signature = signatures.add('', owner)`   | Add a Resource object setting the name and Owner. 
`signature.set_id(20)`                  | Set the ID of the Signature to the **EXISTING** <br> Signature ID to delete. 
`signature.delete()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

## Tasks Commit
The ThreatConnect platform supports [adding](#adding-task-resources), [deleting](#deleting-task-resources), and [updating](#updating-task-resources) of task-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.


Other task-specific data such as `Assignee` or `Escalation Date` can be [modified using built-in library functions](https://github.com/ThreatConnect-Inc/threatconnect-python/blob/master/examples/commit/tasks_commit.py#L175)

## Adding Task Resources
The example below demonstrates how to create a Task Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

###Code Sample

```python
...

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

tasks = tc.tasks()

task = tasks.add('New Task')
task.add_attribute('Description', 'Description Example')
task.add_tag('EXAMPLE')
task.add_security_label('TLP Green')

try:
    task.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

> Note: In the prior example, no API calls are made until the `commit()` method is invoked.

###Code Highlights

Snippet                                   | Description                                                                       |
----------------------------------------- | --------------------------------------------------------------------------------- |
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. |
`tasks = tc.tasks()`                      | Instantiate a Tasks container object. |
`task = tasks.add('New task' own...`      | Add a Resource object setting the name and Owner. |
`task.add_attribute('Description' 'D...`  | Add an Attribute of type **Description** to the Resource. |
`task.add_tag('EXAMPLE')`                 | Add a Tag to the Task. |
`task.add_security_label('TLP Green')`    | Add a Security Label to the task. |
`task.commit()`                           | Trigger API calls to write all added, deleted, or modified data. |

## Updating Task Resources
The example below demonstrates how to update a Task Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

###Code Sample

```python
...

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

tasks = tc.tasks()

task = tasks.add('Updated Task')
task.set_id(20)

task.load_attributes()
for attribute in task.attributes:
    if attribute.type == 'Description':
        task.delete_attribute(attribute.id)

task.add_attribute('Description', 'Updated Description')

task.load_tags()
for tag in task.tags:
    task.delete_tag(tag.name)

task.add_tag('EXAMPLE')

try:
    task.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

> Note: In the prior example, no API calls are made until the `commit()` method is invoked.

*Code Highlights*

Snippet                                   | Description                                                                       |
----------------------------------------- | --------------------------------------------------------------------------------- |
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. |
`tasks = tc.tasks()`                      | Instantiate a Tasks container object. |
`task = Tasks.add('Updated task'...`      | Add a Resource object setting the name and Owner. |
`task.set_id(20)`                       | Set the ID of the task to the ***EXISTING*** task ID to update. |
`task.load_attributes()`                  | Load existing Attributes into the task object. |
`task.delete_attribute(attribute.id)`     | Add a delete flag to the Attribute with type **Description**. |
`task.add_attribute('Description', '...`  | Add an Attribute of type **Description** to the Resource. |
`task.load_tags()`                        | Load existing Tags into the task object. |
`task.delete_tag(tag.name)`               | Add a delete flag to all Tags. |
`task.add_tag('EXAMPLE')`                 | Add a Tag to the Resource. |
`task.commit()`                           | Trigger API calls to write all added, deleted, or modified data. |

## Deleting Task Resources
The example below demonstrates how to delete a Task Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

###Code Sample

```python
...

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

tasks = tc.tasks()

task = tasks.add('', owner)
task.set_id(20)

try:
    task.delete()
except RuntimeError as e:
    print(e)
    sys.exit(1)
```

> Note: In the prior example, no API calls are made until the `commit()` method is invoked.

*Code Highlights*

Snippet                                   | Description                                                                       |
----------------------------------------- | --------------------------------------------------------------------------------- |
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. |
`tasks = tc.tasks()`                      | Instantiate a Tasks container object. |
`task = tasks.add('', owner)`             | Add a Task Resource setting the name and Owner. |
`task.set_id(20)`                         | Set the ID of the task to the **EXISTING** task ID to delete. |
`task.delete()`                           | Trigger API calls to delete the task. |

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

##Threats Commit

> The example below demonstrates how to create a Threat Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

threats = tc.threats()
    
owner = 'Example Community'
threat = threats.add('New Threat', owner)
threat.add_attribute('Description', 'Description Example')
threat.add_tag('EXAMPLE')
threat.set_security_label('TLP Green')
try:
    threat.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
The ThreatConnect platform supports [adding](#add-an-threat-resource), [deleting](#delete-an-threat-resource), and [updating](#update-an-threat-resource) of threat-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Adding Threat Resources</b>

The example demonstrates how to create a Threat Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`threats = tc.threats()`                  | Instantiate a Threats container object. 
`threat = threats.add('New Threat' own...`| Add a Resource object setting the name and Owner. 
`threat.add_attribute('Description' 'D...`| Add an Attribute of type **Description** <br> to the Resource. 
`threat.add_tag('EXAMPLE')`               | Add a Tag to the Threat. 
`threat.set_security_label('TLP Green')`  | Add a Security Label to the Threat. 
`threat.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Updating Threat Resources

> The example below demonstrates how to update a Threat Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

threats = tc.threats()

owner = 'Example Community'
threat = threats.add('Updated Threat', owner)
threat.set_id(20)

threat.load_attributes()
for attribute in threat.attributes:
    if attribute.type == 'Description':
        threat.delete_attribute(attribute.id)

threat.add_attribute('Description', 'Updated Description')

threat.load_tags()
for tag in threat.tags:
    threat.delete_tag(tag.name)

threat.add_tag('EXAMPLE')

try:
    threat.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to update a Threat Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`threats = tc.threats()`                  | Instantiate a Threats container object. 
`threat = threats.add('Updated Threat'...`| Add a Resource object setting the name and Owner. 
`threat.set_id(20)`                     | Set the ID of the Threat to the ***EXISTING*** <br> Threat ID to update. 
`threat.load_attributes()`                | Load existing Attributes into the Threat object. 
`threat.delete_attribute(attribute.id)`   | Add a delete flag to the Attribute with <br> type **Description**. 
`threat.add_attribute('Description', '...`| Add an Attribute of type **Description** to <br> the Resource. 
`threat.load_tags()`                      | Load existing Tags into the Threat object. 
`threat.delete_tag(tag.name)`             | Add a delete flag to all Tags. 
`threat.add_tag('EXAMPLE')`               | Add a Tag to the Resource. 
`threat.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Deleting Threat Resources

> The example below demonstrates how to delete an Threat Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

threats = tc.threats()

threat = threats.add('', owner)
threat.set_id(20)

try:
    threat.delete()
except RuntimeError as e:
    print(e)
    sys.exit(1)
```

The example demonstrates how to delete an Threat Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`threats = tc.threats()`                  | Instantiate a Threats container object. 
`threat = threats.add('', owner)`         | Add a Resource object setting the name and Owner. 
`threat.set_id(20)`                     | Set the ID of the Threat to the **EXISTING** <br> Threat ID to delete. 
`threat.delete()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Victims Commit

> The example below demonstrates hoe to create a Victim Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

victims = tc.victims()
    
owner = 'Example Community'
victim = victims.add('Robin Scherbatsky', owner)

victim.set_nationality('Canadian')
victim.set_org('Royal Canadian Mounted Police')
victim.set_suborg('Quebec Office')
victim.set_work_location('Quebec')

# email address assets can be added to new victim
asset = VictimAssetObject(ResourceType.VICTIM_EMAIL_ADDRESSES)
asset.set_address('victim@victimsareus.com')
asset.set_address_type('Personal')
victim.add_asset(asset)

# network account assets can be added to new victim
asset = VictimAssetObject(ResourceType.VICTIM_NETWORK_ACCOUNTS)
asset.set_account('victim')
asset.set_network('victimsareus Active Directory')
victim.add_asset(asset)

# phone assets can be added to new victim
asset = VictimAssetObject(ResourceType.VICTIM_PHONES)
asset.set_phone_type('555-555-5555')
victim.add_asset(asset)

# social network assets can be added to new victim
asset = VictimAssetObject(ResourceType.VICTIM_SOCIAL_NETWORKS)
asset.set_account('@victim')
asset.set_network('Twitter')
victim.add_asset(asset)

# website assets can be added to new victim
asset = VictimAssetObject(ResourceType.VICTIM_WEBSITES)
asset.set_website('www.victimsareus.com')
victim.add_asset(asset)
    
try:
    victim.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The ThreatConnect platform supports [adding](#add-an-victim-resource), [deleting](#delete-an-victim-resource), and [updating](#update-an-victim-resource) of threat-intelligence data programmatically using the API. The Python SDK features an easy-to-use interface to assist in rapid development of software to manage this data.

<b>Adding Victim Resources</b>

The example demonstrates hoe to create a Victim Resource in the ThreatConnect platform. For more information on the purpose of each line of code see, the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`victims = tc.victims()`                  | Instantiate a Victims container object. 
`victim = victims.add('Robin Scherbats...`| Add a Resource object setting the name and Owner. 
`victim.set_nationality('Canadian')`      | **(OPTIONAL)** Set Victim nationality. 
`victim.set_org('Royal Canadian Mounte...`| **(OPTIONAL)** Set Victim Organization. 
`victim.set_suborg('Quebec Office')`      | **(OPTIONAL)** Set Victim Sub-Organization. 
`victim.set_work_location('Quebec')`      | **(OPTIONAL)** Set Victim location. 
`victim.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Updating Victim Resources
> The example below demonstrates how to update a Victim Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

victims = tc.victims()

owner = 'Example Community'
victim = victims.add('Updated Victim', owner)
victim.set_id(20)

try:
    victim.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The example demonstrates how to update a Victim Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`victims = tc.victims()`                  | Instantiate a Victims container object. 
`victim = victims.add('Updated Victim'...`| Add a Resource object setting the name and Owner. 
`victim.set_id(20)`                     | Set the ID of the Victim to the ***EXISTING*** <br> Victim ID to update. 
`victim.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Deleting Victim Resources

> The example below demonstrates how to delete a Victim Resource in the ThreatConnect platform:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

victims = tc.victims()

victim = victims.add('', owner)
victim.set_id(20)

try:
    victim.delete()
except RuntimeError as e:
    print(e)
    sys.exit(1)
```

The example demonstrates how to delete a Victim Resource in the ThreatConnect platform. For more information on the purpose of each line of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`victims = tc.victims()`                  | Instantiate a Victims container object. 
`victim = victims.add('', owner)`         | Add a Resource object setting the name and Owner. 
`victim.set_id(20)`                     | Set the ID of the Victim to the **EXISTING** <br> Victim ID to delete. 
`victim.delete()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

##Associations

> The following example demonstrates how to **Associate** a Group to an Adversary Resource. For other Resource Groups, Indicators, and Victims, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('New Resource', owner)
resource.associate_group(ResourceType.INCIDENTS, 555)
resource.associate_group(ResourceType.SIGNATURE, 123)

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
The Python SDK provides easy methods to manage all Group, Indicator, and Victim Associations. Associations are supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats)   

An example of the [Associate Group](#associate-group), [Associate Indicator](#associate-indicator), [Associate Victim](#associate-victim), [Disassociate Group](#disassociate-group), [Disassociate Indicator](#disassociate-indicator), and [Disassociate Victim](#disassociate-victim) methods, as well as explanations of the code, are provided in the following section .

##Associate Group

An Association to a Resource Group, Indicator, or Victim can be created to another Resource Group by using the `associate_group()` method and passing the Resource Type and Resource ID. The Associated Resource must exist in the ThreatConnect platform prior to the Association attempt.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('New Resourc...`| Add a Resource object setting the name and Owner. 
`resource.associate_group(ResourceType...`| Add an Association to another Resource. 
`resource.associate_group(ResourceType...`| Add an Association to another Resource. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Associate Indicator

> The following example demonstrates how to **Associate** an Indicator to an Adversary Resource. For other Resource Groups, Indicators, and Victims, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('New Resource', owner)
resource.associate_indicator(ResourceType.EMAIL_ADDRESSES, 'badguy@badguys.com')
resource.associate_indicator(ResourceType.ADDRESSES, '4.3.2.1')
resource.associate_indicator(ResourceType.HOSTS, 'badguys.com')

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

An Association to a Resource Group, Indicator, or Victim can be created to a Indicator by using the `associate_indicator()` method and passing the Resource Type and Indicator Value. The Associated Indicator must exist in the ThreatConnect platform prior to the Association attempt.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('New Resourc...`| Add a Resource object setting the name and Owner. 
`resource.associate_indicator(Resource...`| Add an Association to an Indicator. 
`resource.associate_indicator(Resource...`| Add an Association to an Indicator. 
`resource.associate_indicator(Resource...`| Add an Association to an Indicator. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

##Associate Victim

> The following example demonstrates how to **Associate** a Victim to an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('New Adversary', owner)
resource.associate_victim(325)

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

An Association to a Resource Group or Indicator can be created to a Victim by using the `associate_victim()` method and passing the Victim ID. The Associated Victim must exist in the ThreatConnect platform prior to the Association attempt.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`              | Instantiate a Resources container object. 
`resource = resources.add('New Adversa...`| Add a Resource object setting the name and Owner. 
`resource.associate_victim(325)`          | Add an Association to a Victim. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Disassociate Group

> The following example demonstrates how to **Disassociate** a Group from an Adversary Resource. For other Resource Groups, Indicators, and Victims, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('Existing Resource', owner)

for association in resource.group_associations:
    if association.type == 'Incident':
        resource.disassociate_group(association.resource_type, association.id)

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

An existing Group Association to another Resource Group, Indicator, or Victim can be removed by using the `disassociate_group()` method and passing the Resource Type and Resource ID. If the Resource ID of the Group is not known, all Associated Groups can be retrieved from the API iterating over the [group_associations](/python/retrieve/group_associations_retrieve/#associations) property.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('Existing Re...`| Add a Resource object setting the name and Owner. 
`for association in resource.group_associat...`| Iterate through all Associated Groups. 
`if association.type == 'Incident':`      | Match any Association of type Incidents. 
`res.disassociate_group(association.re...`| Disassociate the Group Resource. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

##Disassociate Indicator

> The following example demonstrates how to **Disassociate** an Indicator from an Adversary Resource. For other Resource Groups and Victim,s the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('Existing Resource', owner)

for association in resource.indicator_associations:
    if association.type == 'EmailAddress':
        resource.disassociate_indicator(association.resource_type, association.indicator)

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

An existing Indicator Association to a Resource Group or Victim can be removed by using the `disassociate_indicator()` method and passing the Resource Type and Indicator Value. If the Indicator Value of the Indicator is not known, all Associated Indicators can be retrieved from the API iterating over the [indicator_associations](/python/retrieve/indicator_associations_retrieve/#retrieving-indicator-associations) property.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('Existing Re...`| Add a Resource object setting the name and Owner. 
`for association in resource.indicator_asso...`| Iterate through all Associated Groups. 
`if association.type == 'EmailAdd':`      | Match any Association of type Incidents. 
`resource.disassociate_indicator(associatio...`| Disassociate the Incident. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

##Disassociate Victim

> The following example demonstrates how to **Disassociate** a Victim from an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('Existing Resource', owner)

for association in resource.victim_associations:
    if association.name == 'Drew Brees':
        resource.disassociate_victim(association.id)

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

An existing Victim Association to a Resource Group or Indicator can be removed by using the `disassociate_victim()` method and passing the Victim ID. If the ID of the Victim is not known, all Associated Victims can be retrieved from the API iterating over the [victim_associations](/python/retrieve/victim_associations_retrieve/#victim-associations-retrieve) property.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('Existing Re...`| Add a Resource object setting the name and Owner. 
`for association in resource.victim_associa...`| Iterate through all Associated Groups. 
`if association.name == 'Drew Brees':`    | Match any Association of type Incidents. 
`res.disassociate_victim(association.i...`| Disassociate the Incident. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

<b>Resource Metadata</b>

<b>Attributes</b>
See the [Loading Attributes Example](#loading-attributes-example).

<b>Security Label</b>
See the [Loading Security Label Documentation](#loading-security-label).

<b>Tags</b>
See the [Loading Tags Documentation](#loading-tags).

<b>Associations</b>

<b>Groups</b>

See the [Group Associations Documentation](#associations).

<b>Indicators</b>

See the [Indicator Associations Documentation](#retrieving-indicator-associations).

<b>Victims</b>

See the [Victim Associations Documentation](#victim-associations-retrieve).

<b>Outputs</b>

<b>CSV</b>

See the [CSV Output Documentation](#csv).

<b>JSON</b>

See the [JSON Output Documentation](#json).

<b>Key Value</b>

See the [Key Value Output Documentation](#key-value).

##Attributes

> The following example demonstrates how to **add** an Attribute to an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('New Adversary', owner)

resource.add_attribute('Description', 'Description Example')
resource.add_attribute('Source', 'SIEM')

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The Python SDK provides easy methods to manage Attributes. Attributes are supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats)   

An example of the [add](#add-attribute), [delete](#delete-attribute), and [update](#update-attribute) methods, as well as explanations of the code, are provided in the following section.

##Adding Attributes

An Attribute can be added to a Resource Group or Indicator using the `add_attribute()` method and passing the Attribute Type and Attribute Value. Attributes can be added while creating a new Resource or during a Resource update. The Attribute Type (e.g., description) must be created in the Organization prior to it being added via the API. Some Attributes come packaged with the ThreatConnect platform, but custom Attributes must have been previously created in the User Interface by the ThreatConnect administrator.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('New Adversa...`| Add a Resource object setting the name and Owner. 
`resource.add_attribute('Description',...`| Add an Attribute of type **Description** to <br> the Resource. 
`resource.add_attribute('Source, 'SIEM')` | Add an Attribute of type **Source** to the Resource. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

##Deleting Attributes

> The following example demonstrates how to **delete** an Attribute for an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('Existing Resource', owner)
resource.add_id(34)

resource.load_attributes()
for attribute in resource.attributes:
    if attribute.type == 'Description':
        resource.delete_attribute(attribute.id)

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
An Attribute can be deleted from an existing Resource Group or Indicator using the `delete_attribute()` method and passing the Attribute ID. If the Attribute ID is not known, all Attributes for this Resource or Indicator can be retrieved from the API using the [load_attributes()](/python/retrieve/loading_attributes_retrieve/#loading-attributes) method.

Note: In the prior example, no API calls are made until the commit() method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('Existing Re...`| Add a Resource object setting the name and Owner. 
`resource.load_attributes()`              | Load existing Attributes. 
`for attribute in resource.attributes:`   | Iterate through Attribute objects. 
`if attribute.type == 'Description':`     | Look for a **Description** Attribute. 
`resource.delete_attribute(attribute.id)` | Delete the Attribute from the Resource.
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

##Update Attribute

> Python SDK Updating Attribute using the load attributes method:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('Existing Resource', owner)
resource.set_id(123)

try:
    resource.retrieve()
except RuntimeError as e:
    print('Error: {0}'.format(e))

resource.load_attributes()
for attribute in resource.attributes:
    if attribute.type == 'Description':
        resource.update_attribute(attribute.id, 'Updated Description')

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

An Attribute can be updated on an existing Resource Group or Indicator using the `update_attribute()` method and passing the Attribute ID and the updated Attribute Value. If the Attribute ID is not known all Attributes for this Resource or Indicator can be retrieved from the API using the [load_attributes()](/python/retrieve/loading_attributes_retrieve/#loading-attributes) method.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('Existing Re...`| Add a Resource object setting the name and Owner. 
`resource.retrieve()`                     | Trigger the API request and retrieve the Adversary intelligence data.
`resource.load_attributes()`              | Load existing Attributes.
`for attribute in resource.attributes:`   | Iterate through Attribute objects. 
`if attribute.type == 'Description':`     | Look for a **Description** Attribute. 
`resource.update_attribute(attribute.i...`| Update the **Description** Attribute.
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

##Security Label

> The following example demonstrates how to **set** a Security Label for an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('New Resource', owner)
resource.set_security_label('TLP Green')

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```
The Python SDK provides easy methods to manage Security Labels, which are supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats)   

An example of the [set](#set-security-label) and [delete](#delete-security-label) methods, as well as explanations of the code, are provided in the following section.

<b>Setting Security Labels</b>

A Security Label can be set on a Resource Group or Indicator using the `set_security_label()` method and passing the Security Label Value. Security Labels can be set while creating a new Resource or during a Resource update. The Security Label (e.g., TLP Green) must be created in the Organization prior to being added via the API. The ThreatConnect administrator can add Security Labels via the User Interface.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate an Adversaries container object. 
`resource = resources.add('New Resourc...`| Add a Resource object setting the name and Owner. 
`resource.set_security_label('TLP Green')`| Set the Security Label on the Resource. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data.

##Deleting Security Labels

> The following example demonstrates how to **delete** a Security Label for an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('New Resource', owner)
resource.delete_security_label('TLP Green')

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

A Security Label can be deleted on a Resource Group or Indicator using the `delete_security_label()` method and passing the Security Label value.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate an Adversaries container object. 
`resource = resources.add('New Resourc...`| Add a Resource object setting the name and Owner. 
`resource.delete_security_label('TLP G...`| Set the Security Label on the Resource. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Tags

> The following example demonstrates how to add a Tag on an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('New Adversary', owner)
resource.add_tag('EXAMPLE')
resource.add_tag('APT')

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

The Python SDK provides easy methods to manage Tags, which are supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats)   

An example of the [add](#adding-tag) and [delete](#deleting-tags) methods are provided in the following section as well as explanations of the code.

## Adding Tags

A Tag can be added to a Group Resource or Indicator using the `add_tag()` method and passing the Tag value. Tags can be added while creating a new Resource or during a Resource update.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id,...`    | Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('New Ads...`    | Add a Resource object setting the name and Owner. 
`resource.add_tag('EXAMPLE')`             | Add a Tag to the Resource. 
`resource.add_tag('APT')`                 | Add a Tag to the Resource. 
`resource.commit()`                       | Trigger API calls to write all added, deleted, <br> or modified data. 

##Deleting Tags

> The following example demonstrates how to delete a Tag on an Adversary Resource. For other Resource Groups and Indicators, the same method should be used:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

resources = tc.adversaries()
    
owner = 'Example Community'
resource = resources.add('Existing Resource', owner)
resource.set_id(123)
resource.delete_tag('EXAMPLE')
resource.delete_tag('APT')

try:
    resource.commit()
except RuntimeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)
```

A Tag can be deleted from a Resource using the `delete_tag()` method and passing the Tag value.

Note: In the prior example, no API calls are made until the `commit()` method is invoked.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tc = ThreatConnect(api_access_id, api...`| Instantiate the ThreatConnect object. 
`resources = tc.adversaries()`            | Instantiate a Resources container object. 
`resource = resources.add('Existing Re...`| Add a Resource object setting the name and Owner. 
`resource.set_id(123)`                    | Set the Resource ID to an existing Adversary. 
`resource.delete_tag('EXAMPLE')`          | Delete a Tag to the Resource. 
`resource.delete_tag('APT')`              | Delete a Tag to the Resource. 
`resource.commit()`                       | Trigger multiple API calls to write all added, deleted, <br> or modified data. 

##Python Advanced

<b>API Settings</b>

The Python SDK provides a few methods that affect interactions with the ThreatConnect API. The default settings should work in most cases.

###Activity Log

> Enabling the Activity Log:

```python
tc.set_activity_log(True)
```

> Disabling the Activity Log:

```python
tc.set_activity_log(False)
```

The ThreatConnect platform tracks all activity by users, including API accounts. When using the API to create thousands of Indicators, the Activity Log could generate excessive data. Activity tracing is **disabled by default** in the Python SDK. This feature can be turned on by calling the `tc.set_activity_log()` method, passing `True` as the argument. To disable tracking again during the same execution period, call the `tc.set_activity_log()` method once more, passing `False`.

###API Request Timeout

>  This timeout value can be changed by passing the new timeout value, in seconds, to the `tc.set_api_request_timeout()` method.

```python
tc.set_api_request_timeout(15)
```

The Python SDK uses the Request module for communicating to the API. To prevent script from hanging on a bad socket, there is a timeout value set to **30 seconds by default**. 

###API Retries/Sleep Period

> To change the default sleep period, call the `set_api_sleep()` method, passing an Integer for the number of seconds to sleep.

```python
tc.set_api_retries(3)
tc.set_api_sleep(30)
```

If the Python SDK loses network connectivity to the API server, it will automatically retry the connection. 

The Python SDK has a **default of 5** retries, with a **default 59-second** sleep between retries before a RunTimeError is raised. To change the default retry value, call the `set_api_retries()` method, passing an Integer for the number of retries. 

Note:  There is a maximum window of 5 minutes before the API will reject the HMAC (hash message authentication code) header due to a time mismatch.

###API Result Limit

> To change the default value, call the `set_api_result_limit()` method, passing an Integer between 1-500.

```python
tc.set_api_result_limit(500)
```

The ThreatConnect API supports a **maximum of 500** results to be returned per API call during pagination. The Python SDK is configured for a **default of 200** results per API request. To change the default value, call the `set_api_result_limit()` method, passing an Integer between 1-500. The higher the number, the less API calls will be made, but in some cases, a lower number is required due to network limitations.

###Proxies

> Proxy Setting (No Authentication)

```python
tc.set_proxies('10.10.10.10', 8443)
```

> Proxy Setting (Authentication Provided)

```python
tc.set_proxies('10.10.10.10', 8443, 'proxy_user', 'password123')
```

In some environments, the server running the Python SDK does not have the required Internet access to connect to the ThreatConnect API server. In these cases, a proxy server can be used to provide the required connectivity. To configure the Python SDK to use a proxy, call the `set_proxies()` method, providing the proxy-server IP address and port number as parameters. If the proxy server requires authentication, also provide the proxy user and proxy password as parameters.

###Filtering

> A list of Filters can also be retrieved by using the `filter1.filters` property:

```python 
owner = 'Example Community'

try:
    filter1 = adversary.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')
except AttributeError as e:
    print('Error: {0}'.format(e))
    sys.exit(1)

    print(filter1)
```

The Python SDK provides a powerful filtering system. When possible, it allows the user to set API Filters that limit the results returned from the API. If further filtering is required, there are Post Filters that allow the user to further refine the result set. The API Filters in a single Filter object will **OR** the results together, while the Post Filter will **AND** the results.

<b>Printing Filter Objects</b>

After creating a Filter object, the object can be printed, which will display the number of Request objects created, as well as the supported API Filters and Post Filters. A list of Filters can also be retrieved by using the `filter1.filters` property.

<b>filter1.filters Resulting Output</b>

| Filter Object     |                         |
|-------------------|-------------------------|
| Filter Properties |                         |
|    Operator       | FilterSetOperator.AND   |
| Request Objects   | 1                       |
|    Owners         |                         |
|    Owner          | Example Community       |
| Filters           |                         |
|    Filter         | api filter by tag "APT" |
| API Filters       |                         |
|    Filter         | add_adversary_id        |
|    Filter         | add_email_id            |
|    Filter         | add_document_id         |
|    Filter         | add_id                  |
|    Filter         | add_incident_id         |
|    Filter         | add_indicator           |
|    Filter         | add_security_label      |
|    Filter         | add_signature_id        |
|    Filter         | add_threat_id           |
|    Filter         | add_tag                 |
|    Filter         | add_victim_id           |
| Post Filters      |                         |
|    Filter         | add_pf_name             |
|    Filter         | add_pf_date_added       |


###Filter Object Basics

> Python SDK Filter Object Basics example:

```python
filter1 = adversary.add_filter()
filter1 = adversary.indicator('10.20.30.40')
filter1 = adversary.victim_id(10)
filter1 = adversary.tag('APT')
```

> Python SDK Post Filter Basics example:

```python
filter1 = adversary.add_filter()
filter1 = adversary.add_pf_name('Bad Guy')
filter1 = adversary.add_pf_date_added('2015-06-18T20:21:45-05:00', FilterOperator.GE)
```

As mentioned above, an API Filter will join the results. In the example, the API results will contain any Adversary that has an Association with the Indicator *10.20.30.40*, **OR** an Association with the Victim with an ID of *10*, **OR** has the Tag of *APT*.

As mentioned above, the Post Filters will intersect the results. In the example, the API results will only contain Adversaries that have the name *"Bad Guy"* **AND** have a date added of >= *2015-06-18T20:21:45-05:00*.

###Owner API Filter

> Python SDK formatted URI example:

```
/v2/indicators/address/10.20.30.40?owner=Example+Community
```

```
/v2/groups/adversaries/5/indicators?owner=Example+Community
```

The Owner API Filter is a special Filter that is applied to all other API Filters in the same Filter Object. This is due to the fact that the API supports adding the Owner as a query String. See the formatted URI examples below.

###Indicator-Type Filter

> Python SDK example Supported Indicator Types:

```python
filter1 = indicators.add_filter(IndicatorType.ADDRESSES)
filter1 = indicators.add_filter(IndicatorType.EMAIL_ADDRESSES)
filter1 = indicators.add_filter(IndicatorType.FILES)
filter1 = indicators.add_filter(IndicatorType.HOSTS)
filter1 = indicators.add_filter(IndicatorType.URLS)
```

An Indicator Filter object supports passing an optional IndicatorType enum argument to the `add_filter` method. This will filter all results in the Filter object to the Indicator Type specified.

| Supported Indicator Types |
|---------------------------|
| ADDRESSES                 |
| EMAIL_ADDRESSES           |
| FILES                     |
| HOSTS                     |
| URLS                      |

###Modified Since API Filter

> Python SDK Modified Since API Filter:

```python

modified_since = (datetime.isoformat(datetime(2015, 6, 17))) + 'Z'
indicators.set_modified_since(modified_since)
```

The **Modified Since** Filter applies to the entire Indicators Container but can only be used on **base** Indicator searches (e.g.,  `/v2/indicators`). If a Filter on **modified since** is required on a different Indicator search, there is a Post Filter for **modified since** that works on all Indicator result sets. 

###Multiple Filter Objects

> Python SDK Multiple Filter Objects example:

```python
owner = 'Example Community'

try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_security_label('TLP Red')
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    filter2 = indicators.add_filter()
    filter2.add_owner(owner)
    filter2.add_filter_operator(FilterSetOperator.AND)
    filter2.add_threat_id(38)
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    filter3 = indicators.add_filter(IndicatorType.ADDRESSES)
    filter3.add_owner(owner)
    filter3.add_filter_operator(FilterSetOperator.OR)
    filter3.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)
```

The Python SDK supports adding multiple Filter objects to a Resource Container. A **filter_operator** allows a user to configure the results sets of the separate Filter objects to be **JOINED** or **INTERSECTED**. No **filter_operator** is required on the first Filter object added. Each subsequent Filter object can be joined (FilterSetOperator.OR) or intersected (FilterSetOperator.AND).

##Manual API Calls

The Python SDK supports a manual way to access the API by allowing the creation of a `RequestObject()` and submitting these objects to the `api_request()` method. The returned result will be a **Python Requests** object containing the HTTP Status Code, Response Headers, and API Results.

###Retrieving Indicators

> The example below displays how to create a `RequestObject` that will retrieve all Indicators from a specified Owner:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

ro = RequestObject()
ro.set_http_method('GET')
ro.set_owner('Example Community')
ro.set_owner_allowed(True)
ro.set_resource_pagination(True)
ro.set_request_uri('/v2/indicators')

results = tc.api_request(ro)
if results.headers['content-type'] == 'application/json':
    data = results.json()
    print(json.dumps(data, indent=4))
```

The example displays how to create a `RequestObject` that will retrieve all Indicators from a specified Owner.

<b>Code Highlights</b>

Refer to [ThreatConnect API documentation](#rest-api) for proper values for the `RequestObject`.

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`ro = RequestObject()`                    | Instantiate and Instance of a Request object. 
`ro.set_http_method('GET')`               | Set the HTTP Method for the Request. 
`ro.set_owner('Example Community')`       | Set the Owner for the Request (optional). 
`ro.set_owner_allowed(True)`              | Set the Owner-Allowed flag for the Request to indicate if <br> this API call supports Owners. 
`ro.set_resource_pagination(True)`        | Set the Pagination flag for the Request to indicate if this <br> API call supports pagination. 
`ro.set_request_uri('/v2/indicators')`    | Set the URI (uniform resource identifier) for the Request. 
`results = tc.api_request(ro)`            | Trigger the API Request and store result as `results`. 

###Downloading Document Contents

> The example below displays how to create a `RequestObject` that will retrieve the contents of a document stored in a Document Resource.

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

ro = RequestObject()
ro.set_http_method('GET')
ro.set_owner('Example Community')
ro.set_owner_allowed(True)
ro.set_resource_pagination(False)
ro.set_request_uri('/v2/groups/documents/19/download')

results = tc.api_request(ro)
if results.headers['content-type'] == 'application/octet-stream':
    file_contents = results.content
    print(file_contents)
```

The example displays how to create a `RequestObject` that will retrieve the contents of a document stored in a Document Resource.

<b>Code Highlights</b>

Refer to [ThreatConnect API documentation](#rest-api) for proper values for the `RequestObject`.

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`ro = RequestObject()`                    | Instantiate and Instance of a Request object. 
`ro.set_http_method('GET')`               | Set the HTTP Method for the Request. 
`ro.set_owner('Example Community')`       | Set the Owner for the Request (optional). 
`ro.set_owner_allowed(True)`              | Set the Owner-Allowed flag for the Request to indicate if <br> this API call supports Owners. 
`ro.set_resource_pagination(True)`        | Set the Pagination flag for the Request to indicate if this <br> API call supports pagination. 
`ro.set_request_uri('/v2/indicators')`    | Set the URI for the Request. 
`results = tc.api_request(ro)`            | Trigger the API Request and store result as `results`. 

###Creating and Uploading Documents

> The example below displays how to create a `RequestObject` that will create a Document Resource in ThreatConnect and upload a file to this Resource.

```python
 
tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

ro = RequestObject()
ro.set_http_method('POST')
body = {'name': 'Raw Upload Example', 'fileName': 'raw_example.txt'}
ro.set_body(json.dumps(body))
ro.set_content_type('application/json')
ro.set_owner('Example Community')
ro.set_owner_allowed(True)
ro.set_resource_pagination(False)
ro.set_request_uri('/v2/groups/documents')

print(ro)

results = tc.api_request(ro)
if results.headers['content-type'] == 'application/json':
    data = results.json()
    print(json.dumps(data, indent=4))

    document_id = data['data']['document']['id']

    ro = RequestObject()
    ro.set_http_method('POST')
    body = 'Raw upload example file Contents.'
    ro.set_body(body)
    ro.set_content_type('application/octet-stream')
    ro.set_owner('Example Community')
    ro.set_owner_allowed(True)
    ro.set_resource_pagination(False)
    ro.set_request_uri('/v2/groups/documents/{0}/upload'.format(document_id))

    results = tc.api_request(ro)
    print('Status Code: {0}'.format(results.status_code))
```


The example displays how to create a `RequestObject` that will create a Document Resource in ThreatConnect and upload a file to this Resource.

<b>Code Highlights</b>

Refer to [ThreatConnect API documentation](#rest-api) for proper values for the `RequestObject`.

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`ro = RequestObject()`                    | Instantiate and Instance of a Request Object. 
`body = {'name': 'Raw Upload Exam...`     | Create the JSON body for POST. 
`ro.set_http_method('POST')`              | Set the HTTP Method for the Request. 
`ro.set_owner('Example Community')`       | Set the Owner for the Request (optional). 
`ro.set_owner_allowed(True)`              | Set the Owner-Allowed flag for the Request to indicate if <br> this API call supports Owners. 
`ro.set_resource_pagination(False)`       | Set the Pagination flag for the Request to indicate if this <br> API call supports pagination. 
`ro.set_request_uri('/v2/groups/doc...`   | Set the URI for the Request. 
`print(ro)`                               | Display the Request Object before submitting (optional). 
`results = tc.api_request(ro)`            | Trigger the API Request and store result as `results`. 
`document_id = data['data']['doc...`      | Get the ID of the created Document to use in the contents upload. 

###Advanced Outputs Formats

The Python SDK allows for a Resource to be returned in multiple standard formats. The SDK currently supports the following formats: CEF (Common Event Format), CSV (Comma-Separated Values), JSON (JavaScript® Object Notation) , KeyVal (Key Value), and LEEF (Log Event Extended Format).

###CEF

> Python SDK CEF Code Sample:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
owner = 'Example Community'

try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    indicators.retrieve()
except RuntimeError as e:
    print(e)
    sys.exit(1)

for indicator in indicators:
    print(indicator.cef)
```

> Python SDK Sample CEF Output:

```
CEF:0|threatconnect|threatconnect|2|355999|TEST attribute #14|2.0|confidence="14" dateAdded="2015-06-21T10:40:33-05:00" dnsActive="None" hostName="www.badguy_014.com" lastModified="2015-06-21T10:40:33-05:00" ownerName="Example Community" type="None" weblink="https://tc.sumx.us/auth/indicators/details/host.xhtml?host\=www.badguy_014.com&owner\=Example+Community" whoisActive="None"
```

The Python SDK provides the `cef` methods to output data structured in CEF, whose output is only supported on [Indicators](#indicators_commit). The CEF-formatted data maps the ThreatConnect Resource properties to the standard fields, when possible, and then uses the extension feature to store non-standard properties.

###CSV

> Python SDK CSV Code Sample:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
owner = 'Example Community'

try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    indicators.retrieve()
except RuntimeError as e:
    print(e)
    sys.exit(1)

print(indicator.csv_header)
for indicator in indicators:
    print(indicator.csv)
```

> Python SDK Sample CSV Output:

```text
{
    "confidence": 14, 
    "dateAdded": "2015-06-21T10:40:33-05:00", 
    "description": "TEST attribute #14", 
    "id": 355999,
    "indicator":"www.badguy_014.com"
    "lastModified": "2015-06-21T10:40:33-05:00", 
    "ownerName": "Example Community", 
    "rating": 1.0, 
    "type": null, 
    "weblink": "https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community", 
}
```

The Python SDK provides the `csv` and `csv_header` methods for CSV output, which are supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats)   

The `csv_header` method should normally be called once per result set.

###JSON

> Python SDK JSON Code Sample:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
owner = 'Example Community'

try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    indicators.retrieve()
except RuntimeError as e:
    print(e)
    sys.exit(1)

for indicator in indicators:
    print(indicator.json)
```

> Python SDK Sample JSON Output:

```json
{
    "confidence": 14, 
    "dateAdded": "2015-06-21T10:40:33-05:00", 
    "description": "TEST attribute #14", 
    "dnsActive": null, 
    "hostName": "www.badguy_014.com", 
    "id": 355999, 
    "lastModified": "2015-06-21T10:40:33-05:00", 
    "ownerName": "Example Community", 
    "rating": 1.0, 
    "type": null, 
    "weblink": "https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community", 
    "whoisActive": null
}
```

The Python SDK provides the `json` method for output in JSON, are supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats)   
The fields in the output depend on the type of Resource that has been requested.

###Key Value

> Python SDK Key Value Code Sample:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
owner = 'Example Community'

try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    indicators.retrieve()
except RuntimeError as e:
    print(e)
    sys.exit(1)

for indicator in indicators:
    print(indicator.keyval)
```

> Sample Key/Value Output:

```text
confidence="14" dateAdded="2015-06-21T10:40:33-05:00" description="TEST attribute #14" dnsActive="None" hostName="www.badguy_014.com" id="355999" lastModified="2015-06-21T10:40:33-05:00" ownerName="Example Community" rating="1.0" type="None" weblink="https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community" whoisActive="None" 
```

The Python SDK provides the `keyval` method for output in the Key Value format, whose output is supported on Indicators as well as Group Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures and Threats)   

The fields in the output depend on the type of Resource that has been requested.

###LEEF

> Python SDK LEEF Code Sample:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
owner = 'Example Community'

try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    indicators.retrieve()
except RuntimeError as e:
    print(e)
    sys.exit(1)

for indicator in indicators:
    print(indicator.leef)
```

> Python SDK Sample LEEF Output:

```text
LEEF:0|threatconnect|threatconnect|2|355999|confidence="14" devTime="2015-06-21T10:40:33-05:00" description="TEST attribute #14" dnsActive="None" hostName="www.badguy_014.com" id="355999" lastModified="2015-06-21T10:40:33-05:00" ownerName="Example Community" severity="1.0" type="None" weblink="https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community" whoisActive="None" 
```

The Python SDK provides the `leef` method to output data structured in LEEF, whose output is only supported on [Indicators](#indicators_commit). The LEEF-formatted data maps the ThreatConnect Resource properties to the standard fields, when possible, and then uses the custom attribute feature to store non-standard properties.

###Regex Overrides

> Python SDK Regex Code Sample

```

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

#
# override FILES Regex
#
md5_re = re.compile(r'^([a-fA-F\d]{32})$')
sha1_re = re.compile(r'^([a-fA-F\d]{40})$')
sha256_re = re.compile(r'^([a-fA-F\d]{64})$')
tc.set_indicator_regex(IndicatorType.FILES, [md5_re, sha1_re, sha256_re])

#
# override HOSTS Regex
#
host_re = re.compile(r'\b((?:(?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+(?i)(?!exe|php|dll|doc' \
    '|docx|txt|rtf|odt|xls|xlsx|ppt|pptx|bin|pcap|ioc|pdf|mdb|asp|html|xml|jpg|gif$|png' \
    '|lnk|log|vbs|lco|bat|shell|quit|pdb|vbp|bdoda|bsspx|save|cpl|wav|tmp|close|ico|ini' \
    '|sleep|run|dat$|scr|jar|jxr|apt|w32|css|js|xpi|class|apk|rar|zip|hlp|tmp|cpp|crl' \
    '|cfg|cer|plg|tmp|lxdns|cgi|xn$)(?:xn--[a-zA-Z0-9]{2,22}|[a-zA-Z]{2,13}))(?:\s|$)')
tc.set_indicator_regex(IndicatorType.HOSTS, host_re)

indicator = indicators.add('new.domain.tld', owner)
indicator.set_confidence(50)
indicator.set_rating('2.0')

try:
    indicator.commit()
except RuntimeError as e:
    print('Error: {0!s}'.format(e))
    sys.exit(1))
```

The Python SDK provides the `set_indicator_regex` method which allows a user to override the baked-in Regular Expressions (Regex) in the SDK with user defined compiled Regexes. The method takes an IndicatorType enum and either a single compiled Regex or a list of Regexes. If a list is provided each Regex will be checked for a match for that Indicator Type.

###Reporting

> The `tc.report.stats` properties method provides an overview of the script results:

```python

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

indicators = tc.indicators()
owner = 'Example Community'

try:
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('EXAMPLE')
except AttributeError as e:
    print(e)
    sys.exit(1)

try:
    indicators.retrieve()
    


print(tc.report.stats)
```

> Sample Report-Statistics Output:

```text
_Stats_

API Stats                               
  API Calls                    32                                                
  Unfiltered Results           3                                                 
  Filtered Results             3                                                 

Filters                                 
  API Filters                  1                                                 
  Post Filters                 0                                                 
  Total Filters                1                                                 

HTTP Methods                            
  PUT                          2                                                 
  POST                         11                                                
  DELETE                       11                                                
  GET                          8                                                 

Status Codes                            
  200                          21                                                
  201                          11                                                

Performance Stats                       
  Request Time           0:00:03.021702                                    
  Processing Time        0:00:00.014082                                    
  Run Time               0:00:03.035795     
```

The Python SDK includes a reporting feature that provides a number of methods for reporting on the execution status of a script that uses the SDK.

<b>Enabling Reporting</b>

The basic data collection of the Reporting feature is always enabled, but the report-entry collection feature is disabled by default. To enable the report-entry collection feature, use the `tc.report_enable()` method. To disable reporting, use the `tc.report_disable()` method.

<b>Statistics</b>

The `tc.report.stats` properties method provides an overview of the script results.

###Failed Reports

> Python SDK failed reports example:

```python

for fail in tc.report.failures:
    print(fail)
```

> Sample Failed-Report Output:

```text
_Report Entry_

Properties                              
Status Code
: 404                                               
Fail Msg
: {"status":"Failure","message":"The requested resource was not found"}
Description
: api filter by incident id 708996                  
Resource Type
: ResourceType.ADVERSARIES                          

HTTP Settings                           
  HTTP Method                 
  GET                                               
  Request URI
  /v2/groups/incidents/708996/groups/adversaries    
  Request URL
  https://tc.sumx.us/api/v2/groups/incidents/708996/groups/adversaries?resultStart=0&resultLimit=500&createActivityLog=false
  Content Type                 None                                              
  Body                         None                                              

Payload                                 
  Payload
  {'resultStart': 0, 'resultLimit': 500, 'createActivityLog': 'false'}
```

All API requests and Post Filters are stored as a report entry in the Reports object. Any request that does not receive a status code of 200, 201 or 202, is stored as a failed-report entry and can be retrieved with the `tc.report.failures` property method. This feature helps debug issues when receiving failures while communicating with the API.

###Other Reporting Features

<b>API Calls</b>

The number of API calls can be retrieved using the `tc.report.api_calls` property method of the Report object.

<b>Runtime</b>

The script execution time can be retrieved using the `tc.report.runtime` property method of the Report object. This method can be called anytime during the script execution to get the current runtime and at the end of the script to get the total runtime.

<b>Request Time</b>

The time spent on API requests can be retrieved using the `tc.report.request_time` property method of the Report object.

<b>Report Entries</b>

All report entries can be accessed via the Report generator. By iterating over `tc.report`, each individual report entry will be returned. These report entries can be printed and the individual properties can be accessed.

# Java Library

> The following is a code sample with line numbers syntax highlighting:

```java
  1     private static void doCreate(Connection conn) {
  2         AbstractGroupWriterAdapter<Adversary> writer WriterAdapterFactory.createAdversaryGroupWriter(conn);
  3         
  4         Adversary adversary = new Adversary();
  5         adversary.setName("Test Adversary");
  6         adversary.setOwnerName("System");
  7         
  8         try {
  9             Adversary savedAdversary = writer.create(adversary);
 10             System.out.println("Saved: " + savedAdversary.toString() );
 11             
 12         } catch (IOException | FailedResponseException ex) {
 13             System.err.println("Error: " + ex.toString()); 
 14         }   
 15         
 16     }   
```

<b>About This Document</b>

This guide details the process of coding Java applications utilizing the ThreatConnect API. The Java SDK offers coverage of all features in version 2.0 of the ThreatConnect API—including the ability to write data to ThreatConnect. This document will provide an overview of the reference implementation of the Java SDK for ThreatConnect. 

The goal of this Java SDK library is to provide a programmatic abstraction layer around the ThreatConnect API without losing functional coverage over the available API resources. This abstraction layer enables developers to focus on writing enterprise functionality without worrying about low-level RESTful calls and authentication management.

This document is not a replacement for the official ThreatConnect API User Guide. This document serves as a companion to the official documentation for the REST API. Read the official documentation to gain a further understanding of the functional aspects of using the ThreatConnect API.

<b>How to Use This Document</b>

This document explains how to create groups, indicators, associations, tags, security labels, and victims—as well as how to create, update, delete, and request data from the API using Java; thus, knowledge of the Java programming Language is a prerequisite.

All code examples will be noted  in a separate box with a monospaced font and line numbers to facilitate explanation of code functionality. 

## Getting Started with Java SDK

* Install [Java JDK 7+](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
* Import [Java SDK for ThreatConnect](https://github.com/ThreatConnect-Inc/threatconnect-java)
* Create an API User, refer to [REST API documentation](#rest-api)

###Maven™ Configuration

> Add the following entries to your POM (project object model) file. This is the preferred method to use the SDK:

```xml
   <properties>
        <threatconnect-sdk.version>2.0.3</threatconnect-sdk.version>
    </properties>


<!-- repository entry -->
  <repositories>
      <repository>
          <id>threatconnect-java-mvn-repo</id>
         <url>https://raw.github.com/ThreatConnect-Inc/threatconnect-java/mvn-repo-${threatconnect-sdk.version}/</url>
           <snapshots>
              <enabled>true</enabled>
              <updatePolicy>always</updatePolicy>
          </snapshots>
      </repository>
  </repositories>


<!-- sdk dependency -->
    <dependencies>
        <dependency>
            <groupId>com.threatconnect.sdk</groupId>
            <artifactId>threatconnect-sdk</artifactId>
            <version>${threatconnect-sdk.version}</version>
         </dependency>
    </dependencies>
```

###Programmatic Configuration 

> To connect to the API using the SDK, create a Configuration object with one of the following constructors:

```java
   public Configuration(String tcApiUrl, String tcApiAccessID, String tcApiUserSecretKey, String defaultOwner);
   public Configuration(String tcApiUrl, String tcApiAccessID, String tcApiUserSecretKey, String defaultOwner, Integer resultLimit);
```

Pass the `Configuration` object when creating a new `Connection`. (See examples in the Reader and Writer sections.)

### Configuration using Properties

> This property can be defined in two ways:

> In the JVM (Java virtual machine), you can call your program with the following -D property flag:

`threatconnect.api.config=<YOUR CONFIG FILE LOCATION>`

> Or the system property can be directly set at runtime using the following code:

```java
System.getProperties().setProperty("threatconnect.api.config", "<YOUR CONFIG FILE LOCATION>");
```

> Once the configuration has been set up, the examples in this document should be executable, as long as the Java SDK for ThreatConnect is part of the classpath. See the following examples for a typical start-up script.

> On Windows:

```shell
 java -cp ".;threatconnect-sdk-<version>.jar" -Dthreatconnect.api.config=myConfig.properties TestClass
```

> On Linux:

```shell
java -cp ".:./threatconnect-sdk-<version>.jar" -Dthreatconnect.api.config=myConfig.properties TestClass
```

The Java SDK will need to be configured with an Access ID and Secret Key. When a no-arg `Configuration` constructor is called, the SDK searches system properties for the "threatconnect.api.config" property. 

The configuration file should contain the following lines at a minimum:

`connection.tcApiUrl=https://api.threatconnect.com`

`connection.tcApiAccessID=<YOUR API ACCESS ID>`

`connection.tcApiUserSecretKey=<YOUR API SECRET KEY>`

<b>Third-Party Dependencies</b>

The SDK utilizes these open-source libraries primarily for RESTful communication and JSON (JavaScript Object Notation) parsing.

Library | Version | Used by 
--------| ------- | ------- 
HTTP Core | 4.4.1 | SDK 
HTTP Client | 4.4.1 | SDK 
↪ Commons Logging | 1.2 | HTTP Client 
↪ Commons Codec | 1.9 | HTTP Client 
Jackson Core| 2.5.3 | SDK 
Jackson Databind| 2.5.3 | SDK 
↪ Jackson Annotation| 2.5.0 | Jackson Databind 

<b>Technical Design</b>

The Java SDK for ThreatConnect was designed with a focus on abstracting the API REST calls while enabling the developer to use an enterprise-level programming language. The abstraction layer is relatively "thin" because it coincides directly with all of the REST API calls. In fact, the entities themselves were ported directly from the ThreatConnect API to enable consistent communication between the Java SDK and the REST API.

![SDK Design](images/sdk-design.png "SDK Technical Design") 

The Java library was designed with common programming design patterns. You’ll notice the "Adapter" pattern used to manage the interaction with the API connection and REST calls. The Java SDK depends on the Apache HTTP components open-source library to handle these calls. Because instantiating an Adapter requires a low-level RequestExecutor, a "Factory" design pattern was utilized to expose reading/writing functionality in a simplified way. 

Java generics are used to type many of the Adapters in an effort to reuse code, as most readers share functional resources. Below is a diagram that will help illustrate common interactions between different classes (Note: Names are conceptual to illustrate interaction. Actual class names and methods will be discussed later in this document) . All  interactions with the Java SDK will follow this programmatic idiom. 

![SDK Architecture](images/sdk-arch.png "SDK Architecture") 

> To facilitate interaction with the full set of Java SDK readers and writers, the use of ReaderAdapterFactory and WriterAdapterFactory, respectively, is highly recommended.

## Example Java App

> Once retrieved, the adversary objects will be printed to the console.

```java
  1 import com.cyber2.api.lib.client.reader.AbstractGroupReaderAdapter;
  2 import com.cyber2.api.lib.client.reader.ReaderAdapterFactory;
  3 import com.cyber2.api.lib.conn.Connection;
  4 import com.cyber2.api.lib.exception.FailedResponseException;
  5 import com.cyber2.api.lib.server.entity.Adversary;
  6 import java.io.IOException;
  7 import java.util.List;
  8 
  9 public class GroupExample {
 10 
 11     public static void main(String[] args) {
 12     
 13         Connection conn = null;
 14         
 15         try {
 16             
 17             System.getProperties().setProperty("threatconnect.api.config", "/config.properties");
 18             conn = new Connection();
 19             
 20             AbstractGroupReaderAdapter<Adversary> reader = ReaderAdapterFactory.createAdversaryGroupReader(conn);
 21             List<Adversary> data = reader.getAll("System");
 22             for (Adversary g : data ) {
 23                 System.out.println( "Adversary: " + g.toString() );
 24             }   
 25             
 26         } catch (IOException | FailedResponseException ex) {
 27             System.err.println("Error: " + ex);
 28         } finally {
 29             if ( conn != null )     conn.disconnect();
 30         }   
 31         
 32     }   
 33     
 34 }   
```

To write the first program using the Java SDK for the ThreatConnect API, an Adversary reader that pulls all adversaries belonging to the "System" Organization must be created. 

Line         | Description                                                     
------------ | --------------------------------------------------------------- 
1-7          | Notable imports include:<br>The `com.cyber2.api.lib.client.reader` package holds all Adapter classes that read<br>data from the API. The `com.cyber2.api.lib.server.entity` package holds all entities <br>returned by the Java SDK. 
17-18        | The platform programmatically define the system property to load the configuration file.<br>This allows the developer to instantiate Connection objects (line 18) with a <br>no-arg constructor. If the `threatconnect.api.config` property is not defined, <br>the developer has the option of passing the configuration file name string in the <br>single-arg Connection constructor.
20           | To create an AbstractGroupReaderAdapter<Adversary> object: Use the<br>ReaderAdapterFactory pattern and generics to enforce compile-time type constraints <br>on this abstract class. Then pass the connection object used by the Adapter to <br>interact with the ThreatConnect API.
21           | Using the reader object, call `getAll()` method and pass it the Organization <br>string name to return all Adversaries for the "System" Organization.
22-24        | Iterate through the data collection to print the contents to the console.
26           | The IOException is potentially thrown if the Connection object cannot find the <br>properties file. The FailedResponseException is thrown if the API request is invalid.
29           | In all cases when processing is complete, call `disconnect()` on the connection <br>object to release resources.

<b>Summary</b>

This section explained:

* How to connect to the ThreatConnect API by passing the configuration file in system properties
* How to get a list of adversaries for the "System" Organization
* What types of exceptions a connection and read operation can potentially throw
* How to close a ThreatConnect API connection

##Deploying a Java App
Apps must be packaged and deployed into ThreatConnect's application runtime environment.

[Example Applications](https://github.com/ThreatConnect-Inc/threatconnect-java/tree/master/threatconnect-sdk-core/src/main/java/com/threatconnect/sdk/examples) 

<b>Supported Version</b>

ThreatConnect Java integrations require Oracle JRE 7 or later. OpenJRE is not supported.

<b>Third-Party Libraries</b>

These libraries are automatically included in the classpath of every Java app. There is no need to include these libraries in the installation zip file. There is also no need to include these libraries in the `configuration` variable named `java.classpath`.

Library | Version 
--------| ------- 
[ThreatConnect SDK](https://github.com/ThreatConnect-Inc/threatconnect-java) | 2.0.0 
[HTTP Core](https://hc.apache.org/httpcomponents-core-ga/) | 4.4.1 | 
[HTTP Client](https://hc.apache.org/httpcomponents-client-ga/) | 4.4.1 |
[Commons Logging](http://commons.apache.org/proper/commons-logging/) | 1.2 |
[Commons Codec](https://commons.apache.org/proper/commons-codec/) | 1.9 | 
[Jackson Core](https://github.com/FasterXML/jackson-core) | 2.5.3 | 
[Jackson Databind](https://github.com/FasterXML/jackson-databind/) | 2.5.3 | 
[Jackson Annotation](https://github.com/FasterXML/jackson-annotations) | 2.5.0 | 

### Deployment Configuration
[Apps use a deployment configuration file to define variables and execution environment](#deployment-configuration-file)

## Command-Line Parameters

The application runtime environment passes standard parameters to all jobs as part of its standard sandbox container. There should be no assumptions made on the naming or existence of paths passed in these variables outside of the lifetime of the job execution. Because all job executions are run in a sandboxed environment, app developers should never hard-code ThreatConnect Parameters.

ThreatConnect Parameter | Description                                                           
-------------- | --------------------------------------------------------------------- 
`tc_log_path`  | Log path for the specific instance of the job execution.               
`tc_tmp_path`  | Temporary storage path for the specific instance of the<br>job execution. 
`tc_out_path`  | Output path for the specific instance of the job execution.            
`tc_api_path`  | Path to the ThreatConnect API server.                                  

### Job Results

Job executions can use a special file called `results.tc` to write results as a mechanism for updating parameters for subsequent runs. A use case for this feature is an app that needs to know the last time it completed successfully in order to process data since that completion. The parameter definitions are quite flexible, with the only restriction being that the parameters written to the `results.tc` file must exist in the `configuration` file in order to be persisted.

Example `results.tc` file:

`param.last_completed_time = 1430619556`

Assuming there is a property with the same name in `configuration`, the job executor will update the new property value in the system for the next run. The property will only be stored if the job execution is successful. This file should be written to the `tc_out_path` passed as one of the standard ThreatConnect parameters.

###Exit Codes

There are standard exit codes that the application runtime environment uses to report whether a program completed successfully. The Java app is responsible for calling `System.exit(N)`, where 'N' is the appropriate exit code highlighted below:

When `System.exit()` is not called by the app, an exit code of zero is returned by default during normal code execution. System-critical errors (e.g., file not found) return non-zero exit codes. The developer is responsible for catching and handling program errors accordingly.

At times a program may want to report a partial failure (e.g., batch process where X out of Y updates completed). In cases of partial failure, the system administrator can retrieve the log file for that job execution and view more detailed output from the program run.

The contents of message.tc are typically written any time the program exits normally or through an error:

Status          | Description                                                    
--------------- | -------------------------------------------------------------- 
Success         | Exit code 0 - Process completed successfully.                   
Partial Failure | Exit code 3 - Process had a partial failure.                    
Failure         | Any value not 0 or 3 (typically Exit code 1) - Process failed.  

###Exit Message File

Exit codes provide a mechanism to report status at a high level. For more granular control of the exit message displayed to the user, the app can write a message to the `tc_out_path` directory under the file named `message.tc`. All content in this file should be limited to 255 characters or less. The job executor reads this file after execution completes on each job and displays the contents in the Job table detail tip.

![Exit Message](images/exit-message-tip.png "Exit Message")

##The Reader Package

The Reader package is the primary package to retrieve data from the ThreatConnect API. It covers all available resources exposed through the ThreatConnect API. The primary classes in the Reader Package, which encompass all read functionality from the API, are listed below.

|Class<br>_Description_| 
|-----------------------------------------------------------------| 
|`ReaderAdapterFactory`<br>Primary entry point to instantiate all readers in the Reader Package.| 
|`AbstractGroupReaderAdapter<T extends Group>`<br>Generic Group Reader Abstract class. Concrete object available in ReaderAdapterFactory.| 
|`AbstractIndicatorReaderAdapter<T extends Indicator>`<br>Generic Indicator Reader Abstract class. Concrete object available in ReaderAdapterFactory.| 
|`AbstractReaderAdapter`<br>Base Abstract Reader for all Reader Adapters in the Reader Package.| 
|`OwnerReaderAdapter`<br>Concrete Reader for Organization owner data. Convenience object available in<br>ReaderAdapterFactory.| 
|`SecurityLabelReaderAdapter`<br>Concrete Reader for SecurityLabel data. Convenience object available in ReaderAdapterFactory.| 
|`TagReaderAdapter`<br>Concrete Reader for Tag data. Convenience object available in ReaderAdapterFactory.| 
|`TaskReaderAdapter`<br>Concrete Reader for Task data. Convenience object available in ReaderAdapterFactory.| 
|`VictimReaderAdapter`<br>Concrete Reader for Victim data. Convenience object available in ReaderAdapterFactory.| 

###Reader Factory

The ReaderAdapterFactory class is, effectively, the "hub" for reader Adapters. It provides convenience objects for all the Adapters in the Reader Package. Below is a list of the static methods and return types of the ReaderAdapterFactory:

|Type<br>_Method_|                                                                 
|------------------------------------------------------| 
|`static AbstractGroupReaderAdapter<Adversary>`<br>createAdversaryGroupReader(Connection conn)|                          
|`static AbstractGroupReaderAdapter<Email>`<br>createEmailGroupReader(Connection conn)|                              
|`static AbstractGroupReaderAdapter<Incident>`<br>createIncidentGroupReader(Connection conn)|                             
|`static AbstractGroupReaderAdapter<Signature>`<br>createSignatureGroupReader(Connection conn)|                            
|`static AbstractGroupReaderAdapter<Threat>`<br>createThreatGroupReader(Connection conn)|                               
|`static AbstractIndicatorReaderAdapter<Address>`<br>createAddressIndicatorReader(Connection conn)|                          
|`static AbstractIndicatorReaderAdapter<EmailAddress>`<br>createEmailAddressIndicatorReader(Connection conn)|                     
|`static AbstractIndicatorReaderAdapter<File>`<br>createFileIndicatorReader(Connection conn)|                             
|`static AbstractIndicatorReaderAdapter<Host>`<br>createHostIndicatorReader(Connection conn)|                             
|`static AbstractIndicatorReaderAdapter<Url>`<br>createUrlIndicatorReader(Connection conn)|                              
|`static BatchReaderAdapter<Indicator>`<br>createIndicatorBatchReader(Connection conn)|                           
|`static DocumentReaderAdapter`<br>createDocumentReader(Connection conn)|        
|`static OwnerReaderAdapter`<br>createOwnerReader(Connection conn)|                                     
|`static SecurityLabelReaderAdapter`<br>createSecurityLabelReader(Connection conn)|                             
|`static TagReaderAdapter`<br>createTagReader(Connection conn)|  
|`static TaskReaderAdapter`<br>createTaskReader(Connection conn)|   
|`static VictimReaderAdapter`<br>createVictimReader(Connection conn)|                                    

###Reader Factory Example

```java
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
```

This example continues building from the first one and uses more Adapters available in the Reader Package. The following example reads all Groups available to the "System" Organization. It then proceeds to iterate through each Group, printing and performing "getById()" lookups to get the full Group object from the ThreatConnect API. (Note: An ellipsis (...) has been substituted for code sections removed for brevity.)

There are more concise ways of handling reading data and purely checking its ID. This code is written in a more verbose form strictly to illustrate the usage of different methods in the ReaderFactory.

Line            | Description                                                                                                  
--------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------
5-10            | Notice how all Group-level entities in the imports are added. Results from<br>reader Adapters will return an entity or a collection of entities from the<br>`com.threatconnect.sdk.server.entity` package. 
52-53           | Groups to which the current API user has access under the "System" Organization<br>should be retrieved. All AbstractGroupReaderAdapter’s have access to the<br>`getAllGroups()` method—it returns a collection of Group objects for the<br>"System" Organization from the ThreatConnect API.
60              | To illustrate the different instantiations, a switch statement on the generic<br>Group object is used. 
61-63           | Based on the Group.Type enum value (in this section, "Adversary"), an<br>AdversaryGroupReader object is created from the ReaderAdapterFactory. <br>The assignment to the adversaryReader variable is typed using generics to enforce<br>compile time checks on the data returned from this reader.
65              | The `getById()` method to retrieve the proper Adversary Group data, based on the<br>ID and Organization name, from the ThreatConnect API, is used here. The<br>`result` variable is assigned an Adversary-type object. 
67-90           | The remaining case statement blocks will check for different Group types, but,<br>effectively, does the same operation. Take some time to review these blocks<br>to understand how the ReaderFactory facilitates the creation of proper readers.
96              | Here the Group ID is compared against the result ID returned by the `getById`<br>method to assert that they are, in fact, the same entity.

###IterableResponse Class

> Using this iterable, the developer can utilize traditional `iterator()` methods to iterate through the results, or, more concisely, the Java for each loop is as follows:

```java
    IterableResponse<Address> data = reader.getAll();
    for(Address a : data) {
       System.out.println("Address: " + a); 
    }
```

In the previous example, the `IterableResponse` class retrieves all Groups for the default owner. The `IterableResponse` class is the primary type returned by all collection-based reader operations. Typically, a collection, like a `List`, would be expected in this scenario, but to resolve the paging limits of the ThreatConnect API, the `IterableResponse` was created. 

All paging is performed behind the scenes, allowing the developer to rely on an Iterable to fulfill its contract and return a `hasNext()` of false when there are no more results. The Iterable will make use of the `resultLimit` value defined during the creation of the `Configuration` object.

##Reader Class Overview

While the main entry point to the Reader Package is the ReaderFactory, getting familiar with the main Adapters helps developers understand how to interact with the data returning from the ThreatConnect API. Although there is extensive use of Java Generics, the method-naming conventions will be familiar and self-explanatory. Parameter naming conventions have been kept abstract to more accurately reflect the identifiers being passed.

###Parameter Naming Convention

Type                | Description                            
------------------- | --------------------------------- 
`uniqueId`            | Identifier for the reader/writer Group or Incident Adapter type.<br>For Groups, this is an Integer that requires an Adversary ID, Email ID,<br>Incident ID, Signature ID, or Threat ID. This identifier is system generated<br>when the group is created in ThreatConnect.<br>For Indicators, this is a String that requires an IP Address,<br>Email Address, File Hash, Host Name, or URL text.<br>This identifier is user generated when the Indicator is created<br>in ThreatConnect.
`victimId`            | Identifier for the Victim Adapter type. This identifier is an Integer created<br>by the system when the Victim entry is created in ThreatConnect.
`assetId`             | Identifier for the VictimAsset Adapter type. This identifier is an Integer created<br>by the system when the VictimAsset is created in ThreatConnect.<br>This identifier represents a VictimEmailAddress ID,<br>VictimNetworkAccount ID, VictimPhone ID, VictimSocialNetwork ID,<br>or VictimWebsite ID.
`securityLabel`       | Identifier for SecurityLabel Adapter type. This is a user-provided String that<br>represents the Security Label.
`tagName`             | Identifier for Iag Adapter type. This is a user-provided String that<br>represents the Tag.

The AbstractGroupReaderAdapter is the object returned when GroupReader is called from the ReaderFactory. These GroupReader instantiations were reviewed in the last example.

The Java SDK library for ThreatConnect comes with JavaDocs in the "apidocs" directory, which is an additional reference to the Java SDK.

###Filtering

> Example filter usage:

```java
IterableResponse<Url> urls 
  = urlReader.getForFilters("System", // owners
                             true,                              // OR filters 
                             ApiFilterType.filterConfidence()   // filter:
                                          .greaterThan(50),     // confidence > 50
                             ApiFilterType.filterRating()       // filter:
                                          .greaterThan(2.5));   // rating > 2.5
```

`ApiFilterType`exposes a builder pattern that can be used to build filters for indicators, groups, documents, tags, and victims.  
Filters can be passed to the `getForFilters(...)` method in the `AbstractBaseReader` class. 

###AbstractGroupReaderAdapter 

The methods below get data for the Group type (T) linked to this Adapter. The uniqueId (P) for Groups is an Integer.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`T`<br>getById(P uniqueId)              |     
|`T`<br>getById(P uniqueId, String ownerName)| 
|`IterableResponse<T>`<br>getForFilters(String ownerName, boolean orParams, ApiFilterType...filters) |                             
|`IterableResponse<T>`<br>getAll()  |                            
|`IterableResponse<T>`<br>getAll(String ownerName)|              

The methods below get generic Group objects associated to this Group type (T).

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<Group>`<br>getAllGroups()                        |
|`IterableResponse<Group>`<br>getAllGroups(String ownerName)        |
|`String`<br>getAllGroupsAsText()                  |

###Associated Groups

The methods below get associated Group elements by distinct type.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<Group>`<br>getAssociatedGroups(Integer uniqueId) |
|`IterableResponse<Group>`<br>getAssociatedGroups(Integer uniqueId, String ownerName) |
|`IterableResponse<Adversary>`<br>getAssociatedGroupAdversaries(Integer uniqueId) |
|`IterableResponse<Adversary>`<br>getAssociatedGroupAdversaries(Integer uniqueId, String ownerName) |
|`Adversary`<br>getAssociatedGroupAdversary(Integer uniqueId, Integer adversaryId) |
|`Adversary`<br>getAssociatedGroupAdversary(Integer uniqueId, Integer adversaryId, String ownerName) |
|`IterableResponse<Email>`<br>getAssociatedGroupEmails(Integer uniqueId) |
|`IterableResponse<Email>`<br>getAssociatedGroupEmails(Integer uniqueId, String ownerName) |
|`Email`<br>getAssociatedGroupEmail(Integer uniqueId, Integer emailId) |
|`Email`<br>getAssociatedGroupEmail(Integer uniqueId, Integer emailId, String ownerName) |
|`IterableResponse<Incident>`<br>getAssociatedGroupIncidents(Integer uniqueId) |
|`IterableResponse<Incident>`<br>getAssociatedGroupIncidents(Integer uniqueId, String ownerName) |
|`Incident`<br>getAssociatedGroupIncident(Integer uniqueId, Integer incidentId) |
|`Incident`<br>getAssociatedGroupIncident(Integer uniqueId, Integer incidentId, String ownerName) |
|`IterableResponse<Signature>`<br>getAssociatedGroupSignatures(Integer uniqueId) |
|`IterableResponse<Signature>`<br>getAssociatedGroupSignatures(Integer uniqueId, String ownerName) |
|`Signature`<br>getAssociatedGroupSignature(Integer uniqueId, Integer signatureId) |
|`Signature`<br>getAssociatedGroupSignature(Integer uniqueId, Integer signatureId, String ownerName) |
|`IterableResponse<Threat>`<br>getAssociatedGroupThreats(Integer uniqueId) |
|`IterableResponse<Threat>`<br>getAssociatedGroupThreats(Integer uniqueId, String ownerName) |
|`Threat`<br>getAssociatedGroupThreat(Integer uniqueId, Integer threatId) |
|`Threat`<br>getAssociatedGroupThreat(Integer uniqueId, Integer threatId, String ownerName) |

###Associated Indicators

The methods below get associated Indicator elements by distinct types.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<Indicator>`<br>getAssociatedIndicators(Integer uniqueId) |
|`IterableResponse<Indicator>`<br>getAssociatedIndicators(Integer uniqueId, String ownerName) |
|`IterableResponse<Address>`<br>getAssociatedIndicatorAddresses(Integer uniqueId) |
|`IterableResponse<Address>`<br>getAssociatedIndicatorAddresses(Integer uniqueId, String ownerName) |
|`Address`<br>getAssociatedIndicatorAddress(Integer uniqueId, String ipAddress) |
|`Address`<br>getAssociatedIndicatorAddress(Integer uniqueId, String ipAddress, String ownerName) |
|`IterableResponse<Email>`<br>getAssociatedIndicatorEmails(Integer uniqueId) |
|`IterableResponse<Email>`<br>getAssociatedIndicatorEmails(Integer uniqueId, String ownerName) |
|`Email`<br>getAssociatedIndicatorEmail(Integer uniqueId, String emailAddress) |
|`Email`<br>getAssociatedIndicatorEmail(Integer uniqueId, String emailAddress, String ownerName) |
|`IterableResponse<File>`<br>getAssociatedIndicatorFiles(Integer uniqueId) |
|`IterableResponse<File>`<br>getAssociatedIndicatorFiles(Integer uniqueId, String ownerName) |
|`File`<br>getAssociatedIndicatorFile(Integer uniqueId, String fileHash) |
|`IterableResponse<Host>`<br>getAssociatedIndicatorHosts(Integer uniqueId) |
|`IterableResponse<Host>`<br>getAssociatedIndicatorHosts(Integer uniqueId, String ownerName) |
|`Host`<br>getAssociatedIndicatorHost(Integer uniqueId, String hostName) |
|`Host`<br>getAssociatedIndicatorHost(Integer uniqueId, String hostName, String ownerName) |
|`IterableResponse<Url>`<br>getAssociatedIndicatorUrls(Integer uniqueId) |
|`IterableResponse<Url>`<br>getAssociatedIndicatorUrls(Integer uniqueId, String ownerName) |
|`Url`<br>getAssociatedIndicatorUrl(Integer uniqueId, String urlText) |
|`Url`<br>getAssociatedIndicatorUrl(Integer uniqueId, String urlText, String ownerName) |

###Associated Security Labels

The methods below get associated SecurityLabel data elements.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<SecurityLabel>`<br>getAssociatedSecurityLabels(Integer uniqueId) |
|`IterableResponse<SecurityLabel>`<br>getAssociatedSecurityLabels(Integer uniqueId, String ownerName) |
|`SecurityLabel`<br>getAssociatedSecurityLabel(Integer uniqueId, String securityLabel) |
|`SecurityLabel`<br>getAssociatedSecurityLabel(Integer uniqueId, String securityLabel, String ownerName) |

###Associated Tags

The methods below get associated Tag data elements.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<Tag>`<br>getAssociatedTags(Integer uniqueId) |
|`IterableResponse<Tag>`<br>getAssociatedTags(Integer uniqueId, String ownerName) |
|`Tag`<br>getAssociatedTag(Integer uniqueId, String tagName) |
|`Tag`<br>getAssociatedTag(Integer uniqueId, String tagName, String ownerName) |

###Associated VictimAssets

The methods below get associated VictimAsset data elements.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<VictimAsset>`<br>getAssociatedVictimAssets(Integer uniqueId) |
|`IterableResponse<VictimAsset>`<br>getAssociatedVictimAssets(Integer uniqueId, String ownerName) |
|`IterableResponse<VictimEmailAddress>`<br>getAssociatedVictimAssetEmailAddresses(Integer uniqueId) |
|`IterableResponse<VictimEmailAddress>`<br>getAssociatedVictimAssetEmailAddresses(Integer uniqueId, String ownerName) |
|`VictimEmailAddress`<br>getAssociatedVictimAssetEmailAddress(Integer uniqueId, Integer assetId) |
|`VictimEmailAddress`<br>getAssociatedVictimAssetEmailAddress(Integer uniqueId, Integer assetId, String ownerName) |
|`IterableResponse<VictimNetworkAccount>`<br>getAssociatedVictimAssetNetworkAccounts(Integer uniqueId) |
|`IterableResponse<VictimNetworkAccount>`<br>getAssociatedVictimAssetNetworkAccounts(Integer uniqueId, String ownerName) |
|`VictimNetworkAccount`<br>getAssociatedVictimAssetNetworkAccount(Integer uniqueId, Integer assetId) |
|`VictimNetworkAccount`<br>getAssociatedVictimAssetNetworkAccount(Integer uniqueId, Integer assetId, String ownerName) |
|`IterableResponse<VictimPhone>`<br>getAssociatedVictimAssetPhoneNumbers(Integer uniqueId) |
|`IterableResponse<VictimPhone>`<br>getAssociatedVictimAssetPhoneNumbers(Integer uniqueId, String ownerName) |
|`VictimPhone`<br>getAssociatedVictimAssetPhoneNumber(Integer uniqueId, Integer assetId) |
|`VictimPhone`<br>getAssociatedVictimAssetPhoneNumber(Integer uniqueId, Integer assetId, String ownerName) |
|`IterableResponse<VictimSocialNetwork>`<br>getAssociatedVictimAssetSocialNetworks(Integer uniqueId) |
|`IterableResponse<VictimSocialNetwork>`<br>getAssociatedVictimAssetSocialNetworks(Integer uniqueId, String ownerName) |
|`VictimSocialNetwork`<br>getAssociatedVictimAssetSocialNetwork(Integer uniqueId, Integer assetId) |
|`VictimSocialNetwork`<br>getAssociatedVictimAssetSocialNetwork(Integer uniqueId, Integer assetId, String ownerName) |
|`IterableResponse<VictimWebSite>`<br>getAssociatedVictimAssetWebsites(Integer uniqueId) |
|`IterableResponse<VictimWebSite>`<br>getAssociatedVictimAssetWebsites(Integer uniqueId, String ownerName) |
|`VictimWebSite`<br>getAssociatedVictimAssetWebsite(Integer uniqueId, Integer assetId) |
|`VictimWebSite`<br>getAssociatedVictimAssetWebsite(Integer uniqueId, Integer assetId, String ownerName) |

###Associated Attributes

The methods below get Attributes and Attribute SecurityLabels for this Group type.

|Type<br>_Method_                                |
|------------------------------------------------------- |
|`IterableResponse<Attribute>`<br>getAttributes(Integer uniqueId) |
|`IterableResponse<Attribute>`<br>getAttributes(Integer uniqueId, String ownerName) |
|`Attribute`<br>getAttribute(Integer uniqueId, Integer attributeId) |
|`Attribute`<br>getAttribute(Integer uniqueId, Integer attributeId, String ownerName) |
|`IterableResponse<SecurityLabel>`<br>getAttributeSecurityLabels(Integer uniqueId, Integer attributeId) |
|`IterableResponse<SecurityLabel>`<br>getAttributeSecurityLabels(Integer uniqueId, Integer attributeId, String ownerName) |
|`SecurityLabel`<br>getAttributeSecurityLabel(Integer uniqueId, Integer attributeId, String securityLabel) |
|`SecurityLabel`<br>getAttributeSecurityLabel(Integer uniqueId, Integer attributeId, String securityLabel, String ownerName) |

###AbstractIndicatorReaderAdapter

AbstractIndicatorReaderAdapter and AbstractGroupReaderAdapter share many of the association actions. Indicators share the ability to associate Groups, Indicators, SecurityLabels, Tags, VictimAssets, and Attributes. The listings below are some distinctions or subtle differences.

All Indicators in the ThreatConnect API have a uniqueId data type of "String". This identifier is provided by each Organization in the form of an Email Address, IP Address, File Hash, Host Name, or URL text. To understand this distinction, read the Indicator section in the ThreatConnect API documentation.

The methods below get data for the Indicator type (T) linked to this Adapter. The uniqueId (P) for Indicators is a String.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`T`<br>getById(P uniqueId)                   |
|`T`<br>getById(P uniqueId, String ownerName) |
|`IterableResponse<T>`<br>getForFilters(String ownerName, boolean orParams, ApiFilterType...filters)                              | 
|`IterableResponse<T>`<br>getAll()                              |
|`IterableResponse<T>`<br>getAll(String ownerName)              |

The method below returns all the generic Indicators to which the current API user has access.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<Indicator>`<br>getIndicators()                       |

The methods below return owners who have created the Indicator under the uniqueId.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<Owner>`<br>getAssociatedOwners(String uniqueId) |
|`IterableResponse<Owner>`<br>getAssociatedOwners(String uniqueId, String ownerName)  |

The methods below return False Positive counts for the Indicator under the uniqueId.

|Type<br>_Method_                                |
-------------------------------------------------------- |
`FalsePositive`<br>getFalsePositive(String uniqueId) |
`FalsePositive`<br>getFalsePositive(String uniqueId, String ownerName) |

The methods below return Observations and Observation counts for the Indicator under the uniqueId.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`IterableResponse<Observation>`<br>getObservations(String uniqueId) |
|`IterableResponse<Observation>`<br>getObservations(String uniqueId, String ownerName) |
|`ObservationCount`<br>getObservationCount(String uniqueId) |
|`ObservationCount`<br>getObservationCount(String uniqueId, String ownerName) |


The AbstractIndicatorReaderAdapter class has a concrete subclass **FileIndicatorReaderAdapter** that exposes the methods below.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`FileOccurrence`<br>getFileOccurrence(String uniqueId, Integer fileOccurrencId) |
|`FileOccurrence` <br>getFileOccurrence(String uniqueId, Integer fileOccurrencId, String ownerName) |

###BatchReaderAdapter

The BatchReaderAdapter class allows the developer to poll for the status of a batch upload file using a batch id. Once a batch is complete (either successfully or with errors), the developer can download errors (if any).


|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`ApiEntitySingleResponse<BatchStatus, BatchStatusResponseData>`<br>getStatus(int batchId)                  |
|`ApiEntitySingleResponse<BatchStatus, BatchStatusResponseData>`<br>getStatus(int batchId, String ownerName)                  |
|`void`<br>downloadErrors(int batchId, Path outputPath) | 
|`void`<br>downloadErrors(int batchId, String ownerName, Path outputPath) |

###DocumentReaderAdapter

The DocumentReaderAdapter class is a subclass of the AbstractGroupReader class. In addition to all GroupReader functionality, the document reader has access to the following method.

|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`void`<br>downloadFile(int uniqueId, String ownerName, Path outputPath) | 

###OwnerReaderAdapter

The OwnerReaderAdapter is a simple Adapter that returns a list of Organizations to which the API user has access. There is a second method called "getOwnerMine()" that returns the default Organization for the API user.

|Type<br>_Method_                                |
|-------------------------------------------------------- |
|`Owner`<br>getOwnerMine()                        |
|`IterableResponse<Owner>`<br> getOwners()                           |

###SecurityLabelReaderAdapter 

The SecurityLabelReaderAdapter class is a concrete class (available through the ReaderFactory) that returns SecurityLabels to which the developer's API user has access, as well as by uniqueId (P). The uniqueId data type for SecurityLabels is a String.

|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`T`<br>getById(P uniqueId)                   |
|`T`<br>getById(P uniqueId, String ownerName) |
|`IterableResponse<T>`<br>getAll()                              |
|`IterableResponse<T>`<br>getAll(String ownerName)              |

In addition to retrieving basic SecurityLabel data, associated [Groups](#associate-groups) and [Indicators](#associate-indicators) can be retrieved. For more details on these methods, see the [AbstractGroupReaderAdapter](#abstractgroupreaderadapter) class.

###TagReaderAdapter Class

The TagReaderAdapter class is a concrete class (available through the ReaderFactory) that returns Tags to which the developer's API user has access, as well as by uniqueId (P). The uniqueId data type for Tags is a String.

|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`T`<br>getById(P uniqueId)                   |
|`T`<br>getById(P uniqueId, String ownerName) |
|`IterableResponse<T>`<br>getForFilters(String ownerName, boolean orParams, ApiFilterType...filters)                              | 
|`IterableResponse<T>`<br>getAll()                              |
|`IterableResponse<T>`<br>getAll(String ownerName)              |

In addition to retrieving basic Tag data, associated [Groups](#associate-groups) and [Indicators](#associate-indicators) can be retrieved. For more details on these methods, review the [AbstractGroupReaderAdapter](#abstractgroupreaderadapter) class.

###TaskReaderAdapter Class

The TaskReaderAdapter class is a concrete class (available through the ReaderFactory) that returns Tasks to which the API user has access, as well as by uniqueId (P). The uniqueId data type for a Task is an Integer.

|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`T`<br>getById(P uniqueId)                   |
|`T`<br>getById(P uniqueId, String ownerName) |
|`IterableResponse<T>`<br>getForFilters(String ownerName, boolean orParams, ApiFilterType...filters)                              | 
|`IterableResponse<T>`<br>getAll()                              |
|`IterableResponse<T>`<br>getAll(String ownerName)              |
|`IterableResponse<

In addition to retrieving basic Task data, associated Assignees and Escalatees can be retrieved.

The methods below return all Assignees or Escalatees associated with a given Task's id

|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`IterableResponse<User>`<br>getAssignees(P uniqueId)                   |
|`IterableResponse<User>`<br>getEscalatees(P uniqueId) |

The methods below return an individual Assignee or Escalatees' information

|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`IterableResponse<User>`<br>getAssignee(P uniqueId, String userName)                   |
|`IterableResponse<User>`<br>getEscalatee(P uniqueId, String userName) |

###VictimReaderAdapter Class

The VictimReaderAdapter class is a concrete class (available through the ReaderFactory) that returns Victims to which the API user has access, as well as by uniqueId (P). The uniqueId data type for a Victim is an Integer.


|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`T`<br>getById(P uniqueId)                   |
|`T`<br>getById(P uniqueId, String ownerName) |
|`IterableResponse<T>`<br>getForFilters(String ownerName, boolean orParams, ApiFilterType...filters)                              | 
|`IterableResponse<T>`<br>getAll()                              |
|`IterableResponse<T>`<br>getAll(String ownerName)              |

In addition to retrieving basic Victim data, associated [Groups](#associate-groups), [Indicators](#associate-indicators), and [VictimAssets](#associated-victimassets) can be retrieved. For more details on these methods, review the  [AbstractGroupReaderAdapter](#abstractgroupreaderadapter) class.

###Reader IP Address and Tag Example

> The following example uses the Reader Package to retrieve associated Tags from our IP address Indicators:

```java
  1 
  2     private static void doGetAssociatedTags(Connection conn) throws IOException, FailedResponseException {
  3         AbstractIndicatorReaderAdapter reader = ReaderAdapterFactory.createAddressIndicatorReader(conn);
  4         IterableResponse<Address> data = reader.getAll();
  5         for (Address address : data) {
  6             System.out.printf("IP Address: %20s", address.getIp() );
  7 
  8             IterableResponse<Tag> associatedTags = reader.getAssociatedTags( address.getIp() );
  9             System.out.printf("\tAssociated Tag:");
 10             for(Tag tag : associatedTags) {
 11                 System.out.printf("%20s", tag.getName() );
 12             }
 13             System.out.println();
 14         }
 15     }
 16 
```

Line            | Description                                                                                                  
--------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------
3-4             |An IndicatorReaderAdapter is created to read all the addresses to which the API user<br>has access. The `getAll()` method returns a collection of addresses from the<br>ThreatConnect API.
5-6             |Each address is iterated through and its uniqueId is printed. As mentioned in the<br>AbstractIndicatorReaderAdapter section, all uniqueIds for Indicators are Strings.<br>In the case of address objects, it is the IP address or the `getIp()` getter method.
8               |To get a collection of associated Tags for the IP Address, the<br>`getAssociatedTags()` method is called.
10-11           |Each Tag returned from the ThreatConnect API for that specific IP address is iterated<br>through and printed to the console.

<b>Summary</b>

This example explained how to:

* Get a collection of Indicators to which the API user has access
* Retrieve associated data (in this case Tags) based on the uniqueId of the Indicator

##The Writer Package

The Writer Package shares many of the concepts of the Reader Package with the distinction of introducing the new functionality of version 2.0 of the ThreatConnect API. Note that the WriterAdapterFactory class is effectively the "hub" for writer Adapters. It provides convenience objects for all the Adapters in the Writer Package. Below is a list of the static methods and return types of the WriterAdapterFactory.

|Class<br>_Description_|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|`WriterAdapterFactory`<br>Primary entry point to instantiate all writers in the Writer Package.|
|`AbstractGroupWriterAdapter<T extends Group>`<br>Generic Group writer abstract class. Concrete object available in WriterAdapterFactory.|
|`AbstractIndicatorWriterAdapter<T extends Indicator>`<br>Generic Indicator writer abstract class. Concrete object available in WriterAdapterFactory.|
|`AbstractWriterAdapter`<br>Base abstract writer for all reader Adapters in the Reader Package.|
|`SecurityLabelWriterAdapter`<br>Concrete writer for SecurityLabel data. Convenience object available in WriterAdapterFactory.|
|`TagWriterAdapter`<br>Concrete writer for Tag data. Convenience object available in WriterAdapterFactory.|
|`TaskWriterAdapter`<br>Concrete writer for Task data. Convenience object available in WriterAdapterFactory.|
|`VictimWriterAdapter`<br>Concrete writer for Victim data. Convenience object available in WriterAdapterFactory.|
|`AbstractBatchWriterAdapter<T>`<br>Writer for batch indicator uploads. Concrete object available in WriterAdapterFactory.|

###Writer Factory

The primary methods for the WriterFactory are listed below. They encompass all write functionality for the ThreatConnect API.

|Class<br>_Method_
|---------------------------------------------------- | -------------------------------------------------------------------------------------------------------
|`static AbstractGroupWriterAdapter<Adversary>`<br>createAdversaryGroupWriter(Connection conn) |
|`static AbstractGroupWriterAdapter<Email>`<br>createEmailGroupWriter(Connection conn) |
|`static AbstractGroupWriterAdapter<Incident>`<br>createIncidentGroupWriter(Connection conn) |
|`static AbstractGroupWriterAdapter<Signature>`<br>createSignatureGroupWriter(Connection conn) |
|`static AbstractGroupWriterAdapter<Threat>`<br>createThreatGroupWriter(Connection conn) |
|`static AbstractIndicatorWriterAdapter<Address>`<br>createAddressIndicatorWriter(Connection conn) |
|`static AbstractIndicatorWriterAdapter<EmailAddress>`<br>createEmailAddressIndicatorWriter(Connection conn) |
|`static AbstractIndicatorWriterAdapter<File>`<br>createFileIndicatorWriter(Connection conn) |
|`static AbstractIndicatorWriterAdapter<Host>`<br>createHostIndicatorWriter(Connection conn) |
|`static AbstractIndicatorWriterAdapter<Url>`<br>createUrlIndicatorWriter(Connection conn) |
|`static AbstractBatchWriterAdapter<Indicator>`<br>createBatchIndicatorWriter(Connection conn) |
|`static DocumentWriterAdapter`<br>createDocumentWriter(Connection conn) |
|`static SecurityLabelWriterAdapter`<br>createSecurityLabelWriter(Connection conn) |
|`static TagWriterAdapter`<br>createTagWriter(Connection conn) |
|`static TaskWriterAdapter`<br>createTaskWriter(Connection conn) |
|`static VictimWriterAdapter`<br>createVictimWriter(Connection conn) |

###Writer Responses

This section details some conventions used in the writer API that will help clarify how deletes, creates, and updates are handled by the Java SDK, and what the developer should expect when a failure occurs.

When a single item is modified (create/delete/update) using the Java SDK, the return type is an ApiEntitySingleResponse object. In an effort to simplify write-operation response handling, the ApiEntitySingleResponse object provides a single object for the developer to validate the modify operation.  

When a collection of items is modified (create/delete/update) using the Java SDK, the return type is a WriteListResponse object. Likewise, in an effort to simplify write-operation response handling, the WriteListResponse object holds collections of failed/succeeded ApiEntitySingleResponse objects. The following listing describes how modify responses should be handled.

Type<br>_Method_                  | Description
----------------------------------|------------------------
`List<ApiEntitySingleResponse>`<br>getFailureList()      | Collection of failed ApiEntitySingleResponse objects<br>for each element the API user attempted a write<br>operation to the ThreatConnect API
`List<ApiEntitySingleResponse>`<br>getSuccessList()      | Collection of successful ApiEntitySingle Response<br>objects for each element the API user attempted a<br>write operation to the ThreatConnect API
`boolean`<br>isSuccess()                                 | Returns whether the attempted operation returned<br>successfully from the ThreatConnect API for the item<br>that is part of this response. This should be the first<br>element.
`String`<br>getMessage()                                 | If `isSuccess()`  returns false, check this field to<br>find the cause of the failure for the item that it<br>is part of this response.
`T`<br>getItem()                                         | This field is a convenience method that returns the<br>item that is part of this response. Note that not<br>all responses return an item 


While the ApiEntitySingleResponse class manages failed write operations to the ThreatConnect API, the developer is responsible for capturing any runtime exceptions that may occur because of network, configuration, or data-related issues.

###Fluent Entities

> The following is a simple Fluent Example:

```java

       Attribute attribute = new AttributeBuilder()
                .withDisplayed(true)
                .withType(type)
                .withDateAdded(new Date())
                .withLastModified(new Date())
                .withValue(value)
                .createAttribute();
```

There are entity classes available using a fluent style to simplify object creation. These classes are part of the SDK and can be used in place of creating a traditional new ThreatConnect entity with all setters. Using the fluent entities in the `com.threatconnect.sdk.client.fluent` package are optional and a matter of preference.

Fluent Types                                 |
------------------------------------ |
`AddressBuilder` |
`AdversaryBuilder` |
`AttributeBuilder` |
`CommunityBuilder` |
`DocumentBuilder` |
`EmailAddressBuilder` |
`EmailBuilder` |
`FileBuilder` |
`FileOccurrenceBuilder` |
`GroupBuilder` |
`HostBuilder` |
`IncidentBuilder` |
`IndicatorBuilder` |
`IndividualBuilder` |
`SecurityLabelBuilder` |
`SignatureBuilder` |
`SourceBuilder` |
`TagBuilder` |
`TaskBuilder` |
`ThreatBuilder` |
`UrlBuilder` |
`UserBuilder` |
`VictimAssetBuilder` |
`VictimBuilder` |
`VictimEmailAddressBuilder` |
`VictimNetworkAccountBuilder` |
`VictimPhoneBuilder` |
`VictimSocialNetworkBuilder` |
`VictimWebSiteBuilder` |

###Writer Create Example

> The following is a simple Writer Create Example:

```java

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

```

<br>Code Sample<br>

Line            | Description                                                                                                  |
--------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------
104             | An AbstractGroupWriterAdapter for the Adversary Group type is created.<br>With this Adapter, Group data elements, Victim assets, Attributes, and associations <br>can be written/updated/deleted. |
106-108         | A simple Adversary with a name and owner (Organization) is created. |
111             | The writer is used to create an Adversary using the ThreatConnect API.<br>For single-item writes, an ApiEntitySingleResponse object is always returned.<br>This object allows for the appropriate inspection and handling of<br>the response. |
112-114         | To see if the create was successful, `isSuccess()` is called.<br>If the check passes, the item associated with the response is delivered using the <br>`getItem()` method (Line 113). The successfully saved Adversary object<br>returns from the ThreatConnect API with a valid ID value. |
116             | If the response is unsuccessful, the response message to the console is printed. |
121             | Any potential runtime exceptions are caught and handled appropriately.<br>In the case of this basic example, it is simply dumped to the console.

<b>Summary</b>

This example explained how to:

* Create an Adapter using the WriterFactory
* Create an Adversary, and verify if the save was successful
* Handle errors from a write operation to the ThreatConnect API

##Writer Class Overview

Most of the conventions in the Reader Package are mirrored in the Writer Package. Much like the Reader Package, the method-naming conventions will be familiar and self-explanatory. [Parameter-naming conventions](reader/#parameter-naming-convention) have been kept abstract to allow for a better representation of the identifiers being passed. Below is a listing of the classes in the Writer Package.

###AbstractGroupWriterAdapter 

The methods below write data for the Group type (T) linked to this Adapter.

* The create methods require a Group type object as a collection or single object.
* The delete methods require the key ID value as a collection or single object.
* The update methods require a Group type object as a collection or single object.

||Type<br>_Method_|
|------------------------------------------- | --------------------------------------------------------------- |
|`WriteListResponse<T>`<br>create(`List<T> itemList`)                                      |
|`ApiEntitySingleResponse`<br>create(`T item`)                                                |
|`ApiEntitySingleResponse`<br>create(`T item`, `String ownerName`)                              |
|`WriteListResponse<P>`<br>delete(`List<P> itemIds`)                                       |
|`WriteListResponse<P>`<br>delete(`List<P> itemIds`, `String ownerName`)                     |
|`ApiEntitySingleResponse`<br>delete(`P itemId`)                                              |
|`ApiEntitySingleResponse`<br>delete(`P itemId`, `String ownerName`)                            |
|`WriteListResponse<T>`<br>update(`List<T> itemList`)                                      |
|`WriteListResponse<T>`<br>update(`List<T> itemList`, `String ownerName`)                    |
|`ApiEntitySingleResponse`<br>update(`T item`)                                                |
|`ApiEntitySingleResponse`<br>update(`T item`, `String ownerName`)                              | 

###Associate Groups

The methods below associate a Group type to another Group type. Groups are associated by passing in the uniqueId (Integer) with the Group ID to which it will be associated. 

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Integer>`<br>associateGroupAdversaries(`Integer uniqueId`, `List<Integer> adversaryIds`) |
|`WriteListResponse<Integer>`<br>associateGroupAdversaries(`Integer uniqueId`, `List<Integer> adversaryIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateGroupAdversary(`Integer uniqueId`, `Integer adversaryId`) |
|`ApiEntitySingleResponse`<br>associateGroupAdversary(`Integer uniqueId`, `Integer adversaryId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateGroupEmails(`Integer uniqueId`, `List<Integer> emailIds`) |
|`WriteListResponse<Integer>`<br>associateGroupEmails(`Integer uniqueId`, `List<Integer> emailIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateGroupEmail(`Integer uniqueId`, `Integer emailId`) |
|`ApiEntitySingleResponse`<br>associateGroupEmail(`Integer uniqueId`, `Integer emailId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateGroupIncidents(`Integer uniqueId`, `List<Integer> incidentIds`) |
|`WriteListResponse<Integer>`<br>associateGroupIncidents(`Integer uniqueId`, `List<Integer> incidentIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateGroupIncident(`Integer uniqueId`, `Integer incidentId`) |
|`ApiEntitySingleResponse`<br>associateGroupIncident(`Integer uniqueId`, `Integer incidentId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateGroupSignatures(`Integer uniqueId`, `List<Integer> signatureIds`) |
|`WriteListResponse<Integer>`<br>associateGroupSignatures(`Integer uniqueId`, `List<Integer> signatureIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateGroupSignature(`Integer uniqueId`, `Integer signatureId`) |
|`ApiEntitySingleResponse`<br>associateGroupSignature(`Integer uniqueId`, `Integer signatureId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateGroupThreats(`Integer uniqueId`, `List<Integer> threatIds`) |
|`WriteListResponse<Integer>`<br>associateGroupThreats(`Integer uniqueId`, `List<Integer> threatIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateGroupThreat(`Integer uniqueId`, `Integer threatId`) |
|`ApiEntitySingleResponse`<br>associateGroupThreat(`Integer uniqueId`, `Integer threatId`, `String ownerName`) |

###Associate Indicators

The methods below associate Indicators to a Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<String>`<br>associateIndicatorAddresses(`Integer uniqueId`, `List<String> ipAddresses`) |
|`WriteListResponse<String>`<br>associateIndicatorAddresses(`Integer uniqueId`, `List<String> ipAddresses`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateIndicatorAddress(`Integer uniqueId`, `String ipAddress`) |
|`ApiEntitySingleResponse`<br>associateIndicatorAddress(`Integer uniqueId`, `String ipAddress`, `String ownerName`) |
|`WriteListResponse<String>`<br>associateIndicatorEmailAddresses(`Integer uniqueId`, `List<String> emailAddresses`) |
|`WriteListResponse<String>`<br>associateIndicatorEmailAddresses(`Integer uniqueId`, `List<String> emailAddresses`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateIndicatorEmailAddress(`Integer uniqueId`, `String emailAddress`) |
|`ApiEntitySingleResponse`<br>associateIndicatorEmailAddress(`Integer uniqueId`, `String emailAddress`, `String ownerName`) |
|`WriteListResponse<String>`<br>associateIndicatorFiles(`Integer uniqueId`, `List<String> fileHashes`) |
|`WriteListResponse<String>`<br>associateIndicatorFiles(`Integer uniqueId`, `List<String> fileHashes`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateIndicatorFile(`Integer uniqueId`, `String fileHash`) |
|`ApiEntitySingleResponse`<br>associateIndicatorFile(`Integer uniqueId`, `String fileHash`, `String ownerName`) |
|`WriteListResponse<String>`<br>associateIndicatorHosts(`Integer uniqueId`, `List<String> hostNames`) |
|`WriteListResponse<String>`<br>associateIndicatorHosts(`Integer uniqueId`, `List<String> hostNames`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateIndicatorHost(`Integer uniqueId`, `String hostName`) |
|`ApiEntitySingleResponse`<br>associateIndicatorHost(`Integer uniqueId`, `String hostName`, `String ownerName`) |
|`WriteListResponse<String>`<br>associateIndicatorUrls(`Integer uniqueId`, `List<String> urlTexts`) |
|`WriteListResponse<String>`<br>associateIndicatorUrls(`Integer uniqueId`, `List<String> urlTexts`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateIndicatorUrl(`Integer uniqueId`, `String urlText`) |
|`ApiEntitySingleResponse`<br>associateIndicatorUrl(`Integer uniqueId`, `String urlText`, `String ownerName`) |

###Associate Security Labels

The methods below associate Security Labels to a Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<String>`<br>associateSecurityLabels(`Integer uniqueId`, `List<String> securityLabels`) |
|`WriteListResponse<String>`<br>associateSecurityLabels(`Integer uniqueId`, `List<String> securityLabels`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateSecurityLabel(`Integer uniqueId`, `String securityLabel`) |
|`ApiEntitySingleResponse`<br>associateSecurityLabel(`Integer uniqueId`, `String securityLabel`, `String ownerName`) |

###Associate Tag

The methods below associate Tags to a Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<String>`<br>associateTags(`Integer uniqueId`, `List<String> tagNames`) |
|`WriteListResponse<String>`<br>associateTags(`Integer uniqueId`, `List<String> tagNames`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateTag(`Integer uniqueId`, `String tagName`) |
|`ApiEntitySingleResponse`<br>associateTag(`Integer uniqueId`, `String tagName`, `String ownerName`) |

###Associate Victim

The methods below associate Victims to a Group type.

|Type<br>_Method_|
|--------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Integer>`<br>associateVictims(`Integer uniqueId`, `List<Integer> victimIds`) |
|`WriteListResponse<Integer>`<br>associateVictims(`Integer uniqueId`, `List<Integer> victimIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateVictim(`Integer uniqueId`, `Integer victimId`) |
|`ApiEntitySingleResponse`<br>associateVictim(`Integer uniqueId`, `Integer victimId`, `String ownerName`) |

###Associate Victim Asset

The methods below associate Victim Assets to a Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Integer>`<br>associateVictimAssetEmailAddresses(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetEmailAddresses(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetEmailAddress(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetEmailAddress(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetNetworkAccounts(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetNetworkAccounts(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetNetworkAccount(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetNetworkAccount(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetPhoneNumbers(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetPhoneNumbers(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetPhoneNumber(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetPhoneNumber(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetSocialNetworks(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetSocialNetworks(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetSocialNetwork(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetSocialNetwork(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetWebsites(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>associateVictimAssetWebsites(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetWebsite(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>associateVictimAssetWebsite(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |

###Add Attributes

The methods below add Attribute types to a Group.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Attribute>`<br>addAttributes(`Integer uniqueId`, `List<Attribute> attributes`) |
|`WriteListResponse<Attribute>`<br>addAttributes(`Integer uniqueId`, `List<Attribute> attribute`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>addAttribute(`Integer uniqueId`, `Attribute attribute`) |
|`ApiEntitySingleResponse`<br>addAttribute(`Integer uniqueId`, `Attribute attribute`, `String ownerName`) |
|`WriteListResponse<String>`<br>addAttributeSecurityLabels(`Integer uniqueId`, `Integer attributeId`, `List<String> securityLabels`) |
|`WriteListResponse<String>`<br>addAttributeSecurityLabels(`Integer uniqueId`, `Integer attributeId`, `List<String> securityLabels`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>addAttributeSecurityLabel(`Integer uniqueId`, `Integer attributeId`, `String securityLabel`) |
|`ApiEntitySingleResponse`<br>addAttributeSecurityLabel(`Integer uniqueId`, `Integer attributeId`, `String securityLabel`, `String ownerName`) |

###Update Attribute

The methods below **update** an Attribute added to a specific Indicator type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Attribute>`<br>updateAttributes(`Integer uniqueId`, `List<Attribute> attributes`) |
|`WriteListResponse<Attribute>`<br>updateAttributes(`Integer uniqueId`, `List<Attribute> attribute`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>updateAttribute(`Integer uniqueId`, `Attribute attribute`) |
|`ApiEntitySingleResponse`<br>updateAttribute(`Integer uniqueId`, `Attribute attribute`, `String ownerName`) |


###Create Observation

The methods below **create** an Observation on a specific Indicator type.

|Type<br>_Method_|                                                          
|----------------------------------------------------------------------------------------------------------| 
|`ApiEntitySingleResponse`<br>createObservation(`Integer uniqueId`)|
|`ApiEntitySingleResponse`<br>createObservation(`Integer uniqueId`, `String ownerName`)| 


###Update False Positive

The methods below **update** the False Positive field on a specific Indicator type.

|Type<br>_Method_|                                                          
|----------------------------------------------------------------------------------------------------------| 
|`ApiEntitySingleResponse`<br>updateFalsePositive(`Integer uniqueId`)|
|`ApiEntitySingleResponse`<br>updateFalsePositive(`Integer uniqueId`, `String ownerName`)| 

###Delete Group Association

The methods below **delete** Group associations to a specific Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Integer>`<br>dissociateGroupAdversaries(`Integer uniqueId`, `List<Integer> adversaryIds`) |
|`WriteListResponse<Integer>`<br>dissociateGroupAdversaries(`Integer uniqueId`, `List<Integer> adversaryIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateGroupAdversary(`Integer uniqueId`, `Integer adversaryId`) |
|`ApiEntitySingleResponse`<br>dissociateGroupAdversary(`Integer uniqueId`, `Integer adversaryId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateGroupEmails(`Integer uniqueId`, `List<Integer> emailIds`) |
|`WriteListResponse<Integer>`<br>dissociateGroupEmails(`Integer uniqueId`, `List<Integer> emailIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateGroupEmail(`Integer uniqueId`, `Integer emailId`) |
|`ApiEntitySingleResponse`<br>dissociateGroupEmail(`Integer uniqueId`, `Integer emailId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateGroupIncidents(`Integer uniqueId`, `List<Integer> incidentIds`) |
|`WriteListResponse<Integer>`<br>dissociateGroupIncidents(`Integer uniqueId`, `List<Integer> incidentIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateGroupIncident(`Integer uniqueId`, `Integer incidentId`) |
|`ApiEntitySingleResponse`<br>dissociateGroupIncident(`Integer uniqueId`, `Integer incidentId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateGroupSignatures(`Integer uniqueId`, `List<Integer> signatureIds`) |
|`WriteListResponse<Integer>`<br>dissociateGroupSignatures(`Integer uniqueId`, `List<Integer> signatureIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateGroupSignature(`Integer uniqueId`, `Integer signatureId`) |
|`ApiEntitySingleResponse`<br>dissociateGroupSignature(`Integer uniqueId`, `Integer signatureId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateGroupThreats(`Integer uniqueId`, `List<Integer> threatIds`) |
|`WriteListResponse<Integer>`<br>dissociateGroupThreats(`Integer uniqueId`, `List<Integer> threatIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateGroupThreat(`Integer uniqueId`, `Integer threatId`) |
|`ApiEntitySingleResponse`<br>dissociateGroupThreat(`Integer uniqueId`, `Integer threatId`, `String ownerName`) |

###Delete Indicator Associations

The methods below **delete** Indicator associations to a specific Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<String>`<br>dissociateIndicatorAddresses(`Integer uniqueId`, `List<String> ipAddresses`) |
|`WriteListResponse<String>`<br>dissociateIndicatorAddresses(`Integer uniqueId`, `List<String> ipAddresses`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorAddress(`Integer uniqueId`, `String ipAddress`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorAddress(`Integer uniqueId`, `String ipAddress`, `String ownerName`) |
|`WriteListResponse<String>`<br>dissociateIndicatorEmailAddresses(`Integer uniqueId`, `List<String> emailAddresses`) |
|`WriteListResponse<String>`<br>dissociateIndicatorEmailAddresses(`Integer uniqueId`, `List<String> emailAddresses`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorEmailAddress(`Integer uniqueId`, `String emailAddress`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorEmailAddress(`Integer uniqueId`, `String emailAddress`, `String ownerName`) |
|`WriteListResponse<String>`<br>dissociateIndicatorFiles(`Integer uniqueId`, `List<String> fileHashes`) |
|`WriteListResponse<String>`<br>dissociateIndicatorFiles(`Integer uniqueId`, `List<String> fileHashes`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorFile(`Integer uniqueId`, `String fileHash`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorFile(`Integer uniqueId`, `String fileHash`, `String ownerName`) |
|`WriteListResponse<String>`<br>dissociateIndicatorHosts(`Integer uniqueId`, `List<String> hostNames`) |
|`WriteListResponse<String>`<br>dissociateIndicatorHosts(`Integer uniqueId`, `List<String> hostNames`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorHost(`Integer uniqueId`, `String hostName`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorHost(`Integer uniqueId`, `String hostName`, `String ownerName`) |
|`WriteListResponse<String>`<br>dissociateIndicatorUrls(`Integer uniqueId`, `List<String> urlTexts`) |
|`WriteListResponse<String>`<br>dissociateIndicatorUrls(`Integer uniqueId`, `List<String> urlTexts`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorUrl(`Integer uniqueId`, `String urlText`) |
|`ApiEntitySingleResponse`<br>dissociateIndicatorUrl(`Integer uniqueId`, `String urlText`, `String ownerName`) |

###Delete Security Label Associations

The methods below **delete** SecurityLabel associations to a specific Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<String>`<br>dissociateSecurityLabel(`Integer uniqueId`, `List<String> securityLabels`) |
|`WriteListResponse<String>`<br>dissociateSecurityLabel(`Integer uniqueId`, `List<String> securityLabels`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateSecurityLabel(`Integer uniqueId`, `String securityLabel`) |
|`ApiEntitySingleResponse`<br>dissociateSecurityLabel(`Integer uniqueId`, `String securityLabel`, `String ownerName`) |

###Delete Tag Associations

The methods below **delete** Tag associations to a specific Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<String>`<br>dissociateTags(`Integer uniqueId`, `List<String> tagNames`) |
|`WriteListResponse<String>`<br>dissociateTags(`Integer uniqueId`, `List<String> tagNames`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateTag(`Integer uniqueId`, `String tagName`) |
|`ApiEntitySingleResponse`<br>dissociateTag(`Integer uniqueId`, `String tagName`, `String ownerName`) |

###Delete Victim Associations

The methods below **delete** Victim associations to a specific Group type.

|Type<br>_Method_|
|--------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Integer>`<br>dissociateVictims(`Integer uniqueId`, `List<Integer> victimIds`) |
|`WriteListResponse<Integer>`<br>dissociateVictims(`Integer uniqueId`, `List<Integer> victimIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateVictim(`Integer uniqueId`, `Integer victimId`) |
|`ApiEntitySingleResponse`<br>dissociateVictim(`Integer uniqueId`, `Integer victimId`, `String ownerName`) |

###Delete VictimAsset Associations

The methods below **delete** VictimAsset associations to a specific Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetEmailAddresses(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetEmailAddresses(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetEmailAddress(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetEmailAddress(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetNetworkAccounts(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetNetworkAccounts(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetNetworkAccount(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetNetworkAccount(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetPhoneNumbers(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetPhoneNumbers(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetPhoneNumber(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetPhoneNumber(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetSocialNetworks(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetSocialNetworks(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetSocialNetwork(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetSocialNetwork(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetWebsites(`Integer uniqueId`, `List<Integer> assetIds`) |
|`WriteListResponse<Integer>`<br>dissociateVictimAssetWebsites(`Integer uniqueId`, `List<Integer> assetIds`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetWebsite(`Integer uniqueId`, `Integer assetId`) |
|`ApiEntitySingleResponse`<br>dissociateVictimAssetWebsite(`Integer uniqueId`, `Integer assetId`, `String ownerName`) |

###Delete Attribute

The methods below **delete** Attributes from a specific Group type.

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<Integer>`<br>deleteAttributes(`Integer uniqueId`, `List<Integer> attributes`) |
|`WriteListResponse<Integer>`<br>deleteAttributes(`Integer uniqueId`, `List<Integer> attribute`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>deleteAttribute(`Integer uniqueId`, `Integer attribute`) |
|`ApiEntitySingleResponse`<br>deleteAttribute(`Integer uniqueId`, `Integer attribute`, `String ownerName`) |
|`WriteListResponse<String>`<br>deleteAttributeSecurityLabels(`Integer uniqueId`, `Integer attributeId`, `List<String> securityLabels`) |
|`WriteListResponse<String>`<br>deleteAttributeSecurityLabels(`Integer uniqueId`, `Integer attributeId`, `List<String> securityLabels`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>deleteAttributeSecurityLabel(`Integer uniqueId`, `Integer attributeId`, `String securityLabel`) |
|`ApiEntitySingleResponse`<br>deleteAttributeSecurityLabel(`Integer uniqueId`, `Integer attributeId`, `String securityLabel`, `String ownerName`) |

###AbstractIndicatorWriterAdapter

The AbstractIndicatorWriterAdapter shares most of the write functionality with the AbstractGroupWriterAdapter. In fact, they both implement the following writer interfaces:

Interface                                 |
----------------------------------------- |
`AttributeAssociateWritable<T>`           |
`GroupAssociateWritable<T>`               |
`IndicatorAssociateWritable<T>`           |
`SecurityLabelAssociateWritable<T>`       |
`TagAssociateWritable<T>`                 |
`VictimAssetAssociateWritable<T>`         |

These interfaces allow the AbstractIndicatorWriterAdapter to run all of the same methods as the AbstractGroupWriterAdapter.

The key parameter-level distinction between the AbstractIndicatorWriterAdapter and the AbstractGroupWriterAdapter is the type (T) for the `uniqueId` parameter. As mentioned in previous sections, Indicator `uniqueId` types are all Strings. The method-naming conventions are the same.

###FileIndicatorWriterAdapter

FileIndicatorWriterAdapter, which all the functionality of the AbstractIndicatorWriterAdapter with the addition of the following write methods:

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<FileOccurrence>`<br>updateFileOccurrences(`String fileHash`, `List<FileOccurrence> fileOccurrences`) |
|`WriteListResponse<FileOccurrence>`<br>updateFileOccurrences(`String fileHash`, `List<FileOccurrence> fileOccurrences`, `String ownerName`) |
|`FileOccurrence`<br>updateFileOccurrence(`String fileHash`, `FileOccurrence fileOccurrence`) |
|`FileOccurrence`<br>updateFileOccurrence(`String fileHash`, `FileOccurrence fileOccurrence`, `String ownerName`) |

###DocumentWriterAdapter

DocumentWriterAdapter has all the functionality of the AbstractGroupWriterAdapter with the addition of the following write methods:

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`ApiEntitySingleResponse`<br>uploadFile(`int uniqueId`, `File file`) |
|`ApiEntitySingleResponse`<br>uploadFile(`int uniqueId`, `File file`, `String ownerName`) |

###AbstractBatchWriterAdapter

The AbstractBatchWriterAdapter class allows batch writing of indicators to the API. The adapter facilitates the initial creation and upload of the batch file using the following write methods:

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`ApiEntitySingleResponse`<br>create(`BatchConfig item` ) |
|`ApiEntitySingleResponse`<br>create(`BatchConfig item`, `String ownerName`) |
|`ApiEntitySingleResponse`<br>uploadFile(`int batchId`, `File file`) |

Once a batch configuration is created, the ApiEntitySingleResponse object returns BatchResponseData with a batchId if successful. This batchId is used to upload the batch file using the `uploadFile` method. At this point, a successfuly response to the upload will trigger the batch. Use the BatchReaderAdapter to poll for the status of the batch. 

###SecurityLabelWriterAdapter

The SecurityLabelWriterAdapter class allows [Group](#associate-groups) and [Indicator](#associate-indicators) associations. Much like the Indicator Adapters, the `uniqueId` is a user-created Security Label String. In addition to creating associations, the SecurityLabelWriterAdapter allows deleting associations from [Group](#dissociate-groups) and [Indicator](#dissociate-indicators) types.

Below is the standard create methods available to all WriterAdapter’s. Note that the deletes require the Security Label as the `uniqueId` String (P). The create and update requires the full SecurityLabel object (T).

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<T>`                        <br>create(`List<T> itemList`)                                        |
|`ApiEntitySingleResponse`                     <br>create(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>create(`T item`, `String ownerName`)                                |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`)                                         |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`, `String ownerName`)                       |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`)                                                |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`, `String ownerName`)                              |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`)                                        |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`, `String ownerName`)                      |
|`ApiEntitySingleResponse`                     <br>update(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>update(`T item`, `String ownerName`)                                |


###TagWriterAdapter

The TagWriterAdapter class allows [Group](#associate-groups) and [Indicator](#associate-indicators) associations. Much like the Indicator Adapters, the uniqueId is a user-created Tag name String. In addition to creating associations, the TagWriterAdapter allows deleting associations from [Group](#dissociate-groups) and [Indicator](#dissociate-indicators) types.

Below is the standard create methods available to all WriterAdapters. Note that the deletes require the Tag Name  as the `uniqueId` String (P). The create and update requires the full Tag object (T).

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<T>`                        <br>create(`List<T> itemList`)                                        |
|`ApiEntitySingleResponse`                     <br>create(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>create(`T item`, `String ownerName`)                                |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`)                                         |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`, `String ownerName`)                       |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`)                                                |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`, `String ownerName`)                              |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`)                                        |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`, `String ownerName`)                      |
|`ApiEntitySingleResponse`                     <br>update(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>update(`T item`, `String ownerName`)                                |

###TaskWriterAdapter

The TaskWriterAdapter allows

Below is the standard create methods available to all WriterAdapters. 

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<T>`                        <br>create(`List<T> itemList`)                                        |
|`ApiEntitySingleResponse`                     <br>create(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>create(`T item`, `String ownerName`)                                |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`)                                         |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`, `String ownerName`)                       |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`)                                                |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`, `String ownerName`)                              |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`)                                        |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`, `String ownerName`)                      |
|`ApiEntitySingleResponse`                     <br>update(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>update(`T item`, `String ownerName`)                                |

In addition to the User-specific methods below. Note the delete methods require the username while the create methods require the entire User object.

|Type<br>_Method_                                |
|---------------------------------------------------------- |
|`UserResponse`<br>createAssignee(P uniqueId, User assignee)                   |
|`UserResponse`<br>createEscalatee(P uniqueId, User escalatee) |
|`UserResponse`<br>deleteAssignee(P uniqueId, String userName)                   |
|`UserResponse`<br>deleteEscalatee(P uniqueId, String userName) |

###VictimWriterAdapter

The TagWriterAdapter class allows [Group](#associate-groups), [Indicator](#associate-indicators), and VictimAsset associations. Much like the Group Adapters, the uniqueId is a user-created Security Label String. In addition to creating associations, the VictimAssetWriterAdapter can remove associations for [Group](#dissociate-groups), [Indicator](#dissociate-indicators), and [VictimAssets](#dissociate-victimasset).

Below is the standard create methods available to all WriterAdapters. Note that the deletes require the system-generated VictimAsset ID  as the `uniqueId` Integer (P). The create and update requires the full VictimAsset object (T).

|Type<br>_Method_|
|---------------------------------------------------------------------------------------------------------- |
|`WriteListResponse<T>`                        <br>create(`List<T> itemList`)                                        |
|`ApiEntitySingleResponse`                     <br>create(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>create(`T item`, `String ownerName`)                                |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`)                                         |
|`WriteListResponse<P>`                        <br>delete(`List<P> itemIds`, `String ownerName`)                       |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`)                                                |
|`ApiEntitySingleResponse`                     <br>delete(`P itemId`, `String ownerName`)                              |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`)                                        |
|`WriteListResponse<T>`                        <br>update(`List<T> itemList`, `String ownerName`)                      |
|`ApiEntitySingleResponse`                     <br>update(`T item`)                                                  |
|`ApiEntitySingleResponse`                     <br>update(`T item`, `String ownerName`)                                |

###Writer Examples

> Writer Delete Example:

```java

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
 
```

This section offers examples on how to create, delete, and update data using the Java SDK for ThreatConnect.

Line         | Description                                                     |
------------ | --------------------------------------------------------------- |
131          | Since Adversary objects from the ThreatConnect API will be created and deleted,<br>an AbstractGroupWriterAdapter with the Adversary parameterized type applied is<br>instantiated. |
138-139      | An Adversary object with the ThreatConnect API is created, the response is captured,<br>and `isSuccess()` is called to check if the save was successful. |
140          | The response Adversary object returned from the ThreatConnect API is printed.<br>The `getItem()`method will return this object with the ID field populated.<br>This method will always hold the saved item on a successful response. |
141-142      | The ID from the successful create is used to delete the same Adversary object.<br>Note that the call to the `delete()` method requires the system-generated<br>Adversary ID. |
143-144      | The delete response is verified as successful, and the original response is dumped. |
146          | With a failed delete, the error message is printed by calling the `getMessage()`<br>method on the response object. |
149          | If the original create failed, the `getMessage()` method is also called to find<br>the cause. |
 
###Writer Update Example

> Writer Update Example:
 
```java

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

```

<b>Code Sample Description</b>

Line         | Description                                                     |
------------ | --------------------------------------------------------------- |
155-164      | A test Adversary is created and saved to the ThreatConnect API. |
166-168      | The created Adversary is assigned to a variable called "updatedAdversary()" so that the<br>Adversary name can be changed (line 167). Before updating the Adversary in<br>ThreatConnect, it is printed to the console. The output should have an<br>ID value populated and the name should read:<br>"UPDATED: Test Adversary".|
170-172      | The "update()" method is called to save the changes to ThreatConnect. The argument to<br>this method is the actual Adversary object. Just like the delete, the response<br>success is verified and written to the console.

###Writer Add Attribute Example

> Writer Add Attribute Example

```java
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
```

<b>Code Sample Description</b>

Line         | Description                                                    |
------------ | --------------------------------------------------------------- |
72-73        | The test email object and the Attribute to be added are created.         |
79-81        | The email in ThreatConnect is created and checked that it is successful. |
86-87        | The `addAttribute()` method takes the Email Group ID and the Attribute <br>object to be added. |
89-90        | To confirm that the Attribute was added successfully, the response is checked. |

###Writer Associate Indicator Example

> Writer Associate Indicator Example

```java
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
```

<b>Code Sample Description</b>

Line         | Description                                                     |
------------ | --------------------------------------------------------------- |
106-107      | Two writers are created: one for the new email and the other for the host <br>to be associated. |
109-110      | The test email object is crated, as well as the host to be associated.        |
117-121      | To set up the example, both email and host are created in ThreatConnect. <br>The create is verified as successful and the items are printed to the console. |
126-128      | The host is associated to the Email Group by using the Email ID and the <br>Host Name (the unique ID for the Host Indicator). |
130-133      | The association is verified as successful.|

###Writer Associate Group Example

> Writer Associate Group Example

```java

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
```

<b>Code Sample Description</b>

Line         | Description                                                     |
------------ | --------------------------------------------------------------- |
153-154      | Two writers are created: one for the new email and the other for the Threat <br>to be associated. |
156-157      | The test email object is created, as well as the Threat to be associated. |
163-167      | To set up the example, both email and Threat are created in ThreatConnect, <br>the create is verified as successful, and the items are printed to the console.|
172-174      | The Threat is associated to the Email Group by using the Email ID and the Threat ID. |
176-179      | The association is verified as successful.|

###Writer Associate Tag Example

> Writer Associate Tag Example

```java

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
```

<b>Code Sample Description</b>

Line         | Description                                                     |
------------ | --------------------------------------------------------------- |
198-199      | Two writers are created: one for the new email and the other for the Tag to associate. |
201-202       | The test email object, and the Tag to associate, are created.|
208-214      | To set up the example, both email and Tag are created in ThreatConnect. The create <br> is verified as successful, and the items are printed to the console.|
219-221      | The Tag is associated to the Email Group by using the Email ID and the Tag name <br>(the `uniqueID` for the Tag). |
223-226      | The association is verified as successful. |

###Writer Associate Victim Example

> Writer Associate Victim Example

```java
 
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
```

<b>Code Sample Description</b>

Line         | Description                                                     |
------------ | --------------------------------------------------------------- |
305-306      | Two writers are created: one for the new email and the other for the Victim to associate. |
308-309      | The test email object, and the Victim to associate, are created. |
315-319      | To set up the example, both email and Victim are created in ThreatConnect. <br>The create is verified as successful, and the items are printed <br>to the console. |
324-326      | The Victim is associated to the Email Group by using the Email ID and the Victim ID. |
328-331      | The association is verified as successful.|

###Writer Remove Association Example

> Writer Remove Association Example

```java

243     private static void doRemoveAssociatedTag(Connection conn) {
244 
245         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
246         TagWriterAdapter tWriter = WriterAdapterFactory.createTagWriter(conn);
247 
248         Email email = createTestEmail();
249         Tag tag = createTestTag();
250 
251         try {
252             // -----------------------------------------
253             // Create Email and Tag 
254             // -----------------------------------------
255             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
256             tWriter.delete(tag.getName()); // delete if it exists
257             ApiEntitySingleResponse<Tag, ?> createResponseTag = tWriter.create(tag);
258 
259             if (createResponseEmail.isSuccess() && createResponseTag.isSuccess() ) {
260                 System.out.println("Created Email: " + createResponseEmail.getItem());
261                 System.out.println("Created Tag: " + createResponseTag.getItem());
262 
263                 // -----------------------------------------
264                 // Associate Tag
265                 // -----------------------------------------
266                 ApiEntitySingleResponse assocResponse
267                     = gWriter.associateTag(createResponseEmail.getItem().getId()
268                                          , createResponseTag.getItem().getName() );
269 
270                 if ( assocResponse.isSuccess() ) {
271                     System.out.println("\tAssociated Tag: " + createResponseTag.getItem().getName() );
272 
273                     // -----------------------------------------
274                     // Delete Association
275                     // -----------------------------------------
276                     ApiEntitySingleResponse dissociateResponse
277                         = gWriter.dissociateTag(createResponseEmail.getItem()
278                                       .getId(), createResponseTag.getItem().getName() );
279 
280                     if ( dissociateResponse.isSuccess() ) {
281                         System.out.println("\tDeleted Associated Tag: " + createResponseTag.getItem().getName() );
282                     } else {
283                         System.err.println("Failed to delete Associated Tag: "+ dissociateResponse.getMessage());
284                     }
285 
286                 } else {
287                     System.err.println("Failed to Associate Tag: " + assocResponse.getMessage());
288                 }
289 
290             } else {
291                 if ( !createResponseEmail.isSuccess() ) {
292                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
293                 }
294                 if ( !createResponseTag.isSuccess() ) {
295                     System.err.println("Failed to Create Tag: " + createResponseTag.getMessage());
296                 }
297             }
298 
299         } catch (IOException | FailedResponseException ex) {
300             System.err.println("Error: " + ex.toString());
301         }
302     }
```

<b>Code Sample Description</b>

Line         | Description                                                    
------------ | ---------------------------------------------------------------
245-271      | The Email Group is created and associated with the Tag item.
276-278      | The `dissociateTag()` method is called using the same parameters as <br> the associate method. The email item ID value is used  with the Tag name.
280-281      | The deleting is verified as successful, and the message is dumped to the console.

<b>Summary</b>

The previous two examples explained how to:

* Delete and update an Adversary and verify that the action was successfully applied to ThreatConnect
* Add an Attribute to a Group item
* Associate Indicators, Groups, Tags, and Victims
* Remove Association from a Group item

# JavaScript Library

<b>About This Document</b>

This section explains the process of coding JavaScript applications, and the implementation of the JavaScript SDK, using the ThreatConnect API. The JavaScript SDK offers coverage of all features in version 4.0 of the ThreatConnect API—including the ability to write data to ThreatConnect.

The goal of this JavaScript SDK library is to provide a programmatic abstraction layer around the ThreatConnect API without losing functional coverage over the available API resources. This abstraction layer enables developers to focus on writing enterprise functionality without worrying about low-level RESTful calls and authentication management.

This document is not a replacement for the ThreatConnect API User Guide. This document serves as a companion to the official documentation for the REST API. Read the official documentation to gain a further understanding of the functional aspects of using the ThreatConnect API.

<b>How to Use This Document</b>

This document explains how to create Groups, Indicators, Associations, Tags, Security Labels, and Victims. Along with creating data elements, a developer will learn how to create, update, delete, and request data from the API using JavaScript. This document assumes the reader knows the JavaScript programming language.

All code examples will be noted in a separate box with a monospaced font and line numbers to facilitate explanation of code functionality. 

## Getting Started

> An example of using configuration to read API configuration values is the following:

```javascript
var apiSettings,
    tcSpaceElementId = getParameterByName('tcSpaceElementId');

if ( tcSpaceElementId ) {
    apiSettings = {
        apiToken: getParameterByName('tcToken'),
        apiUrl: getParameterByName('tcApiPath')
    };
} else {
    apiSettings = {
        apiId: '12345678900987654321',
        apiSec: 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=',
        apiUrl: 'https://api.threatconnect.com'
    };
}
```

```html
<!-- JQuery -->
<script src="./libs/jquery-2.1.4.min.js" type="test/javascript"></script>

<!-- HMAC -->
<script src="./libs/core.js" type="text/javascript"></script>
<script src="./libs/sha256.js" type="text/javascript"></script>
<script src="./libs/hmac.js" type="text/javascript"></script>
<script src="./libs/enc-base64.js" type="text/javascript"></script>

<!-- ThreatConnect -->
<script src="./libs/threatconnect.js" type="text/javascript"></script>
```

The JavaScript SDK is written to support ECMAScript&REG;-5 and should work in most modern browsers.

To use the RESTful API for ThreatConnect, an API user must be provisioned. See the ThreatConnect API User Guide for details on how to create an API user as it is out of scope for this document.

The JavaScript SDK can be configured to use an Access ID and Secret Key or a Token. Token support is only available when working with a Spaces application.

Once the configuration has been set up, the developer should be able to run the examples in this document as long as the JavaScript SDK has been installed. 

The following example illustrates a typical initialization of the ThreatConnect Object:

`var tc = new ThreatConnect(apiSettings);`

<b>Third-Party Dependencies</b>

Name          | Version       | Link
------------- | ------------- | ----------------------
jquery        | 2.1.4         | [https://jquery.com/](https://jquery.com/)
Crypto-JS     | 3.1           | [https://code.google.com/p/crypto-js/](https://code.google.com/p/crypto-js/)

<b>Technical Design</b>

The JavaScript SDK for ThreatConnect was designed with a focus on abstracting the API REST calls while enabling the developer to use an enterprise-level programming language.

<b>Supported Resource Types</b>

The JavaScript SDK supports the Resource Types listed below. There is also a mechanism to do manual API requests to cover any API calls that are not provided with the core functionality.

Object                | Description                      
--------------------- | -----------                      
`groups()`            | Group container object           
`indicators()`        | Indicator container object       
`indicatorsBatch()`   | Batch Indicator container object 
`owners()`            | Owner container object           
`securityLabel()`     | Security Label container object  
`tags()`              | Tag container object             
`tasks()`             | Task container object            
`victims()`           | Victim container object          

## Example JavaScript App

> The example below illustrates how to write a program using the JavaScript SDK for the ThreatConnect API:

```javascript
var apiSettings,
    tcSpaceElementId = getParameterByName('tcSpaceElementId');

if ( tcSpaceElementId ) {
    apiSettings = {
        apiToken: getParameterByName('tcToken'),
        apiUrl: getParameterByName('tcApiPath')
    };
} else {
    apiSettings = {
        apiId: '12345678900987654321',
        apiSec: 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=',
        apiUrl: 'https://demo.threatconnect.com/api'
    };
}

var tc = new ThreatConnect(apiSettings);

tc.owners()
    .done(function(response) {
        console.log('owner response', response);
    })
    .error(function(response) {
        console.log('owner response error', response.error);
    })
    .retrieve();
```

This example illustrates how to write a program using the JavaScript SDK for the ThreatConnect API. An Owner's object will be created in order to pull a collection of all Owners to which the API account being used has access. Once retrieved, the Owners objects will be printed to the console.

<b>Code Highlights</b>

Snippet                                   | Description                                                                       
----------------------------------------- | --------------------------------------------------------------------------------- 
`tcSpaceElementId = getParameterByNam...` | Retrieve Space Element Id (only supported on <br>Spaces application). 
`apiToken: getParameterByName('tcToken')` | Retrieve Token from Spaces. 
`apiUrl: getParameterByName('tcApiPath')` | Retrieve API Path from Spaces. 
`apiId: '12345678900987654321',`          | Set API ID when not using Spaces App. 
`apiSec: 'aabbccddeeffgghhiijjkkllmmn...` | Set API Secret when not using Spaces App. 
`apiUrl: 'https://demo.threatconnect.com/api`         | Set API URL when not using Spaces App. 
`var tc = new ThreatConnect(apiSettings)` | Get ThreatConnect Object. 
`tc.owners()`                             | Get Owners object. 
`.done(function(response) {`              | Set "done" callback. 
`console.log('owner response', response)` | Console log response. 
`.error(function(response) {`             | Set "error" callback. 
`console.log('owner response error', ...` | Console log any error. 
`.retrieve();`                            | Retrieve Owners. 

<b>Summary</b>

This section explained how to:

* Connect to the ThreatConnect API
* Get a list of Owners

##Developing a JavaScript App

This section provides an overview of the JavaScript app development process as it pertains to the Spaces feature within ThreatConnect. This section will also review how to package an app for deployment to the ThreatConnect platform.

### Deployment Configuration
[Apps use a deployment configuration file to define variables and execution environment](#deployment-configuration-file)

###Query Parameters

> For the sample install configuration example above, here is a sample query String passed to the app:

```
tcSpaceElementId=467&tcToken=ABC123&tcApiPath=https://api.threatconnect.com:8443&tcType=Host&tcSelectedItem=greystoneexpress.com&tcSelectedItemOwner=TestOrg&add_tags=OpenDNS Scan&add_confidence=25&add_rating=1&opendns_api_token=abc-123&logging=info
```

> All Spaces apps will have standard 'tc' prefixed parameters passed that may be used by the app.


> The above query string can be parsed with the following JavaScript code:

```javascript
    $(document).ready(function () {

        var type = getParameterByName("tcType");
        var selectedItem = getParameterByName("tcSelectedItem");

        // startApp(type, selectedItem);
    });
 
```

All visible parameters defined in the `configuration` file will be passed to the Spaces app via a query String. The Spaces app is responsible for retrieving parameter values via the SDK's convenience function `getParameterByName`. 

All Spaces apps will have standard 'tc' prefixed parameters passed that may be used by the app.

##Optional Properties

There are some optional flags that may be used by the app to

 * handle Boolean flags that turn features on/off and to
 * encrypt parameters, like API Keys

<b>Parsing Argument Flags</b>

Apps can also use Boolean flags to designate whether to turn on a specific feature. 

The `configuration` file must have the following flag present for a Boolean parameter:

`param.<param-name>.flag`

This property will direct the ThreatConnect application to show a checkbox to the Spaces configuration. The flag will be passed to the Spaces app with a `true` or `false` parameter value. 

<b>Encrypted Parameters</b>

This property should be used to encrypt private passwords used by the app (e.g., API keys). This added level of security will allow the application to persist the password in encrypted form when at rest. The input field during job creation will be "password" text, and the key will not be visible when typed. 

![Encrypted Field](images/encrypted-field.png "Encrypted Field") 

The configuration property is defined for the encrypted parameter using the following flag:

`param.<param-name>.encrypted`

At runtime, ThreatConnect will call the Spaces app with the decrypted key. At no point in time is the password persisted in decrypted form.

Encrypted apps require that the Keychain feature be turned on, or apps with `.encrypted` parameters will not run properly.

##ThreatConnect Parameters

ThreatConnect passes standard parameters to all jobs within its standard sandbox container. There should be no assumptions made on the naming or existence of paths passed in these variables outside of the lifetime of the job execution. 

Since all Spaces apps are managed within ThreatConnect, app developers should never hard-code ThreatConnect Parameters 

ThreatConnect Parameter  | Description                                                                 
------------------------ | --------------------------------------------------------------------- 
`tcSpaceElementId`   | The unique space element instance ID for the user who added this app <br> to their Space. This numeric ID can be used by the app to store state for the user.
`tcToken`            | Session token to be used by the app to access the API. The JavaScript SDK <br> has configuration options for this parameter.
`tcApiPath`          | The path to the API defined in System Settings for all apps.
`tcType`             | Only relevant for context-aware apps. This field corresponds to the <br> runtime.context Attribute defined in the install configuration file.
`tcSelectedItem`     | Only relevant for context-aware apps. This is the actual context-item <br> identifier used within ThreatConnect. For instance, a Host identifier might be: g00gle.com
`tcSelectedItemOwner` | Only relevant for context-aware apps. This is the Owner of the context item.

<b>JavaScript Examples</b>

 * [SDK Sample index.html](https://github.com/ThreatConnect-Inc/threatconnect-javascript/blob/master/index.html)

##Authentication

The example below demonstrates how to authenticate and add an Indicator via the ThreatConnect API, using the JavaScript programming language.

<b>Dependencies</b>

File                     | URL                                             
------------------------ | ----------------------------------------------- 
enc-base-64.js           | [https://code.google.com/p/crypto-js/downloads](https://code.google.com/p/crypto-js/downloads) 
hmac-sha256.js           | [https://code.google.com/p/crypto-js/downloads](https://code.google.com/p/crypto-js/downloads) 
sha256.js                | [https://code.google.com/p/crypto-js/downloads](https://code.google.com/p/crypto-js/downloads) 

##Dependencies Installation (Linux)

> Run these commands to install dependencies:

```shell
mkdir lib
unzip CryptoJS\ v3.1.2.zip
cp CyrptoJS\ v3.1.2/enc-base-64.js lib/
cp CyrptoJS\ v3.1.2/hmac-sha256.js lib/
cp CyrptoJS\ v3.1.2/sha256.js lib/
```

> tc.js code sample:

```javascript
var CryptoJS = require('./lib/hmac-sha256.js'),
    Base64 = require('./lib/enc-base-64.js'),
    https = require('https'),
    querystring = require('querystring'),
    url = require('url');

// https.globalAgent.maxSockets = 20;

var request_time = 0;
CryptoJS = CryptoJS.CryptoJS;

var SETTINGS = {
    api_secret_key: '<ENTER API SECRET KEY HERE>',
    api_access_id: '<ENTER API ACCESS ID HERE>',
    api_base_url: '<ENTER API BASE URL HERE>',
    api_port: '443',
    verify_ssl: false
};

function getUTC() {
    var date = new Date().getTime();
    return Math.floor(date / 1000);
}

function api_request_headers(request_method, api_uri) {
    var timestamp = getUTC(),
        signature = api_uri + ":" + request_method + ":" + timestamp,
        hmac_signature = CryptoJS.HmacSHA256(signature, SETTINGS.api_secret_key),
        authorization = "TC " + SETTINGS.api_access_id + ":" + CryptoJS.enc.Base64.stringify(hmac_signature);

    return { "Timestamp": timestamp, "Authorization": authorization };
}

function apiRequest(request_uri, request_payload, http_method, body, activity_log, content_type) {
    /*
     * Default Values
     */
    activity_log = (activity_log === undefined) ? "false" : activity_log;
    // console.log('activity_log: %s', activity_log);
    body = (body === undefined) ? null : body;
    // console.log('body: %s', body);
    content_type = (content_type === undefined) ? "application/json" : content_type;
    // console.log('content_type: %s', content_type);
    http_method = (http_method === undefined) ? "GET" : http_method.toUpperCase();
    // console.log('http_method: %s', http_method);
    request_payload = (request_payload === undefined) ? {} : request_payload;
    request_payload["createActivityLog"] = activity_log;
    // console.log('request_payload: %s', request_payload);

    request_start = getUTC();

    if (SETTINGS.verify_ssl == false) {
        process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
    }

    /*
     * Prepare Request
     */
    api_url = request_uri + "?" + querystring.stringify(request_payload);
    // console.log('api_url: %s', api_url);
    path_url = url.parse(api_url).path;
    // console.log('path_url: %s', path_url);
    api_headers = api_request_headers(http_method, path_url)


    /*
     * POST
     */
    if (http_method.toUpperCase() == "POST") {
        api_headers["Content-Type"] = content_type;
        api_headers["Content-Length"] = body.length;
    }
    // console.log(JSON.stringify(api_headers, null, 4));

    /*
     * Options
     */
    var options = {
        host: SETTINGS.api_base_url,
        port: SETTINGS.api_port,
        method: http_method,
        path: api_url,
        headers: api_headers,
        keepAlive: 1,
        agent: false
    };
    // console.log(JSON.stringify(options, null, 4));

    /*
     * API call
     */
    // options.agent = new https.Agent(options);
    var api_request = https.request(options, function(res) {
        // console.log('STATUS: ' + res.statusCode);
        // console.log('HEADERS: ' + JSON.stringify(res.headers, null, 4));
        /*
        res.setEncoding('utf8');
        res.on('data', function (chunk) {
            console.log('BODY: ' + chunk);
        });
        */
    });

    api_request.write(body);
    api_request.end();

    request_time += (getUTC() - request_start);
}

function quick_add_ip(ip, rating, confidence, owner) {
    rating = (rating === undefined) ? null : rating;
    confidence = (confidence === undefined) ? null : confidence;
    owner = (owner === undefined) ? null : owner;

    request_uri = '/api/v2/indicators/addresses';

    /* body */
    var body = {"ip": ip};
    if (rating != null) {
        body["rating"] = rating;
    }
    if (confidence != null) {
        body["confidence"] = confidence;
    }

    /*
     * owner
     */
    if (owner != null) {
        var request_payload = {"owner":owner};
    } else {
        var request_payload = {}
    }
    // console.log("%s %j %j", request_uri, request_payload, body)
    apiRequest(request_uri, request_payload, 'POST', JSON.stringify(body), "false", "application/json")
}

var owner = "Example Community";
quick_add_ip('4.3.2.1', '2.5', '75', owner);
```

In the directory in which the script will be installed, run the commands in the right column. Once completed, place the example contents in tc.js.

##Indicator Retrieve

This section explains how to work with ThreatConnect Indicator Resources.

<b>Supported Indicator Types</b>

Indicator Name       | Indicator Constant 
-------------------- | --------------- 
Address              | TYPE.ADDRESS
Email Address        | TYPE.EMAIL_ADDRESS
File                 | TYPE.FILE
Host                 | TYPE.HOST
URL                  | TYPE.URL

###Retrieve Indicator

> Example of Retrieving Indicators:

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    // .type(TYPE.ADDRESS)
    .resultLimit(500)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve(function() {
        if (indicators.hasNext()) {
            indicators.next()
        }
    });
```

This example will demonstrate how to retrieve Indicators. The result set returned from this example will contain the first 500 Indicators in the "Example Community" Owner.

###Retrieve Next

> Example of retrieve.next method:

```javascript
if (indicators.hasNext()) {
    indicators.next();
}
```

> Example Results of the retrieve.next method:

```json
{
  "data": [
    {
      "id": 97262,
      "indicators": "badguys.org",
      "dateAdded": "2015-12-14T02:16:38Z",
      "lastModified": "2015-12-14T02:16:38Z",
      "ownerName": "Example Community",
      "type": "Host",
      "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=badguys.org&owner=Example+Community"
    },
    {
      "id": 94977,
      "indicators": "74.121.142.111",
      "dateAdded": "2015-12-12T01:24:28Z",
      "lastModified": "2015-12-13T23:22:28Z",
      "ownerName": "Example Community",
      "rating": 4,
      "confidence": 75,
      "type": "Address",
      "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=74.121.142.111&owner=Example+Community"
    },
    {
      "id": 94980,
      "indicators": "74.121.139.80",
      "dateAdded": "2015-12-12T01:24:28Z",
      "lastModified": "2015-12-12T01:24:28Z",
      "ownerName": "Example Community",
      "rating": 4,
      "confidence": 50,
      "type": "Address",
      "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=74.121.139.80&owner=Example+Community"
    }
  ],
  "remaining": 35,
  "url": "https://app.threatconnect.com/v2/indicators?owner=Example+Community&resultLimit=5",
  "apiCalls": 1,
  "resultCount": 40,
  "status": "Success"
}
```

The JavaScript SDK provide the `hasNext()` method for checking if more entries are available. To retrieve the next set of entries the `next()` method is available.

Note: Before the `next()` method can be called, the first API must have completed. This should not be an issue if a user click triggers the next call; however, if the `next()` method is being called programmatically then it should be passed in a function to the `retrieve()` method.

Note: The `next()` method will return the same number of results defined in the `resultsLimit()` or the number of results remaining. The same 'done' and 'error' callbacks are also used for the next set of results.

###Single Indicator

> This example will demonstrate how to retrieve a Single Indicator:

```javascipt
var indicators = tc.indicators();

indicators.owner('Example Community')
    .type(TYPE.ADDRESS)
    .indicator('10.20.30.40')
    .includeAdditional(true)     // OPTIONAL: include observationCount and faslePositiveCount
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve()
```

> Single Indicator retrieve Example Results:

```json
{
    "data": [
        {
            "id": 97934,
            "indicators": "10.20.30.40",
            "dateAdded": "2015-12-14T23:23:00Z",
            "lastModified": "2016-01-07T23:47:53Z",
            "ownerName": "Example Community",
            "rating": 3,
            "confidence": 0,
            "observationCount": 1,
            "falsePositiveCount": 0,
            "type": "Address",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=10.20.30.40&owner=Example+Community"
        }
    ],
    "remaining": 0,
    "url": "https://api.threatconnect.com/v2/indicators/addresses/10.20.30.40?owner=Example+Community&includeAdditional=true",
    "apiCalls": 1,
    "resultCount": 0,
    "status": "Success"
}
```

###Filters

> Example of how to retrieve Threats:

```javascript
var filter = new Filter(FILTER.AND);
filter.on('summary', FILTER.SW, 'bad');
filter.on('dateAdded', FILTER.GT, '2015-12-02');

var indicators = tc.indicators();

indicators.owner('Example Community')
    .resultLimit(500)
    .filter(filter)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve();

```
Starting with ThreatConnect version 4.0 the API supports filtering using query string parameters. For more information on which parameters support which operators see the ThreatConnect API Users Guide.

<b>Filter Options</b>

Filter                      | Filter Constant
--------------------------- | ---------------
And                         | FILTER.AND
Or                          | FILTER.OR 
Equal (=)                   | FILTER.OR 
Greater Than (>)            | FILTER.GT 
Greater Than or Equal (>=)  | FILTER.GE 
Less Than (<)               | FILTER.LT 
Less Than or Equal (<=)     | FILTER.LE 
Starts With (^)             | FILTER.SW 

<b>Filter Example</b>

This example will demonstrate how to retrieve Threats that start-with 'thre' and had a dateAdded value great than '2015-12-02' using an API filter.

Note that multiple filter can be added to one API call.

###Batch/Bulk Retrieve

> Example of Batch/Bulk Retrieve:

```javascript
var indicators = tc.indicatorsBatch();

indicators.owner('Example Community')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve('json');
```

Filters are not supported on Batch/Bulk downloads.

###Associations

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    .indicator('74.121.142.111')
    .type(TYPE.ADDRESS)
    .resultLimit(5)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveAssociations({
        type: TYPE.GROUP
    });
```

The JavaScript SDK provides the `retrieveAssociations()` method to retrieve both Indicator and Indicator Associations. The `type()`, and `id()` methods are required to retrieve the associations. The `retrieveAssociations()` method requires that a parameter object containing the Association `type` be provided. Optionally an `id` can be provided to pull a specific association.

###Attributes

> Example of retrieveAttributes() method:

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    .indicator('74.121.142.111')
    .type(TYPE.ADDRESS)
    .resultLimit(5)
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveAttributes();
```

The JavaScript SDK provides the `retrieveAttributes()` method to retrieve attributes. Both the `type()` method and `id()` are required to retrieve the attributes. An `id` can be passed to the `retrieveAttributes()` method to retrieve a specific attribute.

###Retrieve Observations

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    .indicator('74.121.142.111')
    .type(TYPE.ADDRESS)
    .resultLimit(5)
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveObservations();
```

The JavaScript SDK provides the `retrieveObservations()` method to retrieve Observations. Both the `type()` method and `id()` are required to retrieve the Observations.

###Retrieve Observation Count

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    .indicator('74.121.142.111')
    .type(TYPE.ADDRESS)
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveObservationCount();
```

The JavaScript SDK provides the `retrieveObservationCount()` method to retrieve the Observation Count for an Indicator. Both the `type()` method and `id()` are required to retrieve the Observation Count.

NOTE: The Observation Count can also be retrieved with the "Single Indicator" method described above using the includeAdditional parameter.

###Retrieve Security Labels Method

> Example of retrieveSecurityLabel() method:

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    .indicator('74.121.142.111')
    .type(TYPE.ADDRESS)
    .resultLimit(5)
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveSecurityLabel();
```

###Retrieve Tags Method

> Example of retrieveTags() method:

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    .indicator('74.121.142.111')
    .type(TYPE.ADDRESS)
    .resultLimit(5)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveTags();
```

The JavaScript SDK provides the `retrieveTags()` method to retrieve tags. Both the `type()` method and `id()` are required to retrieve the tags.

##Tags Retrieve

> Example of how to retrieve Tags:

```javascript
tc.tags()
    .owner('Example Community')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve();
```

> Example of retrieve Tags results:

```json
{
  "data": [
    {
      "name": "APT",
      "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=APT&owner=Example+Community"
    },
    {
      "name": "BadGuy",
      "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=BadGuy&owner=Example+Community"
    },
    {
      "name": "blah",
      "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=blah&owner=Example+Community"
    },
    {
      "name": "threat_tag",
      "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=threat_tag&owner=Example+Community"
    }
  ],
  "remaining": 0,
  "url": "https://api.threatconnect.com/v2/tags",
  "apiCalls": 1,
  "resultCount": 11,
  "status": "Success"
}
```

This section explains how to work with ThreatConnect Tags Resources.

This example will demonstrate how to retrieve Tags. The result set returned from this example will contain all Tags to which the API credential being used has access. Optionally the `name()` method can be used to pass a specific Tag name.

## Owners Retrieve

> Retrieve Owners Example:

```javascript
tc.owners()
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve();
```

> Example Owners Results:

```json
{
  "data": [
    {
      "id": 2,
      "name": "SumX",
      "type": "Organization"
    },
    {
      "id": 3,
      "name": "Local Common Community",
      "type": "Source"
    },
    {
      "id": 4,
      "name": "Blocklist.de Source",
      "type": "Source"
    },
    {
      "id": 10,
      "name": "Example Community",
      "type": "Community"
    }
  ],
  "remaining": 0,
  "url": "https://demo.threatconnect.com/api/v2/owners",
  "apiCalls": 1,
  "resultCount": 9,
  "status": "Success"
}
```

This section explains how to work with ThreatConnect Owners Resources.

### Metrics

> Retrieving Owner Metrics:

```javascript
tc.owners()
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveMetrics();
```

Starting with ThreatConnect platform version 4.0 retrieving Owner metrics is supported. Owner metrics provides the summed data for the last 15 days. Optionally the `id()` method can be used to pass a specific Owner ID.

## Group Retrieve

This section explains how to work with ThreatConnect Group Resources.

<b>Supported Group Types</b>

Group Name           | Group Constant 
---------------------| --------------- 
Adversary            | TYPE.ADVERSARY
Document             | TYPE.DOCUMENT
Email                | TYPE.EMAIL
Incident             | TYPE.INCIDENT
Signature            | TYPE.SIGNATURE
Threat               | TYPE.THREAT

### Retrieve Group

> Example of how to retrieve Adversaries:

```javascript
groups = tc.groups();

groups.owner('Example Community')
    .type(TYPE.ADVERSARY)
    .resultLimit(500)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve();
```

This example will demonstrate how to retrieve Adversaries. The result set returned from this example will contain the first 500 Adversaries in the "Example Community" Owner.

### Retrieve Next

> Example of hasNext() method:

```javascript
while (groups.hasNext()) {
    groups.next();
}
```

> Example of Results:

```json
{
  "data": [
    {
      "id": 81,
      "name": "adver-000",
      "ownerName": "Example Community",
      "dateAdded": "2015-10-30T05:46:21Z",
      "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=81"
    },
    {
      "id": 189,
      "name": "adver-001",
      "ownerName": "Example Community",
      "dateAdded": "2015-11-02T13:55:45Z",
      "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=189"
    },
    {
      "id": 1,
      "name": "adver-015",
      "ownerName": "Example Community",
      "dateAdded": "2015-10-23T21:10:14Z",
      "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=200"
    }
  ],
  "remaining": 0,
  "url": "https://api.threatconnect.com/v2/groups/adversaries/?createActivityLog=false&resultLimit=500&resultStart=0&owner=Example+Community",
  "apiCalls": 1,
  "resultCount": 15,
  "status": "Success"
}
```

The JavaScript SDK provide the `hasNext()` method for checking if more entries are available. To retrieve the next set of entries the `next()` method is available.

Note: Before the `next()` method can be called the first API must have completed. This should not be an issue if a user click triggers the next call, however if the `next()` method is being called programmaticly then it should be passed in a function to the `retrieve()` method.

Note: The `next()` method will return the same number of results defined in the `resultsLimit()` or the number of results remaining. The same 'done' and 'error' callbacks are also used for the next set of results.

## Filters

> Example of how to retrieve Threats that start-with 'thre' and had a dateAdded value great than '2015-12-02' using an API filter:

```javascript
filter = new Filter(FILTER.AND);
filter.on('name', FILTER.SW, 'threat');
filter.on('dateAdded', FILTER.GT, '2015-12-02');

groups = tc.groups();

groups.owner('Example Community')
    .type(TYPE.THREAT)
    .resultLimit(500)
    .filter(filter)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve();
```
Starting with ThreatConnect version 4.0 the API supports filtering using query string parameters. For more information on which parameters support which operators see the ThreatConnect API Users Guide.

Filter Options              | Filter Constant
--------------------------- | ---------------
And                         | FILTER.AND
Or                          | FILTER.OR
Equal (=)                   | FILTER.OR
Greater Than (>)            | FILTER.GT
Greater Than or Equal (>=)  | FILTER.GE
Less Than (<)               | FILTER.LT
Less Than or Equal (<=)     | FILTER.LE
Starts With (^)             | FILTER.SW

<b>Filter Example</b>

This example will demonstrate how to retrieve Threats that start-with 'thre' and had a dateAdded value great than '2015-12-02' using an API filter.

Note that multiple filter can be added to one API call.

##Retrieve Associations

> Example of retrieveAssociations() method:

```javascript
tc.groups()
    .owner('Example Community')
    .type(TYPE.INCIDENT)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveAssociations({
        type: TYPE.ADVERSARY,
        id: 253
    });
```

The JavaScript SDK provides the `retrieveAssociations()` method to retrieve both Indicator and Group Associations. The `type()`, and `id()` methods are required to retrieve the associations. The `retrieveAssociations()` method requires that a parameter object containing the association `type` be provided. Optionally an `id` can be provided to pull a specific association.

##Retrieve Attributes

> Example of retrieveAttributes() method:

```javascript
tc.groups()
    .owner('Example Community')
    .type(TYPE.INCIDENT)
    .id(173)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveAttributes();
```

The JavaScript SDK provides the `retrieveAttributes()` method to retrieve attributes. Both the `type()` method and `id()` are required to retrieve the attributes. An `id` can be passed to the `retrieveAttributes()` method to retrieve a specific attribute.

##Retrieve Tags

> Example of retrieveTags() method:

```javascript
tc.groups()
    .owner('Example Community')
    .type(TYPE.INCIDENT)
    .id(173)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveTags();
```

The JavaScript SDK provides the `retrieveTags()` method to retrieve tags. Both the `type()` method and `id()` are required to retrieve the tags.

##Retrieve Security Labels

> Example of retrieveSecurityLabel() method:

```javascript
tc.groups()
    .owner('Example Community')
    .type(TYPE.INCIDENT)
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieveSecurityLabel();
```

The JavaScript SDK provides the `retrieveSecurityLabel()` method to retrieve security labels. Both the `type()` method and `id()` are required to retrieve the security label.

## Retrieve Tasks

This example will demonstrate how to retrieve Tasks. The result set returned from this example will contain all Tasks that the API credential being used have access. Optionally the `id()` method can be used to pass a specific task id to retrieve.

### Example

```javascript
tc.tasks()
    .owner('Example Community')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve();
```

### Example Results

```json
{
  "data": [{
    "id": 571,
    "name": "Test Task",
    "ownerName": "Example Community",
    "dateAdded": "2016-03-11T20:15:52Z",
    "webLink": "https://app.threatconnect.com/auth/workflow/task.xhtml?task=571",
    "status": "In Progress",
    "escalated": false,
    "reminded": false,
    "overdue": true,
    "dueDate": "2016-03-11T00:00:00Z",
    "reminderDate": "2016-03-14T20:14:00Z",
    "escalationDate": "2016-03-22T20:14:00Z"
  }],
  "remaining": 0,
  "url": "https://api.threatconnect.com/v2/tasks?resultLimit=500&owner=Example+Community",
  "apiCalls": 1,
  "resultCount": 1,
  "status": "Success"
}
```

## Retrieve Victims

This example will demonstrate how to retrieve Victims. The result set returned from this example will contain all Victims that the API credential being used have access. Optionally the `id()` method can be used to pass a specific task id to retrieve.

### Example

```javascript
tc.victims()
    .owner('Example Community')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .retrieve();
```

### Example Results
```json
{
    "data": [{
        "id": 20,
        "name": "Robin Scherbatsky",
        "org": "Fox News",
        "suborg": "Anchor",
        "workLocation": "New York City, New York",
        "nationality": "Canadian",
        "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=20"
    }, {
        "id": 4,
        "name": "Bob Steal",
        "org": "Fox News",
        "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=4"
    }, {
        "id": 3,
        "name": "Rodney Pear",
        "org": "Fox News",
        "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=3"
    }],
    "remaining": 0,
    "url": "https://api.threatconnect.com/api/v2/victims?resultLimit=500&owner=Example+Community",
    "apiCalls": 1,
    "resultCount": 3,
    "status": "Success"
}
```


##Indicator Commit
This section explains how to work with ThreatConnect Indicator Resources.

<b>Supported Indicator Types</b>

Indicator Name       | Indicator Constant |
-------------------- | --------------- |  
Address              | TYPE.ADDRESS |
Email Address        | TYPE.EMAIL_ADDRESS |
File                 | TYPE.FILE |
Host                 | TYPE.HOST |
URL                  | TYPE.URL |

###Commit Indicator

> Example of how to add an Address indicator to the "Example Community" Owner:

```javascript
var indicators = tc.indicators();

indicators.owner('Example Community')
    .indicator('10.20.30.40')
    .type(TYPE.ADDRESS)
    .rating(3)
    .confidence(75)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commit();
```

> Example Results:

```json
{
  "data": [
    {
      "id": 97932,
      "indicators": "10.20.30.40",
      "dateAdded": "2015-12-14T22:41:39Z",
      "lastModified": "2015-12-14T22:41:39Z",
      "ownerName": "Example Community",
      "rating": 3,
      "confidence": 55,
      "type": "Address",
      "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=10.20.30.40&owner=Example+Community"
    }
  ],
  "remaining": 0,
  "url": "https://api.threatconnect.com/v2/indicators/addresses?owner=Example+Community",
  "apiCalls": 1,
  "body": "{\"ip\":\"10.20.30.40\",\"rating\":3,\"confidence\":55}",
  "resultCount": 0,
  "status": "Success"
}
```

This example will demonstrate how to add an Address indicator to the "Example Community" Owner. For indicator specific parameters refer to the ThreatConnect API User Guide.

###Batch/Bulk Commit

> Example of Batch/Bulk Commit:

```javascript
var indicators = tc.indicatorsBatch();

indicators.owner('Example Community')
    .action('Create')
    .attributeWriteType('Append')
    .haltOnError(false)
    .done(function(response) {
        c.log('response', response);
    })
    .error(function(response) {
        c.log('error response', response);
    });
    

for (i = 1; i <= 5; i++) {
    indicators.indicator('10.10.10.' + i)
        .type(TYPE.ADDRESS)
        .rating(3)
        .confidence(42)
        .attributes([
            {
                type: 'Description',
                value: 'Example Description'
            }
        ])
        .tags([
            'Example',
            'JS_SDK'
        ])
        .add()
}

indicators.commit();
```

Filters are not supported on Batch/Bulk downloads.

###Commit Association

The JavaScript SDK provides the `commitAssociation()` method to add Group Associations. Both `.type()`, and `id()` methods are required to commit the Associations. The value passed to the `commitAssociation()` method must be the specific Group Type (e.g., TYPE.ADVERSARY, TYPE.HOST).

> Example of commitAssociations() method:

```javascript
tc.indicators()
    .owner('Example Community')
    .type(TYPE.ADDRESS)
    .indicator('10.20.30.40')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAssociation({
        type: TYPE.ADVERSARY,
        id: '253'
    });
```

###Commit Attribute

> Example of commitAttributes() method:

```javascript
tc.indicators()
    .type(TYPE.ADDRESS)
    .indicator('10.20.30.40')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAttribute({
        type: 'Description',
        value: 'This is a description.'
    });
```

The JavaScript SDK provides the `commitAttribute()` method to add Attributes. Both `.type()` and `id()` are required to add Attributes. The Attribute object should be passed to `commitAttribute()` method with a type and value parameter.

###Commit Tags

> Example of commitTags() method:

```javascript
tc.indicators()
    .owner('Example Community')
    .type(TYPE.ADDRESS)
    .indicator('10.20.30.40')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitTags('Example Tag');
```

The JavaScript SDK provides the `commitTags()` method to add Tags. Both the `.type()` method and `id()` are required to add the Tags. The Tag value should be passed to the `commitTags()` method.

###Commit Security Labels

> Example of commitSecurityLabel() method:

```javascript
tc.indicators()
    .type(TYPE.ADDRESS)
    .indicator('10.20.30.40')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitSecurityLabel('TLP Red');
```

###Putting it all Together

> Example of how to add an Adversary with a name of 'adver-999' to the "Example Community" owner

```javascript
indicators.owner('Example Community')
    .indicator('10.20.30.40')
    .type(TYPE.ADDRESS)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commit(function() {
        indicators.commitAssociation({
            type: TYPE.INCIDENT,
            id: 256
        });
        indicators.commitAttribute({
            type: 'Description',
            value: 'Example Description.'
        });
        indicators.commitObservation({
            count: 1,
            dateObserved: '2008-12-12T14:26:45-06:00'
        });
        indicators.commitTag('Example');
        indicators.commitSecurityLabel('TLP Red');
    });
```

This example will demonstrate how to add an Adversary with a name of 'adver-999' to the "Example Community" owner. It passes a callback to the commit() method that will add a group and indicators association, attribute, tag, and security label. Any number of Associations, Attributes, or Tags can be added in the callback.

Note: To ensure that commits for the metadata happen after the commit of the Indicator, pass a callback to the Indicator Commit method.

##Group Commit

This section explains how to work with ThreatConnect Group Resources.

<b>Supported Group Types</b>

Group Name           | Group Constant 
---------------------| --------------- 
Adversary            | TYPE.ADVERSARY
Document             | TYPE.DOCUMENT
Email                | TYPE.EMAIL
Incident             | TYPE.INCIDENT
Signature            | TYPE.SIGNATURE
Threat               | TYPE.THREAT

###Commit Group

> Example of how to add an Adversaries with a name of 'adver-001' to the "Example Community" Owner:

```javascript
groups = tc.groups();

groups.owner('Example Community')
    .name('adver-001')
    .type(TYPE.ADVERSARY)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commit();
```

> Example Results:

```json
{
  "data": [
    {
      "id": 265,
      "name": "adver-001",
      "dateAdded": "2015-12-13T15:50:08Z",
      "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=265",
      "ownerName": "Example Community"
    }
  ],
  "remaining": 0,
  "url": "https://api.threatconnect.com/v2/groups/adversaries/?createActivityLog=false&owner=Example+Community",
  "apiCalls": 1,
  "body": "{\"name\":\"adver-001\"}",
  "resultCount": 0,
  "status": "Success"
}
```

This example will demonstrate how to add an Adversary with a name of 'adver-001' to the "Example Community" Owner. For group specific parameters refer to the ThreatConnect API User Guide.

###Commit Associations

> Example of commitAssociations() method:

```javascript
tc.groups()
    .owner('Example Community')
    .type(TYPE.INCIDENT)
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAssociation({
        type: TYPE.ADDRESS,
        id: '74.121.142.111'
    });
```

The JavaScript SDK provides the `commitAssociations()` method to add both Indicator and Group Associations. The `.type()`, `id()`, `associationType()`, and `associationId()` methods are required to commit the associations. The value passed to the `associationType()` method must be the specific Group or Indicator Type (e.g., TYPE.ADVERSARY, TYPE.HOST).

###Commit Attributes

> Example of commitAttributes() method:

```javascript
tc.groups()
    .type(TYPE.INCIDENT)
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAttribute({
        type: 'Description',
        value: 'This is a description.'
    });
```

The JavaScript SDK provides the `commitAttributes()` method to add attributes. The `.type()` and `id()` are required to add attributes. The  attribute object should be passed to the `commitAttribute()` method with a type and value parameter.

###Commit False Positive

```javascript
tc.indicators
    .owner('Example Community')
    .indicator('10.20.30.40')
    .type(TYPE.ADDRESS)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitFalsePositive();
```

The JavaScript SDK provides the `commitFalsePositive()` method to add a False Positive mark on an Indicator. Both .type() and id() are required to add a False Positive mark.

###Commit Observation Method

```javascript
tc.indicators
    .owner('Example Community')
    .indicator('10.20.30.40')
    .type(TYPE.ADDRESS)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitObservation({
        count: 1,
        dateObserved: '2008-12-12T14:26:45-06:00'
    });
```

The JavaScript SDK provides the `commitObservation()` method to add an Indicator Observation. Both .type() and id() are required to add an Observation. The Observation Count and dateObserved values should be passed to the `commitObservation() method`.

###Commit Tag Method

> Example of commitTag() method:

```javascript
tc.groups()
    .type(TYPE.INCIDENT)
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitTag('Example Tag');
```

The JavaScript SDK provides the `commitTag()` method to add tags. Both the `.type()` method and `id()` are required to add the tags. The tag value should be passed to the `commitTag()` method.

###Commit Security Label

> Example of commitSecurityLabel() method:

```javascript
tc.groups()
    .type(TYPE.ADDRESS)
    .indicator('10.20.30.40')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitSecurityLabel('TLP Red');
```



###Putting it all Together

> Example of how to add an Adversary with a name of 'adver-999' to the "Example Community" owner

```javascript
groups = tc.groups();

groups.owner('Example Community')
    .name('adver-999')
    .type(TYPE.ADVERSARY)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commit(function() {
        groups.commitAssociation({
            type: TYPE.ADDRESS,
            id: '74.121.142.111'
        });
        groups.commitAssociation({
            type: TYPE.INCIDENT,
            id: 256
        });
        groups.commitAttribute({
            type: 'Description',
            value: 'Example Description.'
        });
        groups.commitTag('Example');
        groups.commitSecurityLabel('TLP Red');
    });
```

This example will demonstrate how to add an Adversary with a name of 'adver-999' to the Example Community Owner. It passes a callback to the `commit()` method that will add a Group and Indicators Association, Attribute, Tag, and Security Label. Any number of Associations, Attributes, or Tags can be added in the callback.

Note: To ensure that commits for the metadata happen after the commit of the Group pass a callback to the Group Commit method.

## Commit Task
This example will demonstrate how to add a Task with a name of 'task-001' to the "Example Community" Owner.

### Example
```javascript
tc.tasks()
    .owner('Example Community')
    // required
    .name('Test Task')
    // optional
    .assignee([{'userName': 'joe-user@gmail.com'}])
    .escalatee([{'userName': 'juser'}])
    .dueDate('2017-01-02T03:04:05Z')
    .escalationDate('2018-01-02T03:04:05Z')
    .reminderDate('2017-01-01T03:04:05Z')
    .escalated(false)
    .reminded(false)
    .overdue(false)
    .status('In Progress')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commit();
```

### Example Results
```json
{
    "data": {
        "id": 600,
        "name": "Test Task",
        "owner": {
            "id": 2,
            "name": "SumX",
            "type": "Organization"
        },
        "dateAdded": "2016-03-17T17:13:30Z",
        "webLink": "https://demo.threatconnect.com/auth/workflow/task.xhtml?task=600",
        "status": "In Progress",
        "escalated": false,
        "reminded": false,
        "overdue": false,
        "dueDate": "2017-01-02T03:04:05Z",
        "reminderDate": "2017-01-01T03:04:05Z",
        "escalationDate": "2018-01-02T03:04:05Z",
        "assignee": [{
            "userName": "joe-user@gmail.com",
            "firstName": "Joe",
            "lastName": "User"
        }],
        "escalatee": [{
            "userName": "joe-admin@gmail.com",
            "firstName": "Joe",
            "lastName": "Admin"
        }]
    },
    "remaining": 0,
    "url": "https://demo.threatconnect.com/api/v2/tasks/?resultLimit=500&owner=SumX",
    "apiCalls": 1,
    "body": "{\"name\":\"Test Task\",\"assignee\":[{\"userName\":\"joe-user@gmail.com\"}],\"escalatee\":[{\"userName\":\"juser\"}],\"dueDate\":\"2017-01-02T03:04:05Z\",\"escalationDate\":\"2018-01-02T03:04:05Z\",\"reminderDate\":\"2017-01-01T03:04:05Z\",\"escalated\":false,\"reminded\":false,\"overdue\":false,\"status\":\"In Progress\"}",
    "resultCount": 0,
    "status": "Success"
}
```

## Commit Victim
This example will demonstrate how to add a Victim with a name of 'task-001' to the "Example Community" Owner.

### Example
```javascript
victim.owner('Example Community')
    .name('Robin Scherbatsky')
    .org('Fox News')
    .suborg('Anchor')
    .workLocation('New York City, New York')
    .nationality('Canadian')
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .commit();
```

### Example Results
```json
{
    "data": {
        "id": 22,
        "name": "Robin Scherbatsky",
        "org": "Fox News",
        "suborg": "Anchor",
        "workLocation": "New York City, New York",
        "nationality": "Canadian",
        "webLink": "https://demo.threatconnect.com/auth/victim/victim.xhtml?victim=22"
    },
    "remaining": 0,
    "url": "https://demo.threatconnect.com/api/v2/victims?resultLimit=500&owner=Example+Community",
    "apiCalls": 1,
    "body": "{\"name\":\"Robin Scherbatsky\",\"org\":\"Fox News\",\"suborg\":\"Anchor\",\"workLocation\":\"New York City, New York\",\"nationality\":\"Canadian\"}",
    "resultCount": 0,
    "status": "Success"
}
```

## Associations
The JavaScript SDK provides the `commitAssociations()` method to add both Indicator and Group Associations. The `.type()`, `id()`, `associationType()`, and `associationId()` methods are required to commit the associations. The value passed to the `associationType()` method must be the specific Group or Indicator Type (e.g. TYPE.ADVERSARY, TYPE.HOST).

```javascript
tc.tasks()
    .owner('Example Community')
    .id(571)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAssociation({
        type: TYPE.ADDRESS,
        id: '74.121.142.111'
    });
```

```javascript
tc.tasks()
    .owner('Example Community')
    .id(571)
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAssociation({
        type: TYPE.INCIDENT,
        id: 569
    });
```

## Attributes
The JavaScript SDK provides the `commitAttributes()` method to add attributes. The `id()` method is required to add attributes. The  attribute object should be passed to `commitAttribute()` method with a type and value parameter.

```javascript
tc.tasks()
    .id(571)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAttribute({
        type: 'Description',
        value: 'This is a description.'
    });
```

## Tags
The JavaScript SDK provides the `commitTags()` method to add tags. The `id()` method is required to retrieve the task. The tag value should be passed to the `commitTags()` method.

```javascript
tc.tasks()
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitTags('Example Tag');
```

## Security Labels

```javascript
tc.tasks()
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitSecurityLabel('TLP Red');
```

## Putting it all Together

This example will demonstrate how to add a Task with a name of 'task-999' to the "Example Community" owner. It passes a callback to the `commit()` method that will add a group and indicators association, attribute, tag, and security label. Any number of Associations, Attributes, or Tags can be added in the callback.

```javascript
tasks = tc.tasks();

tasks.owner('Example Community')
    .name('task-999')
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commit(function() {
        tasks.commitAssociation({
            type: TYPE.ADDRESS,
            id: '74.121.142.111'
        });
        tasks.commitAssociation({
            type: TYPE.INCIDENT,
            id: 256
        });
        tasks.commitAttribute({
            type: 'Description',
            value: 'Example Description.'
        });
        tasks.commitTag('Example');
        tasks.commitSecurityLabel('TLP Red');
    });
```

> Note: To ensure the commits for the metadata happen after the commit of the task pass a callback to the group commit method.



## Associations
The JavaScript SDK provides the `commitAssociations()` method to add both Indicator and Group Associations. The `.type()`, `id()`, `associationType()`, and `associationId()` methods are required to commit the associations. The value passed to the `associationType()` method must be the specific Group or Indicator Type (e.g. TYPE.ADVERSARY, TYPE.HOST).

```javascript
tc.victims()
    .owner('Example Community')
    .id(571)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAssociation({
        type: TYPE.ADDRESS,
        id: '74.121.142.111'
    });
```

```javascript
tc.victims()
    .owner('Example Community')
    .id(571)
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAssociation({
        type: TYPE.INCIDENT,
        id: 569
    });
```

## Attributes
The JavaScript SDK provides the `commitAttributes()` method to add attributes. The `id()` method is required to add attributes. The  attribute object should be passed to `commitAttribute()` method with a type and value parameter.

```javascript
tc.victims()
    .id(571)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitAttribute({
        type: 'Description',
        value: 'This is a description.'
    });
```

## Tags
The JavaScript SDK provides the `commitTags()` method to add tags. The `id()` method is required to retrieve the victim. The tag value should be passed to the `commitTags()` method.

```javascript
tc.victims()
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitTags('Example Tag');
```

## Security Labels

```javascript
tc.victims()
    .id(256)
    .done(function(response) {
        console.log('response', response);
    })
    .error(function(response) {
        console.log('error response', response);
    })
    .commitSecurityLabel('TLP Red');
```

## Putting it all Together
This example will demonstrate how to add a Victim with a name of 'task-999' to the "Example Community" owner. It passes a callback to the `commit()` method that will add a group and indicators association, attribute, tag, and security label. Any number of Associations, Attributes, or Tags can be added in the callback.

```javascript
victim = tc.victims();

victim.owner('Example Community')
    .name('Robin Scherbatsky')
    .org('Fox News')
    .suborg('Anchor')
    .workLocation('New York City, New York')
    .nationality('Canadian')
    .done(function(response) {
        console.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        console.log('error response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .commit(function() {
        // add email address asset
        victim.address('robin.scherbatsky@foxnews.com')
            .addressType('Work')
            .commitAsset(TYPE.VICTIM_ASSET_EMAIL_ADDRESSES);
            
        // add network account asset
        victim.account('robin')
            .network('LDAP')
            .commitAsset(TYPE.VICTIM_ASSET_NETWORK_ACCOUNTS);
            
        // add phone number asset
        victim.phoneType('222-222-2222')
            .commitAsset(TYPE.VICTIM_ASSET_PHONE_NUMBERS);
            
        // add social network asset
        victim.account('RobinSparkles')
            .network('FaceBook')
            .commitAsset(TYPE.VICTIM_ASSET_SOCIAL_NETWORKS);
            
        // add webSite
        victim.webSite('https://www.robinsparkles.com')
            .commitAsset(TYPE.VICTIM_ASSET_WEBSITES);
    
        // add indicator associations
        victim.commitAssociation({
            type: TYPE.ADDRESS,
            id: '74.121.142.111'
        });
    
        // add group association
        victim.commitAssociation({
            type: TYPE.INCIDENT,
            id: 256
        });
        
        // add attribute association
        victim.commitAttribute({
            type: 'Description',
            value: 'Example Description.'
        });
        
        // add tag
        victim.commitTag('Example');
        
        // add securityLabel
        victim.commitSecurityLabel('TLP Red');
    });
```

> Note: To ensure the commits for the metadata happen after the commit of the task pass a callback to the group commit method.

##Manual API Calls

> The example below accesses the API by allowing the creation of a requestObject():

```
tc.requestObject()
ro.apiRequest(ro);
```

The JavaScript SDK supports a manual way to access the API by allowing the creation of a `requestObject()` and submitting these objects to the `apiRequest()` method. The returned result will contain API response.

###Retrieving Indicators

> The example below displays how to create a `RequestObject` that will retrieve all Indicators from a specified Owner:

```javascript
var ro = tc.requestObject();

ro.owner('Example Community')
    .createActivityLog(false)
    .requestUri('v2/indicators')
    .requestMethod('GET')
    .resultLimit(250)
    .resultStart(0)
    .done(function(response) {
        c.log('response', response);
    })
    .error(function(response) {
        c.log('error response', response);
    })
    .apiRequest('manual');
```

This example displays how to create a `RequestObject` that will retrieve all Indicators from a specified Owner.

###Downloading Document Contents

> The example below displays how to create a `RequestObject` that will retrieve the contents of a document stored in a Document Resource:

```javascript
var ro = tc.requestObject();

ro.owner('Example Community')
    .createActivityLog(false)
    .requestUri('v2/groups/documents/261/download')
    .requestMethod('GET')
    .done(function(response) {
        c.log('response', response);
    })
    .error(function(response) {
        c.log('error response', response);
    })
    .apiRequest('manual');
```

This example displays how to create a `RequestObject` that will retrieve the contents of a document stored in a Document Resource.

###Creating and Uploading Documents

> The example below displays how to create a `RequestObject` that will create a Document Resource in ThreatConnect and upload a file to this Resource.

```javascript
var ro = tc.requestObject();

ro.owner('Example Community')
    .createActivityLog(false)
    .requestUri('v2/groups/documents/263/upload')
    .requestMethod('POST')
    .body('Content of file.')
    .contentType('application/octet-stream')
    .done(function(response) {
        c.log('response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .error(function(response) {
        c.log('error response', response);
        $('#response-content').append(JSON.stringify(response, null, 4));
    })
    .apiRequest('manual');
```

This example displays how to create a `RequestObject` that will create a Document Resource in ThreatConnect and upload a file to this Resource.

###Query String Parameters

> This example shows how to add filters to a manual request using the `payload()` option.

```javascript
var ro = tc.requestObject();

ro.owner('Example Community')
    .payload('filters', 'summary="1.2.3.4",rating>3')


```

The JavaScript SDK `requestObject` provides the `payload()` method to add any additional query string parameters. This example shows how to add filters to a manual request using the `payload()` option.

Query String Parameter | Helper Method 
---------------------- | ------------- 
owner                  | owner() 
createActivityLog      | createActivityLog() 
resultLimit            | resultLimit() 
resultStart            | resultStart() 
filters                | manually via payload() 
orParams               | manually via payload() 

For a full list of query string parameters supported by the ThreatConnect API reference the ThreatConnect API User Guide.

# Deployment Configuration File

A configuration file named `install.json` is used for ThreatConnect apps written in:

- Python
- Java
- JavaScript (Spaces) 

## Standard Section

Standard section defines required and optional properties to all apps in ThreatConnect. The required properties are properties that must be provided for any packaged app installed through the ThreatConnect platform. The optional properties provide additional information based on the type of target app.

The table below lists all of the properties of the Standard section.

| Property|Required?|Allowed Values|Description |
|--- |--- |--- |--- |
|programVersion|Yes|Any|This	property is the version for this app as it should be displayed to the System Settings Page under Apps.|
|programLanguage|Yes|JAVA<br>PYTHON<br>NONE|This	property is the language runtime environment used by the ThreatConnect Job Executor. It is relevant for apps that run on the Job Execution Engine and can be set to NONE for Spaces apps.|
|programMain|Yes	for Python and Java Apps|Any|This property is the entry point into the app. For Python apps, it is generally the .py file (or exclude the extension if running it as a module). For Java apps, it is the main class the Job Execution	Engine should use when calling the app using the Java Runtime Environment.|
|languageVersion|No|Any|This	property is used purely for tracking purposes and does not affect	the version of Python or Java used by the Job Execution Engine.|
|runtimeLevel|Yes|Organization<br>SpaceOrganization<br>System|This	property describes the type of app and how it should be used within ThreatConnect. For further details on this property, see	the “Runtime Level” section.|
|runtimeContext|No|Array of Strings:<br>Url, Host, Address, EmailAddress, File, Threat, Incident, Email, Document, Signature, Tag, Adversary, Victim, Menu, Search|This	property is relevant for SpaceOrganization apps only. This array	of Strings enables Spaces apps to be context aware. For further	details on this property, see the “Runtime Context” section.|
|repeatingMinutes|No|Array of Integers<br>Example:<br>[15,30,60,120,240,360]|This	property is a list of minute increments to display in the “Repeat	Every…” section in the “Schedule” panel in the Job	Wizard. This property is relevant only for Python and Java apps	for which the developer wants to control how frequently an app	can be executed. If this property is not defined, the default	listing is as follows: [ 60, 120, 240, 360, 720 ]|
|allowOnDemand|Yes|Boolean|This	property allows an app to display the “Run Now” button in the ThreatConnect platform when configured as a Job.|

### Runtime Level

The **runtimeLevel** property allows three distinct values that dictate how the app is used within the ThreatConnect platform, as detailed in the table below.

|	Value	|	Description	|
|--- |--- |
|Organization|This	value is a Python or Java app that is run by the Job Execution	Engine. This type of app must be provisioned to specific	organizations (or “Allow All Orgs” must be selected) by the	System Admin. Once provisioned, the app can be scheduled to run	as part of a Job.|
|SpaceOrganization|This value is a Spaces app that is run within ThreatConnect as a Space. This type of app must be provisioned to specific organizations (or “Allow All Orgs” must be selected) by the System Admin. Once provisioned, the app can be added as a Spaces app by any user belonging to the Organization.|
|System|Although not commonly used, the System level is a Python or Java app that is strictly visible by the System Admin. This app can be scheduled only in a System Job.|

### Runtime Context

The **runtimeContext** property enables Spaces apps to be context aware. Users are able to add context-aware Spaces apps to their Spaces in the respective **Details** page of the ThreatConnect platform. Because this property is an array of Strings, the app can be displayed in multiple Spaces within the ThreatConnect platform,
including the **Menu** and **Search** pages.

NOTE: 
Context-aware Spaces apps are passed contextual information via the URL query string when the app is displayed in the ThreatConnect platform. The details of those parameters are out of scope for this document.

## Parameter Array Section

The Parameter Array section of the **install.json** file is the mechanism used by the Job Execution engine and the Spaces framework to pass configuration data at runtime. For Java and Python apps, the entries defined in this section dictate the **Parameters** panel in the Job Wizard in the ThreatConnect platform. Spaces apps have their own configuration screen as part of the user’s Space for each app.

The table below highlights the Parameter Array properties (the **params** array).

|Property|Required|Allowed Values|Description|
|--- |--- |--- |--- |
|name|Yes|Any|This property is the internal parameter name taken from the Job Wizard	and passed to the app at runtime. It is the effective	command-line argument name passed to the app.|
|label|Yes|Any|This	property is a description of the parameter displayed in the	ThreatConnect platform Job Wizard or Spaces Config dialog box.|
|sequence|No|Integer|This	property is the number used to control the ordering of the	parameters in the Job Wizard or Spaces Config dialog box. If it	is not defined, the order of the parameters in the install.json	file is used.|
|required|No|Boolean|This	property designates this parameter as a required field that must	be populated to save the Job. Required parameters would fail an	app at runtime or cause unexpected results.|
|default|No|Any|This	property is the default value pre-populated for new Jobs or	Spaces. The purpose of a default value is to provide the user	with a guidance while allowing edits based on preference.|
|type|No|String, Choice, MultiChoice, Boolean|Data	types enable the UI to display relevant components and allow the Job Executor to adapt how parameters are passed to an app at	runtime. For further details on this parameter, see the “Type Parameter”	section.|
|encrypt|No|Boolean|This	property designates this parameter as an encrypted value.	Parameters defined as encrypted will be managed by the Keychain	feature that encrypts password while at rest. This flag should be	used with the “String” type and will render a password input	textbox in the Job and Spaces configuration.|
|allowMultiple|No|Boolean|The	value of this property is automatically set to “true” if the	“MultiChoice” type is used. If a “String” type is used,	this flag allows the user to define multiple values in a single	input field delimited by a pipe (“|”) character.|
|validValues|No|String	Array|This	property is used with the “Choice” and “MultiChoice”	types to restrict the possible values a user can select. For	instance, to define a “loggingLevel” parameter, this field	could have the following values: ["FATAL", "ERROR",	"WARN", "INFO", "DEBUG", "TRACE"].|
|hidden|No|Boolean|If	this property is set to “true”, this parameter will be hidden	from the Job Wizard. Hidden parameters allow the developer to	persist parameters between job executions without the need to	render the values in the Job Wizard. This option is valid only for Python and Java apps. Further details on persisting	parameters from the app directly are out of scope for this	document.|
|setup|No|Boolean|This	property is reserved for the App Profiles feature. Further	details on this feature are out of scope for this document.|

NOTE:
In Python, parameters are called by using the “--param &lt;value&gt;” syntax handled by the argparse library. For Java apps, the system environment arguments are passed by using the <BR>“-Dparam=&lt;value&gt;” syntax. Discussion of app argument parsing is out of scope for this document.

### Type Parameter

The **type** parameter serves a dual purpose in the ThreatConnect platform, depending on the actual type defined. The table below lists the available types and how they affect elements within the platform.

|Type|Description|
|--- |--- |
|String|This	type renders an HTML Input textbox in the Job Wizard or Spaces	configuration dialog box. This allows the user to enter	free-form text as a parameter.	Values	are passed as a String to Python and Java apps.|
|Choice|This	type renders an HTML Select option in the Job Wizard or Spaces	configuration dialog box. This allows the user to select	predefined text values as a parameter. (See the description of	the “validValues” string array property in 3.)	Values	are passed as a String to Python and Java apps.|
|MultiChoice|This	type renders an HTML Multi-Checkbox Select  option in the Job	Wizard or Spaces configuration dialog box. This allows the user	to select multiple predefined text values as a parameter. (See	the description of the “validValues” string array property	in 3.)	The	same parameter is passed multiple times for a Python app. Python	apps should use the argparse “action='append'” option to	receive the parameters as an array. Java and Spaces apps will	receive the parameter as a single value separated by a pipe	character. Values are passed as a String to Python and Java apps.	This	selection must be used together with the “allowMultiple” flag defined as "true”.|
|Boolean|This type renders an HTML Checkbox in the Job Wizard or Spaces	configuration dialog box. This allows the user to turn on a flag as a parameter. Values	are passed as a “--flag” style parameter to Python apps. (See the “action='store_true'” option in the argparse module.) Java and Spaces apps receive the actual Boolean value “true” or “false”. These apps should parse the string to resolve the Boolean flag value.|

## Variable Expression

The variable-expression feature enables developers to reference “$” style variables in the **install.json** file and have the ThreatConnect platform resolve the values when displayed in the Job Wizard or Spaces configuration dialog box. The external-variables component can go one step further by resolving the value at the time a Job executes. Variable expressions are allowed only in the **params** section of the **install.json** file.

### Internal Variables

Internal variables are predefined (reserved) variables that can be explicitly declared in the **install.json** file. Apps declaring these variables will direct the Job Wizard and Spaces configuration dialog box to convert the variables into literal values. Internal variables should be used only with the **Choice** and **MultiChoice** types. They should be defined in the **validValues** property.

> Example of a validValues parameter definition example:

```json
{
   "name": "owner",
   "label": "Owner",
   "type": "choice",
   "validValues": ["${OWNERS}"]
}
```

The variables listed in the table below are internal variables understood by the ThreatConnect platform.

|Variable|Resolves As Type|Example of Usage|Description|
|--- |--- |--- |--- |
|OWNERS|String Array|["${OWNERS}"]|The OWNERS variable resolves to the available owners to which the current user has access. Since this determination is dynamically resolved at runtime, the owners rendered depend on the user. This	variable is useful when an app needs to have a defined owner passed as a parameter. The string value of the owner(s) is passed as an argument to the app.|
|ATTRIBUTES|String Array|["${ATTRIBUTES:Address}"]|The ATTRIBUTES variable resolves to attributes the current organization has available. This variable has a second, optional,	component, :<type>,	that further refines the attributes resolved to the specific Indicator or group type. This component gives the developer further control over the attribute type values rendered at	runtime. The string value of the attribute(s) is passed as an argument to the app.|


When the $ATTRIBUTES internal variable is used with a :&lt;type&gt; suffix, the types can be any of the Indicator or group types in the ThreatConnect platform: Address, Adversary, Document, Email, EmailAddress, File, Host, Incident, Signature, Task,Threat, URL, and Victim.

### External Variables

External variables offer the user an additional level of convenience by directing the Job Wizard and Spaces configuration dialog box to take advantage of the Variables feature.

NOTE:
The Variables feature in the ThreatConnect platform allows any user to create variable key/value pairs. Once created, these values can be selected by the user in the Job Wizard or Spaces configuration dialog box to reduce the need to copy and paste keys and plain-text data.

Since the variable names are not known by the app developer, the generic form of the variables is referenced instead in a **&lt;level:type&gt;** format. 

> For instance, to allow the user to select one of their plain-text variables from Organization and User levels, the **install.json** file would reference them as follows:

```json
"validValues": ["{USER:TEXT}", "${ORGANIZATION: TEXT}"]
```

The left-hand component of the variable is the level. The level can be any of the options listed in the table below.

|Level Option|Description|
|--- |--- |
|User|This option displays the list of the user’s variables in the Job Wizard or Spaces configuration dialog box.|
|Organization|This option displays the list of Organization variables available to the current user in the Job wizard or Spaces configuration dialog box.|
|System|This option displays the list of system variables available to the current user in the Job Wizard or Spaces configuration dialog box.|

The right-hand component of the variable is the type. The type can either of the options listed in the table below.

|Type Option|Description|
|--- |--- |
|Text|This option restricts the values in the level to those variables defined as plain text.|
|Keychain|This option restricts the values in the level to those variables defined as keychain. These parameters  are typically set to “encrypt: true” in the configuration.|
Multiple external-variable expressions can be included in string array form.

## Example JSON File

This section provides an example of an **install.json** file for a Python app. The key elements are described with line-number references in 8, below the example.

> Example install.json file for a Python app:

```json
{
 "programVersion": "1.0.0",
 "programLanguage": "PYTHON",
 "programMain": "auto_enrich",
 "languageVersion": "2.7",
 "runtimeLevel": "Organization",
 "allowOnDemand": true,
 "params": [{
  "name": "api_access_id",
  "label": "Local ThreatConnect API Access ID",
  "sequence": 1,
  "required": true,
  "validValues": ["${USER:TEXT}", "${ORGANIZATION:TEXT}"]
 }, {
  "name": "api_secret_key",
  "label": "Local ThreatConnect API Secret Key",
  "sequence": 2,
  "encrypt": true,
  "required": true,
  "validValues": ["${USER:KEYCHAIN}", "${ORGANIZATION:KEYCHAIN}"]
 }, {
  "name": "owner",
  "label": "Destination Owner",
  "sequence": 3,
  "required": true,
  "type": "choice",
  "validValues": ["${OWNERS}"]
 }, {
  "name": "remote_api_access_id",
  "label": "Remote ThreatConnect API Access ID",
  "sequence": 4,
  "required": true,
  "validValues": ["${USER:TEXT}", "${ORGANIZATION:TEXT}"]
 }, {
  "name": "remote_api_secret_key",
  "label": "Remote ThreatConnect API Secret Key",
  "sequence": 5,
  "encrypt": true,
  "required": true,
  "validValues": ["${USER:KEYCHAIN}", "${ORGANIZATION:KEYCHAIN}"]
 }, {
  "name": "remote_api_path",
  "label": "Remote ThreatConnect API Path",
  "sequence": 6,
  "required": true,
  "default": "https://api.threatconnect.com",
  "validValues": ["${USER:TEXT}", "${ORGANIZATION:TEXT}"]
 }, {
  "name": "remote_owner",
  "label": "Remote Owner",
  "sequence": 7,
  "required": true
 }, {
  "name": "apply_threat_assess_rating",
  "label": "Apply ThreatAssessRating from Remote Owner",
  "type": "Boolean",
  "sequence": 8
 }, {
  "name": "apply_rating",
  "label": "Apply Rating from Remote Owner if ThreatAssesRating
  is not Available ", "
  type " : "
  Boolean ", "
  sequence " : 9
 }, {
  "name": "apply_threat_assess_confidence",
  "label": "Apply ThreatAssessConfidence from Remote Owner",
  "type": "Boolean",
  "sequence": 10
 }, {
  "name": "apply_confidence",
  "label": "Apply Confidence from Remote Owner if
  ThreatAssessConfidence is not Available ", "
  type " : "
  Boolean ",
  "sequence": 11
 }, {
  "name": "apply_tags",
  "label": "Apply Tags from Remote Owner",
  "type": "Boolean",
  "sequence": 12
 }, {
  "name": "apply_auto_enrich_tag",
  "label": "Apply 'AutoEnriched' Tag",
  "type": "Boolean",
  "sequence": 13
 }, {
  "name": "apply_proxy_tc",
  "label": "Apply Proxy to Local API Connection",
  "type": "Boolean",
  "sequence": 14,
  "default": false
 }, {
  "name": "apply_proxy_ext",
  "label": "Apply Proxy to Remote API Connection",
  "type": "Boolean",
  "sequence": 15,
  "default": false
 }, {
  "name": "logging",
  "label": "Logging Level",
  "sequence": 16,
  "default": "info",
  "type": "choice",
  "validValues": ["debug", "info", "warning", "error", "critical"]
 }]
}
```

|Line Number|Description|
|--- |--- |
|2|The “programVersion” is 1.0.0. This value is rendered in the apps listing for System Administrators.|
|4|The “programMain” will direct the Job Executor to run this app as a main module.|
|6|The “runtimeLevel” for this app is “Organization”. This app will allow Jobs to be configured only for an Organization (assuming the System Admin has provisioned the Org).|
|8|This line is the start of the “params” array. The contents in this array are purely for parameter definitions.|
|9–13|This parameter describes the “api_access_id” argument for the app. The app will be passed an argument called “--api_access_id” at execution time. The label in the Job Wizard will be "Local ThreatConnect API Access ID”. Since the sequence is defined as “1”, this parameter will be the first parameter displayed in the Job Wizard. This parameter is required, and the user can	benefit from User- and Organization-level plain-text variables, if defined. Otherwise, the user is allowed to enter free-form text (the default type if no variables are defined).|
|35–40|This	parameter describes the “remote_api_secret_key” argument for the app. The app will be passed an argument called	“--remote_api_secret_key” at execution time. The label in the Job Wizard will be “Remote ThreatConnect API Secret Key”.	This parameter will be the 5th parameter in the Job Wizard 				“Parameters” panel. Since the parameter is set to “encrypt”, the input field will be displayed as a password with a masked value. Encrypted parameters will also be stored in encrypted form in the database. At runtime, the decrypted password will be passed to the app. Finally, the user can benefit from User- and 			Organization-level keychain variables, if defined. Otherwise, the user is allowed to enter free-form password text.|
|65–68|This	parameter describes the “apply_threat_assess_confidence” Boolean argument for the app. The app will be passed an argument called “--apply_threat_assess_confidence” at execution time only if the user selects this value in the Job Wizard. The Job Wizard will display a label called “Apply ThreatAssessRating from Remote Owner”, along with a checkbox. The argparse style flag (without an argument) and the checkbox displayed in the Job Wizard are dictated by the “Boolean” type in the parameter definition. This parameter will be the 8th parameter in the Job Wizard “Parameters” panel.|
|98–103|This parameter describes the “logging” argument for the app. The app will be passed a parameter named “--logging” with a string argument. The “Logging Level” label will be displayed in the Job Wizard. This parameter will be the 16th (and last) parameter in the Job Wizard parameter panel. The type for this parameter is “Choice”, and the definition dictates that a valid value for this parameter is one of “debug”, “info”, “warning”, “error”, or “critical”. The user will not	be able to edit this drop-down list, and the default value for new Jobs will be logging level “info”.|




# Trademarks

- ThreatConnect<sup>&reg;</sup> is a registered trademark of ThreatConnect, Inc. 
- Maven<sup>&trade;</sup> is a trademark of the Apache Software Foundation. 
- Mac<sup>&reg;</sup> is a registered trademark of Apple, Inc. 
- CrowdStrike<sup>&reg;</sup> is a registered trademark of CrowdStrike, Inc. 
- ECMAScript<sup>&reg;</sup> is a registered trademark of Ecma International. 
- GitHub<sup>&reg;</sup> is a registered trademark of GitHub, Inc. 
- Linux<sup>&reg;</sup> is a registered trademark of Linus Torvalds.  
- Windows<sup>&reg;</sup> is a registered trademark of the Microsoft Corporation. 
- Java<sup>&reg;</sup>, JavaScript<sup>&reg;</sup>, and Oracle<sup>&reg;</sup> are registered trademarks of the Oracle Corporation. 
- Python<sup>&reg;</sup> is a registered trademark of the Python Software Foundation.