import threading
import typing as t
from tempfile import mktemp

import datapane as dp


def divider() -> dp.Text:
    """
    Create a divider within your View

    :return: a Dp.Text block
    """
    return dp.Text("---")


def section(new_heading: str = "") -> t.List[dp.Blocks]:
    """
    Create a Section dividier within your View

    :param new_heading: A heading for the new section (markdown)
    :return: A list of Blocks
    """

    if new_heading:
        return [divider(), dp.Text(new_heading)]
    else:
        return [divider()]


def attach_report(blocks, name: str = "") -> dp.Attachment:
    """
    Save a collection of Blocks to a static report and make it available within
    your Report or App

    :param blocks: A collection of blocks that make up your report
    :param name: The name of the report
    :return: An attachment block that links to the saved report
    """
    f_name = mktemp(prefix="dp-report-", suffix=".html")

    dp.save_report(blocks, f_name)

    return dp.Attachment(file=f_name, filename=name or None)


T = t.TypeVar("T")


class Box(t.Generic[T]):
    """Thread-safe single element container, for storing Views (and object objects) globally"""
    def __init__(self, default: T):
        self._x: T = default
        self._lock = threading.Lock()

    def get(self) -> T:
        with self._lock:
            return self._x

    def set(self, x: T) -> None:
        with self._lock:
            self._x = x
