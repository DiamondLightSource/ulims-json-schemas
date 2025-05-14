# Tutorial 1: basic schema with no references

This first tutorial explains how to add a new
schema to the repository using the tools enabled. It
highlights:

* every schema must have a folder with
  a "current" file and that file must use
  exact patterns for "title" and "$id" values.

* a schema build must be done which will overwrite
  the "latest" release by default. If build fails edit the
  current file until issue(s) are fixed.

* a SRC (schema root check) is required to pass after
  all builds have been completed. Among other things
  it confirms the latest (and previous releases) of every
  schema in the repository are still valid.

## Using "emptyj" schema folder for a basic schema

The following creates a new basic schema from an
example within the repository. If you have an existing basic
schema the filename and certain values will require changing
to those explained in this section. A second tutorial showing
another example for an advanced schema is later. 

1. Doing a SRC via command `npm run check` is recommended
   before adding a new schema folder.

### Steps A and B: Create schema folder and define the latest version

2. Copy the **examples/emptyj** schema folder to the location picked
   for the new schema. The location *schemas/practice* will be
   used to store schema folders in tutorials. This tutorial
   is defining the "quickeg" schema which will be used by
   tutorial 2.

> [!WARNING]
> The SRC will now fail until step 3 and 4 are completed.

3. Edit **schema/practice/quickeg/current.json** and alter
   the following values. The filename "current.json" is a
   required value in a schema folder. 

   * **"title"** value MUST match the new location in the schema
     root, excluding the root folder name. *ie. practice/quickeg*

   * **$id** is the most important value. It has three purposes.

      * It defines the latest release at build time and **must**
            end with semantic versioning. 

      * It defines this schema within a schema root
            and must be unique.  *ie. /practice/quickeg/1.0.0*

      * It enables advanced schema (anywhere in a root) to
           find this schema release, so properties can be defined
           once and reused.

### Steps C and D:  Doing a schema release of latest version (takes ~10 seconds) 

A schema release has two stages and both need to be
completed. This release cycle is fast so doing often
whilst editing can reduce the effort required
to track down issues or find schema syntax errors.

4. Save the changes to "title" and $id and build the latest version
with the shortcut command `npm run build-all`

The file **0.0.1.json** will be overwritten and all soft links
will be updated to point at the new file. This is a basic
schema so the content will be almost identical to current.

> [!TIP]
> The `build-new` command exists to target an exact schema
> which can speed up build and check cycles while reducing
> the risk of many changes to existing schema. For
> this schema it would have 
> been: `npm run build-new schemas/practice/quickeg/current.json`
> The `npm run build-modified` command uses
> a git diff to target schema folders where current file changed
> and is recommended when changing a schema already merged to
> main. The `npm run build-all¬ commmand rewrites the
> latest release of every schema.

5. Stage two is confirm the SRC `npm run check` passes
   and [fix any issues](srcfixes.md) highlighted.

### Step E: Change body of schema

The version in the $id needs changing once whilst creating or
editing a schema. Schema "quickeg" is new, with a draft status
so we can keep overwriting version 0.0.1 on this occasion.

6. Edit **current.json** with the changes required for
   the latest release. (If you have a schema created elsewhere
   you can overwrite most of the content. Note, $schema
   value must be draft7 as per emptyj example. Repeat
   steps 4 and 5 until all changes are completed.

There are some changes that will complete step 4 but step 5
will highlight required changes. See the SRC fixes page.

#### Editing an existing schema (merged previously) is nearly identical

Create a branch from main and do steps 1 and 3. **Change the $id
before doing** step 4 and 5. Do step 6 which has the main
change to the schema.

> [!IMPORTANT] 
> Changing the $id in step 3 **before** a build in step 4 is
> important if you are editing a "completed" schema. For
> draft schema the $id can stay the same which 
> will overwrite the latest release.

### Step F: Finalise a release

Schema version control has nothing to do with source version
control. The latter (ie. git) tries to keep only one copy of
a file which appears in a tagged release. The former requires
all releases to exist at the same time for the lifetime of
a schema whilst need to validate data against a release exists.

7. Change the $id to 1.0.0 and do step 4 and 5. Delete files
   created by earlier releases.  *ie. files 0.0.1 and 0.0.1.json*

8. Edit the changelog.md. Each release should have an entry
   with date, summary and person/team making the edit.

9. Add the schema folder to git and commit. Push branch
   to github and do PR. 

#### About status and release versions (schema are considered seperate)

All schema have status draft unless marked as "status-completed". The
status can be ignored by new writers. Applications can ignore
the status if the risks are understood, see the status section
of the application [details](appdetails.md) page.