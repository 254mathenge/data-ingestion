import logging
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

import pandas as pd
import psycopg2


load_dotenv()

# -----------------------------
# Logging
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Config
# -----------------------------
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

TABLE_NAME = "posts"

STATE_FILE = Path("state/last_run_pg.txt")
OUTPUT_PATH = Path("data/processed/posts_from_postgres.csv")

# -----------------------------
# Helpers
# -----------------------------
def get_last_run_time() -> datetime:
    if not STATE_FILE.exists():
        return datetime.min

    with open(STATE_FILE, "r") as f:
        return datetime.fromisoformat(f.read().strip())


def save_last_run_time(timestamp: datetime):
    STATE_FILE.parent.mkdir(exist_ok=True)
    with open(STATE_FILE, "w") as f:
        f.write(timestamp.isoformat())

# -----------------------------
# Ingestion
# -----------------------------
def ingest_from_postgres():
    last_run_time = get_last_run_time()
    logging.info(f"Last ingestion time: {last_run_time}")

    conn = psycopg2.connect(**DB_CONFIG)

    query = f"""
        SELECT *
        FROM {TABLE_NAME}
        WHERE updated_at > %s
        ORDER BY updated_at;
    """

    df = pd.read_sql(query, conn, params=(last_run_time,))
    conn.close()

    if df.empty:
        logging.info("No new records found")
        return

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    max_timestamp = df["updated_at"].max()
    save_last_run_time(max_timestamp)

    logging.info(f"Ingested {len(df)} rows from PostgreSQL")
    logging.info(f"Data saved to {OUTPUT_PATH}")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    ingest_from_postgres()
