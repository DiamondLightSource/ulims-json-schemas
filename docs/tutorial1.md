# Tutorial 1: basic schema with no references

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

## Using "emptyj" schema folder for a basic schema

The following tutorial creates a new basic schema from an
example within the repository. If you have an existing basic
schema the filename and certain values will require changing
to those explained in this section. A second tutorial showing
another example for an advanced schema is later. 

1. A strong recommendation before adding a new schema folder
   is do SRC via command `npm run check` and
   [fix any issues](srcfixes.md) highlighted. 

### Create schema folder and define the latest version

2. Copy the **sroot/emptyj** schema folder to the location picked
   for the new schema. The location *schema/practice* can
   be used to store schema folders on a first attempt and
   don't commit new files created. *ie. a "quickeg" schema**

> [!WARNING]
> The SRC will now fail until step 3 and 4 are completed.

3. Edit **schema/practice/quickeg/current.json** and alter
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
with `npm run build-new schema/practice/quickeg/current.json`

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
