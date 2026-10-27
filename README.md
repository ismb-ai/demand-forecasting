# Demand forecasting & time-series experiments

Python experiments for demand forecasting and operational time series developed in the context of AI for business at **Makes**. The collection includes window construction, horizon selection, regression, SVR, random forests, ARIMA and recurrent neural networks.

| Area | Source to explore |
| --- | --- |
| Sliding windows and random-forest experiments | [Linear models](projects/Forecasting_v1/linear_machine/) |
| Statistical forecasting | [ARIMA experiments](projects/Forecasting_v1/ARIMA/) |
| LSTM, CNN and recurrent networks | [Neural experiments](projects/Forecasting_v1/machine_learning/) |
| Earlier forecasting application and notebooks | [John](projects/John/) |
| Operational preprocessing notebooks | [Notebook collection](projects/todos_os_cadernos/) |
| Related team source, credited to Ricardo Costa | [forecast_makes-main](projects/forecast_makes-main/) |

The runnable example demonstrates the original sliding-window transformation. It does not train a model or imply a measured forecasting improvement.

## Run the minimal example

The example uses **synthetic data only** and requires Python 3.10+ with NumPy and pandas. It exercises selected original functions without importing the large dashboard/training environments.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-demo.txt
python examples/demo.py
python -m unittest discover -s tests -v
python tools/check_sources.py
```

See [example output and validation](docs/VALIDATION.md). The full historical projects have separate dependencies and are not covered by this minimal environment. Recovered dependency files remain inside their project folders.

## Repository guide

- `projects/`: recovered applications and experiments, preserving their source structure.
- `examples/`: a small, independently executable demonstration using selected original functions.
- `tests/`: behavioural checks of that example.
- [Project index](docs/PROJECTS.md), [data contracts](docs/DATA.md), [modelling notes](docs/LIMITATIONS.md), [attribution](docs/ATTRIBUTION.md).
- [Complete source history](https://github.com/ismb-ai/makes-ai-archive): all historical versions and provenance.

**Status:** historical research and application code with a verified minimal example. Full dashboards and training pipelines have not been validated end to end; no production-readiness or predictive-performance claim is made.
