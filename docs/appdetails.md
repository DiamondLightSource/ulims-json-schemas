# Application details

The schema in this repository can be used by any application
and this page explains the meaning of "latest" release
and what "status" means.

## Soft link to latest release

A schema build will always create a "latest" file. Appications
with a cached copy of the schemas folder can use the
[latest.json](schemas/examples/reposhow/advslow/latest.json?raw=1)
soft link. If certain values are changed by writers, all
previous releases will continue to work.

Draft schema are subject to change (without new release numbers)
and applications will break if not designed for that.

## Status of schema

A schema has a status which is (encoded) as a comment in
the schema. Two exist and schema missing the encoding
should be considered draft:

### Draft schema ("status-draft")

All schema start with this status. Release 1.0.0 of a schema is
expected to be draft for an agreed time. It can
be reused by other schema or applications if the risks
have been considered. Schema will change without notice.

### Completed schema ("status-completed")

A completed status means a schema is ready for reuse by an
advanced schema or by applications. Schema will change
with notice. It requires all contributors to that
schema to agree three things:

  * no future changes are expected for repository lifetime
  * any change requires a new release with a different number
  * advanced schema using the old release will get new
    releases with that change applied.

High major or point numbers can signal the draft status
was changed too quickly.
