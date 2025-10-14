#!/usr/bin/env python3
import subprocess, os, datetime

def git_push(commit_msg="auto-update"):
    repo_path = os.path.expanduser("~/Firsty")
    try:
        os.chdir(repo_path)
        subprocess.run(["git", "add", "."], check=True)
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"{commit_msg} — {stamp}"
        subprocess.run(["git", "commit", "-m", msg], check=False)
        subprocess.run(["git", "push"], check=True)
        print("🚀  GitHub auto-push complete.")
    except Exception as e:
        print(f"⚠️  Auto-push failed: {e}")

if __name__ == "__main__":
    git_push()
