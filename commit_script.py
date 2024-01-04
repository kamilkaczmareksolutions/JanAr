import subprocess
import datetime
import time

def commit_and_push():
    # Use the path where the repo is copied in the Docker container
    repo_dir = '/app'
    subprocess.call(['git', '-C', repo_dir, 'commit', '--allow-empty', '-m', f'Empty commit on {datetime.datetime.now()}'])
    subprocess.call(['git', '-C', repo_dir, 'push'])

if __name__ == "__main__":
    while True:
        commit_and_push()
        print("Commit done. Next commit in 24 hours.")
        time.sleep(300)  # Sleep for 24 hours (86400)