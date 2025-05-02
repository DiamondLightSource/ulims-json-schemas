# Introduction for schema writers

The ulims-json-schemas repository provides a version controlled
location to store schema required by different applications. It
enables schema to reuse schema to avoid duplication.

This document starts with introduction for people new
to JSON schema. It explains adding a schema to the repository 
which contains four tutorials that build on each: 1st for
a basic schema; 2nd for an advanced schema; 3rd for schema
change over time, 4th for people doing reviews and merge
to main.

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

This repository supports both basic and advanced schema, with
a required check that confirms all references resolve for
the lifetime of a schema. A tutorial for doing both is below. 

## Adding a schema to the repository

Summary: create a schema folder
with a "current" file with certain values. Do a "latest"
release of the schema. Repeat release whilst editing current
files until all changes are completed. If release needs
to be shared commit to git, then push and request
merge to main.

### Setup on a new machine

A text editor and git is often already installed, but NPM
isn't: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

* git clone https://github.com/DiamondLightSource/ulims-json-schemas.git
* Confirm in repository root and get required tools with: `npm install` 
* Confirm CLI is working: `npx jsonschema-tools --version`

When adding (or editing a schema) always create a new
branch from main: `git checkout -b quickeg1`

### Four key points about a schema folder

* The repository has a schema root (sroot) folder which **contains
  all schema**. A schema root check (SRC) confirms all schema in
  every folder is valid and passes minimum requirements.

* A **schema consists of a folder** that can be anywhere
  in that root. To avoid future issues a suitable
  location in the folder structure should be found and
  the repository team can advise on good locations based on
  how much reuse by advanced schema is expected.

* A schema folder **contains a "current" file** which defines
  the "latest" release for next build. Each release get
  two files which must always exist whilst that release
  has value or is reused by another schema release.
  
* The **path to a schema folder** within the root is a required
  value in every current file and SRC will fail if wrong.

## Tutorial 1: using "emptyj" schema folder for a basic schema

The following tutorial creates a new basic schema from an
example within the repository. If you have an existing basic
schema the filename and certain values will require changing
to those explained in this section. A second tutorial showing
another example for an advanced schema is later. 

1. A strong recommendation before adding a new schema folder
   to the schema root is do SRC via command `npm run check` and
   [fix any issues](srcfixes.md) highlighted. 

### Create schema folder and define the latest version

2. Copy the **sroot/emptyj** schema folder to the location picked
   for the new schema. The location *sroot/zdemo/practice* can
   be used to store schema folders on a first attempt and
   don't commit new files created. *ie. a "quickeg" schema**

> [!WARNING]
> The SRC will now fail until step 3 and 4 are completed.

3. Edit **sroot/zdemo/practice/quickeg/current.json** and alter
   the following values. The filename "current.json" is a
   required value in a schema folder. 

   * **"title"** value MUST match the new location in the schema
     root folder excluding the root. *ie. zdemo/practice/quickeg*

   * **$id** is the most important value. It has three purposes.

      * It defines the latest release at build time and **must**
            end with semantic versioning. 

      * It defines this schema within a schema root
            and must be unique.  *ie. /zdemo/practice/quickeg/0.0.1*

      * It enables advanced schema (anywhere in a root) to
           find this schema release, so properties can be defined
           once and reused.

### Doing a schema release of latest version (takes ~10 seconds)

A schema release has two stages and both should complete before
files are committed to git. This release cycle is fast so
doing often whilst editing can reduce the effort required
to track down issues or find schema syntax errors.

4. Save the changes to "title" and $id and build the latest version
with `npm run build-new sroot/zdemo/practice/quickeg/current.json`

The file **0.0.1.json** will be overwritten and all soft links
will be updated to point at the new file. This is a basic
schema so the content will be almost identical to current.

> [!TIP]
> Using *build-new* targets the exact schema being worked on
> and reduces the risk of many changes to existing
> releases. The *npm run build-modified* command uses
> a git diff to target schema folders where current file changed
> and is recommended when changing a schema already merged to
> main. The *npm run build-all* commmand rewrites the
> latest release of every schema so slows down a regular
> build and check cycle suggested whilst editing a schema.

5. Stage two is confirm the SRC `npm run check` passes
   and [fix any issues](srcfixes.md) highlighted.

### Change body of schema

The version in the $id needs changing once whilst creating or
editing a schema. Schema "quickeg" is new so we can keep
overwriting version 0.0.1 on this occasion.

6. Edit **current.json** with the changes required for
   the latest release. (If you have a schema created elsewhere
   you can overwrite most of the content. Note, $schema
   value must be draft7 as per emptyj example. Repeat
   steps 4 and 5 until all changes are completed.

There are some changes that will complete step 4 but step 6
will highlight the $id MUST have a major release. See 
[fixes](srcfixes.md) about deleting files step 4 generated.

#### Editing an existing schema (merged to main) is nearly identical

Create a branch from main and do steps 1, 3 to 6 above.

> [!IMPORTANT]
> You should change the $id value BEFORE making changes to the
> schema body because step 4 will always overwrite the "latest"
> version. Advanced schema or applications can be using the
> original version. If $id is not changed first it's similar
> to releasing a new standard with the same name and saying
> nothing changed.

It is possible to use the same release number on a schema if
all advanced schema (using that release) are rebuilt and
all applications can support that reuse. A good case for this
is whilst a new schema is being finalised or a major version
reaches 2 digits.

### Finalise a release

Schema version control has nothing to do with source version
control. The latter (ie. git) tries to keep only one copy of
a file which appears in a tagged release. The former requires
all releases to exist at the same time for the lifetime of
a schema whilst need to validate data against a release exists.

7. Change the $id to 1.0.0 and do step 4 and 5. Delete files
   created by earlier releases.  *ie. files 0.0.1 and 0.0.1.json*

8. Edit the readme.md in the schema folder. Start with a short
   summary and status (draft, completed, retired). The team managing
   that schema with list of contributors. Ending with a list of
   changes in a release. See the copied emptyj folder as example.

9. Add the schema folder to git and commit. Push to github
   and do PR. An aim is to merge to main within 48 hours, for
   any new schema with a draft status.

#### About status and release versions (schema are considered seperate)

* Each schema before release 1.0.0 is unstable and should not
be reused by advanced schema or by applications unless the risks
have been considered.

* The same applies to a schema release 1.0.0 whilst status
  is draft. This means writers do not have to edit the $id
  every time a change is required and build just overwrites.

* The majority of new schema could reach draft 1.0.0
  quickly (in hours) with no committed point releases. All
  drafts in main should reach completed 1.0.0 status within
  an agreed schedule or get removed after N months.
  
A completed status means a schema is ready for reuse by an
advanced schema or by applications. It requires all
contributors to that schema to agree three things:

  * no future changes are expected for repository lifetime
  * change requires a new release with a different number
  * advanced schema using the old release will get new
    releases with that change applied.

High major or point numbers can signal the draft status
was changed too quickly. 

## Tutorial 2: using "emptyjref" schema folder for advanced schema

This tutorial explains how to add a new advanced schema
which reuses a basic schema. Steps are almost identical
to the first tutorial. The main difference is highlighted
after step 4. The edit in step 6 is limited to altering
the $ref so it points at the release done during tutorial 1.

1. Do SRC `npm run check` and fix any issues.

2. Copy the **sroot/emptyjref** schema folder to
   the location picked for the new schema. 

3. Edit **sroot/zdemo/practice/quickegref/current.json** and
   change title and $id to the required values.

4. Save the changes and build the latest version
with `npm run build-new sroot/zdemo/practice/quickegref/current.json`

The file **0.0.1.json** will be overwritten and all soft links
will be updated to point at the new file. This is an advanced
schema so the content **will NOT** be identical to
current. This is the most powerful feature of the tools
used to manage JSON schema. It has merged emptyj 0.0.1 release
into this schema. So quickegref release 0.0.1 is now
a "basic" schema from an application perspective, a single
standalone file.

5. Confirm the SRC `npm run check` passes
   and [fix any issues](srcfixes.md) highlighted.

### Changing $ref to point at quickeg 0.0.1 release

6. Edit **current.json** again and alter the $ref
   so it matches the $id of the schema release that needs
   merging into this schema. *ie. change ".../emptyj/..."
   to ".../practice/quickeg/...*

7. Repeat step 4 and 5 which completes a new release 0.0.1 of
   this schema. Commit, push and request PR when not tutorial.

Notice the content of 0.0.1.json has changed and has now merged
the content of quickeg into this schema. If quickeg had reached
"completed" status (and gets changed) all advanced schemas
using it should get new releases where **$id and $ref** have
changed.

## Tutorial 3: Changing two "completed" schema N months later

You can avoid the following if you make sure a schema
never requires changing or decide to avoid using $ref
keyword that automates property reuse, which is the most powerful
full feature of the tools. Assuming change is required...

<details>

<summary>Details... State of schema after tutorial 1 and 2. Two steps for change.</summary>

### State of quickeg and quickegref at start of tutorial 3

This tutorial pretends schema quickeg and schema quickegref
were finalised at release 1.0.0 and have a "completed"
status that was merged to main 12 months ago, so files for
1.0.0 exist on disk and earlier 0.0.1 files were deleted.

### Two steps over two days (simulates time passing)

The steps are almost identical to tutorials 1 and 2 but
the **order** they are done are important. Also, remember
each schema is seperate and can have a different
teams reponsible for it.

1. Day 1, Do SRC `npm run check` and fix any issues. Then,

2. Complete tutorial 1. Edit $id in quickeg/current.json with
new number before making changes and keep doing releases until
happy with the change. Remember the $id used. For a real
completed schema this would ideally be committed, pushed and
merged to main before doing day
two. *eg. "$id": "/zdemo/practice/quickeg/1.0.5"*

3. Day 2, Do SRC `npm run check` and fix any issues. (Pretend
   merge occured on day 1.) Then,

4. Complete tutorial 2. Edit $id in quickegref/current.json with
   a new number before making changes. Change the $ref to match
   the $id in step 2. *eg. "$id": "/zdemo/practice/quickegref/1.0.1"
   and "$ref": "/zdemo/practice/quickeg/1.0.5"*

Release numbers have nothing to do with each other. Numbers
are likely to be similar at the start but can diverge over
time if releases of basic schema occur more often. In this
case the advanced schema is pretending to skip over a point
releases (1.0.1 to  1.0.4) done on the basic schema over
the last year. If a $ref is changed to a release that
does not exist on disk the SRC will fail.

5. Repeat step 4 (tutorial 2) on every advanced schema using
   the basic schema. It is possible to edit $id and $ref in
   every schema and after building each do SRC once. Using
   command `npm run build-modified` is suggested to target
   build on any current file changed since last commit.

A schema flagged as "popular" might require step 5 to be done
by the team managing the advanced schema. That team can work
to the own timetables for confirming change does not
break their systems.

#### Why changing $id is imporant

An aim of schema releases is that past, present
and future releases are available at the same time
to allow applications to migrate over time at
different rates for testing and deployment.

If a change was made to quickref and its $id was not
udated **before the build** so causing the latest file
to be overwritten, divergence can occur. It will mean
any built advanced schema using this as a $ref will appear to
be using the same "$id" but the **definition will differ**
until next build. An advanced schema can $ref another
advanced schema and not changing the $id causes
a 2nd level of difference.

Using the `npm run build-all` command might solve this
problem but increases the chance of schema changes
before all applications has tested it.

</details>

## Tutorial 4: repeating tutorial 3, but with merge to main

All schema in main branch **must never break** for lifetime
of the repository. There is one exception which allows
tutorial 3 to be done with changes merged. 

Anyone writing schema can do this tutorial. Day 1 and 2
are expected to have been done by anyone looking
at PR for schema and doing merge the main. Day 5
shows edits from days 1 - 4 can be combined so
four schema changes are merged at same time.

<details>

<summary>Details... Schema to edit and suggested order of changes</summary>

### Five schema and what to edit when in tutorial 4

The schema group [reposhow](../sroot/zdemo/reposhow/readme.md)
contains five schema. Suggested order of editing is
as follows and imagine a day equals 6+ months. Doing day
1 and 2 is suggested for most repository contributors. If
a PR for an earlier day exist it should be merged
to main first and the next day uses a branch from main. Ask
repo team complete the PR outstanding. 

* day 1: change basic [fast schema](../sroot/zdemo/reposhow/basic/fast/current.json?raw=1)
release number and add a new property. If a required property
you must increase the major number before the next check.

* day 2: change [advfast schema](../sroot/zdemo/reposhow/advfast/current.json?raw=1)
release number and alter $ref to the release of fast schema
wanted. This might be what you did on day 1 unless multiple
people are doing the tutorial.

Day 3 and 4 is effecively tutorial 3 again because
the changes on day 1 and 2 have been used for N months. 

* day 3: change [advslow schema](../sroot/zdemo/reposhow/advslow/current.json?raw=1)
release number and alter $ref to wherever advfast used. Imagine
this schema is used by a production system that needs a schema
to change more slowly.

* day 4: change [advtop schema](../sroot/zdemo/reposhow/advtop/current.json?raw=1)
release number and alter $ref to wherever advslow has reached. This
might be what you did on day 3 unless multiple people are doing
the tutorial. Imagine 5+ schema exist that use advslow to define
themselves.

This is combining days 1-4 so a single PR will do all
changes. Imagine a popular basic schema has been used
as a $ref for 5+ years and something needs changing. The
change might break older applications.

* day 5: Four schema need changing. Firstly, change
basic [slow schema](../sroot/zdemo/reposhow/basic/slow/current.json?raw=1)
release number and add a new property like day 1. Avoid making
your new property required the first time you do this. Secondly,
alter the $ref in advfast and advslow to change just made. Thirdly,
repeat day 4. The PR should contain new releases for four
schema changed and old releases remain unchanged. Later, old
releases get deleted as per (to be agreed) processes.

</details>

## Technical details

The following provide more detail about files and two
other ways of doing the schema root check. 

### Files in a schema folder

The schema folder has at least six files:

* **current.json** - the most important file used to build
  the latest version of a schema. 

* **0.0.1.json** - a schema fixed at the point of last
  build. If a schema version has not changed a build will
  always overwrite with the same content.

* **0.0.1** & **latest** & **latest.json** - soft links to
  fixed schema. The last two update **if** a certain
  line of current gets edited.

* **current.yaml** - a blank file required for schema
  root check to pass.

The "yaml first" method is almost identical. See "empty"
schema readme for the two differences.

### Doing schema root check inside container

The Dockerfile uses the same container image that the wikimedia
primary root users. It copies configuration and adds the
schema folder before running test. 

* Whilst in project root: docker/podman build -t jsonschematools .

If container build completes all schemas passed all tests.

### Schema check within github workflows

All local checks should pass before being committed or
pushed to remote. However, github actions are used to
confirm pushes or pull requests pass the checks.

### Renaming folder for schema group

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


## Compatibility enforcement

There are some changes to schema files which require
major, minor or point releases to pass checks. This
section documents them. 

### Required values (major release required)

Schema properties are not required by default. Changing a
property to required **MUST** be a major release. All schema
using that schema must also get a major release.

### How to fix

A simple way to bypass is to delete all generated files on
disk before the schema release being worked on. The build
will update the soft links so check passes again. *ie.
release 0.0.2 was attempted and built okay but check
failed, so change $id to 1.0.0 do a rebuild, delete 0.0.2.json
and check will pass again.
