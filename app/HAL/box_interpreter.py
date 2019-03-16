from app.Models.sensors_data import SensorsData
from flask import jsonify

params_names = {
    "light" : "light",
    "soil_humidity" : "soil_humidity",
    "temperature" : "temperature",
    "air_humidity" : "air_humidity",
}

def model_from_data(raw_data):
    return SensorsData(light=raw_data[params_names["light"]],
                       soil_humidity=raw_data[params_names["soil_humidity"]],
                       temperature=raw_data[params_names["temperature"]],
                       air_humidity=raw_data[params_names["air_humidity"]])

def data_from_model(model):
    return jsonify(vars(model))
