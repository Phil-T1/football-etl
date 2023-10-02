"""Logging functions."""

import logging
import logging.config


def instantiate_logger(logger_name: str = "simpleExample"):
    """Create loggging instance."""
    # Loads The Config File
    logging.config.fileConfig("logging.conf")

    # Create a logger with the name from the config file.
    # This logger now has StreamHandler with DEBUG Level,
    # and the specified format in the logging.conf file
    return logging.getLogger(logger_name)
