# Scope and modelling notes

- Many original scripts assume an existing `training_data` object or a private local data path. They are historical experiments rather than standalone applications.
- Some neural scripts fit scalers before splitting. Fit preprocessing on training periods only before comparing forecasting accuracy.
- Check overlapping-window leakage and use a gap appropriate to the forecast horizon when validating temporal models.
- Benchmark against last-value and seasonal-naive forecasts. Historical results are not reproduced here and no performance improvement is claimed.
- The minimal example checks window/target alignment only. It does not validate any predictive model or business outcome.
- The `forecast_makes-main` project retains author metadata crediting Ricardo Costa; it is presented as related team work.
