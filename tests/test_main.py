# Trivial tests to ensure basics working for now

import pytest
import datapane as dp


def _check_view(v) -> None:
    _ = dp.stringify_report(v)


def test_heatmap():
    from datapane_components import calendar_heatmap

    v = calendar_heatmap.example()
    _check_view(v)


def test_timeline():
    from datapane_components import timeline

    v = timeline.example()
    _check_view(v)


def test_datasets():
    from datapane_components import datasets

    df = datasets.load_dataset(dict(upload=None, dataset="airports"))
    assert df.shape == (3376, 7)

    with pytest.raises(AttributeError):
        df = datasets.load_dataset(dict(upload=None, dataset="airports1"))
