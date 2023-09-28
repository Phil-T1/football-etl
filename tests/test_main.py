"""Test main functions."""
import append_src_to_path
import unittest
from src.main import read_dotenv


class MainTest(unittest.TestCase):
    def test_has_values(self):
        """All vars should have values."""
        val_list = read_dotenv().values()
        self.assertTrue(None not in val_list)


if __name__ == "__main__":
    unittest.main()
