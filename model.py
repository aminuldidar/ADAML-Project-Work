import numpy as np


class Model:
    def __init__(self, model_params, model, scalers,
                 train_mse_scores, train_f1_scores, train_r2_scores,
                 valid_mse_scores, valid_f1_scores, valid_r2_scores):
        self.model = model
        self.scalers = scalers

        self.train_metrics = np.array([train_mse_scores, train_f1_scores, train_r2_scores])
        self.valid_metrics = np.array([valid_mse_scores, valid_f1_scores, valid_r2_scores])

        self.window_size = model_params[0]
        self.num_components = model_params[1]
