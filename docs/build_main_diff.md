# Using Github action to build and commit schema changes

The five steps on the introduction to
[schema writers](readme.md) page are recommended
for new schema. Existing schema can
updated via a Github (GH) action which will
make commits to your branch, for pulling.

1. Make sure you have the latest origin main and have created
   a new branch via `git checkout -b your-schema-branch`. One
   schema change per branch is recommended.

2. Find the folder with the schema to be edited.

3. Edit current.json with alterations required. Changing
   the number in **$id first** is recommended to avoid overwriting
   existing releases. This is **very important** for schema
   at 1.0.0 or newer being used by production systems. If
   you forget to change the $id now, a cleanup will
   be required in many cases after step 6. Draft schema
   can overwrite themselves.

> [!TIP]
> Running `npm run build-main-diff` and `npm run check`
> locally before step 4 can save time. The action can
> be expected to complete because you've already solved
> every issue. Leaving the action to commit most files.

4. Commit current.json and in commit message mention:
   the schema name, version change made to $id and
   optionally what changed. The basic and advanced
   examples have a changelog.md which is recommended
   for most schema. Example commit message: "Bump <schemaD> to 1.0.1
   using newer <ref-schemaE> 2.0.6"

You should avoid running the build and check commands locally
until step 6 is completes. If run (whilst waiting for the action
to finish) delete the files created before attempting the pull.

5. Execute `git push origin your-schema-branch` and
   visit https://github.com/DiamondLightSource/ulims-json-schemas
   to start a pull request on your branch. (Your push should
   have appeared with a button to start a pull-request. If not,
   contact the repository support team.)
   
6. The action "Build current.json different..." will run and
   appear on the GH `Actions` tab. A green tick will appear if
   everything builds and the check passes. Technically, this
   action is doing `npm run build-main-diff` then commiting
   new files to your branch.

> [!TIP]
> The commit message "Schema(s) build and commit via GH action."
> will appear if the alterations made in step 3 caused new files or
> the "latest" softlinks to change.

The following is how to solve issues when a red cross appears
on the GH action. Also, it proves the GH action and local
actions produce identical results.

6. On workstation `git pull origin your-schema-branch` to get
   the built files. This will usually pull four files which are
   those that would have been created by running a build
   command locally. If four files are not pulled the edited
   current.json file probably has issues that need fixing.

Using `npm run build-main-diff` the `npm run check` locally is
recommended when trying to solve any issues. It removes most
delays caused by steps 3-5 so build/check iterations can be
quicker. Once everything passes, repeat from step 3 and the
action will commit the other files.

> [!TIP]
> A green tick on action, then a pull and new local build should
> cause no schema related files to appear in a `git status` or
> `git diff` output.
