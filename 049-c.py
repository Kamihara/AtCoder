import sys

s = raw_input()

if "eraser" in s:
    s = s.replace("eraser", "")
if "erase" in s:
    s = s.replace("erase", "")
if "dreamer" in s:
    s = s.replace("dreamer", "")
if "dream" in s:
    s = s.replace("dream", "")
print "YES" if len(s) == 0 else "NO"
