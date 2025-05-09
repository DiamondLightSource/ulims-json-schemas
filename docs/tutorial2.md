# Tutorial 2: schema using references

This tutorial explains how to add a new advanced schema
which reuses a basic schema. Steps are almost identical
to the first tutorial. The key difference is highlighted
after step 4. The edit in step 6 is limited to altering
the $ref so it points at the release done during tutorial 1.

1. Do SRC `npm run check` and fix any issues.

2. Copy the **sroot/emptyjref** schema folder to
   the location picked for the new schema. 

3. Edit **schema/practice/quickegref/current.json** and
   change title and $id to the required values.

4. Save the changes and build the latest version
with `npm run build-new schema/practice/quickegref/current.json`

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

## Changing $ref to point at quickeg 0.0.1 release

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
