import logging
from webserver import Server


logger = logging.getLogger(__name__)

class Controller:
  def __init__(self):
    logging.basicConfig(filename="controller.log", level=logging.INFO)
    logger.info("Controller Started")
    Server()