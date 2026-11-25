# Deletion of schemas in schemas/data_catalogue/shared/

We accidentally used "shared" instead of "_shared" and this
page documents removal process. A CI job that runs on PRs will
stop this occurring again.

## Schemas ($id) that need checking for in systems

The following IDs must not appear in any database with data
validated against it.

* "/data_catalogue/i08/generic_scan/1.0.0"
* "/data_catalogue/i08-1/generic_scan/1.0.0"
* "/data_catalogue/i14/mapping_scan/2.0.0"

The above can can be worked out via the `npm run check` which
signals and `npm run build-all` which says which contains
the $id to be looked for. Like below.


## Process

```
git rm -r schemas/data_catalogue/shared/
rm 'schemas/data_catalogue/shared/imaging/sample_common/1.0.0.json'
rm 'schemas/data_catalogue/shared/imaging/sample_common/current.json'
rm 'schemas/data_catalogue/shared/imaging/scan_common/1.0.0.json'
rm 'schemas/data_catalogue/shared/imaging/scan_common/current.json'
```

### Result of check
```
1) Schema Repository Structure in ./schemas/
       Schema with title data_catalogue/i08/generic_scan
         current version 1.0.0 must be equal to materialized latest version 1.0.0:
     
  2) Schema Repository Structure in ./schemas/
       Schema with title data_catalogue/i08-1/generic_scan
         current version 1.0.0 must be equal to materialized latest version 1.0.0:

  3) Schema Repository Structure in ./schemas/
       Schema with title data_catalogue/i14/mapping_scan
         current version 2.0.0 must be equal to materialized latest version 2.0.0:

```

### Result of build-all

```
[2026-11-25 15:02:49.985 +0000]: Failed dereferencing schema with $id /data_catalogue/i08/generic_scan/1.0.0 {"title":"data_catalogue/i08/generic_scan","$id":"/data_catalogue/i08/generic_scan/1.0.0","$schema":"http://json-schema.org/draft-07/schema#","description":"Generic scan on I08","type":"object","additionalProperties":false,"properties":{"scan_common":{"$ref":"/data_catalogue/shared/imaging/scan_common/1.0.0.json"},"sample_common":{"$ref":"/data_catalogue/shared/imaging/

[2026-11-25 15:02:49.985 +0000]: Failed dereferencing schema with $id /data_catalogue/i08-1/generic_scan/1.0.0 {"title":"data_catalogue/i08-1/generic_scan","$id":"/data_catalogue/i08-1/generic_scan/1.0.0","$schema":"http://json-schema.org/draft-07/schema#","description":"Generic scan on I08-1","type":"object","additionalProperties":false,"properties":{"scan_common":{"$ref":"/data_catalogue/shared/imaging/scan_common/1.0.0.json"},"sample_common":{"$ref":"/data_catalogue/shared/imaging/sample_common/1.0.0.json"}

[2026-11-25 15:02:49.985 +0000]: Failed dereferencing schema with $id /data_catalogue/i14/mapping_scan/2.0.0 {"title":"data_catalogue/i14/mapping_scan","$id":"/data_catalogue/i14/mapping_scan/2.0.0","$schema":"http://json-schema.org/draft-07/schema#","description":"Mapping scan on I14","type":"object","additionalProperties":false,"properties":{"scan_common":{"$ref":"/data_catalogue/shared/imaging/scan_common/1.0.0.json"},"sample_common":{"$ref":"/data_catalogue/shared/imaging/sample_common/1.0.0.json"},"scan_parameters":{"title":"Scan Parameters",
```

