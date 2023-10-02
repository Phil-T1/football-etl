"""Test main functions."""

import pytest
from src.main import read_dotenv


def test_has_values():
    """All vars should have values."""
    val_list = read_dotenv().values()
    assert None not in val_list
