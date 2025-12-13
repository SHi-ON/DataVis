from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

DATA_DIR = Path("data")
FIGURES_DIR = Path("figures")
FIFA_FIGURE = FIGURES_DIR / "fifa_time_series.png"


def load_fifa() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "fifa.csv", index_col="Date", parse_dates=True)
    return df.sort_index()


def plot_fifa(df: pd.DataFrame) -> Path:
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, ax=ax)
    ax.set_title("FIFA Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    fig.savefig(FIFA_FIGURE, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return FIFA_FIGURE


def main(show: bool = False) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    df = load_fifa()
    plot_fifa(df)
    if show:
        plt.show()


if __name__ == "__main__":
    main()

