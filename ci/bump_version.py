#!/usr/bin/env python
from datetime import date
import sh


def _get_new_version():
    """We're utilising calver

    returns string of form: YYYY.MM.DD
    Does not include leading zeros
    """
    today = date.today()
    return f'{today.year}.{today.month}.{today.day}'


def main():
    new_version = _get_new_version()
    sh.poetry.version("-vv", "--", new_version, _fg=True)


if __name__ == '__main__':
    main()
