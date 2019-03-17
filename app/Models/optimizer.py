from app.Models.control_data import ControlData

# Here will be our model to optimize plant growth
class Optimizer:
    optimal_model = ControlData(255, 255, 255, 63) #, "2019-03-17"

    def optimize(self, model):
        return self.optimal_model
