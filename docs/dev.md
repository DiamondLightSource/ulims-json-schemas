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
