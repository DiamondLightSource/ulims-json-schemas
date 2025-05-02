# ULIMS JSON schemas

A collection of JSON schemas for ULIMS systems.

## About

This repository uses the method the Wikipedia team
use for managing JSON schemas over time. They have
two schema roots whilst ULIMS has this one. Links
to Wikipedia usage end this document.

## Usage

Applications can download and use a released schema to
validate data against that schema. Schema have no
external dependency once downloaded. Various releases
of each schema can be maintained on disk and systems
should cache those needed. Github raw can be used in
the first instance and applications should do a systems
check against a reposhow schema before raising issues.

* [Can host see this schema?](sroot/zdemo/reposhow/advslow/1.0.0.json?raw=1)

The schema linked above includes example data for required
values. A writer can override with custom examples so all
applications can use the same test cases for a schema release.

## Schema sets available

Schema can be put anywhere in the schema root but to avoid
future issues the following sets exist to keep
schema folders in. Additional sets might appear.

1. [zdemo](sroot/zdemo/readme.md) - A minimum set for
   confirming a schema root can be built. It contains
   a pre-defined "empty" schema for copying with a
   schema group for trying it out. See readme for
   schema writers below.

2. [shared](sroot/shared/readme.md) - A common set of schemas
   that provides the highest level of reuse across all schema
   sets, systems and applications. For examples, units
   or chemical elements.
  
3. [instruments](sroot/instruments/readme.md) - Schemas 
   unique to instruments, where each gets a folder.

## Documentation for schema writers

The documentation for [schema writers](docs/readme.md) explains
how to add a new schema. It starts with some links for writers
new to JSON schema. Tutorials 1 and 2 should be done by
new contributors including those who have written
schema before. Tutorial 3 simulates schema change
over time.

The tutorial explains every schema **must**
have a "current" file and releases merge schema. For
example, the schema linked above is an application
point of view. Writers get
a [different point](sroot/zdemo/reposhow/advslow/current.json?raw=1)
of view. 

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

## JSON schema version

The jsonschema-tools (as of 1.3.0) check will fail if any
current file has a $schema not using draft 7.
 
* ~~"$schema": "https://json-schema.org/draft/2020-12/schema"~~

* "$schema": "https://json-schema.org/draft-07/schema"