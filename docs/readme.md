# Introduction for schema writers

The ulims-json-schemas repository provides a version controlled
location to store schema required by different applications. It
enables schema to reuse schema to avoid duplication.

This document starts with introduction for people new
to JSON schema. It explains adding a schema to the repository 
and links to some tutorials. If you have not contributed
previously the setup at the end of this page maybe required.

## New to JSON schema

The json schema website provides a
[getting started](https://json-schema.org/learn) section
and you should have read at least creating your
[first schema](https://json-schema.org/learn/getting-started-step-by-step).

A basic schema defines everything in a single file. An advanced
schema can use
[external references](https://json-schema.org/learn/getting-started-step-by-step#add-an-external-reference)
via the $ref keyword. Using a $ref enables a schema to reuse
another basic or advanced schema to avoid duplication. 

This repository supports both basic and advanced schema. A
required check must pass for all schema. This is explained
below and in the first tutorial.

## Adding a schema to the repository

There are six steps, in summary:

A. Create a folder inside the schema root. Folder "schemas"
is the root of this repository. Folders in "schemas" exist
and new schema folders will need to be inside the most suitable
location by the end of step 6.

B. Inside that new folder create a "current.json" file with "title"
   and $id matching an exact pattern based on path in root. 

C. Build the latest release. The $id in step 2 is important and
   defines the release number. There are recommendations for
   when to change the number. A JSON schema is valid if no
   errors occur. There is little point committing to git until
   a build completes at least once.

D. Confirm the schema root check (SRC) passes. This is
   done automatically on pushes to github
   repository. If issues are shown it will often be
   quicker to run this locally whilst editing file(s).

E. Populate current file with the unique parts of a
   schema. Step 2 and 5 can be combined. Steps 3 and 4
   is required before a schema will be merged to main.

F. Once the SRC passes create a pull request asking for
   a merge to main. 

A shortcut for step 3 is command `npm run build-all` but more
targeted commands exist that are recommended at certain
times. The tutorials use those other commands.

Step 4 is the command is `npm run check` which confirms every
schema (and every release of a schema) meet minimum quality
and security standard. For example, are $ref to a particular
schema release still valid?

## Tutorials

There are two tutorials which build on each other.

* [Tutorial one](tutorial1.md) explains the exact patterns
required in step 2 for a basic schema. It uses a pre-created
schema folder in this repository for copying at step 1 with
most of step 2 done so release 1.0.0 can be done quickly via
steps 3 and 4 and it will just work for a new schema.

* [Tutorial two](tutorial2.md) is nearly identical to the first
but applies it to an advanced schema using a $ref. It uses
another pre-created schema folder for coping in step 1
and assumes the exact pattern are understood. It hightlights
how a build of a basic schema differs from an advanced
scheme. This difference has implications for schema
change over time.

The following tutorials are intended for anyone
who wants to do the merge to main.

* [Tutorial three](tutorial3.md) uses the schema created
in tutorials 1 and 2 to explain the implications and
how to migrate both over time.

* [Tutorial four](tutorial4.md) applies tutorial 3 using
schema examples that can be merged to main.

## Setup on a new machine

A text editor and git is often already installed, but NPM
isn't: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

* git clone https://github.com/DiamondLightSource/ulims-json-schemas.git
* Confirm in repository root and get required tools with: `npm install` 
* Confirm CLI is working: `npx jsonschema-tools --version`

When adding (or editing a schema) always create a new
branch from main: `git checkout -b quickeg1`


## Additional docs

*[Technical details](techdetails.md)

