# Tutorial 4: repeating tutorial 3, but with merge to main

All schema in main branch **must never break** for lifetime
of the repository. There is one exception which allows
tutorial 3 to be done with changes merged. 

Anyone writing schema can do this tutorial. Day 1 and 2
are expected to have been done by anyone looking
at PR for schema and doing merge the main. Day 5
shows edits from days 1 - 4 can be combined so
four schema changes are merged at same time.


## Five schema and what to edit when in tutorial 4

The schema group [reposhow](../schemas/examples/reposhow/readme.md)
contains five schema. Suggested order of editing is
as follows and imagine a day equals 6+ months. Doing day
1 and 2 is suggested for most repository contributors. If
a PR for an earlier day exist it should be merged
to main first and the next day uses a branch
from main. Flag outstanding PR to repo team.

* day 1: change basic [fast schema](../schemas/examples/reposhow/basic/fast/current.json?raw=1)
release number and add a new property. If a required property
you must increase the major number before the next check.

* day 2: change [advfast schema](../schemas/examples/reposhow/advfast/current.json?raw=1)
release number and alter $ref to the release of fast schema
wanted. This might be what you did on day 1 unless multiple
people are doing the tutorial.

Day 3 and 4 is effecively tutorial 3 again because
the changes on day 1 and 2 have been used for N months. 

* day 3: change [advslow schema](../schemas/examples/reposhow/advslow/current.json?raw=1)
release number and alter $ref to wherever advfast used. Imagine
this schema is used by a production system that needs a schema
to change more slowly.

* day 4: change [advtop schema](../schemas/examples/reposhow/advtop/current.json?raw=1)
release number and alter $ref to wherever advslow has reached. This
might be what you did on day 3 unless multiple people are doing
the tutorial. Imagine 5+ schema exist that use advslow to define
themselves.

This is combining days 1-4 so a single PR will do all
changes. Imagine a popular basic schema has been used
as a $ref for 5+ years and something needs changing. The
change might break older applications.

* day 5: Four schema need changing. Firstly, change
basic [slow schema](../schemas/examples/reposhow/basic/slow/current.json?raw=1)
release number and add a new property like day 1. Avoid making
your new property required the first time you do this. Secondly,
alter the $ref in advfast and advslow to change just made. Thirdly,
repeat day 4. The PR should contain new releases for four
schema changed and old releases remain unchanged. Later, old
releases get deleted as per (to be agreed) processes.

