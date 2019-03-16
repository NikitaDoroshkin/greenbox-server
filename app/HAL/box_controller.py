from flask import Blueprint, request, abort
from app.HAL.box_interpreter import data_from_model, model_from_data
from app.DAL.repository import Repository
from app.Models.optimizer import Optimizer


box_controller = Blueprint('box_controller', __name__)
optimizer = Optimizer()
repository = Repository()

@box_controller.route('/synchronize_sensors', methods=['POST'])
def synchronize_sensors():
    content = request.get_json()

    model = model_from_data(content)
    repository.add(model)
    optimized_model = optimizer.optimize(model)

    return data_from_model(optimized_model)




