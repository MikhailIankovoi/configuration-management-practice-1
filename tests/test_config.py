import unittest

from src.config import parse_args


class TestConfig(unittest.TestCase):
    def test_vfs_argument(self):
        args = parse_args(["--vfs", "vfs_samples"])

        self.assertEqual(args.vfs, "vfs_samples")
        self.assertIsNone(args.script)

    def test_script_argument(self):
        args = parse_args(["--script", "scripts/startup_ok.txt"])

        self.assertIsNone(args.vfs)
        self.assertEqual(args.script, "scripts/startup_ok.txt")

    def test_all_arguments(self):
        args = parse_args([
            "--vfs",
            "vfs_samples",
            "--script",
            "scripts/startup_ok.txt"
        ])

        self.assertEqual(args.vfs, "vfs_samples")
        self.assertEqual(args.script, "scripts/startup_ok.txt")


if __name__ == "__main__":
    unittest.main()