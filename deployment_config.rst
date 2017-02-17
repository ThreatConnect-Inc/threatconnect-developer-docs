App Deployment Configuration File
=============================

A configuration file named ``install.json`` is used for ThreatConnect
apps written in:

-  Python
-  Java
-  JavaScript (Spaces)

Standard Section
----------------

Standard section defines required and optional properties to all apps in
ThreatConnect. The required properties are properties that must be
provided for any packaged app installed through the ThreatConnect
platform. The optional properties provide additional information based
on the type of target app.

The table below lists all of the properties of the Standard section.

+------+------+------+------+
| Prop | Requ | Allo | Desc |
| erty | ired | wed  | ript |
|      | ?    | Valu | ion  |
|      |      | es   |      |
+======+======+======+======+
| prog | Yes  | Any  | This |
| ramV |      |      | prop |
| ersi |      |      | erty |
| on   |      |      | is   |
|      |      |      | the  |
|      |      |      | vers |
|      |      |      | ion  |
|      |      |      | for  |
|      |      |      | this |
|      |      |      | app  |
|      |      |      | as   |
|      |      |      | it   |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | be   |
|      |      |      | disp |
|      |      |      | laye |
|      |      |      | d    |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | Syst |
|      |      |      | em   |
|      |      |      | Sett |
|      |      |      | ings |
|      |      |      | Page |
|      |      |      | unde |
|      |      |      | r    |
|      |      |      | Apps |
|      |      |      | .    |
+------+------+------+------+
| prog | Yes  | JAVA | This |
| ramL |      | PYTH | prop |
| angu |      | ONNO | erty |
| age  |      | NE   | is   |
|      |      |      | the  |
|      |      |      | lang |
|      |      |      | uage |
|      |      |      | runt |
|      |      |      | ime  |
|      |      |      | envi |
|      |      |      | ronm |
|      |      |      | ent  |
|      |      |      | used |
|      |      |      | by   |
|      |      |      | the  |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t    |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utor |
|      |      |      | .    |
|      |      |      | It   |
|      |      |      | is   |
|      |      |      | rele |
|      |      |      | vant |
|      |      |      | for  |
|      |      |      | apps |
|      |      |      | that |
|      |      |      | run  |
|      |      |      | on   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utio |
|      |      |      | n    |
|      |      |      | Engi |
|      |      |      | ne   |
|      |      |      | and  |
|      |      |      | can  |
|      |      |      | be   |
|      |      |      | set  |
|      |      |      | to   |
|      |      |      | NONE |
|      |      |      | for  |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | apps |
|      |      |      | .    |
+------+------+------+------+
| prog | Yes  | Any  | This |
| ramM | for  |      | prop |
| ain  | Pyth |      | erty |
|      | on   |      | is   |
|      | and  |      | the  |
|      | Java |      | entr |
|      | Apps |      | y    |
|      |      |      | poin |
|      |      |      | t    |
|      |      |      | into |
|      |      |      | the  |
|      |      |      | app. |
|      |      |      | For  |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | apps |
|      |      |      | ,    |
|      |      |      | it   |
|      |      |      | is   |
|      |      |      | gene |
|      |      |      | rall |
|      |      |      | y    |
|      |      |      | the  |
|      |      |      | .py  |
|      |      |      | file |
|      |      |      | (or  |
|      |      |      | excl |
|      |      |      | ude  |
|      |      |      | the  |
|      |      |      | exte |
|      |      |      | nsio |
|      |      |      | n    |
|      |      |      | if   |
|      |      |      | runn |
|      |      |      | ing  |
|      |      |      | it   |
|      |      |      | as a |
|      |      |      | modu |
|      |      |      | le). |
|      |      |      | For  |
|      |      |      | Java |
|      |      |      | apps |
|      |      |      | ,    |
|      |      |      | it   |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | main |
|      |      |      | clas |
|      |      |      | s    |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utio |
|      |      |      | n    |
|      |      |      | Engi |
|      |      |      | ne   |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | use  |
|      |      |      | when |
|      |      |      | call |
|      |      |      | ing  |
|      |      |      | the  |
|      |      |      | app  |
|      |      |      | usin |
|      |      |      | g    |
|      |      |      | the  |
|      |      |      | Java |
|      |      |      | Runt |
|      |      |      | ime  |
|      |      |      | Envi |
|      |      |      | ronm |
|      |      |      | ent. |
+------+------+------+------+
| lang | No   | Any  | This |
| uage |      |      | prop |
| Vers |      |      | erty |
| ion  |      |      | is   |
|      |      |      | used |
|      |      |      | pure |
|      |      |      | ly   |
|      |      |      | for  |
|      |      |      | trac |
|      |      |      | king |
|      |      |      | purp |
|      |      |      | oses |
|      |      |      | and  |
|      |      |      | does |
|      |      |      | not  |
|      |      |      | affe |
|      |      |      | ct   |
|      |      |      | the  |
|      |      |      | vers |
|      |      |      | ion  |
|      |      |      | of   |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | or   |
|      |      |      | Java |
|      |      |      | used |
|      |      |      | by   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utio |
|      |      |      | n    |
|      |      |      | Engi |
|      |      |      | ne.  |
+------+------+------+------+
| runt | Yes  | Orga | This |
| imeL |      | niza | prop |
| evel |      | tion | erty |
|      |      | Spac | desc |
|      |      | eOrg | ribe |
|      |      | aniz | s    |
|      |      | atio | the  |
|      |      | nSys | type |
|      |      | tem  | of   |
|      |      |      | app  |
|      |      |      | and  |
|      |      |      | how  |
|      |      |      | it   |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | be   |
|      |      |      | used |
|      |      |      | with |
|      |      |      | in   |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t.   |
|      |      |      | For  |
|      |      |      | furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | ,    |
|      |      |      | see  |
|      |      |      | the  |
|      |      |      | "Run |
|      |      |      | time |
|      |      |      | Leve |
|      |      |      | l"   |
|      |      |      | sect |
|      |      |      | ion. |
+------+------+------+------+
| runt | No   | Arra | This |
| imeC |      | y    | prop |
| onte |      | of   | erty |
| xt   |      | Stri | is   |
|      |      | ngs: | rele |
|      |      | Url, | vant |
|      |      | Host | for  |
|      |      | ,    | Spac |
|      |      | Addr | eOrg |
|      |      | ess, | aniz |
|      |      | Emai | atio |
|      |      | lAdd | n    |
|      |      | ress | apps |
|      |      | ,    | only |
|      |      | File | .    |
|      |      | ,    | This |
|      |      | Thre | arra |
|      |      | at,  | y    |
|      |      | Inci | of   |
|      |      | dent | Stri |
|      |      | ,    | ngs  |
|      |      | Emai | enab |
|      |      | l,   | les  |
|      |      | Docu | Spac |
|      |      | ment | es   |
|      |      | ,    | apps |
|      |      | Sign | to   |
|      |      | atur | be   |
|      |      | e,   | cont |
|      |      | Tag, | ext  |
|      |      | Adve | awar |
|      |      | rsar | e.   |
|      |      | y,   | For  |
|      |      | Vict | furt |
|      |      | im,  | her  |
|      |      | Menu | deta |
|      |      | ,    | ils  |
|      |      | Sear | on   |
|      |      | ch   | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | ,    |
|      |      |      | see  |
|      |      |      | the  |
|      |      |      | "Run |
|      |      |      | time |
|      |      |      | Cont |
|      |      |      | ext" |
|      |      |      | sect |
|      |      |      | ion. |
+------+------+------+------+
| repe | No   | Arra | This |
| atin |      | y    | prop |
| gMin |      | of   | erty |
| utes |      | Inte | is a |
|      |      | gers | list |
|      |      | Exam | of   |
|      |      | ple: | minu |
|      |      | [15, | te   |
|      |      | 30,6 | incr |
|      |      | 0,12 | emen |
|      |      | 0,24 | ts   |
|      |      | 0,36 | to   |
|      |      | 0]   | disp |
|      |      |      | lay  |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | "Rep |
|      |      |      | eat  |
|      |      |      | Ever |
|      |      |      | y…"  |
|      |      |      | sect |
|      |      |      | ion  |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | "Sch |
|      |      |      | edul |
|      |      |      | e"   |
|      |      |      | pane |
|      |      |      | l    |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd.  |
|      |      |      | This |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | rele |
|      |      |      | vant |
|      |      |      | only |
|      |      |      | for  |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | and  |
|      |      |      | Java |
|      |      |      | apps |
|      |      |      | for  |
|      |      |      | whic |
|      |      |      | h    |
|      |      |      | the  |
|      |      |      | deve |
|      |      |      | lope |
|      |      |      | r    |
|      |      |      | want |
|      |      |      | s    |
|      |      |      | to   |
|      |      |      | cont |
|      |      |      | rol  |
|      |      |      | how  |
|      |      |      | freq |
|      |      |      | uent |
|      |      |      | ly   |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | can  |
|      |      |      | be   |
|      |      |      | exec |
|      |      |      | uted |
|      |      |      | .    |
|      |      |      | If   |
|      |      |      | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | not  |
|      |      |      | defi |
|      |      |      | ned, |
|      |      |      | the  |
|      |      |      | defa |
|      |      |      | ult  |
|      |      |      | list |
|      |      |      | ing  |
|      |      |      | is   |
|      |      |      | as   |
|      |      |      | foll |
|      |      |      | ows: |
|      |      |      | [    |
|      |      |      | 60,  |
|      |      |      | 120, |
|      |      |      | 240, |
|      |      |      | 360, |
|      |      |      | 720  |
|      |      |      | ]    |
+------+------+------+------+
| allo | Yes  | Bool | This |
| wOnD |      | ean  | prop |
| eman |      |      | erty |
| d    |      |      | allo |
|      |      |      | ws   |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | to   |
|      |      |      | disp |
|      |      |      | lay  |
|      |      |      | the  |
|      |      |      | "Run |
|      |      |      | Now" |
|      |      |      | butt |
|      |      |      | on   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t    |
|      |      |      | plat |
|      |      |      | form |
|      |      |      | when |
|      |      |      | conf |
|      |      |      | igur |
|      |      |      | ed   |
|      |      |      | as a |
|      |      |      | Job. |
+------+------+------+------+

Runtime Level
~~~~~~~~~~~~~

The **runtimeLevel** property allows three distinct values that dictate
how the app is used within the ThreatConnect platform, as detailed in
the table below.

+------+------+
| Valu | Desc |
| e    | ript |
|      | ion  |
+======+======+
| Orga | This |
| niza | valu |
| tion | e    |
|      | is a |
|      | Pyth |
|      | on   |
|      | or   |
|      | Java |
|      | app  |
|      | that |
|      | is   |
|      | run  |
|      | by   |
|      | the  |
|      | Job  |
|      | Exec |
|      | utio |
|      | n    |
|      | Engi |
|      | ne.  |
|      | This |
|      | type |
|      | of   |
|      | app  |
|      | must |
|      | be   |
|      | prov |
|      | isio |
|      | ned  |
|      | to   |
|      | spec |
|      | ific |
|      | orga |
|      | niza |
|      | tion |
|      | s    |
|      | (or  |
|      | "All |
|      | ow   |
|      | All  |
|      | Orgs |
|      | "    |
|      | must |
|      | be   |
|      | sele |
|      | cted |
|      | )    |
|      | by   |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n.   |
|      | Once |
|      | prov |
|      | isio |
|      | ned, |
|      | the  |
|      | app  |
|      | can  |
|      | be   |
|      | sche |
|      | dule |
|      | d    |
|      | to   |
|      | run  |
|      | as   |
|      | part |
|      | of a |
|      | Job. |
+------+------+
| Spac | This |
| eOrg | valu |
| aniz | e    |
| atio | is a |
| n    | Spac |
|      | es   |
|      | app  |
|      | that |
|      | is   |
|      | run  |
|      | with |
|      | in   |
|      | Thre |
|      | atCo |
|      | nnec |
|      | t    |
|      | as a |
|      | Spac |
|      | e.   |
|      | This |
|      | type |
|      | of   |
|      | app  |
|      | must |
|      | be   |
|      | prov |
|      | isio |
|      | ned  |
|      | to   |
|      | spec |
|      | ific |
|      | orga |
|      | niza |
|      | tion |
|      | s    |
|      | (or  |
|      | "All |
|      | ow   |
|      | All  |
|      | Orgs |
|      | "    |
|      | must |
|      | be   |
|      | sele |
|      | cted |
|      | )    |
|      | by   |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n.   |
|      | Once |
|      | prov |
|      | isio |
|      | ned, |
|      | the  |
|      | app  |
|      | can  |
|      | be   |
|      | adde |
|      | d    |
|      | as a |
|      | Spac |
|      | es   |
|      | app  |
|      | by   |
|      | any  |
|      | user |
|      | belo |
|      | ngin |
|      | g    |
|      | to   |
|      | the  |
|      | Orga |
|      | niza |
|      | tion |
|      | .    |
+------+------+
| Syst | Alth |
| em   | ough |
|      | not  |
|      | comm |
|      | only |
|      | used |
|      | ,    |
|      | the  |
|      | Syst |
|      | em   |
|      | leve |
|      | l    |
|      | is a |
|      | Pyth |
|      | on   |
|      | or   |
|      | Java |
|      | app  |
|      | that |
|      | is   |
|      | stri |
|      | ctly |
|      | visi |
|      | ble  |
|      | by   |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n.   |
|      | This |
|      | app  |
|      | can  |
|      | be   |
|      | sche |
|      | dule |
|      | d    |
|      | only |
|      | in a |
|      | Syst |
|      | em   |
|      | Job. |
+------+------+

Runtime Context
~~~~~~~~~~~~~~~

The **runtimeContext** property enables Spaces apps to be context aware.
Users are able to add context-aware Spaces apps to their Spaces in the
respective **Details** page of the ThreatConnect platform. Because this
property is an array of Strings, the app can be displayed in multiple
Spaces within the ThreatConnect platform, including the **Menu** and
**Search** pages.

NOTE: Context-aware Spaces apps are passed contextual information via
the URL query string when the app is displayed in the ThreatConnect
platform. The details of those parameters are out of scope for this
document.

Parameter Array Section
-----------------------

The Parameter Array section of the **install.json** file is the
mechanism used by the Job Execution engine and the Spaces framework to
pass configuration data at runtime. For Java and Python apps, the
entries defined in this section dictate the **Parameters** panel in the
Job Wizard in the ThreatConnect platform. Spaces apps have their own
configuration screen as part of the user’s Space for each app.

The table below highlights the Parameter Array properties (the
**params** array).

+------+------+------+------+
| Prop | Requ | Allo | Desc |
| erty | ired | wed  | ript |
|      |      | Valu | ion  |
|      |      | es   |      |
+======+======+======+======+
| name | Yes  | Any  | This |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | inte |
|      |      |      | rnal |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | name |
|      |      |      | take |
|      |      |      | n    |
|      |      |      | from |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd   |
|      |      |      | and  |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | app  |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime. |
|      |      |      | It   |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | effe |
|      |      |      | ctiv |
|      |      |      | e    |
|      |      |      | comm |
|      |      |      | and- |
|      |      |      | line |
|      |      |      | argu |
|      |      |      | ment |
|      |      |      | name |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | app. |
+------+------+------+------+
| labe | Yes  | Any  | This |
| l    |      |      | prop |
|      |      |      | erty |
|      |      |      | is a |
|      |      |      | desc |
|      |      |      | ript |
|      |      |      | ion  |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | disp |
|      |      |      | laye |
|      |      |      | d    |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t    |
|      |      |      | plat |
|      |      |      | form |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd   |
|      |      |      | or   |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | Conf |
|      |      |      | ig   |
|      |      |      | dial |
|      |      |      | og   |
|      |      |      | box. |
+------+------+------+------+
| sequ | No   | Inte | This |
| ence |      | ger  | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | numb |
|      |      |      | er   |
|      |      |      | used |
|      |      |      | to   |
|      |      |      | cont |
|      |      |      | rol  |
|      |      |      | the  |
|      |      |      | orde |
|      |      |      | ring |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd   |
|      |      |      | or   |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | Conf |
|      |      |      | ig   |
|      |      |      | dial |
|      |      |      | og   |
|      |      |      | box. |
|      |      |      | If   |
|      |      |      | it   |
|      |      |      | is   |
|      |      |      | not  |
|      |      |      | defi |
|      |      |      | ned, |
|      |      |      | the  |
|      |      |      | orde |
|      |      |      | r    |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | inst |
|      |      |      | all. |
|      |      |      | json |
|      |      |      | file |
|      |      |      | is   |
|      |      |      | used |
|      |      |      | .    |
+------+------+------+------+
| requ | No   | Bool | This |
| ired |      | ean  | prop |
|      |      |      | erty |
|      |      |      | desi |
|      |      |      | gnat |
|      |      |      | es   |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | as a |
|      |      |      | requ |
|      |      |      | ired |
|      |      |      | fiel |
|      |      |      | d    |
|      |      |      | that |
|      |      |      | must |
|      |      |      | be   |
|      |      |      | popu |
|      |      |      | late |
|      |      |      | d    |
|      |      |      | to   |
|      |      |      | save |
|      |      |      | the  |
|      |      |      | Job. |
|      |      |      | Requ |
|      |      |      | ired |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | woul |
|      |      |      | d    |
|      |      |      | fail |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime  |
|      |      |      | or   |
|      |      |      | caus |
|      |      |      | e    |
|      |      |      | unex |
|      |      |      | pect |
|      |      |      | ed   |
|      |      |      | resu |
|      |      |      | lts. |
+------+------+------+------+
| defa | No   | Any  | This |
| ult  |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | defa |
|      |      |      | ult  |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | pre- |
|      |      |      | popu |
|      |      |      | late |
|      |      |      | d    |
|      |      |      | for  |
|      |      |      | new  |
|      |      |      | Jobs |
|      |      |      | or   |
|      |      |      | Spac |
|      |      |      | es.  |
|      |      |      | The  |
|      |      |      | purp |
|      |      |      | ose  |
|      |      |      | of a |
|      |      |      | defa |
|      |      |      | ult  |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | is   |
|      |      |      | to   |
|      |      |      | prov |
|      |      |      | ide  |
|      |      |      | the  |
|      |      |      | user |
|      |      |      | with |
|      |      |      | a    |
|      |      |      | guid |
|      |      |      | ance |
|      |      |      | whil |
|      |      |      | e    |
|      |      |      | allo |
|      |      |      | wing |
|      |      |      | edit |
|      |      |      | s    |
|      |      |      | base |
|      |      |      | d    |
|      |      |      | on   |
|      |      |      | pref |
|      |      |      | eren |
|      |      |      | ce.  |
+------+------+------+------+
| type | No   | Stri | Data |
|      |      | ng,  | type |
|      |      | Choi | s    |
|      |      | ce,  | enab |
|      |      | Mult | le   |
|      |      | iCho | the  |
|      |      | ice, | UI   |
|      |      | Bool | to   |
|      |      | ean  | disp |
|      |      |      | lay  |
|      |      |      | rele |
|      |      |      | vant |
|      |      |      | comp |
|      |      |      | onen |
|      |      |      | ts   |
|      |      |      | and  |
|      |      |      | allo |
|      |      |      | w    |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utor |
|      |      |      | to   |
|      |      |      | adap |
|      |      |      | t    |
|      |      |      | how  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | are  |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | to   |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime. |
|      |      |      | For  |
|      |      |      | furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r,   |
|      |      |      | see  |
|      |      |      | the  |
|      |      |      | "Typ |
|      |      |      | e    |
|      |      |      | Para |
|      |      |      | mete |
|      |      |      | r"   |
|      |      |      | sect |
|      |      |      | ion. |
+------+------+------+------+
| encr | No   | Bool | This |
| ypt  |      | ean  | prop |
|      |      |      | erty |
|      |      |      | desi |
|      |      |      | gnat |
|      |      |      | es   |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | as   |
|      |      |      | an   |
|      |      |      | encr |
|      |      |      | ypte |
|      |      |      | d    |
|      |      |      | valu |
|      |      |      | e.   |
|      |      |      | Para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | defi |
|      |      |      | ned  |
|      |      |      | as   |
|      |      |      | encr |
|      |      |      | ypte |
|      |      |      | d    |
|      |      |      | will |
|      |      |      | be   |
|      |      |      | mana |
|      |      |      | ged  |
|      |      |      | by   |
|      |      |      | the  |
|      |      |      | Keyc |
|      |      |      | hain |
|      |      |      | feat |
|      |      |      | ure  |
|      |      |      | that |
|      |      |      | encr |
|      |      |      | ypts |
|      |      |      | pass |
|      |      |      | word |
|      |      |      | whil |
|      |      |      | e    |
|      |      |      | at   |
|      |      |      | rest |
|      |      |      | .    |
|      |      |      | This |
|      |      |      | flag |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | be   |
|      |      |      | used |
|      |      |      | with |
|      |      |      | the  |
|      |      |      | "Str |
|      |      |      | ing" |
|      |      |      | type |
|      |      |      | and  |
|      |      |      | will |
|      |      |      | rend |
|      |      |      | er   |
|      |      |      | a    |
|      |      |      | pass |
|      |      |      | word |
|      |      |      | inpu |
|      |      |      | t    |
|      |      |      | text |
|      |      |      | box  |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | and  |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | conf |
|      |      |      | igur |
|      |      |      | atio |
|      |      |      | n.   |
+------+------+------+------+
| allo | No   | Bool | The  |
| wMul |      | ean  | valu |
| tipl |      |      | e    |
| e    |      |      | of   |
|      |      |      | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | auto |
|      |      |      | mati |
|      |      |      | call |
|      |      |      | y    |
|      |      |      | set  |
|      |      |      | to   |
|      |      |      | "tru |
|      |      |      | e"   |
|      |      |      | if   |
|      |      |      | the  |
|      |      |      | "Mul |
|      |      |      | tiCh |
|      |      |      | oice |
|      |      |      | "    |
|      |      |      | type |
|      |      |      | is   |
|      |      |      | used |
|      |      |      | .    |
|      |      |      | If a |
|      |      |      | "Str |
|      |      |      | ing" |
|      |      |      | type |
|      |      |      | is   |
|      |      |      | used |
|      |      |      | ,    |
|      |      |      | this |
|      |      |      | flag |
|      |      |      | allo |
|      |      |      | ws   |
|      |      |      | the  |
|      |      |      | user |
|      |      |      | to   |
|      |      |      | defi |
|      |      |      | ne   |
|      |      |      | mult |
|      |      |      | iple |
|      |      |      | valu |
|      |      |      | es   |
|      |      |      | in a |
|      |      |      | sing |
|      |      |      | le   |
|      |      |      | inpu |
|      |      |      | t    |
|      |      |      | fiel |
|      |      |      | d    |
|      |      |      | deli |
|      |      |      | mite |
|      |      |      | d    |
|      |      |      | by a |
|      |      |      | pipe |
|      |      |      | ("   |
+------+------+------+------+
| vali | No   | Stri | This |
| dVal |      | ng   | prop |
| ues  |      | Arra | erty |
|      |      | y    | is   |
|      |      |      | used |
|      |      |      | with |
|      |      |      | the  |
|      |      |      | "Cho |
|      |      |      | ice" |
|      |      |      | and  |
|      |      |      | "Mul |
|      |      |      | tiCh |
|      |      |      | oice |
|      |      |      | "    |
|      |      |      | type |
|      |      |      | s    |
|      |      |      | to   |
|      |      |      | rest |
|      |      |      | rict |
|      |      |      | the  |
|      |      |      | poss |
|      |      |      | ible |
|      |      |      | valu |
|      |      |      | es   |
|      |      |      | a    |
|      |      |      | user |
|      |      |      | can  |
|      |      |      | sele |
|      |      |      | ct.  |
|      |      |      | For  |
|      |      |      | inst |
|      |      |      | ance |
|      |      |      | ,    |
|      |      |      | to   |
|      |      |      | defi |
|      |      |      | ne   |
|      |      |      | a    |
|      |      |      | "log |
|      |      |      | ging |
|      |      |      | Leve |
|      |      |      | l"   |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r,   |
|      |      |      | this |
|      |      |      | fiel |
|      |      |      | d    |
|      |      |      | coul |
|      |      |      | d    |
|      |      |      | have |
|      |      |      | the  |
|      |      |      | foll |
|      |      |      | owin |
|      |      |      | g    |
|      |      |      | valu |
|      |      |      | es:  |
|      |      |      | ["FA |
|      |      |      | TAL" |
|      |      |      | ,    |
|      |      |      | "ERR |
|      |      |      | OR", |
|      |      |      | "WAR |
|      |      |      | N",  |
|      |      |      | "INF |
|      |      |      | O",  |
|      |      |      | "DEB |
|      |      |      | UG", |
|      |      |      | "TRA |
|      |      |      | CE"] |
|      |      |      | .    |
+------+------+------+------+
| hidd | No   | Bool | If   |
| en   |      | ean  | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | set  |
|      |      |      | to   |
|      |      |      | "tru |
|      |      |      | e",  |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | will |
|      |      |      | be   |
|      |      |      | hidd |
|      |      |      | en   |
|      |      |      | from |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd.  |
|      |      |      | Hidd |
|      |      |      | en   |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | allo |
|      |      |      | w    |
|      |      |      | the  |
|      |      |      | deve |
|      |      |      | lope |
|      |      |      | r    |
|      |      |      | to   |
|      |      |      | pers |
|      |      |      | ist  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | betw |
|      |      |      | een  |
|      |      |      | job  |
|      |      |      | exec |
|      |      |      | utio |
|      |      |      | ns   |
|      |      |      | with |
|      |      |      | out  |
|      |      |      | the  |
|      |      |      | need |
|      |      |      | to   |
|      |      |      | rend |
|      |      |      | er   |
|      |      |      | the  |
|      |      |      | valu |
|      |      |      | es   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd.  |
|      |      |      | This |
|      |      |      | opti |
|      |      |      | on   |
|      |      |      | is   |
|      |      |      | vali |
|      |      |      | d    |
|      |      |      | only |
|      |      |      | for  |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | and  |
|      |      |      | Java |
|      |      |      | apps |
|      |      |      | .    |
|      |      |      | Furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | pers |
|      |      |      | isti |
|      |      |      | ng   |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | from |
|      |      |      | the  |
|      |      |      | app  |
|      |      |      | dire |
|      |      |      | ctly |
|      |      |      | are  |
|      |      |      | out  |
|      |      |      | of   |
|      |      |      | scop |
|      |      |      | e    |
|      |      |      | for  |
|      |      |      | this |
|      |      |      | docu |
|      |      |      | ment |
|      |      |      | .    |
+------+------+------+------+
| setu | No   | Bool | This |
| p    |      | ean  | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | rese |
|      |      |      | rved |
|      |      |      | for  |
|      |      |      | the  |
|      |      |      | App  |
|      |      |      | Prof |
|      |      |      | iles |
|      |      |      | feat |
|      |      |      | ure. |
|      |      |      | Furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | this |
|      |      |      | feat |
|      |      |      | ure  |
|      |      |      | are  |
|      |      |      | out  |
|      |      |      | of   |
|      |      |      | scop |
|      |      |      | e    |
|      |      |      | for  |
|      |      |      | this |
|      |      |      | docu |
|      |      |      | ment |
|      |      |      | .    |
+------+------+------+------+

NOTE: In Python, parameters are called by using the "--param <value>"
syntax handled by the argparse library. For Java apps, the system
environment arguments are passed by using the "-Dparam=<value>" syntax.
Discussion of app argument parsing is out of scope for this document.

Type Parameter
~~~~~~~~~~~~~~

The **type** parameter serves a dual purpose in the ThreatConnect
platform, depending on the actual type defined. The table below lists
the available types and how they affect elements within the platform.

+------+------+
| Type | Desc |
|      | ript |
|      | ion  |
+======+======+
| Stri | This |
| ng   | type |
|      | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Inpu |
|      | t    |
|      | text |
|      | box  |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | ente |
|      | r    |
|      | free |
|      | -for |
|      | m    |
|      | text |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | Stri |
|      | ng   |
|      | to   |
|      | Pyth |
|      | on   |
|      | and  |
|      | Java |
|      | apps |
|      | .    |
+------+------+
| Choi | This |
| ce   | type |
|      | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Sele |
|      | ct   |
|      | opti |
|      | on   |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | sele |
|      | ct   |
|      | pred |
|      | efin |
|      | ed   |
|      | text |
|      | valu |
|      | es   |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | (See |
|      | the  |
|      | desc |
|      | ript |
|      | ion  |
|      | of   |
|      | the  |
|      | "val |
|      | idVa |
|      | lues |
|      | "    |
|      | stri |
|      | ng   |
|      | arra |
|      | y    |
|      | prop |
|      | erty |
|      | in   |
|      | 3.)  |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | Stri |
|      | ng   |
|      | to   |
|      | Pyth |
|      | on   |
|      | and  |
|      | Java |
|      | apps |
|      | .    |
+------+------+
| Mult | This |
| iCho | type |
| ice  | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Mult |
|      | i-Ch |
|      | eckb |
|      | ox   |
|      | Sele |
|      | ct   |
|      | opti |
|      | on   |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | sele |
|      | ct   |
|      | mult |
|      | iple |
|      | pred |
|      | efin |
|      | ed   |
|      | text |
|      | valu |
|      | es   |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | (See |
|      | the  |
|      | desc |
|      | ript |
|      | ion  |
|      | of   |
|      | the  |
|      | "val |
|      | idVa |
|      | lues |
|      | "    |
|      | stri |
|      | ng   |
|      | arra |
|      | y    |
|      | prop |
|      | erty |
|      | in   |
|      | 3.)  |
|      | The  |
|      | same |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | pass |
|      | ed   |
|      | mult |
|      | iple |
|      | time |
|      | s    |
|      | for  |
|      | a    |
|      | Pyth |
|      | on   |
|      | app. |
|      | Pyth |
|      | on   |
|      | apps |
|      | shou |
|      | ld   |
|      | use  |
|      | the  |
|      | argp |
|      | arse |
|      | "act |
|      | ion= |
|      | 'app |
|      | end' |
|      | "    |
|      | opti |
|      | on   |
|      | to   |
|      | rece |
|      | ive  |
|      | the  |
|      | para |
|      | mete |
|      | rs   |
|      | as   |
|      | an   |
|      | arra |
|      | y.   |
|      | Java |
|      | and  |
|      | Spac |
|      | es   |
|      | apps |
|      | will |
|      | rece |
|      | ive  |
|      | the  |
|      | para |
|      | mete |
|      | r    |
|      | as a |
|      | sing |
|      | le   |
|      | valu |
|      | e    |
|      | sepa |
|      | rate |
|      | d    |
|      | by a |
|      | pipe |
|      | char |
|      | acte |
|      | r.   |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | Stri |
|      | ng   |
|      | to   |
|      | Pyth |
|      | on   |
|      | and  |
|      | Java |
|      | apps |
|      | .    |
|      | This |
|      | sele |
|      | ctio |
|      | n    |
|      | must |
|      | be   |
|      | used |
|      | toge |
|      | ther |
|      | with |
|      | the  |
|      | "all |
|      | owMu |
|      | ltip |
|      | le"  |
|      | flag |
|      | defi |
|      | ned  |
|      | as   |
|      | "tru |
|      | e".  |
+------+------+
| Bool | This |
| ean  | type |
|      | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Chec |
|      | kbox |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | turn |
|      | on a |
|      | flag |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | "--f |
|      | lag" |
|      | styl |
|      | e    |
|      | para |
|      | mete |
|      | r    |
|      | to   |
|      | Pyth |
|      | on   |
|      | apps |
|      | .    |
|      | (See |
|      | the  |
|      | "act |
|      | ion= |
|      | 'sto |
|      | re\_ |
|      | true |
|      | '"   |
|      | opti |
|      | on   |
|      | in   |
|      | the  |
|      | argp |
|      | arse |
|      | modu |
|      | le.) |
|      | Java |
|      | and  |
|      | Spac |
|      | es   |
|      | apps |
|      | rece |
|      | ive  |
|      | the  |
|      | actu |
|      | al   |
|      | Bool |
|      | ean  |
|      | valu |
|      | e    |
|      | "tru |
|      | e"   |
|      | or   |
|      | "fal |
|      | se". |
|      | Thes |
|      | e    |
|      | apps |
|      | shou |
|      | ld   |
|      | pars |
|      | e    |
|      | the  |
|      | stri |
|      | ng   |
|      | to   |
|      | reso |
|      | lve  |
|      | the  |
|      | Bool |
|      | ean  |
|      | flag |
|      | valu |
|      | e.   |
+------+------+

Variable Expression
-------------------

The variable-expression feature enables developers to reference "$"
style variables in the **install.json** file and have the ThreatConnect
platform resolve the values when displayed in the Job Wizard or Spaces
configuration dialog box. The external-variables component can go one
step further by resolving the value at the time a Job executes. Variable
expressions are allowed only in the **params** section of the
**install.json** file.

Internal Variables
~~~~~~~~~~~~~~~~~~

Internal variables are predefined (reserved) variables that can be
explicitly declared in the **install.json** file. Apps declaring these
variables will direct the Job Wizard and Spaces configuration dialog box
to convert the variables into literal values. Internal variables should
be used only with the **Choice** and **MultiChoice** types. They should
be defined in the **validValues** property.

Example of a validValues parameter definition example:

.. code:: json

    {
       "name": "owner",
       "label": "Owner",
       "type": "choice",
       "validValues": ["${OWNERS}"]
    }

The variables listed in the table below are internal variables
understood by the ThreatConnect platform.

+------------+------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Variable   | Resolves As Type | Example of Usage                               | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
+============+==================+================================================+=========================================================================================================================================================================================================================================================================================================================================================================================================================+
| OWNERS     | String Array     | ["${OWNERS}"]                                  | The OWNERS variable resolves to the available owners to which the current user has access. Since this determination is dynamically resolved at runtime, the owners rendered depend on the user. This variable is useful when an app needs to have a defined owner passed as a parameter. The string value of the owner(s) is passed as an argument to the app.                                                          |
+------------+------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ATTRIBUTES | String Array     | ["${ATTRIBUTES}"] or ["${ATTRIBUTES:<type>}"]  | The ATTRIBUTES variable resolves to attributes the current organization has available. This variable has a second, optional component, :<type>, that further refines the attributes resolved to the specific Indicator or Group type (for example: ["${ATTRIBUTES:Address}"]). The string value of the attribute(s) is passed as an argument to the app.                                                                |
+------------+------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

When the $ATTRIBUTES internal variable is used with a :<type> suffix,
the types can be any of the Indicator, Group, Task, or Victim types in
the ThreatConnect platform: Address, Adversary, Campaign, Document,
Email, EmailAddress, File, Host, Incident, Signature, Task, Threat, and
URL.

External Variables
~~~~~~~~~~~~~~~~~~

External variables offer the user an additional level of convenience by
directing the Job Wizard and Spaces configuration dialog box to take
advantage of the Variables feature.

NOTE: The Variables feature in the ThreatConnect platform allows any
user to create variable key/value pairs. Once created, these values can
be selected by the user in the Job Wizard or Spaces configuration dialog
box to reduce the need to copy and paste keys and plain-text data.

Since the variable names are not known by the app developer, the generic
form of the variables is referenced instead in a **<level:type>**
format.

For instance, to allow the user to select one of their plain-text
variables from Organization and User levels, the **install.json** file
would reference them as follows:

.. code:: json

    "validValues": ["{USER:TEXT}", "${ORGANIZATION: TEXT}"]

The left-hand component of the variable is the level. The level can be
any of the options listed in the table below.

+------+------+
| Leve | Desc |
| l    | ript |
| Opti | ion  |
| on   |      |
+======+======+
| User | This |
|      | opti |
|      | on   |
|      | disp |
|      | lays |
|      | the  |
|      | list |
|      | of   |
|      | the  |
|      | user |
|      | ’s   |
|      | vari |
|      | able |
|      | s    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
+------+------+
| Orga | This |
| niza | opti |
| tion | on   |
|      | disp |
|      | lays |
|      | the  |
|      | list |
|      | of   |
|      | Orga |
|      | niza |
|      | tion |
|      | vari |
|      | able |
|      | s    |
|      | avai |
|      | labl |
|      | e    |
|      | to   |
|      | the  |
|      | curr |
|      | ent  |
|      | user |
|      | in   |
|      | the  |
|      | Job  |
|      | wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
+------+------+
| Syst | This |
| em   | opti |
|      | on   |
|      | disp |
|      | lays |
|      | the  |
|      | list |
|      | of   |
|      | syst |
|      | em   |
|      | vari |
|      | able |
|      | s    |
|      | avai |
|      | labl |
|      | e    |
|      | to   |
|      | the  |
|      | curr |
|      | ent  |
|      | user |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
+------+------+

The right-hand component of the variable is the type. The type can
either of the options listed in the table below.

+------+------+
| Type | Desc |
| Opti | ript |
| on   | ion  |
+======+======+
| Text | This |
|      | opti |
|      | on   |
|      | rest |
|      | rict |
|      | s    |
|      | the  |
|      | valu |
|      | es   |
|      | in   |
|      | the  |
|      | leve |
|      | l    |
|      | to   |
|      | thos |
|      | e    |
|      | vari |
|      | able |
|      | s    |
|      | defi |
|      | ned  |
|      | as   |
|      | plai |
|      | n    |
|      | text |
|      | .    |
+------+------+
| Keyc | This |
| hain | opti |
|      | on   |
|      | rest |
|      | rict |
|      | s    |
|      | the  |
|      | valu |
|      | es   |
|      | in   |
|      | the  |
|      | leve |
|      | l    |
|      | to   |
|      | thos |
|      | e    |
|      | vari |
|      | able |
|      | s    |
|      | defi |
|      | ned  |
|      | as   |
|      | keyc |
|      | hain |
|      | .    |
|      | Thes |
|      | e    |
|      | para |
|      | mete |
|      | rs   |
|      | are  |
|      | typi |
|      | call |
|      | y    |
|      | set  |
|      | to   |
|      | "enc |
|      | rypt |
|      | :    |
|      | true |
|      | "    |
|      | in   |
|      | the  |
|      | conf |
|      | igur |
|      | atio |
|      | n.   |
+------+------+

Multiple external-variable expressions can be included in string array
form.

Example JSON File
-----------------

This section provides an example of an **install.json** file for a
Python app. The key elements are described with line-number references
in 8, below the example.

Example install.json file for a Python app:

.. code:: json

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

+------+------+
| Line | Desc |
| Numb | ript |
| er   | ion  |
+======+======+
| 2    | The  |
|      | "pro |
|      | gram |
|      | Vers |
|      | ion" |
|      | is   |
|      | 1.0. |
|      | 0.   |
|      | This |
|      | valu |
|      | e    |
|      | is   |
|      | rend |
|      | ered |
|      | in   |
|      | the  |
|      | apps |
|      | list |
|      | ing  |
|      | for  |
|      | Syst |
|      | em   |
|      | Admi |
|      | nist |
|      | rato |
|      | rs.  |
+------+------+
| 4    | The  |
|      | "pro |
|      | gram |
|      | Main |
|      | "    |
|      | will |
|      | dire |
|      | ct   |
|      | the  |
|      | Job  |
|      | Exec |
|      | utor |
|      | to   |
|      | run  |
|      | this |
|      | app  |
|      | as a |
|      | main |
|      | modu |
|      | le.  |
+------+------+
| 6    | The  |
|      | "run |
|      | time |
|      | Leve |
|      | l"   |
|      | for  |
|      | this |
|      | app  |
|      | is   |
|      | "Org |
|      | aniz |
|      | atio |
|      | n".  |
|      | This |
|      | app  |
|      | will |
|      | allo |
|      | w    |
|      | Jobs |
|      | to   |
|      | be   |
|      | conf |
|      | igur |
|      | ed   |
|      | only |
|      | for  |
|      | an   |
|      | Orga |
|      | niza |
|      | tion |
|      | (ass |
|      | umin |
|      | g    |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n    |
|      | has  |
|      | prov |
|      | isio |
|      | ned  |
|      | the  |
|      | Org) |
|      | .    |
+------+------+
| 8    | This |
|      | line |
|      | is   |
|      | the  |
|      | star |
|      | t    |
|      | of   |
|      | the  |
|      | "par |
|      | ams" |
|      | arra |
|      | y.   |
|      | The  |
|      | cont |
|      | ents |
|      | in   |
|      | this |
|      | arra |
|      | y    |
|      | are  |
|      | pure |
|      | ly   |
|      | for  |
|      | para |
|      | mete |
|      | r    |
|      | defi |
|      | niti |
|      | ons. |
+------+------+
| 9–13 | This |
|      | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "api |
|      | \_ac |
|      | cess |
|      | \_id |
|      | "    |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | an   |
|      | argu |
|      | ment |
|      | call |
|      | ed   |
|      | "--a |
|      | pi\_ |
|      | acce |
|      | ss\_ |
|      | id"  |
|      | at   |
|      | exec |
|      | utio |
|      | n    |
|      | time |
|      | .    |
|      | The  |
|      | labe |
|      | l    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | will |
|      | be   |
|      | "Loc |
|      | al   |
|      | Thre |
|      | atCo |
|      | nnec |
|      | t    |
|      | API  |
|      | Acce |
|      | ss   |
|      | ID". |
|      | Sinc |
|      | e    |
|      | the  |
|      | sequ |
|      | ence |
|      | is   |
|      | defi |
|      | ned  |
|      | as   |
|      | "1", |
|      | this |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | firs |
|      | t    |
|      | para |
|      | mete |
|      | r    |
|      | disp |
|      | laye |
|      | d    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd.  |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | requ |
|      | ired |
|      | ,    |
|      | and  |
|      | the  |
|      | user |
|      | can  |
|      | bene |
|      | fit  |
|      | from |
|      | User |
|      | -    |
|      | and  |
|      | Orga |
|      | niza |
|      | tion |
|      | -lev |
|      | el   |
|      | plai |
|      | n-te |
|      | xt   |
|      | vari |
|      | able |
|      | s,   |
|      | if   |
|      | defi |
|      | ned. |
|      | Othe |
|      | rwis |
|      | e,   |
|      | the  |
|      | user |
|      | is   |
|      | allo |
|      | wed  |
|      | to   |
|      | ente |
|      | r    |
|      | free |
|      | -for |
|      | m    |
|      | text |
|      | (the |
|      | defa |
|      | ult  |
|      | type |
|      | if   |
|      | no   |
|      | vari |
|      | able |
|      | s    |
|      | are  |
|      | defi |
|      | ned) |
|      | .    |
+------+------+
| 35–4 | This |
| 0    | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "rem |
|      | ote\ |
|      | _api |
|      | \_se |
|      | cret |
|      | \_ke |
|      | y"   |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | an   |
|      | argu |
|      | ment |
|      | call |
|      | ed   |
|      | "--r |
|      | emot |
|      | e\_a |
|      | pi\_ |
|      | secr |
|      | et\_ |
|      | key" |
|      | at   |
|      | exec |
|      | utio |
|      | n    |
|      | time |
|      | .    |
|      | The  |
|      | labe |
|      | l    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | will |
|      | be   |
|      | "Rem |
|      | ote  |
|      | Thre |
|      | atCo |
|      | nnec |
|      | t    |
|      | API  |
|      | Secr |
|      | et   |
|      | Key" |
|      | .    |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | 5th  |
|      | para |
|      | mete |
|      | r    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | "Par |
|      | amet |
|      | ers" |
|      | pane |
|      | l.   |
|      | Sinc |
|      | e    |
|      | the  |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | set  |
|      | to   |
|      | "enc |
|      | rypt |
|      | ",   |
|      | the  |
|      | inpu |
|      | t    |
|      | fiel |
|      | d    |
|      | will |
|      | be   |
|      | disp |
|      | laye |
|      | d    |
|      | as a |
|      | pass |
|      | word |
|      | with |
|      | a    |
|      | mask |
|      | ed   |
|      | valu |
|      | e.   |
|      | Encr |
|      | ypte |
|      | d    |
|      | para |
|      | mete |
|      | rs   |
|      | will |
|      | also |
|      | be   |
|      | stor |
|      | ed   |
|      | in   |
|      | encr |
|      | ypte |
|      | d    |
|      | form |
|      | in   |
|      | the  |
|      | data |
|      | base |
|      | .    |
|      | At   |
|      | runt |
|      | ime, |
|      | the  |
|      | decr |
|      | ypte |
|      | d    |
|      | pass |
|      | word |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | to   |
|      | the  |
|      | app. |
|      | Fina |
|      | lly, |
|      | the  |
|      | user |
|      | can  |
|      | bene |
|      | fit  |
|      | from |
|      | User |
|      | -    |
|      | and  |
|      | Orga |
|      | niza |
|      | tion |
|      | -lev |
|      | el   |
|      | keyc |
|      | hain |
|      | vari |
|      | able |
|      | s,   |
|      | if   |
|      | defi |
|      | ned. |
|      | Othe |
|      | rwis |
|      | e,   |
|      | the  |
|      | user |
|      | is   |
|      | allo |
|      | wed  |
|      | to   |
|      | ente |
|      | r    |
|      | free |
|      | -for |
|      | m    |
|      | pass |
|      | word |
|      | text |
|      | .    |
+------+------+
| 65–6 | This |
| 8    | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "app |
|      | ly\_ |
|      | thre |
|      | at\_ |
|      | asse |
|      | ss\_ |
|      | conf |
|      | iden |
|      | ce"  |
|      | Bool |
|      | ean  |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | an   |
|      | argu |
|      | ment |
|      | call |
|      | ed   |
|      | "--a |
|      | pply |
|      | \_th |
|      | reat |
|      | \_as |
|      | sess |
|      | \_co |
|      | nfid |
|      | ence |
|      | "    |
|      | at   |
|      | exec |
|      | utio |
|      | n    |
|      | time |
|      | only |
|      | if   |
|      | the  |
|      | user |
|      | sele |
|      | cts  |
|      | this |
|      | valu |
|      | e    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd.  |
|      | The  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | will |
|      | disp |
|      | lay  |
|      | a    |
|      | labe |
|      | l    |
|      | call |
|      | ed   |
|      | "App |
|      | ly   |
|      | Thre |
|      | atAs |
|      | sess |
|      | Rati |
|      | ng   |
|      | from |
|      | Remo |
|      | te   |
|      | Owne |
|      | r",  |
|      | alon |
|      | g    |
|      | with |
|      | a    |
|      | chec |
|      | kbox |
|      | .    |
|      | The  |
|      | argp |
|      | arse |
|      | styl |
|      | e    |
|      | flag |
|      | (wit |
|      | hout |
|      | an   |
|      | argu |
|      | ment |
|      | )    |
|      | and  |
|      | the  |
|      | chec |
|      | kbox |
|      | disp |
|      | laye |
|      | d    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | are  |
|      | dict |
|      | ated |
|      | by   |
|      | the  |
|      | "Boo |
|      | lean |
|      | "    |
|      | type |
|      | in   |
|      | the  |
|      | para |
|      | mete |
|      | r    |
|      | defi |
|      | niti |
|      | on.  |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | 8th  |
|      | para |
|      | mete |
|      | r    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | "Par |
|      | amet |
|      | ers" |
|      | pane |
|      | l.   |
+------+------+
| 98–1 | This |
| 03   | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "log |
|      | ging |
|      | "    |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | a    |
|      | para |
|      | mete |
|      | r    |
|      | name |
|      | d    |
|      | "--l |
|      | oggi |
|      | ng"  |
|      | with |
|      | a    |
|      | stri |
|      | ng   |
|      | argu |
|      | ment |
|      | .    |
|      | The  |
|      | "Log |
|      | ging |
|      | Leve |
|      | l"   |
|      | labe |
|      | l    |
|      | will |
|      | be   |
|      | disp |
|      | laye |
|      | d    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd.  |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | 16th |
|      | (and |
|      | last |
|      | )    |
|      | para |
|      | mete |
|      | r    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | para |
|      | mete |
|      | r    |
|      | pane |
|      | l.   |
|      | The  |
|      | type |
|      | for  |
|      | this |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | "Cho |
|      | ice" |
|      | ,    |
|      | and  |
|      | the  |
|      | defi |
|      | niti |
|      | on   |
|      | dict |
|      | ates |
|      | that |
|      | a    |
|      | vali |
|      | d    |
|      | valu |
|      | e    |
|      | for  |
|      | this |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | one  |
|      | of   |
|      | "deb |
|      | ug", |
|      | "inf |
|      | o",  |
|      | "war |
|      | ning |
|      | ",   |
|      | "err |
|      | or", |
|      | or   |
|      | "cri |
|      | tica |
|      | l".  |
|      | The  |
|      | user |
|      | will |
|      | not  |
|      | be   |
|      | able |
|      | to   |
|      | edit |
|      | this |
|      | drop |
|      | -dow |
|      | n    |
|      | list |
|      | ,    |
|      | and  |
|      | the  |
|      | defa |
|      | ult  |
|      | valu |
|      | e    |
|      | for  |
|      | new  |
|      | Jobs |
|      | will |
|      | be   |
|      | logg |
|      | ing  |
|      | leve |
|      | l    |
|      | "inf |
|      | o".  |
+------+------+