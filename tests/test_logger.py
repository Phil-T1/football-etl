"""Test logging functions."""

import append_src_to_path
import unittest
import os
import logging
from src.logger import (
    initialise_logger,
    file_handler,
    console_handler,
    instantiate_logger,
)


class TestLoggingFunctions(unittest.TestCase):
    def setUp(self):
        # Remove the log file if it exists before each test
        if os.path.exists("football_table_standings.log"):
            os.remove("football_table_standings.log")

    def tearDown(self):
        # Remove the log file after each test
        if os.path.exists("football_table_standings.log"):
            os.remove("football_table_standings.log")

    def test_initialise_logger(self):
        # Call the function to be tested
        initialise_logger()

        # Check if the logger has been initialized properly
        logger = logging.getLogger()
        self.assertIsNotNone(logger)
        self.assertEqual(logger.level, logging.INFO)

    def test_file_handler(self):
        # Call the function to be tested
        file_handler()

        # Check if the file handler has been created and configured properly
        logger = logging.getLogger()
        handlers = logger.handlers
        self.assertEqual(len(handlers), 1)
        # file_handler = handlers[0]
        # self.assertIsInstance(file_handler, logging.FileHandler)
        # self.assertEqual(file_handler.level, logging.DEBUG)
        # formatter = file_handler.formatter
        # self.assertIsInstance(formatter, logging.Formatter)
        # self.assertEqual(
        #     formatter._fmt, "%(asctime)s - %(levelname)s - %(message)s"
        # )

    def test_console_handler(self):
        # Call the function to be tested
        console_handler()

        # Check if the console handler has been created and configured properly
        logger = logging.getLogger()
        handlers = logger.handlers
        self.assertEqual(len(handlers), 1)
        # console_handler = handlers[0]
        # self.assertIsInstance(console_handler, logging.StreamHandler)
        # self.assertEqual(console_handler.level, logging.DEBUG)
        # formatter = console_handler.formatter
        # self.assertIsInstance(formatter, logging.Formatter)
        # self.assertEqual(
        #     formatter._fmt, "%(asctime)s - %(levelname)s - %(message)s"
        # )

    def test_instantiate_logger(self):
        # Call the function to be tested
        logger = instantiate_logger()

        # Check if the logger has been instantiated properly
        self.assertIsNotNone(logger)
        self.assertEqual(
            logger.level, logging.NOTSET
        )  # Default level when no handlers are added

        handlers = logger.handlers
        self.assertEqual(
            len(handlers), 2
        )  # Should have both file and console handlers

        file_handler = handlers[0]
        console_handler = handlers[1]

        self.assertIsInstance(file_handler, logging.FileHandler)
        self.assertEqual(file_handler.level, logging.DEBUG)

        self.assertIsInstance(console_handler, logging.StreamHandler)
        self.assertEqual(console_handler.level, logging.DEBUG)


if __name__ == "__main__":
    unittest.main()
