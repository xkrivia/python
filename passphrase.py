# passphrase.py
# Written by: ChrisTheCaribou
# This program generates an n-length passphrase and copies it to the clipboard
# Useful if you don't trust websites and desire to use your OWN system memory

# Requires: pyperclip, termcolor
# > pip install pyperclip
# > pip install colorama
# > pip install termcolor

import string
import random
import sys
import pyperclip
from termcolor import colored
from colorama import init

init()

print(colored(sys.version, 'grey'))
if sys.version_info[0] < 3:
    #raise Exception("Python 3 or a more recent version is required.")
    input(colored('ERROR: Python 3+ is required.','red'))
    sys.exit(0)

# Call out a bad user for faulty inputs!
try:
    plength = int(input('Enter the number of characters in the passphrase: '))
except ValueError:
    print(colored('ERROR: You did not enter a valid integer!', 'red'))
    sys.exit(0)
except NameError:
    print(colored('ERROR: You did not enter a valid integer!', 'red'))
    sys.exit(0)

# Some websites prohibit punctuation in passphrases because they run shitty
# AS400s for servers
punctQ = input('Include punctuation characters? (Y/N): ')
if (punctQ == "Y"):
    pQ = True
    print('You have selected a passhrase of length', plength,
    'with inclusive punctuation.')
if (punctQ == "N"):
    pQ = False
    print('You have selected a passhrase of length', plength,
    'without inclusive punctuation.')
else:
    pQ = True

# Actual program logic
def passphrase(size, punct):
    if (punct == False):
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(size))

# Output it to console & copy to clipboard for easy use elsewhere
print('Your passhrase, generated in local memory is:\n')
passphrase = passphrase(plength, pQ)
print(colored(passphrase,'green'))
pyperclip.copy(passphrase)
print('\nThis passphrase has been copied to the system clipboard.')
input('Press any key to exit ...')
