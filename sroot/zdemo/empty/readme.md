# Empty schema

This empty schema contains the minimum set of files required
to create a schema. It can be copied into another scheme set
or group and **must be edited** before the schema root
is next checked. There are two files and four soft links.

* **current.yaml** - the most important file used to build
  the latest version of a schema. 

* **0.0.1.json** - a schema fixed at the point of last
  build. If a schema version has not changed a build will
  always overwrite with the same content.

* **0.0.1** & **latest** & **latest.json** - soft links to
  fixed schema. The last two update **if** a certain
  line of current gets edited.

* **current.json** - soft link to latest.json which is a
  requirement for the schema root test to pass. If missing, 
  copy the fixed .json last built from current.yaml


## Creating a new schema using this schema.

1. Run schema root check **npm run check** and correct
   any issues before continuing. This command should be reused
   within a few seconds of any edit and build.

2. Decide a location in a schema set or group. Quick attempts
can use the: *zdemo/practice/* group folder, making sure the
pasted folder name contains no spaces. For a "real" schema
a folder name and location in a schema root can change
until 1.0.0 is reached.

3. Edit **current.yaml** in a text editor and alter values for:

   * **title** - must match the folder structure excluding
     the schema root. ie. *zdemo/practice/quickeg*
    
   * **$id** - is the most important value. It has three purposes.

      1. It defines this schema within a schema root
         and must be unique. ie. */zdemo/practice/quickeg/0.0.1*
      
      2. It enables shared schemas (anywhere in a root) to find
         each other so properties can be defined once and reused.

      3. Most importantly, it controls the version the
         build command will generate. A command exists to
         automatically detect changes to this value provided
         the last built version was committed to git.

4. Save those changes and execute build-new command. ie. *npm
   run build-new sroot/zdemo/practice/quickeg/current.yaml*

5. The file *0.0.1.json* will be overwritten and all
   soft links updated to point at the new file.

6. Execute **npm run check** and your new schema should
   appear on the list tested with any issues highlighted.

7. Fix issue(s) before changing the rest of the file.

8. Change schema and repeat from step 4.

### Time passes - point releasing new schema

A real schema would have had the six files above committed
into git when happy with the first draft. Versions should
be merged into main at the earliest point with changes (based
on review/comments) a point release.

Schema version 0.0.1 needs changing based on comments in
the github issues on the main branch.

1. Execute *npm run check* to confirm schema root has no issues
   and fix if any existing before making changes.

2. Edit the current file and alter values for:

    * **$id** - change the version on the end of the line
                to a suitable value. ie. *from 0.0.1 to 0.0.2*

3. Use the build-new command as step 4 above and a new json
   file for that version will appear. Soft links will change.

4. Repeat step 1.

6. Change the schemas as required and repeat 3 and 4 until
   happy with the changes.

5. Update changes in the readme.md to explain the new version
   and link to discussions that caused it.

6. Add and commit to git when fully completed.

### Automation of these steps

If writing a new schema set or group creating a build
script for step 3 is suggested so all "current" schemas
being working on can be built quickly. Retaining 
the script if future work will be need on
that set. ie. *sroot/zdemo/build.sh*

Once a schema is commited at least once a command exists
that will automatically detect and build changed version
with optional git add. This will be documented elsewhere.

## Changes

* **0.0.1** - First draft of empty schema (March 2025)
