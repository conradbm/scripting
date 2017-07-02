# Source:https://stackoverflow.com/questions/8689795/how-can-i-remove-non-ascii-characters-but-leave-periods-and-spaces-using-python
# Goal: Remove weird non-asci characters from string

import string
printable = set(string.printable)
filter(lambda x: x in printable, yourString)

