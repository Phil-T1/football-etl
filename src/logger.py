"""Logging functions."""

import logging


def initialise_logger():
    """Initialise logger."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def file_handler():
    """Configure file logging."""
    file_handler = logging.FileHandler("football_table_standings.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )


def console_handler():
    """Configure console logging."""
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )


def instantiate_logger():
    """Create logging instance."""
    # Instantiate the logger object
    logger = logging.getLogger()
    # Add the file handler to the logger
    logger.addHandler(file_handler())
    # Add the console handler to the logger
    logger.addHandler(console_handler())
    return logger
