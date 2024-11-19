import logging
from webserver import Server


logger = logging.getLogger(__name__)

class Controller:
  """
  Controller initializes the environment and all the interconnected processes that are required to make the
  web application run as intended.

  Currently, there is only one dependency that is required for this project. The Server class initializes all
  components required to make the web application run as intended. However, this Controller class may become necessary
  if a future requirement comes and additional needs must be met. In such a case, those subroutines should be
  initialized in the Controller constructor.

  Subroutines:
  - webserver Server
  """
  def __init__(self):
    logging.basicConfig(filename="controller.log", level=logging.INFO)
    logger.info("Controller Started")
    Server()