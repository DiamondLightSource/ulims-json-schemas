# Technical details

The following provides additional details.

## JSON schema version

The jsonschema-tools (as of 1.3.0) check will fail if any
current file has a $schema not using draft 7.
 
* ~~"$schema": "https://json-schema.org/draft/2020-12/schema"~~

* "$schema": "https://json-schema.org/draft-07/schema"


## Files in a schema folder

The schema folder has at least five files:

* **current.json** - the most important file used to build
  the latest version of a schema. 

* **0.0.1.json** - a schema fixed at the point of last
  build. If a schema version has not changed a build will
  always overwrite with the same content.

* **0.0.1** & **latest** & **latest.json** - soft links to
  fixed schema. The last two update **if** a certain
  line of current gets edited.

The "yaml first" method is almost identical. See "empty"
schema readme for the two differences.

## Doing schema root check inside container

The Dockerfile uses the same container image that the wikimedia
primary root users. It copies configuration and adds the
schema folder before running test. 

* Whilst in project root: docker/podman build -t jsonschematools .

If container build completes all schemas passed all tests.

## Schema check within github workflows

All local checks should pass before being committed or
pushed to remote. However, github actions are used to
confirm pushes or pull requests pass the checks.

## Renaming folder for schema group

A schema should be put in the best location at the
earliest time to remove the need to make a large number
of schema releases. A schema with completed status
would ideally never change location.

It is possible to change the folder name for a schema
set or group.

1. Do SRC and fix any issues.

1. Rename folder. An IDE will not automatically replace
   occurances in schema.

2. Search and replace the old folder name with the new in
   every file using it. The title, $id any $refs need
   changing. It includes rewriting old releases.

3. Build all changed files and do SRC. Fix any issues.


# Compatibility enforcement

There are some changes to schema files which require
major, minor or point releases to pass checks. This
section documents them. 

## Required values (major release required)

Schema properties are not required by default. Changing a
property to required **MUST** be a major release. All schema
using that schema must also get a major release.

## How to fix

A simple way to bypass is to delete all generated files on
disk before the schema release being worked on. The build
will update the soft links so check passes again. *ie.
release 0.0.2 was attempted and built okay but check
failed, so change $id to 1.0.0 do a rebuild, delete 0.0.2.json
and check will pass again.
