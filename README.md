# Data Ingestion Pipeline (Python)

## 📌 Project Overview

This project demonstrates a **basic but production-style data ingestion pipeline** built with Python. It focuses on ingesting raw data files, validating schema, handling missing values, and logging pipeline activity.

The goal of this project is to showcase **core data engineering concepts** such as data quality checks, reusable ingestion logic, and clean data preparation for downstream analytics or storage.

---

## 🎯 Objectives

* Ingest raw CSV or JSON data
* Validate required schema columns
* Handle missing and invalid values
* Log pipeline steps and errors
* Produce a clean, analysis-ready dataset

---

## 🗂️ Project Structure

```
data-ingestion/
│
├── data/
│   ├── raw/                # Raw input data
│   └── processed/          # Cleaned output data
│
├── scripts/
│   └── ingest.py           # Main ingestion script
│
├── venv/                   # Python virtual environment
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 📊 Dataset Description

The dataset simulates **social media engagement data** with the following columns:

| Column Name | Description                                     |
| ----------- | ----------------------------------------------- |
| date        | Date the post was published                     |
| platform    | Social media platform (e.g. Twitter, Instagram) |
| post_type   | Type of post (image, video, text)               |
| likes       | Number of likes                                 |
| shares      | Number of shares                                |
| comments    | Number of comments                              |
| views       | Number of views                                 |

---

## ⚙️ Technologies Used

* Python 3
* Pandas
* Logging module
* Virtual environments (venv)

---

## 🚀 How the Pipeline Works

1. Reads raw CSV or JSON files
2. Checks if the file exists
3. Validates required schema columns
4. Handles missing numeric values
5. Drops rows with missing critical fields
6. Converts date fields to proper datetime format
7. Logs each step of the ingestion process

---

## ▶️ How to Run the Project

### 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run ingestion script

```bash
python scripts/ingest.py
```

---

## 🧪 Example Output

```
INFO - Reading file: data/raw/social_media_data.csv
INFO - File loaded successfully with 1000 rows
INFO - Schema validation passed
INFO - Missing numeric values before: 27, after: 0
INFO - Data ingestion completed successfully
INFO - Final dataset shape: (987, 7)
```

---

## 📈 Skills Demonstrated

* Data ingestion (batch processing)
* Schema validation
* Data cleaning
* Logging and error handling
* Writing reusable Python functions
* Production-style project structure

---

## 🔮 Future Improvements

* API-based ingestion
* Database ingestion
* Scheduling with Airflow
* Writing unit tests
* Saving processed data to a data warehouse

---

## 👩🏽‍💻 Author

**Faith Mathenge**
Computer Science Student | Aspiring Data Engineer
Learning data engineering through hands-on projects

---

## 📬 Contact

Feel free to connect with me on LinkedIn and follow my learning journey.
