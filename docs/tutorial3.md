# Tutorial 3: Changing two "completed" schema N months later

You can avoid the following if you make sure a schema
never requires changing or decide to avoid using $ref
keyword that automates property reuse, which is the most powerful
full feature of the tools. Assuming change is required...

## State of quickeg and quickegref at start of tutorial 3

This tutorial pretends schema quickeg and schema quickegref
were finalised at release 1.0.0 and have a "completed"
status that was merged to main 12 months ago, so files for
1.0.0 exist on disk and earlier 0.0.1 files were deleted.

## Two steps over two days (simulates time passing)

The steps are almost identical to tutorials 1 and 2 but
the **order** they are done are important. Also, remember
each schema is seperate and can have a different
teams reponsible for it.

1. Day 1, Do SRC `npm run check` and fix any issues. Then,

2. Complete tutorial 1. Edit $id in quickeg/current.json with
new number before making changes and keep doing releases until
happy with the change. Remember the $id used. For a real
completed schema this would ideally be committed, pushed and
merged to main before doing day
two. *eg. "$id": "/zdemo/practice/quickeg/1.0.5"*

3. Day 2, Do SRC `npm run check` and fix any issues. (Pretend
   merge occured on day 1.) Then,

4. Complete tutorial 2. Edit $id in quickegref/current.json with
   a new number before making changes. Change the $ref to match
   the $id in step 2. *eg. "$id": "/zdemo/practice/quickegref/1.0.1"
   and "$ref": "/zdemo/practice/quickeg/1.0.5"*

Release numbers have nothing to do with each other. Numbers
are likely to be similar at the start but can diverge over
time if releases of basic schema occur more often. In this
case the advanced schema is pretending to skip over a point
releases (1.0.1 to  1.0.4) done on the basic schema over
the last year. If a $ref is changed to a release that
does not exist on disk the SRC will fail.

5. Repeat step 4 (tutorial 2) on every advanced schema using
   the basic schema. It is possible to edit $id and $ref in
   every schema and after building each do SRC once. Using
   command `npm run build-modified` is suggested to target
   build on any current file changed since last commit.

A schema flagged as "popular" might require step 5 to be done
by the team managing the advanced schema. That team can work
to the own timetables for confirming change does not
break their systems.

### Why changing $id is important

An aim of schema releases is that past, present
and future releases are available at the same time
to allow applications to migrate over time at
different rates for testing and deployment.

If a change was made to quickref and its $id was not
udated **before the build** so causing the latest file
to be overwritten, divergence can occur. It will mean
any built advanced schema using this as a $ref will appear to
be using the same "$id" but the **definition will differ**
until next build. An advanced schema can $ref another
advanced schema and not changing the $id causes
a 2nd level of difference.

Using the `npm run build-all` command might solve this
problem but increases the chance of schema changes
before all applications has tested it.

