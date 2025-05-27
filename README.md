# ULIMS JSON schemas

A collection of JSON schemas for ULIMS systems.

## About

This repository uses the method the Wikipedia team
use for managing JSON schemas over time. They have
two schema roots whilst ULIMS has this one. Links
to Wikipedia usage end this document.

## Usage by applications

Applications can use a released schema to validate
data against that schema.

For `latest.json` and specific versions (`X.X.X.json`) schema
references are resolved such that a schema can be used
directly without reference to any external dependencies.

Github raw can be used for accessing schemas for now.
The example schemas can be used for testing, such
as [examples/advanced/1.0.0.json](schemas/examples/advanced/1.0.0.json?raw=1).

The schema linked above includes example data for required
values. A writer can override with custom examples so all
applications can use the same test cases for a schema release.

## Schema sets available

Schema can be put anywhere in the schema root. The following
sets exist for putting schema into and new ones can be
added when needed:

* [examples](schemas/examples/) - - A minimum set that can be
  used for testing and checking release process.

* [shared](schemas/shared/) - A common set of schemas
   that can but reused across all schema, services and
   applications. For examples, units or chemical elements.

* [samples](schemas/samples/) - Schemas for samples
  service.

## Documentation for schema writers

The documentation for [schema writers](docs/readme.md) explains
how to add a new schema. It starts with some links for writers
new to JSON schema before moving to the six steps for adding.

It explains every schema **must** have a "current" file for
building the "latest" release. A build will combine
schema when needed so writers get
a [simpler view](schemas/examples/advanced/current.json?raw=1)
which just shows a link to the referenced schema.

## Wikimedia Example Usage

The two roots show possible arrangements of schemas and
how to use the tools on a repository. Applications access
built schemas via a web server with mounted filesystem. 

* Schema root 1: https://gitlab.wikimedia.org/repos/data-engineering/schemas-event-primary/
* Schema root 2: https://gitlab-replica-b.wikimedia.org/repos/data-engineering/schemas-event-secondary/
* Application access (ie. filesystem on web so "latest" links work): https://schema.wikimedia.org/#!/
* Build tools: https://gitlab.wikimedia.org/repos/data-engineering/jsonschema-tools
* Why jsonschema: https://wikitech.wikimedia.org/wiki/Event_Platform/Schemas
* Why git: https://phabricator.wikimedia.org/T201643
