
import logging

# 设置级别，如果不设置级别level默认为WARNING

LOG_FORMAT = "%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s"

logging.basicConfig(level=logging.DEBUG, filename="tianying.log", format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

# 也可以这样写
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")