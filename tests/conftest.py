import pytest

from datapane import DPMode, set_dp_mode
from datapane.client import config
from datapane.client.utils import _setup_dp_logging


@pytest.fixture(autouse=True)
def dp_setup(request, monkeypatch, tmp_path):
    """
    Set up the common environment and clean default config for each test.
    """
    # Monkeypatch config file into a tmp dir
    config_dir = tmp_path / "config"
    config_dir.mkdir(parents=True)
    monkeypatch.setattr(config, "APP_DIR", config_dir)
    monkeypatch.setattr(config, "CONFIG_PATH", config_dir / config.CONFIG_FILENAME)
    monkeypatch.setattr(config, "LEGACY_CONFIG_PATH", config_dir / config.LEGACY_CONFIG_FILENAME)

    # Init API with full debug logging
    set_dp_mode(DPMode.SCRIPT)
    _setup_dp_logging(verbosity=2)
    config.init()
