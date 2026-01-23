# Developers

A page for developers.

## Editing datafile in VScode against schema

It is possible to create, edit or debug data files with
schema validation whilst typing. If starting with an empty
file all required values will be created on first code
completion. Properties, enums etc. will populate
when needed.

The repo has `.vscode/settings.json` enabled for two
examples schema. Local or remote schema can be
used. See https://code.visualstudio.com/docs/languages/json. For
example, this repo uses local relative but other repos can use
[remote URL](https://raw.githubusercontent.com/DiamondLightSource/ulims-json-schemas/refs/heads/main/schemas/examples/basic/1.0.1.json)
for the schema they want to use.

It is not possible to target by filename or extension
so folders are used. The `/data_examples` has folders for
two examples. Any json file within will validate on
opening. The files example_1.json were created on
first code completion.

# Updating jsonschema-tools

There are two stages: updating the `@wikimedia/jsonschema-tools` dependency, and updating our patches where needed.

## Tools
The latest version of `@wikimedia/jsonschema-tools` are published here: https://gitlab.wikimedia.org/repos/data-engineering/jsonschema-tools/-/packages/

The version and details link below should be changed whenever
tools is updated change. The url in the install will
update the value in package.json

Current tools version: 1.9.0
Details: https://gitlab.wikimedia.org/repos/data-engineering/jsonschema-tools/-/packages/1606

## Patches

Files in `patches` are tied to particular versions and file
for new version should be created with old one removed. 

1. Use `npm run check` to confirm everything is working with
   current version and all schema are good.
2. `npm install <url to .tgz found on details page above>` which
   installs that version and `packages.json` changed. It applied
   all patches found for package, which changed files
   in `node_modules/@wikimedia/jsonschema-tools`.
3. Patching can be redone/confirmed via `npx patch-package` and
   it will show warnings patch for old was applied to new.
4. `npx patch-package @wikimedia/jsonschema-tools` to generate
   file in patches folder. For example, package with 1606 in details
   url resulted in: `patches/@wikimedia+jsonschema-tools+1.9.0.patch`
5. Repeat step 1. The error "The expression evaluated to
   a falsy value" indicates patch did not work.
6. The two files in `patches` should be close to identical. Diff
   them to confirm.
7. Commit the new patch and remove the old one. The warning
   during step 2 and 3 should have gone.
   
### Patching issues

Disable patches, such as changing file extension. Repeat
step 2 so have unpatched new version. Look at patches and
manually change files indicated. Repeat step 4 to create
new patch file. Repeat step 3 and confirm new patch
applied. Continue from step 5.
