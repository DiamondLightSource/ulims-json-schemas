# Introduction for schema writers

The ulims-json-schemas repository provides a version controlled
location to store schema required by different applications. It
enables schema to reuse schema to avoid duplication.

This document starts with introduction for people new
to JSON schema. It explains adding a schema to the repository 
via automatic and advanced methods. If you have not contributed
previously the setup at the end of this page maybe required.

## New to JSON schema

The json schema website provides a
[getting started](https://json-schema.org/learn) section
and you should have read at least creating your
[first schema](https://json-schema.org/learn/getting-started-step-by-step).

A basic schema defines everything in a single file. An advanced
schema can use
[external references](https://json-schema.org/learn/getting-started-step-by-step#add-an-external-reference)
via the `$ref` keyword. Using a `$ref` enables a schema to reuse
another basic or advanced schema to avoid duplication. 

This repository supports both basic and advanced schema. A
required check must pass for all schema. This is explained
below and in the first tutorial.

## Adding a schema to the repository - automatic build (recommended)

There are six steps.

1. Make sure you have the latest origin main and have created
   a new branch via `git checkout -b your-schema-branch`. One
   schema change per branch is recommended.

2. Create a schema folder inside the appropriate folder
   under `schemas` and instrument, for example `schemas/samples/p99/newschemaone`

3. Inside that new folder create a "current.json" file with "title"
   and $id matching an exact pattern based on path in root. See
   basic and advanced schema in examples folder for pattern. Create
   the schema as required.

> [!IMPORTANT]
> For existing schema, changing the number
> in **$id first** is recommended to avoid overwriting
> existing releases. This is **very important** for schema
> at 1.0.0 or newer being used by production systems. If
> you forget to change the $id now, a cleanup via the advanced
> method is required in many cases after step 6. Draft schema
> can overwrite themselves.

4. Commit current.json and in commit message mention:
   the schema name, version change made to $id and
   optionally what changed. The basic and advanced
   examples have a changelog.md which is recommended
   for most schema. Example commit message: "Bump schemaD to 1.0.1
   using newer ref-schemaE 2.0.6"

5. Execute `git push origin your-schema-branch` and
   visit https://github.com/DiamondLightSource/ulims-json-schemas
   to start a pull request on your branch. (Your push should
   have appeared with a button to start a pull-request if you
   are logged in.
   
6. The action "Build current.json different..." will run and
   appear on the GH `Actions` tab. A green tick will appear if
   everything builds and the check passes. Technically, this
   action is doing `npm run build-main-diff` then **commiting
   new files to your branch** which you can pull to see changes.

> [!TIP]
> The commit message "Schema(s) build and commit via GH action."
> will appear if the alterations made in step 3 caused new files or
> the "latest" softlinks to change.

If a red cross appears then you can click on it to see
more information about the failures. Check any
failures in "Build current.json different than main and commit".

If getting a lot of errors it is recommended to try running this 
process locally. See the "Setup on a new machine" section for 
information on the set-up. Then run `npm run build-main-diff` 
and `npm run check` to test locally. It removes most delays 
caused by steps 3-6 so build/check iterations can be quicker. 
Once everything passes, repeat from step 4 and the action 
will commit the other four files a build generates.

> [!TIP]
> A green tick on action, then a pull and new local build should
> cause no schema related files to appear in a `git status` or
> `git diff` output.


## Adding a schema to the repository - local build (advanced)

There are five steps, in summary:

1. Create a schema folder inside the appropriate folder
   under `schemas` and instrument, for example `schemas/samples/p99/newschemaone`

2. Inside that new folder create a "current.json" file with "title"
   and $id matching an exact pattern based on path in root. See
   basic and advanced schema in examples folder for pattern. Create
   the schema as required.

3. Build the latest release by running `npm run build-all`. The
   $id in step B is important and defines the release number.
   There are recommendations for when to change the number.
   A JSON schema is valid if no errors occur.

4. Confirm the check passes with `npm run check`. This
   is done automatically on pushes to github
   repository. If issues are shown it will often be
   quicker to run this locally whilst editing file(s).

5. Once the check passes create a pull request asking for
   a merge to main. 


A page of [common build or check issues](common_issues.md)
starts with some tips and shows messages the jsonschema-tools
can cause. Expand the message to see cause and fixes.

### Stable and beta releases

The `$id` define releases and it must end with semantic
numbers. Release 1.0.0 is the first stable release. Earlier
numbers are beta releases that could change without notice.

* Changes to a stable schema should be point releases unless
  major or minor release are forced by step 4. Old releases
  should continue to work for lifetime of repository until
  a release is phased out.

* Schema writers of beta releases do not have to alter
  the number in $id for every change. This avoids keeping
  multiple releases on disk. For example, having an $id end
  with `/0.0.1` will overwrite `0.0.1.json` on every build. 

> [!TIP]
> Advanced schema using a basic schema can evolve at
> different speeds and release numbers can appear to
> be related. But, each schema is standalone so
> each release number is separate from the other.


## Setup on a new machine

A text editor and git is often already installed, but NPM
isn't: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

* git clone https://github.com/DiamondLightSource/ulims-json-schemas.git
* Confirm in repository root and get required tools with: `npm install` 
* Confirm CLI is working: `npx jsonschema-tools --version`

When adding (or editing a schema) always create a new
branch from main: `git checkout -b quickeg1`
