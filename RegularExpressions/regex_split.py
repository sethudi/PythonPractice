#!./venv/bin/python

import re

def main():
    text = "one, two ,three, four"
    # fields = text.split(",")

    fields = re.split(r"\s*,\s*", text)

    print(fields)
    
main()