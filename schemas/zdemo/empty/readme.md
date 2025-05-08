# Empty schema - current.yaml as main source

The **emptyj (json first)** is the preferred schema for
copying when creating a new schema. This schema is
for reference only and is used for lower level confirmation
of the schema tools build. It uses yaml first method
and works the same after build.

* **Status:**  draft (completed, retired)

* **Team managing schema:** Team name or email address

* **Contributors:** Person 1, Person 2

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
