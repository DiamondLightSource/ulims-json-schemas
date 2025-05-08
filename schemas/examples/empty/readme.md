# Empty schema - current.yaml as main source

The **emptyj (json first)** is the preferred schema for
copying when creating a new schema. This schema is
for reference only and is used for lower level confirmation
of the schema tools build. It uses yaml first method
and works the same after build.

## Changes

* **0.0.1** - First draft of empty schema (April 2025)

# Differences to JSON first schema

This schema is almost identical to a JSON first schema. The
differences are:

* **current.yaml** - the most important file used to build
  the latest version of a schema.

* **current.json** - soft link to latest.json which is a
  requirement for the schema root check to pass. If missing, 
  copy the fixed .json last built from current.yaml

# Comparing empty and emptyj built JSON files

The examples empty and emptyj are expected to generate
nearly identical JSON files at build time. There should
be 8 differences via this command caused by having a
different schema name and location in root.

`diff schemas/zdemo/empty/0.0.1.json schemas/zdemo/emptyj/0.0.1.json`

There is another diff first seen in May 2025 which highlighted
the $comment keyword in this yaml first schema gets stripped
at build time whilst that keyword is retained in json first
schema. Regarding that keyword the JSON spec
says "... implementations.... may even strip them at any time"
at build time.

https://json-schema.org/understanding-json-schema/reference/comments
