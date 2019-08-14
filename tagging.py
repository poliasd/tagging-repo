import sys
import git
from datetime import datetime

repo = git.Repo(".")

branch_name = repo.active_branch.name
current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Accepts as a parameter the name of the tag and creates the tag if it doesn't exist.
def tag_repo(tag_name):
    try:
        tag = repo.create_tag(tag_name)
        repo.remotes.origin.push(tag)
    except git.GitCommandError:
        print('Tag "{}" already exists'.format(tag_name))
    else:
        print('Tag "{}" added.'.format(tag_name))

tag_repo(current_time)

if branch_name != "master":
    tag_repo(branch_name)

if len(sys.argv) > 1:
    tag_repo(sys.argv[1])