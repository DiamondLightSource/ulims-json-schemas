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

# Updating schema-tools

There are two stages. Update tools and update our patches where
needed.

## Tools
The tools have not been updated in NPM but a packaged version is
available. The tarball method can be used to update package. The
versions available are here: https://gitlab.wikimedia.org/repos/data-engineering/jsonschema-tools/-/packages/

The following two lines should be changed whenever
tools is updated change. The url in the install will
update the value in package.json.

Current tools version: 1.9.0
Details: https://gitlab.wikimedia.org/repos/data-engineering/jsonschema-tools/-/packages/1606

* `npm install <url to .tgz found on details page>`

## Patches

Files in `patches` are tied to particular versions. At the minimum
a new file tied to version installed is needed.

* Install it
* `npm run check` and probably see errors (ie. "The expression
evaluated to a falsy value") until patching is done.
* Make all changes in `node_modules/@wikimedia/jsonschema-tools`.
* `npx patch-package @wikimedia/jsonschema-tools` to generate
  file in patches folder. For example, package with 1606 in details
  url resulted in: `patches/@wikimedia+jsonschema-tools+1.9.0.patch`

If a change is missing, repeat the install so starts with
unpatched version and patch-package should detect change which
overwrites existing patch file for version being patched.
