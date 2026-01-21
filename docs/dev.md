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
for new version should be created:

* `npm install <url to .tgz found on details page above>`
* `npm run check` and probably see errors (ie. "The expression
evaluated to a falsy value") until patching is done.
* Make all changes in `node_modules/@wikimedia/jsonschema-tools`.
* `npx patch-package @wikimedia/jsonschema-tools` to generate
  file in patches folder. For example, package with 1606 in details
  url resulted in: `patches/@wikimedia+jsonschema-tools+1.9.0.patch`

### Change missing?

Look at patch for the old version to see probable changes
in new version. New version will have different patch
references. If a change missing between the two files:

1. Disable patch for old version, such as changing file extension.
2. Repeat the install so version in `node_modules` is an
   unpatched version. 
3. Make changes.
4. Patch-package should detect and will overwrite
   existing patch file for version being patched.
