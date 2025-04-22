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

## Documentation

The following documentation exists for schema writers:

* [glossary of terms](docs/glossary.md)

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

* "$schema": "https://json-schema.org/draft-07/schema#"git s