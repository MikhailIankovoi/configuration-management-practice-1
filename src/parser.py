import shlex


def parse_command(user_input):
    try:
        parts = shlex.split(user_input)
    except ValueError:
        return None, None

    if not parts:
        return "", []

    return parts[0], parts[1:]