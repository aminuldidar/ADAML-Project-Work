import numpy as np


class Model:
    def __init__(self, model_params, model, scalers, centers=None,
                 train_mse_scores=None, train_q2_scores=None, train_r2_scores=None,
                 valid_mse_scores=None, valid_q2_scores=None, valid_r2_scores=None):
        self.model = model
        self.scalers = scalers

        self.train_metrics = [train_mse_scores if train_mse_scores is not None else [],
                              train_q2_scores if train_q2_scores is not None else [],
                              train_r2_scores if train_r2_scores is not None else []]
        self.valid_metrics = [valid_mse_scores if valid_mse_scores is not None else [],
                              valid_q2_scores if valid_q2_scores is not None else [],
                              valid_r2_scores if valid_r2_scores is not None else []]
        self.y_centers = centers if centers is not None else []

        self.window_size = model_params[0]
        self.num_components = model_params[1]
