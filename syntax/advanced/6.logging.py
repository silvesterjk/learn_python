import logging

"""
5 levels of logging are:

1. DEBUG: Detailed information, typically of interest only when diagnosing problems.
2. INFO: Confirmation that things are working as expected.
3. WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
4. ERROR: Due to a more serious problem, the software has not been able to perform some function.
5. CRITICAL: A serious error, indicating that the program itself may be unable to continue running. 

"""

logging.basicConfig(level=logging.DEBUG) # By default, the level is set to WARNING
logging.debug("This is a debug message") # This will not get printed
logging.info("This is an info message") # This will not get printed
logging.warning("This is a warning message") # This will get printed
logging.error("This is an error message") # This will get printed
logging.critical("This is a critical message") # This will get printed

# basicConfig
logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s")
# format="%(name)s - %(levelname)s - %(message)s" --> This will print the name of the logger, the level of the message and the message itself
# format="%(asctime)s - %(name)s - %(levelname)s - %(message)s" --> This will print the time the message was logged, the name of the logger, the level of the message and the message itself
# datefmt="%d-%b-%y %H:%M:%S" --> This will print the time in the format specified
# filemode="w" --> This will overwrite the file each time the program is run. If you want to append the messages to the file, use "a" instead of "w"
# stream=sys.stdout --> This will print the messages to the console instead of a file
# style="%" --> This is the default style. It can also be "{"
# level=logging.DEBUG --> This will print all the messages. If you want to print only the critical messages, use logging.CRITICAL instead of logging.DEBUG
# handlers=[logging.FileHandler("app.log")] --> This will write the messages to a file called app.log
# handlers=[logging.StreamHandler()] --> This will write the messages to the console
# handlers=[logging.StreamHandler(sys.stdout)] --> This will write the messages to the console
# handlers=[logging.StreamHandler(sys.stderr)] --> This will write the messages to the console

# getLogger
# It is a good practice to create a logger object and use it to log messages
# Otherwise it is assigned to the root logger by default
logger = logging.getLogger(__name__)
logger.info("This is an info message")

# level and the format
# By default, the level is set to WARNING
# By default, the format is set to "%(levelname)s: %(message)s"
# The format can be changed using the basicConfig method

# StreamHandler
# This will write the messages to the console
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.warning("This is a warning message")

# FileHandler
# This will write the messages to a file
file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)
logger.error("This is an error message")

# Formatter
# This will format the messages
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.error("This is an error message")