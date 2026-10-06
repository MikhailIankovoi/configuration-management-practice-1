from src.config import parse_args
from src.parser import parse_command
from src.startup import run_startup_script

VFS_NAME = "my_vfs"


def execute_command(command, args):
    if command == "ls":
        print("ls", args)
        return True, True

    if command == "cd":
        print("cd", args)
        return True, True

    if command == "exit":
        if args:
            print("Ошибка: команда exit не принимает аргументы.")
            return True, False

        return False, True

    print(f"Ошибка: неизвестная команда '{command}'.")
    return True, False


def print_config(args):
    vfs_path = args.vfs if args.vfs else "не указан"
    script_path = args.script if args.script else "не указан"

    print("Параметры запуска:")
    print(f"VFS: {vfs_path}")
    print(f"Стартовый скрипт: {script_path}")
    print()


def run_interactive():
    while True:
        user_input = input(f"{VFS_NAME}> ")
        command, args = parse_command(user_input)

        if command is None:
            print("Ошибка: некорректные кавычки.")
            continue

        if not command:
            continue

        should_continue, _ = execute_command(command, args)

        if not should_continue:
            break


def main():
    args = parse_args()
    print_config(args)

    if args.script:
        should_continue, success = run_startup_script(
            args.script,
            VFS_NAME,
            execute_command
        )

        if not success:
            print("Выполнение стартового скрипта остановлено.")

        if not should_continue:
            return

    run_interactive()


if __name__ == "__main__":
    main()