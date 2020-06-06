import logging
import time
import arrow


def instantiate(file_name: str) -> None:
    """
    simple logging
    """
    iso_8601 = arrow.now().format('YYYY-MM-DD')
    unix_epoch = int(time.time())
    felli_time = str(iso_8601)+"-"+str(unix_epoch)

    file_dir, file_ext = "logs/", ".log"
    full_log_file_path = file_dir+felli_time+"-"+file_name+file_ext

    logging.basicConfig(filename=full_log_file_path, level=logging.DEBUG)
    logging.info("beginning simple logger on "+felli_time+" ... ")

    return None
