#!./venv/bin/python

import re

def main():
    text = """
        one
        two
        three
    """

    result = re.match(r"(.*?two.*?)$", text, re.DOTALL|re.MULTILINE)
    print(result)
    if result is None:
        print("No match")
    else:
        print(f"Match: '{result.group(1)}'")

main()