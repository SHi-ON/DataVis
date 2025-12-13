from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import linear_model as lm

sns.set_theme(style="whitegrid")

BASE_DIR = Path(__file__).resolve().parent.parent
FIGURES_DIR = BASE_DIR / "figures"
IRIS_RELATIONSHIP_FIG = FIGURES_DIR / "iris_relationships.png"


def load_iris() -> pd.DataFrame:
    return sns.load_dataset("iris")


def fit_regression(df: pd.DataFrame) -> lm.LinearRegression:
    """Fit a simple model predicting sepal width from petal length."""
    model = lm.LinearRegression()
    X = df[["petal_length"]]
    y = df["sepal_width"]
    model.fit(X, y)
    return model


def plot_iris(df: pd.DataFrame, model: lm.LinearRegression) -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Relationship: petal length vs sepal width with regression line
    sns.regplot(data=df, x="petal_length", y="sepal_width", ax=axes[0], line_kws={"color": "orange"})
    axes[0].set_title("Sepal Width vs Petal Length")
    axes[0].set_xlabel("Petal length (cm)")
    axes[0].set_ylabel("Sepal width (cm)")

    # Distribution of petal length by species
    sns.boxplot(data=df, x="species", y="petal_length", ax=axes[1])
    axes[1].set_title("Petal Length by Species")
    axes[1].set_xlabel("Species")
    axes[1].set_ylabel("Petal length (cm)")

    fig.tight_layout()
    fig.savefig(IRIS_RELATIONSHIP_FIG, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return IRIS_RELATIONSHIP_FIG


def main(show: bool = False) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    df = load_iris()
    model = fit_regression(df)
    plot_iris(df, model)
    if show:
        plt.show()


if __name__ == "__main__":
    main()
