# Developers

A page for developers.

## Editing datafile in VScode against schema

It is possible to create, edit or debug data files with
schema validation whilst typing. If starting with an empty
file all required values will be created on first code
completion. Properties, enums etc. will populate
when needed.

The repo has `.vscode/settings.json` enabled for two
examples schema. Remote or local schema can be
used. See https://code.visualstudio.com/docs/languages/json

It is not possible to target by filename or extension
so folders are used. The `/data/examples` has folders for
two examples. Any json file within will validate on
opening. The files 1one.json were created on
first code completion.
