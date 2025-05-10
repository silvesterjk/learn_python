import logging

# Default:

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("This is an informational message")
logger.error("This is an error message")
logger.warning("This is a warning message")
logger.debug("This is a debug message")
logger.critical("This is a critical message")

"""
The logs would get printed like this:
1. INFO:root:This is an informational message
2. ERROR:root:This is an error message
3. WARNING:root:This is a warning message
4. DEBUG:root:This is a debug message
5. CRITICAL:root:This is a critical message
"""

# Custom Handler:

handler = logging.StreamHandler()
filer_handler = logging.Filter("__main__")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
