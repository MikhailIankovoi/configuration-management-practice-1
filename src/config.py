import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Эмулятор командной оболочки"
    )

    parser.add_argument(
        "--vfs",
        help="Путь к физическому расположению VFS"
    )

    parser.add_argument(
        "--script",
        help="Путь к стартовому скрипту"
    )

    return parser.parse_args(argv)