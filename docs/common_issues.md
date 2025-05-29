# Common issues during build and check tasks

This page highlights some common issues and fixes.

> [!TIP]
> Doing the check is recommended before and after making any
> change to a schema when having issues.

## General approach

When fixing errors in general you will need to:

1. Edit current.json file to fix problem as highlighted below.

2. Target the build: `npm run build-new path-to-current-dot-json`
   or `npm run build-modified` if changes were made to a
   committed files. The `npm run build-all` command can
   make it more difficult to track down some issues
   and fix them.

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
