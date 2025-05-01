#!/usr/bin/env bash
#
# This will overwrite the last run of this command
# if a schema version has not changed since last run.
#
# The lowest child needs building first. If schema
# starts standalone it can be anywhere in build.
#
# Templates for new schemas. Two types exist but
# only one is available currently.
#
npm run build-new sroot/zdemo/empty/current.yaml
npm run build-new sroot/zdemo/emptyj/current.json
npm run build-new sroot/zdemo/emptyjref/current.json

# Build self-check schema
#
# Do basics before advanced schema
npm run build-new sroot/zdemo/reposhow/basic/fast/current.json
npm run build-new sroot/zdemo/reposhow/basic/slow/current.json
npm run build-new sroot/zdemo/reposhow/advfast/current.json
npm run build-new sroot/zdemo/reposhow/advslow/current.json
npm run build-new sroot/zdemo/reposhow/advtop/current.json
