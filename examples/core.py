# Selected original functions; Makes 2024 Copyright. Original credits retained.
# Original source: projects/Forecasting_v1/linear_machine/random_forest.py
# Extracted for a small, independent portfolio example in 2026.
import numpy as np

def prepare_data(data, window_size, horizon):
    """Function to prepare data for time-series prediction"""
    X, y = list(), list()
    start = 0
    for _ in range(len(data)):
        end = start + window_size
        if end + horizon <= len(data):
            X.append(data[start:end])
            y.append(data[end:end+horizon])
        start += 1
    return np.array(X), np.array(y)
