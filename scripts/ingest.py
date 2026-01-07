import pandas as pd
import logging
from pathlib import Path

# -----------------------------
# Logging configuration
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Expected schema
# -----------------------------
REQUIRED_COLUMNS = {
    "date",
    "platform",
    "post_type",
    "likes",
    "shares",
    "comments",
    "views"
}

# -----------------------------
# File paths
# -----------------------------
RAW_DATA_PATH = Path("data/raw/social_media_data.csv")


# Ingestion function
# -----------------------------
def ingest_data(file_path: Path) -> pd.DataFrame:
    """
    Reads raw data from CSV or JSON, validates schema,
    handles missing values, and returns a clean DataFrame.
    """

    if not file_path.exists():
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"{file_path} does not exist")

    logging.info(f"Reading file: {file_path}")

    # Detect file type
    if file_path.suffix == ".csv":
        df = pd.read_csv(file_path)
    elif file_path.suffix == ".json":
        df = pd.read_json(file_path)
    else:
        logging.error("Unsupported file format")
        raise ValueError("Only CSV and JSON files are supported")

    logging.info(f"File loaded successfully with {len(df)} rows")

    # -----------------------------
    # Schema validation
    # -----------------------------
    actual_columns = set(df.columns)
    missing_columns = REQUIRED_COLUMNS - actual_columns

    if missing_columns:
        logging.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"Schema validation failed. Missing: {missing_columns}")

    logging.info("Schema validation passed")

    # -----------------------------
    # Handle missing values
    # -----------------------------
    numeric_columns = ["likes", "shares", "comments", "views"]

    missing_before = df[numeric_columns].isnull().sum().sum()

    df[numeric_columns] = df[numeric_columns].fillna(0)

    missing_after = df[numeric_columns].isnull().sum().sum()

    logging.info(
        f"Missing numeric values before: {missing_before}, after: {missing_after}"
    )

    # Drop rows with missing critical fields
    df = df.dropna(subset=["date", "platform", "post_type"])

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    logging.info("Missing values handled successfully")

    return df


# -----------------------------
# Script entry point
# -----------------------------
if __name__ == "__main__":
    clean_df = ingest_data(RAW_DATA_PATH)
    logging.info("Data ingestion completed successfully")
    logging.info(f"Final dataset shape: {clean_df.shape}")
