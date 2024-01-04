import subprocess
import datetime
import time
import os

def commit_and_push():
    repo_dir = '/app'
    token = os.environ.get('GITHUB_TOKEN')  # Retrieve the token from the environment variable

    # Configure the remote URL to include the personal access token for authentication
    subprocess.call(['git', '-C', repo_dir, 'config', '--local', 'http.extraHeader', f'Authorization: basic {token}'])
    
    # Perform the empty commit
    subprocess.call(['git', '-C', repo_dir, 'commit', '--allow-empty', '-m', f'Empty commit on {datetime.datetime.now()}'])
    
    # Push using the configured token for authorization
    subprocess.call(['git', '-C', repo_dir, 'push', 'origin', 'master'])

if __name__ == "__main__":
    while True:
        commit_and_push()
        print("Commit done. Next commit in 24 hours.")
        time.sleep(300)  # Sleep for 24 hours (86400)