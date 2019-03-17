from app.Models.sensors_data import SensorsData

# Here will be our model to optimize plant growth
class Optimizer:
    optimal_model = SensorsData(1, 2, 3, 4, "2019-03-17")

    def optimize(self, model):
        return self.optimal_model
