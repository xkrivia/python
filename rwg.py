# CHRIS FELLI, 2019
# This program generates an n-length series of random words, which I use for
# website logins. Also copies to clipboard!

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
import urllib.request

# Initialize terminal ANSI color for Windows users
init()

# Python 3.0 check
print(colored(sys.version, 'grey'))
if sys.version_info[0] < 3:
    #raise Exception("Python 3 or a more recent version is required.")
    input(colored('ERROR: Python 3+ is required.','red'))
    sys.exit(0)

# Pull dictionary from the Internet
word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

# Generates some typologies to work with
upper_words = [word for word in words if word[0].isupper()]
lower_words = [word for word in words if word[0].islower()]
name_words  = [word for word in upper_words if not word.isupper()]
rand_name   = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])

# Prints the real deal
for n in range(10):
    print(' '.join([lower_words[random.randint(0,len(lower_words))] for i in range(4)]))
