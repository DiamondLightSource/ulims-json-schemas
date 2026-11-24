# Image should be built from project root, e.g. docker build -f server/Dockerfile

# Validation stage
FROM python:3.13-alpine AS validator

WORKDIR /work

RUN pip install --no-cache-dir jsonschema

COPY schemas/ /input/
COPY server/validate_schemas.py .

RUN python validate_schemas.py


# Runtime stage
FROM nginx/nginx-unprivileged:stable-alpine

COPY --from=validator /output/ /usr/share/nginx/html/

EXPOSE 8080
