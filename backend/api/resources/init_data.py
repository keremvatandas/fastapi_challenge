import csv
import os
from datetime import datetime

from models import app, screenshot


def read_and_prepare_data():
    sample_apps_csv = f"{os.getcwd()}/resources/sample_apps.csv"
    sample_ss_csv = f"{os.getcwd()}/resources/sample_screeshots.csv"

    app_reader = csv.DictReader(open(sample_apps_csv))
    ss_reader = csv.DictReader(open(sample_ss_csv))

    appsObj = []
    for item in app_reader:
        appsObj.append(
            app.App(
                id=item["id"],
                name=item["name"],
                icon=item["icon"],
                created_at=datetime.strptime(item["created_at"], "%Y-%m-%d %H:%M:%S"),
            )
        )

    ssObj = []
    for item in ss_reader:
        ssObj.append(
            screenshot.Screenshot(
                id=item["id"],
                app_id=item["app_id"],
                file_name=item["file_name"],
                created_at=datetime.strptime(item["created_at"], "%Y-%m-%d %H:%M:%S"),
            )
        )

    return (appsObj, ssObj)
