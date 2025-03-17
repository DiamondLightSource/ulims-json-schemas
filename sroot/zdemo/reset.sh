#!/usr/bin/env bash

# Schema writers can try building multiple versions
# but need to reset back so checkout of current files
# will cause build to generate 0.0.1 again.
rm sroot/zdemo/pattern1/child/*/0.0*
rm sroot/zdemo/pattern1/top/0.0*
./