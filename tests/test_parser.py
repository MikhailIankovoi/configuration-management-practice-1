import unittest

from src.parser import parse_command


class TestParser(unittest.TestCase):
    def test_simple_command(self):
        command, args = parse_command("ls documents")

        self.assertEqual(command, "ls")
        self.assertEqual(args, ["documents"])

    def test_quoted_argument(self):
        command, args = parse_command('cd "My Documents"')

        self.assertEqual(command, "cd")
        self.assertEqual(args, ["My Documents"])

    def test_invalid_quotes(self):
        command, args = parse_command('cd "My Documents')

        self.assertIsNone(command)
        self.assertIsNone(args)


if __name__ == "__main__":
    unittest.main()