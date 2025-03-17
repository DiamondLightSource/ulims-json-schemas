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

## Changes

* **0.0.1** - First point release of pattern 9 schemas where all
schemas have same version (March 2025)
