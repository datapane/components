#!/usr/bin/env python
from datetime import date
import sh


def _get_new_version():
    """We're utilising calver

    returns string of form: YYYY.MM.DD
    Does not include leading zeros
    """
    today = date.today()
    return f"{today.year}.{today.month}.{today.day}"


def _commit_and_tag(new_version: str):
    prefixed_version = f"v{new_version}"

    sh.git.add("pyproject.toml")
    sh.git.commit("-m", f"Release {prefixed_version}")
    sh.git.tag("-a", f"{prefixed_version}", "-m", f"Release {prefixed_version}")


def main(git: bool = False):
    new_version = _get_new_version()
    sh.poetry.version("-vv", "--", new_version, _fg=True)

    if git:
        _commit_and_tag(new_version)


if __name__ == "__main__":
    main()
