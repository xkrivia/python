import logging
import string
import random
import sys
import pyperclip

FILE_NAME = "logs/passphrase"
FILE_NAME_LOG = FILE_NAME + ".log"
logging.basicConfig(filename=FILE_NAME_LOG, level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


def passphrase(length: int) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    return str(''.join(random.choice(chars) for i in range(length)))


def main():
    logging.warning('Exiting peacefully')
    sys.exit(0)


def test_passphrase_10_sets_of_10():
    assert len(passphrase(10)) == 10
