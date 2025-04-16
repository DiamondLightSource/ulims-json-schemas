# ULIMS JSON schemas

A collection of JSON schemas for ULIMS systems.

## About

This repository uses the method the Wikipedia team
use for managing JSON schemas over time. They have
two schema roots whilst ULIMS has this one. Links
to Wikipedia usage end this document.

## Usage

Applications can download and use a built schema to
validate data against that schema. A built schema has no
external dependency. Various versions of each schema
are maintained on disk and systems should cache
those need. Github raw can be used in the first instance
and applications should do a systems check against
release top 0.0.1 before raising issues.

* [Can host see this schema?](sroot/zdemo/pattern1/top/0.0.1.json?raw=1)
* [Can schema downloaded validate this data?](sroot/zdemo/pattern1/top/checkpy.datafile?raw=1)

The [zdemo readme](sroot/zdemo/readme.md) explains how to use
this repository to test all existing schemas and explains
creating and building a standalone or shared schemas. 

## Schema sets available

The following sets exist.

1. [zdemo](sroot/zdemo/readme.md) - A minimum set for
   confirming a schema root can be built with design 
   patterns that applications can test themselves against. It
   contains a pre-defined "empty" schema for copying with a
   schema group for trying it out.

2. [shared](sroot/shared/readme.md) - A common set of schemas
   that provides the highest level of reuse across all schema
   sets, systems and applications.
  
3. [instruments](sroot/instruments/readme.md) - Schemas 
   unique to instruments.


## Glossary

The following terms are used in the documentation.

* **schema root** - all schemes are kept in a root which any
  schema can reference by using / in certain places. Multiple
  roots could exist but scripts expect a single. Folder *sroot*
  is the root of this schema repository. 

* **schema set** - a collection of schemas which can
  often reference themselves. A macro application
  or microservice might have a set. Folder *sroot/zdemo* is
  an example set.

* **schema group** - a collection of schemas related
  to each other and recommended level for a
  schema. Folder *sroot/zdemo/pattern1* is an example group
  which also has a child sub groups.

* **schema** - a schema is a complete JSON schema and always
  has a unique folder containing a "current"
  version. Folder *sroot/zdemo/empty* can be copied
  into a scheme set or group and **after editing**
  version 0.0.1 of a new schema can be built. Three types exists,
  where the first is easiest.

  * **standalone** - have properties and no external references. A
    build for low level schema (like empty) appears to do almost
    nothing. This type is how most schema will start until
    reuse patterns emerge. Folder *sroot/zdemo/pattern1/child/three*
    is example.

  * **shared** - has references to other schemas which means
    properties come from an exact version of a standalone
    schema **when** built. Child one and two are examples
    in pattern 1.

  * **top** - a shared schema expected to be cached by
    applications which is built from a collection of shared
    schemas. Folder *sroot/zdemo/pattern1/top* is example. A
    large number of top schemas could exist which are close
    to identical except for some properties. 

A schema root **MUST** be built and tested when a schema version
changes. Additional terms:

* **SRC (Schema Root Check)** - all schemas in all folders
  must pass this check before being committed. Doing a SRC
  means running command **npm run check** and it reporting
  no outstanding issues.

* **current** - the source of a built schema with an $id that
  encodes the version of this schema. The **only** file that
  should edited manually in a schema folder.

* **built** - a schema needs building at least once to generate
  the necessary files. The version in $id will be used to
  generate an exact versioned schema and make soft links.

* **latest** - a build will always update a "latest"
  soft link **if** the version in $id is newer. It signals
  a point release is due. Schemas using the old version
  will continue to work and build with version they pinned.

* **pinned** - references in current between schemas
should be pinned to an exact version of a schema. (A current
can use latest of another schema, but pinned is best)

Technically, a build turns schemas of all types into
standalone versions that applications are free to cache.

## Useful links

The two roots show possible arrangements of schemas and
how to use the tools on a repository. Applications access
built schemas via a web server with mounted filesystem. 

* Schema root 1: https://gitlab.wikimedia.org/repos/data-engineering/schemas-event-primary/
* Schema root 2: https://gitlab-replica-b.wikimedia.org/repos/data-engineering/schemas-event-secondary/
* Application access (ie. filesystem on web): https://schema.wikimedia.org/#!/
* Build tools: https://gitlab.wikimedia.org/repos/data-engineering/jsonschema-tools
* Why jsonschema: https://wikitech.wikimedia.org/wiki/Event_Platform/Schemas
* Why git: https://phabricator.wikimedia.org/T201643

## Schema version

The jsonschema-tools (as of 1.3.0) test will fail if any file
contains the latest (as of March 2025) JSON schema draft
and requires use of draft 7
 
* ~~"$schema": "https://json-schema.org/draft/2020-12/schema"~~

* "$schema": "https://json-schema.org/draft-07/schema#"