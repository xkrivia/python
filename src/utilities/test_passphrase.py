import logging
import string
import random
import sys
import pyperclip

FILE_NAME = "logs/passphrase"
FILE_NAME_LOG = FILE_NAME + ".log"
logging.basicConfig(filename=FILE_NAME_LOG, level=logging.DEBUG)

def passphrase(length: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    product = str(''.join(random.choice(alphabet) for i in range(length)))
    logging.info(product)
    return(product)

def test_passphrase_10_sets_of_10():
    assert len([passphrase(10) for _ in range(10)]) == 10
