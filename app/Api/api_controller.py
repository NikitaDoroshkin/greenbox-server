from flask import Blueprint, request, jsonify

from app.DAL import repository

api_controller = Blueprint('api_controller', __name__)


@api_controller.route('/get_state', methods=['GET'])
def synchronize_sensors():
    from_arg = request.args.get('from')
    to_arg = request.args.get('to')

    data = repository.get((from_arg, to_arg))

    return jsonify(vars(data))
