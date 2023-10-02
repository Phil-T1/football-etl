"""Test logging functions."""

import pytest
import logging
from src.logger import instantiate_logger


def test_instantiate_logger():
    logger = instantiate_logger()
    assert isinstance(logger, logging.Logger)
