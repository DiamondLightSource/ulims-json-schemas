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
# npm run build-new sroot/zdemo/emptyj/current.json

# Build pattern 1 schemas.
#
# Child 3 before child 2. Children before top parent.
npm run build-new sroot/zdemo/pattern1/child/three/current.yaml 
npm run build-new sroot/zdemo/pattern1/child/two/current.yaml 
npm run build-new sroot/zdemo/pattern1/child/one/current.yaml 
npm run build-new sroot/zdemo/pattern1/top/current.yaml 
