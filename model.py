import numpy as np


class Model:
    def __init__(self, model_params, model, scalers, centers=None,
                 train_mse_scores=None, train_q2_scores=None, train_r2_scores=None,
                 test_mse_scores=None, test_q2_scores=None, test_r2_scores=None):
        self.model = model
        self.scalers = scalers

        self.train_metrics = [train_mse_scores if train_mse_scores is not None else [],
                              train_q2_scores if train_q2_scores is not None else [],
                              train_r2_scores if train_r2_scores is not None else []]
        self.test_metrics = [test_mse_scores if test_mse_scores is not None else [],
                              test_q2_scores if test_q2_scores is not None else [],
                              test_r2_scores if test_r2_scores is not None else []]
        self.y_centers = centers if centers is not None else []

        self.window_size = model_params[0]
        self.num_components = model_params[1]
