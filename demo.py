from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


logging.info("welcome to custom log ")


try:
    a = 20
except Exception as e:
    raise USvisaException(e , sys)