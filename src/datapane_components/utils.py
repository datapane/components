import typing as t
from tempfile import mktemp

import datapane as dp


print(dp.__version__)
print(dp.__rev__)


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
