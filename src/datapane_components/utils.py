import typing as t
import datapane as dp


def Divider() -> dp.Text:
    return dp.Text("---")


def Section(new_heading: str = "") -> t.List[dp.Block]:
    if new_heading:
        return [Divider(), dp.Text(new_heading)]
    else:
        return [Divider()]
