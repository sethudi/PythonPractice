#!./venv/bin/python

import re

def main():
    text = "You could get a developer job. E.g. in robotics. Maybe. Or web development."

    # anything after ?= is not included in the match, however is used to just look if something is there.
    results = re.findall(r"\s+(\w+)\.(?=\s+|$)", text)

    print(results)
    
main()