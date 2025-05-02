# Fixes for build and schema root check (SRC) issues

This page highlights some fixes for common error. Doing
the SRC is recommended before and after making any
change to a schema. The common solution is:

1. Edit current.json file to fix problem.

2. Target the build: `npm run build-new path-to-current-dot-json`
   or `npm run build-modified` if changes were made to
   commited file. The build-all command can make it more
   difficult to track issues.

3. Run schema root check `npm run check`

## Issues and fixes

<details>

<summary>Message to look during build or check</summary>

### Overview of issue

A longer description of the issue if summary not clear.

### How to fix

What to change.

</details>
