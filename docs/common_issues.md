# Common issues during build and check tasks

This page highlights some common issues and fixes.

> [!TIP]
> Doing the check is recommended before and after making any
> change to a schema when having issues.

## Common solution

The common solution is:

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

### Using values in $id that never change (ie. draft schema)

The value in $id is important and **must be** correct. A "draft"
schema can retain the same value (where $id ending
with "/0.0.1" is recommended at start) and builds overwrites.
An $id ending in 1.0.0 or higher
is considered "completed" where the $id should be alter
with certain patterns to increase robustness of schema
change over time so all old, current and future
versions are available at the same time.

## Values for "title" or "$id" are wrong

These issues are mostly likely to occur when creating a
new schema folder (containing a current.json) OR an
existing schema folder was moved without updating
required values.

<details>

<summary>check: "schema title must match relative schema directory"</summary>

### Edit "title" in current

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

### Edit "$id" in current

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

This can occur for different reasons. A typo most often
but sometimes it will be because the schema
being referenced has not been built at least once. Later (N months)
a more important cause is a schema moved location
in the root without all references in all
versions being changed to correct values.

**Fix:** Confirm not a typo. If not: find the schema folder
for $ref schema, check current.json exists
and version in $id, then check does a file
for that version exists on disk, if not
build it; then build faulty schema again. Running `build-all`
twice will sometimes fix the issue.

**Tools output:** The error above.

**Background:** The location of a schema on disk is
important and so are each version. A schema folder
moving in the schema root requires every $ref in
every version to be updated to the new
path. Build order is important for schema.

#### Example fix
Error occurs on `npm run build-new schemas/examples/advanced/current.json`
if the $ref is `schemas/examples/basic/1.0.2` so expecting to
find a 1.0.2.json file. Looking at basic schema folder can see
a build of release 1.0.1 was
done `npm run build-new schemas/examples/basic/current.json`
and that current file shows its $id ending with 1.0.1 and
file 1.0.1.json exists. So, typo on the point number? But, if
basic $id ended with 1.0.2 a build is needed. Build basic first
or run `build-all` twice with issue disappearing on 2nd run.

> [!CAUTION] Alter $id on advanced schema before build
> Say, advanced/1.0.0 is used by M applications who need
> it for N years. The **first edit** before altering
> the $ref value and doing a build (which caused this error),
> should have been to update its $id so advanced/1.0.1 will
> contain changes (ie. use a newer version of basic). If build
> overwrote files for advanced 1.0.0 then undo those changes.

</details>
