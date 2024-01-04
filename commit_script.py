import subprocess
import datetime
import time
import os

def commit_and_push():
    repo_dir = '/app'
    token = os.environ.get('GITHUB_TOKEN')  # Retrieve the token from the environment variable

    # Configure the remote URL to include the personal access token for authentication
    remote_url_with_token = f'https://{token}:x-oauth-basic@github.com/kamilkaczmareksolutions/JanAr.git'
    subprocess.call(['git', '-C', repo_dir, 'remote', 'set-url', 'origin', remote_url_with_token])

    # Perform the empty commit and push
    subprocess.call(['git', '-C', repo_dir, 'commit', '--allow-empty', '-m', f'Empty commit on {datetime.datetime.now()}'])
    subprocess.call(['git', '-C', repo_dir, 'push', 'origin', 'master'])

if __name__ == "__main__":
    while True:
        commit_and_push()
        print("Commit done. Next commit in 24 hours.")
        time.sleep(300)  # Sleep for 24 hours (86400)