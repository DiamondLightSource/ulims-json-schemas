#!/usr/bin/env python3
"""CLI for checking library of JSON schema whole or built from fragments."""
from dataclasses import dataclass
from pathlib import Path
import json
from typing_extensions import Annotated

import typer

from registry import populate, validate_data_against_registry


# There are expected to many JSON schemas and where possible
# they should have been confirmed as being independant of any
# system. The following is configuration required to check
# a schema against a data file sample.
@dataclass
class Enabled:
    folder: Path
    filecount: int
    schema_root: str
    valid_sample: Path


app = typer.Typer()


def _confirm(pattern: Enabled, resolve: bool = True) -> None:
    """Check a library of whole or fragmented JSON schema files."""
    loaded = populate(pattern.folder)
    if len(loaded) != pattern.filecount:
        msg = "Number of resources did not match expected value. Found:"
        typer.secho(msg, fg=typer.colors.BRIGHT_RED)
        for res in loaded:
            typer.echo(res)

    if not resolve:
        return None

    # Confirms all $ref resolve when checking data files.
    okay, _ = validate_data_against_registry(
        pattern.valid_sample, pattern.folder, pattern.schema_root
    )
    if okay:
        msg = f"Confirmed files OK"
        mcolour = typer.colors.BRIGHT_GREEN
    else:
        msg = "There is at least 1 problem with a JSON schema or data file"
        mcolour = typer.colors.BRIGHT_RED
    typer.secho(f"{msg} in: {pattern.folder}", fg=mcolour)


@app.command()
def checkdir() -> None:
    """Confirm JSON schema and data files in the check directory okay.

    This command can be used whilst editing the files in "checkdir"
    to see if any changes have broken the "whole" schema which
    is built from the partial schemas. These partial schemes
    can be hardcoded into "definitions" within a single JSON
    schema file. A datafile known to validate is checked.
    """
    confirm(
        Path(Path.cwd(), "checkdir", "datafiles", "sample1.json"),
        Path(Path.cwd(), "checkdir", "schemas"),
        5,  # there are five $id spread across 5 schema files
        "urn:ulims:base:1.0",
    )

@app.command()
def zdemo() -> None:
    """Confirm JSON schemas and data files in the zdemo are okay.

    This command can be used whilst editing the files
    in "sroot/zdemo" to see if any changes have broken
    the "top" schema. A datafile known to validate with
    top version 0.0.1 is checked.
    """
    confirm(Path(Path.cwd(), "sroot", "zdemo", "pattern1", "top", "checkpy.datafile"),
            Path(Path.cwd(), "sroot", "zdemo"),
            5,
            "/zdemo/pattern1/top/0.0.1"
            )

@app.command()
def confirm(
    datafile: Annotated[
        Path,
        typer.Option("-d", "--datafile", help="JSON datafile to check against schemas"),
    ],
    schemas: Annotated[
        Path,
        typer.Option("-s", "--schemas", help="Folder with JSON schema files"),
    ],
    scount: Annotated[
        int,
        typer.Option(
            "-c",
            "--scount",
            help="Number of JSON schemas expected to be loaded into registry.",
        ),
    ],
    sroot: Annotated[
        str,
        typer.Option(
            "-r",
            "--sroot",
            help="Root $id in JSON schemas files to validate datafile against.",
        ),
    ],
):
    """Confirm JSON datafile and schemas pass minimum checks.

    A folder with a set of schemes is loaded into a registry
    which will have constant count unless changes are being
    made to the schema files. If count is wrong a list of "$id"
    is shown so the "bad" schema file can be tracked down. The
    schema folder can have one or more "roots" ($id) enabling
    reuse of schemas across schemas. This command requires
    a root to be picked (which will be an $id in one of
    the schema files) and the datafile is validated.

    The command *checkdir* provides a shortcut for a folder
    in the repo whose files can be edited to see how "bad"
    changes to schemas or datafiles alter output. 
    """
    with open(datafile) as source:
        content = json.load(source)

    pattern = Enabled(
        folder=schemas,
        filecount=scount,
        schema_root=sroot,
        valid_sample=content,
    )
    _confirm(pattern)


@app.command()
def version() -> str:
    "Show version and exit"
    return "0.1"


if __name__ == "__main__":
    app()
