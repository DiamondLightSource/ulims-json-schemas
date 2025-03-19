# The Docker file used to build From container is defined
# here: https://github.com/wikimedia/integration-config/tree/master/dockerfiles/node20-test
FROM docker-registry.wikimedia.org/releng/node20-test:20.16.0

# Files unique for ULIMS schemas.
COPY package.json package.json 
COPY package-lock.json package-lock.json 
COPY test/jsonschema/repository.test.js test/jsonschema/repository.test.js
COPY .jsonschema-tools.yaml  .jsonschema-tools.yaml
ADD sroot sroot

# https://github.com/wikimedia/integration-config/blob/master/dockerfiles/node20-test/run.sh
RUN /run.sh

# The image build should fail with the same error seen
# locally when doing: npm run test
