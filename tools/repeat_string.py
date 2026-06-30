# tool: repeat_string
# description: Repeats a string N times 
# author: @rdhadge
# example: repeat_string "ha" "3" -> "hahaha"


def run(*args) -> str:
    string = args[0]
    repetition = int(args[1])
    return string * repetition
