from src.parser import parse_command

VFS_NAME = "my_vfs"


def execute_command(command, args):
    if command == "ls":
        print("ls", args)
        return True

    if command == "cd":
        print("cd", args)
        return True

    if command == "exit":
        if args:
            print("Ошибка: команда exit не принимает аргументы.")
            return True

        return False

    print(f"Ошибка: неизвестная команда '{command}'.")
    return True


def main():
    while True:
        user_input = input(f"{VFS_NAME}> ")

        command, args = parse_command(user_input)

        if command is None:
            print("Ошибка: некорректные кавычки.")
            continue

        if not command:
            continue

        if not execute_command(command, args):
            break


if __name__ == "__main__":
    main()