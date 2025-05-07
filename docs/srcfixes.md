# Fixes for build and schema root check (SRC) issues

This page highlights some fixes for common error. Doing
the SRC is recommended before and after making any
change to a schema. The common solution is:

1. Edit current.json file to fix problem.

2. Target the build: `npm run build-new path-to-current-dot-json`
   or `npm run build-modified` if changes were made to
   commited file. The build-all command can make it more
   difficult to track issues.

3. Run schema root check `npm run check`

Example
<details>

<summary>Message to look during build or check</summary>

### Overview of issue

A longer description of the issue if summary not clear.

### How to fix

What to change.

</details>

## Tutorial 1 and 2 issues

These can occur during build commands or later
during the SRC which are marked. They are here
but can occur whenever a schema folder moves
within the schema root. 

<details>

<summary>SRC: "schema title must match relative schema directory"</summary>

### New or moved schema folder without a required value 

You have created a new schema folder or an existing
schema folder was moved without updating "title" value.

### Edit "title" in current

Bullet point 3 of tutorial 1 explains what the value should
be. The value in green is wrong, value in red correct value. A
build is optional to fix this.

</details>

<details>

<summary>SRC: "could not find latest schema version file"</summary>

### New or moved schema folder without a required value

You have created a new schema folder or an existing
schema folder was moved without updating "$id" value.

### Edit "$id" in current

Bullet point 3 of tutorial 1 explains what the value should be. The
required value is the title prefixed by a forward slash. A build
is needed to fix this.

</details>

<details>

<summary>Build: "ENOENT: no such file or directory, open 'sroot/zdemo/practice/quickeg/0.0.1"</summary>

### A $ref points at a release that does not exist on disk

This can occur for different reasons. You made a typo or
created a schema using a $ref before a build has occured
on the schema referenced. For example, doing step 6 of
tutorial 2 before doing tutorial 1. 

The more important cause is the scheme release on disk was
deleted BEFORE all schema using it had a new release. This
should never occur for schema having a "completed" status. A
schema folder moving location in schema root can cause
this issue.

### Recreate or change release used

Fix typo or use the value in $ref to search for that value
in an $id. Requires a build before check will pass.

The original release must be recreated OR the $ref must change
to a release that exists on disk. A GH issue should be raised if
it occurs on a "completed" schema. It indicates documentation
or processes need reviewing and updating.

</details>

## Additional issues

<details>
<summary>SRC: Requiredness of properties cannot be modified at: .required</summary>

### Property changed from optional to required in current release

All releases must use semantic versions and all minor or point
releases must be compatible with each other. The issue will
be in red and folder with the current file will be above. **In
summary, get a schema correct whilst in draft status.**

### Do a major release

A schema with draft status can just be overwritten so
the $id does not need changing. The same applies to
completed schema if all parties agree it will not break
any system and that reuse is discouraged.

If there is doubt and agreement can't be reached the
fix has two steps for completed schema.

Step 1 is to edit the major
number in $id, add to all example(s), release again, deleting
files from point release. For example: say release 1.0.2 added
an optional value; an attempt
was made on 1.0.3 making it required; Issue occurs; the $id in
current should end in 2.0.0 and get a release; the files for
release 1.0.3 will still exist on disk and SRC will fail
until they are deleted.

#### Step 2: major release N schema having $ref to this schema

Repeat step 1 in every schema using this completed schema
as a $ref. This includes adding the required values
to every current file. You must do this unless the
editors of those schema agree to complete it. The
tools are designed to support multiple releases
with different rates of change.


</details>



<details>
<summary>SRC: "example 0 did not validate against schema: data should NOT have additional properties"</summary>

### Example of data in released schema is invalid for release

A current schema can define "example" data which must be valid
for the release its within. All examples in all releases must
be valid to pass. The number highlights which example needs fixing.

If example data does not exist a latest build will
automatically add example 0 containing required
properties. Adding examples manually is suggested so
applications using a schema get more test cases.

This issue should never occur on a completed schema because
changed properties should have been a new release. All old
releases should continue to work with old examples.

### Edit current or released files 

Confirm the current file and the latest release contains
valid examples. If you changed property names or made a
property required make sure all examples in current were
altered to reflect the change.

</details>

<details>
<summary>SRC: "unexpected end of the stream within a flow collection"</summary>

### Release edited manually and left invalid

The reason above will be in green and occurs when you edit
a released schema referenced by another schema and leave
that edited file as invalid JSON. The other schema will
build okay because it ignores the $ref when writing files. It
occurs most likely after editing a current file and accidently
changing the referenced version (ie. 1.0.0.json) that was
opened to review its properties.

### Fix the JSON file being referenced

The "mark.name" value says what file to edit. If any schema
was built whilst the file referenced was invalid a rebuild
is required.

</details>

