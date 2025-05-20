import argparse
from datetime import datetime
from src.utils import (
    END_DATE,
    NUM_COMMITS,
    FILE_PATH,
    repo,
    COMMIT_MESSAGE,
    write_json,
    generate_random_dates
)

DEFAULT_START_DATE = datetime(2025, 1, 1)


def commit_and_push_for_date(date):
    formatted_date = date.isoformat()
    write_json(formatted_date)

    repo.index.add([str(FILE_PATH)])
    repo.index.commit(
        COMMIT_MESSAGE.format(formatted_date=formatted_date),
        author_date=formatted_date,
        commit_date=formatted_date
    )
    print(f"Changes committed with custom date: {formatted_date}")

    origin = repo.remote(name="origin")
    try:
        origin.push(refspec="main")
        print("Changes pushed to the remote repository.")
    except Exception as e:
        print(f"Error pushing to the remote repository: {e}")


def run(start_date: str = None):
    try:
        start = datetime.fromisoformat(start_date) if start_date else DEFAULT_START_DATE
        commit_dates = generate_random_dates(start, END_DATE, NUM_COMMITS)
        for date in commit_dates:
            commit_and_push_for_date(date)
    except Exception as e:
        print(f"Error during commit workflow: {e}")

    print("All selected dates have been processed and pushed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Git timestamp-based commit CLI")

    parser.add_argument(
        "--start-date",
        type=str,
        help="ISO start date (e.g., 2024-12-04) for generating random commits",
    )

    args = parser.parse_args()
    run(start_date=args.start_date)
