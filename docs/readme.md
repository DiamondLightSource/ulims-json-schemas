# Introduction for schema writers

The ulims-json-schemas repository provides a version controlled
location to store schema required by different applications. It
enables schema to reuse schema to avoid duplication.

This document starts with introduction for people new
to JSON schema. It explains adding a schema to the repository 
via automatic and advanced methods. If you have not contributed
previously the setup at the end of this page maybe required.

## New to JSON schema

The json schema website provides a
[getting started](https://json-schema.org/learn) section
and you should have read at least creating your
[first schema](https://json-schema.org/learn/getting-started-step-by-step).

A basic schema defines everything in a single file. An advanced
schema can use
[external references](https://json-schema.org/learn/getting-started-step-by-step#add-an-external-reference)
via the `$ref` keyword. Using a `$ref` enables a schema to reuse
another basic or advanced schema to avoid duplication. 

This repository supports both basic and advanced schema. A
required check must pass for all schema. This is explained
below and in the first tutorial.

## Writing a schema for your beamline

It is often easier to write a schema if you can see what the UI would 
look like as you write it. You can do this using a tool like 
[this](rjsf-team.github.io/react-jsonschema-form). It is recommended 
that Beamline staff first try and write their own schema by doing the
following:
1. Take an existing schema from https://github.com/DiamondLightSource/ulims-json-schemas/tree/main/schemas
2. Paste it into the `JSONSchema` box on rjsf-team.github.io/react-jsonschema-form e.g. see [here](https://rjsf-team.github.io/react-jsonschema-form/#eyJmb3JtRGF0YSI6eyJjb21wb3NpdGlvbiI6IkMiLCJkZW5zaXR5IjoxLCJwYWNraW5nX2ZyYWN0aW9uIjowLjUsImNvbW1lbnQiOiIifSwic2NoZW1hIjp7InRpdGxlIjoic2FtcGxlcy9pMTUtMS9wb3dkZXIiLCIkaWQiOiIvc2FtcGxlcy9pMTUtMS9wb3dkZXIvMC4wLjEiLCIkc2NoZW1hIjoiaHR0cDovL2pzb24tc2NoZW1hLm9yZy9kcmFmdC0wNy9zY2hlbWEjIiwidHlwZSI6Im9iamVjdCIsInJlcXVpcmVkIjpbImNvbXBvc2l0aW9uIiwiZGVuc2l0eSIsInBhY2tpbmdfZnJhY3Rpb24iXSwicHJvcGVydGllcyI6eyJjb21wb3NpdGlvbiI6eyJ0aXRsZSI6IkNvbXBvc2l0aW9uIiwiZGVzY3JpcHRpb24iOiJNb2xhciBjb21wb3NpdGlvbiBvZiBzYW1wbGUiLCJ0eXBlIjoic3RyaW5nIiwiZGVmYXVsdCI6IkMifSwiZGVuc2l0eSI6eyJ0aXRsZSI6IkRlbnNpdHkiLCJkZXNjcmlwdGlvbiI6IkRlbnNpdHkgb2Ygc2FtcGxlIGluIGcvY21eMyIsInR5cGUiOiJudW1iZXIiLCJkZWZhdWx0IjoxLCJtaW5pbXVtIjowLCJtYXhpbXVtIjoxMDAwfSwicGFja2luZ19mcmFjdGlvbiI6eyJ0aXRsZSI6IlBhY2tpbmcgRnJhY3Rpb24iLCJkZXNjcmlwdGlvbiI6IlBhY2tpbmcgZnJhY3Rpb24gb2YgdGhlIHNhbXBsZSBpbiB0aGUgY2FwaWxsYXJ5IiwidHlwZSI6Im51bWJlciIsImRlZmF1bHQiOjAuNSwibWluaW11bSI6MCwibWF4aW11bSI6MX0sImNhcGlsbGFyeSI6eyJ0aXRsZSI6IkNhcGlsbGFyeSIsImRlc2NyaXB0aW9uIjoiVGhlIGNhcGlsbGFyeSB0eXBlIG9mIHRoaXMgc2FtcGxlLiIsInR5cGUiOiJzdHJpbmciLCJlbnVtIjpbImJzMS4wIiwiYnMxLjUiLCJiczIuMCIsImZxMC40IiwiZnExLjAiLCJmcTEuNSIsImZxMi4wIiwiZnEyLjUiLCJmcTMuMTciLCJwaTEuMCIsInBpMS41IiwicGkyLjAiXX0sImNvbW1lbnQiOnsidGl0bGUiOiJDb21tZW50IiwiZGVzY3JpcHRpb24iOiJDb21tZW50IG9uIHRoaXMgc2FtcGxlIiwidHlwZSI6InN0cmluZyIsImRlZmF1bHQiOiIifX0sImV4YW1wbGVzIjpbeyJjb21wb3NpdGlvbiI6IkMiLCJkZW5zaXR5IjoxLCJwYWNraW5nX2ZyYWN0aW9uIjowLjUsImNvbW1lbnQiOiIiLCJjYXBpbGxhcnkiOiJiczEuNSJ9XX0sInVpU2NoZW1hIjp7fSwidGhlbWUiOiJkZWZhdWx0IiwibGl2ZVNldHRpbmdzIjp7InNob3dFcnJvckxpc3QiOiJ0b3AiLCJ2YWxpZGF0ZSI6ZmFsc2UsImRpc2FibGVkIjpmYWxzZSwibm9IdG1sNVZhbGlkYXRlIjpmYWxzZSwicmVhZG9ubHkiOmZhbHNlLCJvbWl0RXh0cmFEYXRhIjpmYWxzZSwibGl2ZU9taXQiOmZhbHNlLCJleHBlcmltZW50YWxfY29tcG9uZW50VXBkYXRlU3RyYXRlZ3kiOiJjdXN0b21EZWVwIiwiZXhwZXJpbWVudGFsX2RlZmF1bHRGb3JtU3RhdGVCZWhhdmlvciI6eyJhcnJheU1pbkl0ZW1zIjoicG9wdWxhdGUiLCJhbGxPZiI6InNraXBEZWZhdWx0cyIsImNvbnN0QXNEZWZhdWx0cyI6ImFsd2F5cyIsImVtcHR5T2JqZWN0RmllbGRzIjoicG9wdWxhdGVBbGxEZWZhdWx0cyIsIm1lcmdlRGVmYXVsdHNJbnRvRm9ybURhdGEiOiJ1c2VGb3JtRGF0YUlmUHJlc2VudCIsIm5lc3RlZERlZmF1bHRzUHJlY2VkZW5jZSI6ImRlc2NlbmRhbnRXaW5zIiwicmVxdWlyZWRCb29sZWFuRGVmYXVsdCI6InBvcHVsYXRlRmFsc2UifSwidXNlRmFsbGJhY2tGaWVsZCI6ZmFsc2UsInVzZUZhbGxiYWNrVWlGb3JVbnN1cHBvcnRlZFR5cGUiOmZhbHNlLCJsaXZlVmFsaWRhdGUiOmZhbHNlLCJpZFByZWZpeCI6InJvb3QiLCJpZFNlcGFyYXRvciI6Il8ifSwidmFsaWRhdG9yIjoiQUpWOCIsInNhbXBsZU5hbWUiOiJCbGFuayJ9)
3. Modify the schema to make it fit your beamline
4. Click `Share Playground` to get a link to your schema
5. Open a [new issue](https://github.com/DiamondLightSource/ulims-json-schemas/issues/new) and paste this into it
6. Repeat for an experiment definition, e.g. starting from [here](https://rjsf-team.github.io/react-jsonschema-form/#eyJmb3JtRGF0YSI6eyJiZWFtX2VuZXJneSI6NzYuNywiZm9jdXNlZF9iZWFtX3NpemUiOjIwMCwidGltZV9wZXJfcGRmIjo2MDAsInFfbWF4IjoyNSwiZnJhbWVzIjoxLCJjb21tZW50IjoiIiwiY29tcG9zaXRpb24iOiJDIiwiZGVuc2l0eSI6MSwicGFja2luZ19mcmFjdGlvbiI6MC41fSwic2NoZW1hIjp7InRpdGxlIjoiZXhwZXJpbWVudF9kZWZpbml0aW9uL2kxNS0xL3Jvb21fdGVtcGVyYXR1cmUiLCJkZXNjcmlwdGlvbiI6IkEgcm9vbSB0ZW1wZXJhdHVyZSBkYXRhIGNvbGxlY3Rpb24gb24gSTE1LTEuIENhbiBiZSBvbmUgUERGIG9yIG11bHRpcGxlIFBERnMgYXMgYSBmdW5jdGlvbiBvZiB0aW1lLiIsIiRpZCI6Ii9leHBlcmltZW50X2RlZmluaXRpb24vaTE1LTEvcm9vbV90ZW1wZXJhdHVyZS8xLjAuMCIsIiRzY2hlbWEiOiJodHRwOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LTA3L3NjaGVtYSMiLCJ0eXBlIjoib2JqZWN0IiwicmVxdWlyZWQiOlsiYmVhbV9lbmVyZ3kiLCJmb2N1c2VkX2JlYW1fc2l6ZSIsImZyYW1lcyIsInFfbWF4IiwidGltZV9wZXJfcGRmIl0sInByb3BlcnRpZXMiOnsiYmVhbV9lbmVyZ3kiOnsidGl0bGUiOiJCZWFtIEVuZXJneSAoa2VWKSIsImRlc2NyaXB0aW9uIjoiQmVhbSBFbmVyZ3kgaW4ga2VWIiwidHlwZSI6Im51bWJlciIsImVudW0iOls0MCw2NS42LDc2LjddLCJkZWZhdWx0Ijo3Ni43fSwiZm9jdXNlZF9iZWFtX3NpemUiOnsidGl0bGUiOiJGb2N1c2VkIEJlYW0gU2l6ZSAowrVtKSIsImRlc2NyaXB0aW9uIjoiVGhlIHZlcnRpY2FsIGV4dGVudCBvZiB0aGUgcHJpbWFyeSBiZWFtIGF0IHRoZSBzYW1wbGUgcG9zaXRpb24uIDIwMCDCtW0gYXQgdGhlIHNhbXBsZSBwb3NpdGlvbiBtZWFucyB3ZSBmb2N1cyBvbiB0aGUgZGV0ZWN0b3IgZm9yIG1heGltdW0gcmVjaXByb2NhbCBzcGFjZSByZXNvbHV0aW9uLiIsInR5cGUiOiJudW1iZXIiLCJlbnVtIjpbMTAsMjAwXSwiZGVmYXVsdCI6MjAwfSwidGltZV9wZXJfcGRmIjp7InRpdGxlIjoiVGltZSBwZXIgUERGIChzZWNvbmRzKSIsImRlc2NyaXB0aW9uIjoiVG90YWwgZXhwb3N1cmUgdGltZSBmb3IgZWFjaCBkaWZmcmFjdGlvbiBwYXR0ZXJuL1BERiBpbiBzZWNvbmRzLiIsInR5cGUiOiJudW1iZXIiLCJkZWZhdWx0Ijo2MDAsIm1pbmltdW0iOjAsIm1heGltdW0iOjk5OTk5Ljl9LCJxX21heCI6eyJ0aXRsZSI6IlEtbWF4ICjDheKBu8K5KSIsImRlc2NyaXB0aW9uIjoiVGhlIHJlcXVpcmVkIG1heGltdW0gbW9tZW50dW0gdHJhbnNmZXIgZm9yIHRoaXMgY29sbGVjdGlvbiwgaW4gcmVjaXByb2NhbCBBbmdzdHJvbXMuIiwidHlwZSI6Im51bWJlciIsImRlZmF1bHQiOjI1LCJtaW5pbXVtIjowLCJtYXhpbXVtIjoxMDB9LCJmcmFtZXMiOnsidGl0bGUiOiJGcmFtZXMiLCJkZXNjcmlwdGlvbiI6IlRoZSBudW1iZXIgb2YgUERGcyBbYXQgZWFjaCB0ZW1wZXJhdHVyZV0uIFRoZSB0b3RhbCB0aW1lIGZvciB0aGlzIGV4cGVyaW1lbnQgd2lsbCBiZSAodGltZSBwZXIgUERGKSDDlyAoZnJhbWVzKSDDlyAobnVtYmVyIG9mIHRlbXBlcmF0dXJlcykuIiwidHlwZSI6ImludGVnZXIiLCJkZWZhdWx0IjoxLCJtaW5pbXVtIjoxLCJtYXhpbXVtIjoxMDAwMH0sImNvbW1lbnQiOnsidGl0bGUiOiJDb21tZW50IiwiZGVzY3JpcHRpb24iOiJBZGQgYSBjb21tZW50IHRvIHRoaXMgZXhwZXJpbWVudCBkZWZpbml0aW9uLCB0byBwcm92aWRlIGFkZGl0aW9uYWwgaW5mb3JtYXRpb24gb3IgY29udGV4dC4gVGhlIGNvbW1lbnQgd2lsbCBoYXZlIG5vIGltcGFjdCBvbiB0aGUgZXhwZXJpbWVudCBkZWZpbml0aW9uIGl0c2VsZiwgYW5kIGlzIHB1cmVseSBmb3IgaW5mb3JtYXRpb25hbCBwdXJwb3Nlcy4iLCJ0eXBlIjoic3RyaW5nIiwiZGVmYXVsdCI6IiIsIm1heExlbmd0aCI6MTAwMH19LCJleGFtcGxlcyI6W3siYmVhbV9lbmVyZ3kiOjc2LjcsImZvY3VzZWRfYmVhbV9zaXplIjoyMDAsImZyYW1lcyI6MSwicV9tYXgiOjI1LCJ0aW1lX3Blcl9wZGYiOjYwMCwiY29tbWVudCI6IiJ9XX0sInVpU2NoZW1hIjp7fSwidGhlbWUiOiJkZWZhdWx0IiwibGl2ZVNldHRpbmdzIjp7InNob3dFcnJvckxpc3QiOiJ0b3AiLCJ2YWxpZGF0ZSI6ZmFsc2UsImRpc2FibGVkIjpmYWxzZSwibm9IdG1sNVZhbGlkYXRlIjpmYWxzZSwicmVhZG9ubHkiOmZhbHNlLCJvbWl0RXh0cmFEYXRhIjpmYWxzZSwibGl2ZU9taXQiOmZhbHNlLCJleHBlcmltZW50YWxfY29tcG9uZW50VXBkYXRlU3RyYXRlZ3kiOiJjdXN0b21EZWVwIiwiZXhwZXJpbWVudGFsX2RlZmF1bHRGb3JtU3RhdGVCZWhhdmlvciI6eyJhcnJheU1pbkl0ZW1zIjoicG9wdWxhdGUiLCJhbGxPZiI6InNraXBEZWZhdWx0cyIsImNvbnN0QXNEZWZhdWx0cyI6ImFsd2F5cyIsImVtcHR5T2JqZWN0RmllbGRzIjoicG9wdWxhdGVBbGxEZWZhdWx0cyIsIm1lcmdlRGVmYXVsdHNJbnRvRm9ybURhdGEiOiJ1c2VGb3JtRGF0YUlmUHJlc2VudCIsIm5lc3RlZERlZmF1bHRzUHJlY2VkZW5jZSI6ImRlc2NlbmRhbnRXaW5zIiwicmVxdWlyZWRCb29sZWFuRGVmYXVsdCI6InBvcHVsYXRlRmFsc2UifSwidXNlRmFsbGJhY2tGaWVsZCI6ZmFsc2UsInVzZUZhbGxiYWNrVWlGb3JVbnN1cHBvcnRlZFR5cGUiOmZhbHNlLCJsaXZlVmFsaWRhdGUiOmZhbHNlLCJpZFByZWZpeCI6InJvb3QiLCJpZFNlcGFyYXRvciI6Il8ifSwidmFsaWRhdG9yIjoiQUpWOCIsInNhbXBsZU5hbWUiOiJCbGFuayJ9)

Either let your DAQ support engineer know that you have made the schema and send them a link to the issue or, if you are comfortable doing so, follow the next steps to get the schema into this repository.

## Adding a schema to the repository - automatic build (recommended)

There are six steps.

1. Make sure you have the latest origin main and have created
   a new branch via `git checkout -b your-schema-branch`. One
   schema change per branch is recommended.

2. Create a schema folder inside the appropriate folder
   under `schemas` and instrument, for example `schemas/samples/p99/newschemaone`

3. Inside that new folder create a "current.json" file with "title"
   and $id matching an exact pattern based on path in root. See
   basic and advanced schema in examples folder for pattern. Create
   the schema as required.

4. Commit current.json and in commit message mention:
   the schema name and version used in $id. Example commit
   message: "SchemaD release 0.0.1"

5. Execute `git push origin your-schema-branch` and
   visit https://github.com/DiamondLightSource/ulims-json-schemas
   to start a pull request on your branch. (Your push should
   have appeared with a button to start a pull-request if you
   are logged in.)
   
6. The action "Build current.json different..." will run and
   appear on the GH `Actions` tab. A green tick will appear if
   everything builds and the check passes. Technically, this
   action is doing `npm run build-all` then **committing
   new files to your branch** which you can pull to see changes.

> [!TIP]
> Looking at the details of a workflow run on the following
> page will highlight if the CI has built and committed to
> your branch with a recommendation. https://github.com/DiamondLightSource/ulims-json-schemas/actions/workflows/pr_build_commit.yml
>
> The commit message "Schema(s) build and commit via GH action."
> will appear if the alterations made in step 3 caused new files.

If a red cross appears then you can click on it to see
more information about the failures. Check any
failures in "Build current.json different than main and commit".

If getting a lot of errors it is recommended to try running this 
process locally. See the "Setup on a new machine" section for 
information on the set-up. Then run `npm run build-main-diff`
for targeted build or `npm run build-all` for every current schema
and `npm run check` to test locally. It removes most delays 
caused by steps 3-6 so build/check iterations can be quicker. 
Once everything passes, repeat from step 4 and the action 
will commit the other four files a build generates.

> [!TIP]
> A green tick on action, then a pull and new local build should
> cause no schema related files to appear in a `git status` or
> `git diff` output.


## Adding a schema to the repository - local build (advanced)

There are five steps, in summary:

1. Create a schema folder inside the appropriate folder
   under `schemas` and instrument, for example `schemas/samples/p99/newschemaone`

2. Inside that new folder create a "current.json" file with "title"
   and $id matching an exact pattern based on path in root. See
   basic and advanced schema in examples folder for pattern. Create
   the schema as required.

3. Build the latest release by running `npm run build-all`. The
   $id in step B is important and defines the release number.
   There are recommendations for when to change the number.
   A JSON schema is valid if no errors occur.

4. Confirm the check passes with `npm run check`. This
   is done automatically on pushes to github
   repository. If issues are shown it will often be
   quicker to run this locally whilst editing file(s).

5. Once the check passes create a pull request asking for
   a merge to main. 


A page of [common build or check issues](common_issues.md)
starts with some tips and shows messages the jsonschema-tools
can cause. Expand the message to see cause and fixes.

## Updating a Schema

Edit current.json with alterations required. Changing the
number in $id first is recommended to avoid overwriting existing
releases. This is very important for schema at 1.0.0 or newer
being used by production systems. If you forget to change
the $id now, a cleanup will be required in many cases
after merging the changes. Draft schema can overwrite themselves.

Commit current.json and in commit message mention: the schema
name, version change made to $id and optionally what changed. The
basic and advanced examples have a changelog.md which is recommended
for most schema. Example commit message:
 "Bump schemaD to 1.0.1 using newer ref-schemaE 2.0.6".

## Stable and beta releases

The `$id` define releases. They should be normalised to
lowercase so folder names need to be the same. It must
end with semantic numbers.

Release 1.0.0 is the first stable release. Earlier
numbers are beta releases that could change without notice.

* Changes to a stable schema should be point releases unless
  major or minor release are forced by step 4. Old releases
  should continue to work for lifetime of repository until
  a release is phased out.

* Schema writers of beta releases do not have to alter
  the number in $id for every change. This avoids keeping
  multiple releases on disk. For example, having an $id end
  with `/0.0.1` will overwrite `0.0.1.json` on every build. 

> [!TIP]
> Advanced schema using a basic schema can evolve at
> different speeds and release numbers can appear to
> be related. But, each schema is standalone so
> each release number is separate from the other.


## Setup on a new machine

A text editor and git is often already installed, but NPM
isn't: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

* git clone https://github.com/DiamondLightSource/ulims-json-schemas.git
* Confirm in repository root and get required tools with: `npm install` 
* Confirm CLI is working: `npx jsonschema-tools --version`

When adding (or editing a schema) always create a new
branch from main: `git checkout -b quickeg1`
