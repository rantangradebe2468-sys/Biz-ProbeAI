# data.py

import csv
import os

business_data = {}

# Get correct file path
file_path = os.path.join(os.path.dirname(__file__), "data.csv")

try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            business_type = row["business_type"]

            business_data[business_type] = {
                "keywords": row["keywords"].split(","),
                "demand": float(row["demand"]),
                "competition": float(row["competition"])
            }

except Exception as e:
    print("Error loading data.csv:", e)