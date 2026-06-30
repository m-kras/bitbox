# tool: title_case
# description: Converts the input string to a title case string
# author: @rdhadge
# example: title_case "hello world" -> "Hello World"


def run(*args) -> str:
    text = args[0]
    return text.title()
