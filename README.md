# DataVis

Small collection of quick visualization scripts for a few datasets (FIFA time series, US PhD degrees, iris, and a UNH salary snapshot). Generated plots land in `figures/`.

## Setup
- Python 3.10+ and [uv](https://docs.astral.sh/uv/)
- Install env: `uv sync`

## Generate figures
- FIFA time series: `uv run python hello.py`
- US PhD degrees: `uv run python phd_degrees_usa.py`
- Iris relationships: `uv run python playground.py`
- UNH salary plots (uses extracted CSV; add `--refresh-from-pdf` to re-extract): `uv run python salaries.py`

Data files live under `data/`; outputs go to `figures/`.
