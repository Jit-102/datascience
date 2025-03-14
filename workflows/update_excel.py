import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
import os

# Path to the Excel file inside the repo
excel_path = "metrics/dora_metrics.xlsx"

# Load the existing Excel file
wb = load_workbook(excel_path)
ws = wb.active

# Get environment variables from GitHub Actions
repo_name = os.getenv("GITHUB_REPOSITORY", "Unknown Repo")
lead_time = os.getenv("LEAD_TIME", "0")

# Add a new row with DORA metrics
new_data = [
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
    repo_name,  # Repository Name
    "Success",  # Deployment Status
    lead_time,  # Lead Time
    "5%",  # Example Failure Rate
    "10"   # Example MTTR
]

ws.append(new_data)
wb.save(excel_path)

print("✅ Excel file updated successfully!")
