import logging
import string
import random
import sys
import pyperclip
import os
import time
from slogger import instantiate


this_scripts_name = str(os.path.splitext(os.path.basename(__file__))[0])
instantiate(this_scripts_name)


def passphrase(length: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    product = str(''.join(random.choice(alphabet) for i in range(length)))
    logging.info(" "+product)
    return(product)

def test_passphrase_10_sets_of_10():
    assert len([passphrase(10) for _ in range(10)]) == 10
