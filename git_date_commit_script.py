import subprocess
import os
from datetime import datetime, timedelta
import random

## DATE Formats accepted by github
github_working_date = "Tue 28 Jan 2025 15:19:19 BST"
git_internal_date = "1738183106.371134 EST"
iso8601_date = "2025-01-15T22:13:13"
rfc2822_date = "Fri, 24 Jan 2025 22:13:13 +0200"

# Create a copy of the current environment
env = os.environ.copy()

def git_add_and_commit(message, timestamp):
    timestamp = str(timestamp)
    try:
        # Modify the environment variables as needed
        env["GIT_COMMITTER_DATE"] = timestamp

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message, "--date", timestamp], check=True, env=env)
        print("Commit successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during commit: {e}")

def git_push():
    try:
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during push: {e}")

def is_weekday(datetime_obj):
    num = datetime_obj.weekday();
    return num < 5 

if __name__ == "__main__":
    yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y.%m.%d')
    start_date = input("Enter start date: (YYYY.MM.DD, default=yesterday)") or yesterday_date
    end_date = input("Enter end date: (YYYY.MM.DD, default=yesterday)") or yesterday_date
    weekday_min = input("Enter min commit for a weekday (default=3): ") or 3
    weekday_max = input("Enter max commit for a weekday (default=7): ") or 7
    weekend_min = input("Enter min commit for a weekend (default=0): ") or 0
    weekend_max = input("Enter max commit for a weekend (default=1): ") or 1

    start_date = datetime.strptime(start_date, "%Y.%m.%d")
    end_date = datetime.strptime(end_date, "%Y.%m.%d")
    current_date = start_date

    while (current_date <= end_date):
        num_commits = random.randint(weekday_min, weekday_max) if is_weekday(current_date) else random.randint(weekend_min, weekend_max)

        for i in range(0, num_commits):
            date = current_date + timedelta(hours=random.randint(0,23), minutes=random.randint(0,59), seconds=random.randint(0,59))
            timestamp = date.timestamp()
            text = date.isoformat() + "\n"
            file = open("dummy.txt", mode="a", encoding="utf-8")
            file.write(text)
            file.close()
            git_add_and_commit("This is a scripted commit on: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'), timestamp)

        current_date = current_date + timedelta(days=1)

    push_commits = input("Push all commits to origin? (y/n) ") or "y"
    if push_commits == "y":
        git_push()
    
    

