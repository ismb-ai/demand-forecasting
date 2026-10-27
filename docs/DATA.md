# Data contract

The minimal example accepts a one-dimensional, chronologically ordered numerical series, a positive window size and a positive horizon. Every feature window precedes its target block. With `N` observations, a complete window requires `window_size + horizon` observations. Insufficient history yields empty arrays in the recovered function.

Original forecasting scripts frequently expect a DataFrame called `training_data` with `sum_quant_item`; some also use a numeric `time_scale`. Aggregate to a regular interval, sort by time and explicitly decide how to treat missing intervals and stock-outs. Split chronologically before fitting preprocessing. No real sales data or forecast accuracy claims are included.
