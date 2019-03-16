from flask import Flask
app = Flask(__name__)

from app.HAL.box_controller import box_controller
app.register_blueprint(box_controller)