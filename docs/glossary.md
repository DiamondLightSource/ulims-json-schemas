# Glossary

The following terms are used in the documentation.

* **schema root** - all schemes are kept in a root which any
  schema can reference by using / in certain places. Multiple
  roots could exist but scripts expect a single. Folder *sroot*
  is the root of this schema repository. 

* **schema set** - a collection of schemas which can
  often reference themselves. A macro application
  or microservice might have a set. Folder *sroot/zdemo* is
  an example set.

* **schema group** - a collection of schemas related
  to each other and recommended level for a
  schema. Folder *sroot/zdemo/pattern1* is an example group
  which also has a child sub groups.

* **schema** - a schema is a complete JSON schema and always
  has a unique folder containing a "current"
  version. Folder *sroot/zdemo/empty* can be copied
  into a scheme set or group and **after editing**
  version 0.0.1 of a new schema can be built. Three types exists,
  where the first is easiest.

  * **standalone** - have properties and no external references. A
    build for low level schema (like empty) appears to do almost
    nothing. This type is how most schema will start until
    reuse patterns emerge. Folder *sroot/zdemo/pattern1/child/three*
    is example.

  * **shared** - has references to other schemas which means
    properties come from an exact version of a standalone
    schema **when** built. Child one and two are examples
    in pattern 1.

  * **top** - a shared schema expected to be cached by
    applications which is built from a collection of shared
    schemas. Folder *sroot/zdemo/pattern1/top* is example. A
    large number of top schemas could exist which are close
    to identical except for some properties. 

A schema root **MUST** be built and tested when a schema version
changes. Additional terms:

* **SRC (Schema Root Check)** - all schemas in all folders
  must pass this check before being committed. Doing a SRC
  means running command **npm run check** and it reporting
  no outstanding issues.

* **current** - the source of a built schema with an $id that
  encodes the version of this schema. The **only** file that
  should edited manually in a schema folder.

* **built** - a schema needs building at least once to generate
  the necessary files. The version in $id will be used to
  generate an exact versioned schema and make soft links.

* **latest** - a build will always update a "latest"
  soft link **if** the version in $id is newer. It signals
  a point release is due. Schemas using the old version
  will continue to work and build with version they pinned.

* **pinned** - references in current between schemas
should be pinned to an exact version of a schema. (A current
can use latest of another schema, but pinned is best)

Technically, a build turns schemas of all types into
standalone versions that applications are free to cache.