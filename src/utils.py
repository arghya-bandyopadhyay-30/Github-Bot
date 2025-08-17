import json
from datetime import datetime, timedelta
from pathlib import Path
import random
from git import Repo
import uuid

REPO_PATH = Path(__file__).resolve().parent.parent
FILE_PATH = REPO_PATH / 'data.json'
END_DATE = datetime.now()
repo = Repo(REPO_PATH)
COMMIT_MESSAGE = """Updated data.json with timestamp: {formatted_date}"""


def generate_random_dates(start, end, num_dates):
    random_dates = set()
    days_difference = (end - start).days

    while len(random_dates) < num_dates:
        random_day_offset = random.randint(0, days_difference)
        random_date = start + timedelta(days=random_day_offset)
        random_dates.add(random_date)

    return list(random_dates)


def write_json(date):
    data_to_write = {
        "date": date,
        "uuid": str(uuid.uuid4())  # To ensure Git sees content change
    }

    with open(FILE_PATH, 'w') as json_file:
        json.dump(data_to_write, json_file, indent=2)
        print(f"Data successfully written for date: {date}")
