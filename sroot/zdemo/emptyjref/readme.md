# Empty schema - current.json references other schemas release

This empty schema contains the minimum set of files required
to create a schema that uses other schemas as the main source
of properties. It can be copied into another scheme set
of group and **must be edited** before the schema root
is next tested. There are two files and four soft links.

It is nearly identical to the emptyj folder but references
version 0.0.1 of that schema to define its properties.

* **current.json** - the most important file used to build
  the latest version of a schema. It is not a soft link
  in this empty schema. A build will merge all references
  and do a release.

* **0.0.1.json** - a schema fixed at the point of last
  build. If a schema version has not changed a build will
  always overwrite with the same content.

* **0.0.1** & **latest** & **latest.json** - soft links to
  fixed schema. The last two update **if** a certain
  line of current gets edited.

* **current.yaml** - unlike the other empty schema this
  is a blank file required for schema root check to pass.

## Creating a new schema using this schema.

1. Run schema root check **npm run check** and correct
   any issues before continuing. This command should be reused
   within a few seconds of any edit and build.

2. Decide a location in a schema set or group. Quick attempts
can use the: *zdemo/practice/* group folder, making sure the
pasted folder name contains no spaces. For a "real" schema
a folder name and location in a schema root can change
until 1.0.0 is reached.

3. Edit **current.json** in a text editor and alter values for:

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
   
   * **properties/empty_from/$ref** is what makes this empty
     schema different than the other. It sources properties
     from other schema versions. Edit "empty_from" to suitable
     value. The $ref **must** refer to an $id that appears
     somewhere else in the schema root or the $ref must 
     resolve at build so release can be saved to disk.

4. Save those changes and execute build-new command. ie. *npm
   run build-new sroot/zdemo/practice/quickeg/current.json*

5. The file *0.0.1.json* will be overwritten and all
   soft links updated to point at the new file.

6. Execute **npm run check** and your new schema should
   appear on the list tested with any issues highlighted.

7. Fix issue(s) before changing the rest of the file.

8. Change schema and repeat from step 4.

### Time passes - releasing schema where references change

A real schema would have had the six files above committed
into git when happy with the first draft. Releases should
be merged into main at the earliest point with changes (based
on review/comments) a point release of this schema.

Schema version 0.0.1 needs changing based on comments in
the github issues on the main branch and needs to use a newer
release of referenced schemas.

1. Execute *npm run check* to confirm schema root has no issues
   and fix if any existing before making changes.

2. Edit the current file and alter values for:

    * **$id** - change the version on the end of the line
                to a suitable value. ie. *from 0.0.1 to 0.0.2*
   
    * **$ref** - change release to newer release. 

3. Use the build-new command as step 4 above and a new json
   file for that version will appear. Soft links will change.

4. Repeat step 1.

5. Change the schemas as required and repeat 3 and 4 until
   happy with the changes. If there is more than one $ref
   to alter consider changing them one-by-one in this step
   so if any breaks the check will detect.

6. Update changes in the readme.md to explain the new version
   and link to discussions that caused it.

7. Add and commit to git when fully completed.

## Changes

* **0.0.1** - First draft of emptyjref schema (March 2025)
