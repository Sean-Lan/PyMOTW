import difflib
from difflib_data import *

d = difflib.HtmlDiff()
print d.make_table(text1_lines, text2_lines)
