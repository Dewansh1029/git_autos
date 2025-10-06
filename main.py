import subprocess

def run_command(command, show_output=True):
    """Run a shell command and optionally print its output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if show_output:
        if result.returncode == 0:
            print(result.stdout.strip())
        else:
            print(f"❌ Error running command: {command}\n{result.stderr}")
    return result.returncode

def git_auto_branch(branch_name: str, commit_message: str):
    """Automate creating a branch, committing, and pushing."""

    print("🔍 Checking current status...")
    run_command("git status")

    print(f"\n🌿 Creating and switching to branch '{branch_name}'...")
    if run_command(f"git checkout -b {branch_name}") != 0:
        print(f"⚠️ Branch '{branch_name}' may already exist. Switching instead...")
        run_command(f"git checkout {branch_name}")

    print("\n🟢 Adding all changes...")
    run_command("git add .")

    print("\n🟡 Committing changes...")
    commit_exit = run_command(f'git commit -m "{commit_message}"')
    if commit_exit != 0:
        print("⚠️ No changes to commit. Skipping commit step.")

    print(f"\n🚀 Pushing branch '{branch_name}' to remote...")
    run_command(f"git push -u origin {branch_name}")

    print("\n✅ All steps completed successfully!")#

if __name__ == "__main__":
    # Ask for user input in terminal
    branch_name = input("Enter branch name: ").strip()
    commit_message = input("Enter commit message: ").strip()

    git_auto_branch(branch_name, commit_message)#er
