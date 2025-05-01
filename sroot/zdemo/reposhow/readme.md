# Repository show folder

The schema in the repository must never break. An exception
are those in this folder. A schema breaking in here indicates
our processes need a review or updating. This schema group
has three purposes:

1. It enables schema writers (or writing applications) to
   do tutorial 3 (schema change over time) and get a
   schema merged to main via the agreed processes
   before touching a schema that must never break.

2. It enables all read applications to use a common set of
   schema to prove they can use main for loading schema
   and can cope with schema change over time.

4. It contains a minimum set of schema the repository
   can be stripped back to show all systems are
   working for the 4 ways schema can be defined.

All manual processes, scripts and automated actions
on main are expected to first applied to schema in
here. Once they have been used for an agreed time
they can be applied to schema that must never break.

## Basic schema available

There are two basic schema that are used by advanced
schema. The purpose of these is to show the main
branch and applications can ignore different
frequencies of schema release. A real schema
should be closer to "slow" whilst "fast" is
an extreme case.

* [readme in slow](basic/slow/readme.md) - a schema
 that has releases closer to recommended frequency.

* [readme in fast](basic/fast/readme.md) - a schema
 that has releases more often than recommended. It
 probably means the "completed" status discussed
 in tutorial 1 was agreed to quickly.

## Advanced schema available

There are three advanced schema. The purpose of the
first two is to show the main branch can be used
by any instance type (test, staging or production) and
helps show schema and applications can evolve at
different speeds.

* [readme in advslow](advslow/readme.md) - a schema
 that tries to change at a slower rate suitable for
 production instances. It uses older releases of
 the two basic schema to define itself.

* [readme in advfast](advfast/readme.md) - a schema
 that tries to keep up with releases to both basic
 schema. It acts like a "next" schema to the advslow
 schema enabling more rapid changes.

The purpose of the third advanced schema is to show
another level of reuse is possible to reduce
duplication further. 

* [readme in advtop](advtop/readme.md) - a schema that
 is mostly defined by another advanced schema. It adds
 a second level of $ref and shows an advanced
 schema (advslow) using a basic schema (slow) can
 be defined once and get reused by N schema.

## Changes

The five schema in this folder are expected to evolve at
a quicker pace than normal, so change history differs.

* The history below should be updated at least once per year.

* The release number each reach depends on how many writers
  complete tutorial 3 and what they changed. Schema should
  take years to change this much.

    * For new writers suggested order is change basic
      fast on day 1 then change advfast on day 2 to use
      it. Tutorial 3 can be repeated: change
      advslow on day 1 to match advfast then change
      advtop on day 2 to use new release of advslow.

* Older releases will be deleted manually in first
  instances. An aim of the schema "completed" status
  is to stop this being needed.

* If certain changes are made the compatibility
  enforcement will result in two digit major numbers, a
  manual schema reset can be done.

  * Every schema is seperate and release numbers
  have nothing to do with each other so can
  diverge over time. The schema reset changes all
  releases in this group back to 1.0.0 and old numbers
  cease to exist apart from being documented below. A
  schema (or schema group) should avoid resets, unless
  applications have been shown to support them.

### History of changes

#### April 2024

Start reposhow group with 5 schema that reached completed status.

   * basic/fast 1.0.0
   * basic/slow 1.0.0
   * advslow 1.0.0 (uses both basic schema at release shown)
   * advfast 1.0.0 (uses both basic schema at release shown)
   * advtop 1.0.0 (uses advslow as $ref at release shown)
   