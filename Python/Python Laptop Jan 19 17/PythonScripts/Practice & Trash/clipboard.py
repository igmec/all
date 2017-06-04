#! python3
#clipboard.py manages some passwords

import pyperclip
import sys

PASS = {'email':'REDACTED',
        'facebook':'REDACTED',
        'google':'REDACTED'}

print(sys.argv)
#sys.exit()

if len(sys.argv) == 2:
    pyperclip.copy(PASS[sys.argv[1].lower()])
    print("Password for " + sys.argv[1] + " copied.")

else:
    pyperclip.copy("sample text")
    print(pyperclip.paste())
