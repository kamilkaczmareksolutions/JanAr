import subprocess
import datetime
import time
import os

def configure_git_credentials(token):
    # Configures Git to use a token for HTTPS authentication
    config_commands = [
        "git config --global credential.helper store",
        f"echo https://x-access-token:{token}@github.com > /root/.git-credentials"
    ]
    for cmd in config_commands:
        subprocess.call(cmd, shell=True)

def commit_and_push():
    repo_dir = '/app'

    # Perform the empty commit
    subprocess.call(['git', '-C', repo_dir, 'commit', '--allow-empty', '-m', f'Empty commit on {datetime.datetime.now()}'])
    
    # Push the commit
    subprocess.call(['git', '-C', repo_dir, 'push', 'origin', 'master'])

if __name__ == "__main__":
    token = os.environ.get('GITHUB_TOKEN')  # Retrieve the token from the environment variable
    configure_git_credentials(token)

    while True:
        commit_and_push()
        print("Commit done. Next commit in 24 hours.")
        time.sleep(300)  # Sleep for 24 hours (86400)