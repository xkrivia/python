import logging
import os
import inspect
import time


def instantiate(file_name: str): 
	"""
	simple logging	
	"""
	file_dir, file_ext = "logs/", ".log"
	full_log_file_path = file_dir + file_name + file_ext
	
	epoch_time = int(time.time())
	logging.basicConfig(filename=full_log_file_path, level=logging.DEBUG)
	logging.info("beginning slogger on " + str(epoch_time) + " ... ")	
	
	return None
