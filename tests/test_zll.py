import os
import sys
import unittest
import unittest.mock
from pathlib import Path

# Add parent directory to path to import zll module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from zll import add_connection, create_config_file, delete_connection, read_connections


class TestZLL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Store original file_path from zll module
        import zll.zll as zll_module

        cls.original_file_path = zll_module.config_file_path

    def setUp(self):
        # Set up test environment
        self.test_file_path = Path("test_hosts.csv")
        self.test_file_path.write_text("User,Host,Port,Description\n")

    def tearDown(self):
        # Clean up after tests
        if self.test_file_path.exists():
            self.test_file_path.unlink()

    def test_create_config_file(self):
        import zll.zll as zll_module

        # Temporarily change the file path
        zll_module.config_file_path = self.test_file_path
        create_config_file()
        self.assertTrue(self.test_file_path.exists())
        # Restore original file path
        zll_module.config_file_path = self.original_file_path

    def test_read_connections(self):
        import zll.zll as zll_module

        # Temporarily change the file path
        zll_module.config_file_path = self.test_file_path
        self.test_file_path.write_text(
            "User,Host,Port,Description\nuser1,host1,22,test1\n"
        )
        header, rows = read_connections()
        self.assertEqual(header, ["User", "Host", "Port", "Description"])
        self.assertEqual(rows, [["user1", "host1", "22", "test1"]])
        # Restore original file path
        zll_module.config_file_path = self.original_file_path

    def test_add_connection(self):
        import zll.zll as zll_module

        # Temporarily change the file path
        zll_module.config_file_path = self.test_file_path
        with (
            unittest.mock.patch(
                "builtins.input",
                side_effect=["testuser", "testhost", "2222", "testdesc"],
            ),
            unittest.mock.patch("zll.zll.main"),  # Mock main to prevent recursive call
        ):
            add_connection()
        header, rows = read_connections()
        self.assertEqual(rows[-1], ["testuser", "testhost", "2222", "testdesc"])
        # Restore original file path
        zll_module.config_file_path = self.original_file_path

    def test_delete_connection(self):
        import zll.zll as zll_module

        # Temporarily change the file path
        zll_module.config_file_path = self.test_file_path
        self.test_file_path.write_text(
            "User,Host,Port,Description\nuser1,host1,22,test1\nuser2,host2,22,test2\n"
        )
        with unittest.mock.patch("zll.zll.main"):  # Mock main to prevent recursive call
            delete_connection("0")
        header, rows = read_connections()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], ["user2", "host2", "22", "test2"])
        # Restore original file path
        zll_module.config_file_path = self.original_file_path


if __name__ == "__main__":
    unittest.main()
