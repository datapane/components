"""Wrapper around vega_datasets for use in Datapane Apps"""
import typing as t

import vega_datasets as v
import pandas as pd
import datapane as dp


dataset_names: t.List[str] = v.local_data.list_datasets()
_default: str = dataset_names[0]

# a reusable control to add to a form
data_choice = dp.Controls(
    dp.Choice(name="dataset", options=dataset_names, initial=_default, label="Select a built-in dataset")
)

data_choice_with_file = data_choice + dp.Controls(
    dp.File(name="upload", label="(Optional) Upload test data", allow_empty=True)
)


def load_dataset(params: t.Dict) -> pd.DataFrame:
    upload = params["upload"]
    return pd.read_csv(upload) if upload else v.local_data(params["dataset"])


# def get_dataset(name: str = _default) -> pd.DataFrame:
#     """Return the sample dataset"""
#     return v.local_data(name)
