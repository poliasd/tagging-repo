import sys
from git import Repo
from datetime import datetime

repo = Repo(".")

branch_name = repo.active_branch.name

current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
date_tag = repo.create_tag(current_time)
repo.remotes.origin.push(date_tag)

if branch_name != "master":
    branch_tag = repo.create_tag(branch_name)
    repo.remotes.origin.push(branch_tag)

if len(sys.argv) > 1:
    param_tag = repo.create_tag(sys.argv[1])
    repo.remotes.origin.push(param_tag)