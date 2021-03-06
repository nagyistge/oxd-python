# module metadata
__description__ = "A Python Client for oxD Server"
__version__ = "2.4.4"
__author__ = "Gluu"

# setup logging system
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

# expose Client
from client import Client
