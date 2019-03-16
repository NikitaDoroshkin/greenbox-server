from app.Models.sensors_data import SensorsData


class Optimizer:
    optimal_model = SensorsData(1, 2, 3, 4)

    def optimize(self, model):
        return self.optimal_model
