import re

print(re.match(r"[a-z\d\-\.]+", "a-b.c3d"))

print(re.match(r"([a-z][a-z\d\-\.]+)@(\w+)\.(\w+)", "john.purcell@caveofprogramming.com"))