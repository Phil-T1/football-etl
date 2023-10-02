"""Test logging functions."""

import pytest
import logging
import logging.config
from src.logger import instantiate_logger


@pytest.fixture
def logger():
    return instantiate_logger()


def test_instantiate_logger(logger):
    # Check if the logger is correctly configured
    assert isinstance(logger, logging.Logger)

    # Check if the logger has a Stream Handler and Console Handler
    stream_handler_exists = False
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            stream_handler_exists = True
            assert handler.level == logging.DEBUG
    # Check handlers exist
    assert stream_handler_exists
