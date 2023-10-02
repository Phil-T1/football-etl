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

    # Check if the logger has a Console Handler and File Handler
    console_handler_exists = False
    file_handler_exists = False

    logger.debug(logger.handlers)
    for handler in logger.handlers:
        # Check console handler
        if isinstance(handler, logging.StreamHandler):
            console_handler_exists = True
            assert handler.level == logging.DEBUG
        # Check file handler
        if isinstance(handler, logging.FileHandler):
            file_handler_exists = True
            assert handler.level == logging.DEBUG

    # Check handlers exist
    assert console_handler_exists
    assert file_handler_exists
