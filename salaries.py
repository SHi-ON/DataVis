from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

DATA_DIR = Path("data")
FIGURES_DIR = Path("figures")
PDF_PATH = DATA_DIR / "usnh_salary_book_2018.pdf"
EXTRACTED_CSV = DATA_DIR / "usnh_salary_book_2018_extracted.csv"
JOB_TITLE_FIG = FIGURES_DIR / "usnh_job_title_distribution.png"
PROFESSOR_SALARY_FIG = FIGURES_DIR / "usnh_top_professor_salaries.png"


def extract_data() -> pd.DataFrame:
    """Extract the PDF into CSV. Requires Java and tabula-py."""
    from tabula import read_pdf  # Imported lazily; only needed when refreshing from PDF.

    columns = ["Campus", "Name", "Job Title", "FTE", "Annual Base Pay"]
    df = read_pdf(
        PDF_PATH,
        pages="all",
        pandas_options={"header": None},
    )
    df.columns = columns
    df.to_csv(EXTRACTED_CSV, index=False)
    return df


def load_salaries(from_pdf: bool = False) -> pd.DataFrame:
    df = extract_data() if from_pdf else pd.read_csv(EXTRACTED_CSV)
    df["Annual Base Pay"] = (
        df["Annual Base Pay"].astype(str).str.replace(r"[^0-9.]", "", regex=True).astype(float)
    )
    return df


def plot_job_titles(df: pd.DataFrame) -> Path:
    counts = df["Job Title"].value_counts().head(10).sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))
    counts.plot(kind="barh", ax=ax, color="#4C72B0")
    ax.set_title("Top 10 Job Titles by Count (USNH 2018)")
    ax.set_xlabel("Number of employees")
    ax.set_ylabel("Job title")
    fig.tight_layout()
    fig.savefig(JOB_TITLE_FIG, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return JOB_TITLE_FIG


def plot_professor_salaries(df: pd.DataFrame) -> Path:
    prof_df = df[df["Job Title"].str.contains("professor", case=False, na=False)]
    top_prof = prof_df.nlargest(15, "Annual Base Pay").sort_values("Annual Base Pay")

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(data=top_prof, x="Annual Base Pay", y="Name", ax=ax)
    ax.set_title("Top 15 Professor Salaries (USNH 2018)")
    ax.set_xlabel("Annual base pay (USD)")
    ax.set_ylabel("Name")
    fig.tight_layout()
    fig.savefig(PROFESSOR_SALARY_FIG, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return PROFESSOR_SALARY_FIG


def main(show: bool = False, refresh_from_pdf: bool = False) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    df = load_salaries(from_pdf=refresh_from_pdf)
    plot_job_titles(df)
    plot_professor_salaries(df)
    if show:
        plt.show()


if __name__ == "__main__":
    main()
