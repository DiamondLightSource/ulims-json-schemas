# Common issues during build and check tasks

This page highlights some common issues and fixes.

> [!TIP]
> Doing the check is recommended before and after making any
> change to a schema when having issues.

## General approach

When fixing errors in general you will need to:

1. Edit current.json file to fix problem as highlighted below.

2. Target the build: `npm run build-new path-to-current-dot-json`
   for single file or  `npm run build-main-diff` to build
   current.json files different than origin/main branch.
   The `npm run build-all` command can make it more difficult
   to track down some issues and fix them.

3. Do check via: `npm run check` 

Issues prefixed with "check" occur during step 3 and others
during step 2.

> [!TIP]
> Create schema that do not use $ref keyword first. When 2 and 3
> complete create a new schema where the $ref is the $id you
> just checked is okay and build will merge everything
> into a single file.

## Values for "title" or "$id" are wrong

These issues are mostly likely to occur when creating a
new schema folder (containing a current.json) OR an
existing schema folder was moved without updating
required values.

<details>

<summary>check: "schema title must match relative schema directory"</summary>

### Edit "title" in current.json

**Fix:** Depends on path to schema folder. See
file `schemas/examples/basic/current.json` for context and it
has: "title" = "examples/basic"

**Tools output:** The value in green is wrong, value in red
correct value. 

**Background:** The "title" acts like an internal references
that will never change. It enables the tools to ignore
release numbers so it can support multiple versions at
the same time without having to parse other variables
found after guessing what json file to look at.

</details>

<details>

<summary>check: "could not find latest schema version file"</summary>

### Edit "$id" in current.json

**Fix:** Depends on path to schema folder. See
file `schemas/examples/basic/current.json` for context and it
has: "$id" = "/examples/basic/1.0.0"

**Tools output:** The required value is the title prefixed by a
forward slash. (Version can be any semantic number.)

**Background:** The "$id" enables tools to increase the
robustness of schema change over time. It means all
previous releases can exist at the same time with
validation of every release.

</details>

## Values in $ref are wrong or schema missing from disk

<details>

<summary>build: "ENOENT: no such file or directory, open 'schemas/examples/basic/1.0.2"</summary>

### A $ref points at a release that does not exist on disk

This can occur for different reasons. It is most often
due to a typo but sometimes it will be because the schema
being referenced has not been built at least once. It could
also be because a schema moved location in the root without
all references in all versions being changed to correct values.

**Fix:** Confirm the path in $ref is correct and starts
with a '/'. If it is find the schema folder
for $ref schema, check current.json exists
and version in $id, then check if a file
for that version exists on disk (like 1.2.3.json). If not
build it, then build faulty schema again. Running `build-all`
twice will sometimes fix the issue.

**Tools output:** The error above.

**Background:** The location of a schema on disk is
important and so are each version. A schema folder
moving in the schema root requires every $ref in
every version to be updated to the new
path. Build order is important for schema.

</details>

## Schema changed and $id number was not updated correctly

All changes to a schema should start with the $id
being edited in current.json to make at least
a point release. It helps ensure all schema files do
not change in uncontrolled ways which applications
cannot be expected to detect or support. Changing
the $id is not enforced, except in certain
cases like these. If you see any of the following it means
semantic version number in $id was wrong in some way.

<details>
<summary>check: "Requiredness of properties cannot be modified at: .required"</summary>

### Major release is needed

This occurs whenever a property become required and there has
been least one previous release. The property may have
been optional in an earlier release. 

The fix below uses a pretend schema that had
release 1.1.6 merged to main. Months later an attempt
to make a property required caused this issue.

1. Edit the $id value so the major version is increased
   by one. Reset minor and point numbers to 0. So, an $id
   ending with 1.1.7 would become 2.0.0 to fix the issue.

2. The next build will create new files and update the
   latest links. Two tips: do cleanup before push to
   github; start a new branch if cleanup 3 is needed and
   follow the recommendation.

#### Cleanup is required before check will pass

The first cleanup assumes a point release in $id was the
first value altered before other changes. Cleanup 2 and 3
are required when that recommendation was not applied.

   * **Cleanup 1 (best case)** - Files built or committed with
that release need deleting from branch. In example, files 1.1.7
and 1.1.7.json were built and need deleting.

   * **Cleanup 2 (okay case)** The files (already merged to
main) **must** be restored to the branch. In example, changes
to files 1.1.6 and 1.1.6.json need undoing.

   * **Cleanup 3 (worse case)** when the $id being fixed has
been used as a $ref and `build-new` command was not used. A
git diff or commit log will show pairs of files that
need restoring from main. Since
each schema is seperate they will have different
release numbers. Often quicker to start new branch.

#### Informing schema writers about this major release

If the $id being fixed has been used as a $ref you should raise
a Github issue labelled "major" that is mentioned on a PR. To
find these do a search for the $id without semantic version and
look for $ref lines. Add the $id of any current.json file found
to the issue. Writers of those schema can decided when to do
major release after your major release is merged to main.

</details>


## Issues with examples

The build will add an example block
to every file released which uses the example block from
current.json or generates that block containing
required properties. Can also occur when editing
released json files manually.

Example number and message can vary. Example 0 should
always be the required properties. Example 1 is recommended
to contain properties most commonly used by applications.

<details>
<summary>check: "example 0 did not validate against schema: data should NOT have additional properties"</summary>

### Check typo or remove property from example

**Fix:** Edit current.json and confirm the property in the example
is defined by the schema. If not, remove from example or correct
spelling mistake. Rebuild and check will pass again.

</details>


## Other issues

<details>
<summary>check: "unexpected end of the stream within a flow collection"</summary>

### Restore the json file being referenced

The probable cause is a current.json file has a $ref and the
current.json or released files for that $ref has
been left as invalid JSON. For example, it was edited my
mistake whilst reviewing the properties being reused.

**Fix:** Find the $id being referenced and restore the required
file to its original state.

</details>