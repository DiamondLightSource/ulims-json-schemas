# Pattern 9

This schema set shows how schemas can change over time
at different paces. It enables all processes using this
schema root to confirm they are working and can
detect changes.

## Frequency of point release

Schemas do point releases which builds a specific version
of that schema. In pattern1 these are fixed at 0.0.1
and should never change.

Pattern 9 in contrast is expected to be an extreme
example of how schemas evolve at different rates
over time.

**Schema writers should aim for frequency between pattern 1 and 9**

## Schemas in pattern 9

There are 2 top and 2 children that at 0.0.1 release
are the same mostly.

* **faster** a child schema that has point releases very often.

* **slower** a child schema that has point releases less often

* **topfast** a top schema that tries to stay stay with faster.

* **topslow** a top schema that tries to stays with slower.

The faster child will update most often but schemas using
it can ignore the latest change. Fast top should get updated
when a schema author decides when there are enough changes to
the children. The slower child and slow top should fall
behind the current version.

## How to change releases

The empty schema readme documents how to alter a particular
schema and build the latest version. This readme assumes those
basics are understood.

1. **npm run check** to confirm all existing files pass
   minimum requirements.

2. Edit current file

   * **$id** change the version on the end of the line

   * Make other changes to schema

3. **npm run build-modified** will (via git diff) detect
   changes, build a JSON file and redirect soft links to it

4. **npm run check** to confirm new schema release passes
   minimum requirements and compatibility checks.

5. Update the readme for each schema changed
   and commit to git.

It is possible to alter multiple schemas before step 3. A
schema that uses a schema can be updated at the same time
if necessary. See topfast 1.0.0 for example.

### Compatibility enforcement

There are some changes to schema files which require
major, minor or point releases to pass checks. This
section documents them.

#### Required values (major release required)

Schema properties are not required by default. Changing a
property to required **MUST** be a major release. Faster
schema demonstrates that in release 1.0.0. This applies
to all schemas using a schema, so topfast release 1.0.0
used newer version faster.

### Bypassing checks (before release 1.0.0)

A simple way to bypass is to delete all generated files on
disk before the schema release being worked on. The build
will update the soft links so test passes again.

Delete is needed for uncommitted point releases when
a schema change should have been a major release. So,
topfast 0.0.3 built fine but test failed due to new
required property. The rebuild as 1.0.0 did not
not remove failed files.

## Changes / Summary of schema state change

* **0.0.1** - First point release of pattern 9 schemas where all
schemas have same version (March 2025)

* **March 19th 2025** Number of releases per schema: faster had 5,
  topfast had 4, slower had 2 and topslow unchanged. Topslow
  release outstanding, if systems using topfast don't
  break. Afterwards, slower 0.0.1 can have schema retirement policy
  applied, since no others in the schema root will be using it, so
  can be removed from git version control.
