import logging
from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
logger = logging.getLogger(__name__)

class Server:
  def __init__(self):
    logging.basicConfig(filename="server.log", level=logging.INFO)
    logger.info("Flask Server Started")
    app.run(debug=True, port=8000)
