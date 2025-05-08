# About zdemo schemas set

Zdemo contains files and folders which follow a standard
pattern expected for a set of schemas. Schema should
never be in schema root. Using schema groups (ie. sub-folders)
is recommended, as this set does.

## Schema and schema groups available

All schemas defined in this set **MUST NOT** be used outside
of this set. In contrast, other sets should assume any
schema they define is are getting reused by other schema
outside of their set.

### empty - standard folders for creating a new schema

The zdemo set provides three folders for copying into other
schema sets. It provides the minimum files to get started
with version 0.0.1 of a new schema.

* [readme in /zdemo/emptyj/](emptyj/readme.md) - a standard
folder for new basic schema in repository using current.json
to define latest release. See tutorial 1 about how to use this.

* [readme in /zdemo/emptyjref/](emptyjref/readme.md) - a standard
folder for new schema using references to other schemas all
that are defined with current.json files. See tutorial 2
about how to use this.

* [readme in /zdemo/empty/](empty/readme.md) - a standard folder
for new schema in repository using current.yaml. This schema is
creating a JSON schema in original way the team writing the tool
use the tools to define schema. It can be used to reset or
regenerate emptyj if the tools change behaviour.

### Reposhow schema group

The schema in the repository must never break. An exception
are those in this folder. See [reposhow readme](reposhow/readme.md)
for more details.

### Practice schema group

A folder with a [single readme](practice/readme.md). It exists
to enable tutorial 1 and 2 to be done on a fresh clone
of the repository and the schema folders are created
at the recommended depth for a new schema. 

## Changes

Major changes to the zdemo schema

### April 2024

* Start of set with reposhow and practice schema groups.
