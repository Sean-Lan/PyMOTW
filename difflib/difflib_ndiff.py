import difflib
from difflib_data import *

diff = difflib.ndiff(text1_lines, text2_lines)
print '\n'.join(list(diff))
