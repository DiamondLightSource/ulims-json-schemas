#!/usr/bin/env bash
#
# This will overwrite the last run of this command
# if a schema $id has not changed since last run.
#
# The lowest child needs building first. If schema
# starts standalone it can be anywhere in build.
#
# The following enables schema tools vanilla usage
# and output to be confirmed first.
npm run build-new schemas/examples/reposhow/empty/current.yaml

# The following two are how this repository is using the
# tools. The output of the first is near identical to the
# previous. The second uses are reference to the first.
npm run build-new schemas/examples/emptyj/current.json
npm run build-new schemas/examples/emptyjref/current.json

# Do basics before advanced schema
npm run build-new schemas/examples/reposhow/basic/fast/current.json
npm run build-new schemas/examples/reposhow/basic/slow/current.json
npm run build-new schemas/examples/reposhow/advfast/current.json
npm run build-new schemas/examples/reposhow/advslow/current.json

# Depends on advslow, so must be last.
npm run build-new schemas/examples/reposhow/advtop/current.json
