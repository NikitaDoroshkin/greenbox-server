from flask import Flask
app = Flask(__name__)

from app.HAL.box_controller import box_controller
app.register_blueprint(box_controller)

from app.Api.api_controller import api_controller
app.register_blueprint(api_controller)