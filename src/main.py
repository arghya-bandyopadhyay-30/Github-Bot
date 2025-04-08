from src.utils import START_DATE, END_DATE, NUM_COMMITS, FILE_PATH, repo, COMMIT_MESSAGE, write_json, generate_random_dates

def commit_and_push_for_date(date):
    formatted_date = date.isoformat()
    write_json(formatted_date)

    repo.index.add([str(FILE_PATH)])
    repo.index.commit(COMMIT_MESSAGE.format(formatted_date=formatted_date), author_date=formatted_date, commit_date=formatted_date)
    print(f"Changes committed with custom date: {formatted_date}")

    origin = repo.remote(name='origin')
    try:
        origin.push(refspec='main')
        print("Changes pushed to the remote repository.")
    except Exception as e:
        print(f"Error pushing to the remote repository: {e}")

def main():
    commit_dates = generate_random_dates(START_DATE, END_DATE, NUM_COMMITS)

    for date in commit_dates:
        try:
            commit_and_push_for_date(date)
        except Exception as e:
            print(f"Error committing for date {date}: {e}")

if __name__ == "__main__":
    main()
    print("All randomly selected dates have been processed and pushed.")