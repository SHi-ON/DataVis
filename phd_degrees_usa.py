from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_DIR = Path("data")
FIGURES_DIR = Path("figures")
PERCENT_FIGURE = FIGURES_DIR / "us_phd_percent_population.png"
MALE_TOTAL_FIGURE = FIGURES_DIR / "us_phd_male_degrees.png"

sns.set_theme(style="whitegrid")


def load_population() -> pd.DataFrame:
    population = pd.read_csv(DATA_DIR / "us_population.csv", dtype={"year": int, "population": int})
    # Represent each academic period as <start year>-<end year two digits>, e.g., 2018-19.
    population["period"] = population["year"].astype(str) + "-" + (population["year"] + 1).astype(str).str[-2:]
    return population


def load_degrees() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "us_phd_degrees.csv", dtype={"period": str, "male": int, "female": int})


def build_dataset() -> pd.DataFrame:
    population = load_population()
    degrees = load_degrees()

    merged = (
        population.merge(degrees, on="period", how="inner")
        .assign(
            percent_pop_male=lambda df: df["male"] / df["population"] * 100,
            percent_pop_female=lambda df: df["female"] / df["population"] * 100,
            start_year=lambda df: df["period"].str[:4].astype(int),
        )
        .sort_values("start_year")
        .drop(columns="start_year")
    )
    return merged


def plot_population_share(df: pd.DataFrame) -> Path:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(df["period"], df["percent_pop_male"], label="Male")
    ax.plot(df["period"], df["percent_pop_female"], label="Female")
    ax.set_title("US PhD Degrees as Share of Population")
    ax.set_xlabel("Period")
    ax.set_ylabel("Percent of population awarded PhDs")
    ax.legend()
    ax.grid(True)
    fig.autofmt_xdate(rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig(PERCENT_FIGURE, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return PERCENT_FIGURE


def plot_male_totals(df: pd.DataFrame) -> Path:
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.lineplot(data=df, x="period", y="male", ax=ax)
    ax.set_title("US PhD Degrees Awarded to Males")
    ax.set_xlabel("Period")
    ax.set_ylabel("Male degrees")
    ax.grid(True)
    fig.autofmt_xdate(rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig(MALE_TOTAL_FIGURE, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return MALE_TOTAL_FIGURE


def main(show: bool = False) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    dataset = build_dataset()
    plot_population_share(dataset)
    plot_male_totals(dataset)
    if show:
        plt.show()


if __name__ == "__main__":
    main()
