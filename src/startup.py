from pathlib import Path

from src.parser import parse_command


def run_startup_script(script_path, prompt, execute_command):
    path = Path(script_path)

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        print(f"Ошибка: не удалось открыть скрипт '{script_path}'.")
        return False, False

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue

        print(f"{prompt}> {line}")

        command, args = parse_command(line)

        if command is None:
            print("Ошибка: некорректные кавычки.")
            print(f"Ошибка в строке {line_number} стартового скрипта.")
            return True, False

        if not command:
            continue

        should_continue, success = execute_command(command, args)

        if not success:
            print(f"Ошибка в строке {line_number} стартового скрипта.")
            return True, False

        if not should_continue:
            return False, True

    return True, True