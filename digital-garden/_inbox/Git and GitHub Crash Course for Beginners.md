YouTube Link: [Git & GitHub Crash Course for Beginners [2026] - YouTube](https://www.youtube.com/watch?v=mAFoROnOfHs)

**who created git?**
Git was created by Linus Torvalds

**local vs remote**
local = your computer
remote = online repo (typically GitHub)

**local git workflow**
directory > staging (stage) > local repo (commit)

**what is the staging stage?**
marking files ready for next steps (committing)

#Question **what is the purpose of staging? what happens if we skip staging?**

#### **what is a repository?**
a repository is a place where all the versions of your files and their complete change history are stored 

**local repository** = inside working directory
**remote repository** = github

**how to show git version / confirm git is installed**
```
git --version
```

**downloading a remote repository from github**
```
git clone <github-link>
```

`git status` = checks what exactly changed in the files


# staging
**staging/unstaging**
- `git add` - stage files
	- `git add --all` / `git add -A` - stage every change across the project; no difference about the two commands
	- `git add .` - stage every change under the current directory (and everything inside it) only
	- `git add *` - stage only new or modified files, not deleted files
	- `git add <file/folder>` - stage only specific file/folder
- `git reset` - unstage files
	- note: a normal reset does not bring back deleted files
	- `git reset -- hard` - brings back deleted files

# commit
**committing** - saving from staging to local repository

#### **how to commit changes to local repo**
```
git commit -m "message" 
```

#### **how to undo last commit**
```
git reset HEAD~
```

**git rm - delete a file and stage the change**
```
git rm <file>
```

note: if a file has uncommitted changes, `git rm` returns an error

**to force deletion of uncommitted files:**
```
git rm -f <file>
```

note: `-f` means *force removal*

**to remove file from staging area (keeps file on working directory)**
```
git rm --cached <file
```

**removes a folder and subsequent folders inside**
```
git rm -r <folder>
```
note: 
- `-r` means recursive
- if `-r` tag is removed, only the particular folder is removed, not its contents

**how to view commit logs**
```
# show logs
git log

# compact version
git log --oneline
```

# branching & merging

merge = means combining two branches into one

**how to list all your branches
```
# list all branches
git branch

# create a new branch
git branch <branch_name>
```

**how to move to another branch** / **how to go back to previous commit**
```
moving to another branch
git checkout <branch_name>

# restoring previous commit
git checkout <commit_id>

# move to latest version on main
git checkout main
```

**how to merge branches**
```
# merge changes from main to development
git checkout development
git merge main -m "message"

# merge changes from development to main
git checkout main
git merge development -m "message"
```

**how to compare commits**
```
git diff <commit id 1> <commit id 2>
```
note: to exit the log view, press the `Q` button

# remote
**push** = sending local changes to remote
**fetch** = bringing remote changes to local repository, but not merging them yet (updates don't reflect on working directory)
**pull** = fetching and merging remote changes to your current working directory

basically, *pull = fetch + merge*

**how to push to remote repository**
```
# pushing main branch to remote repo
git push origin main

# push other branch
git checkout development
git push origin development
```
note:
- origin - refers to the remote repository
- main - refers to the primary branch


# restore
**git restore - used to discard local changes**
**how to go back to previous committed state**
```
# quickly undo local uncommitted stages
git restore

# restore a specific file directory
git restore <directory>

# restore entire repository
git restore .

# restore staging
git restore --staged <filename/directory>
git restore --staged .
```
# stash
**git stash - temporarily set aside unfinished/uncommitted work and switch to another branch**
This is used when you want to save but not ready to commit.

#### stashing uncommitted changes
```
# from main; stash uncommitted changes and switch branch
git stash
git checkout development

# go back to main branch and restore stashed changes
git checkout main
git stash pop
```
note: 
- you can stash multiple times (creates stash 1, stash 2, ...)
- git stash pop brings back the most recent stash (can also be used as many times as existing stash)

#### listing, removing and restoring stashed changes
```
# see stash list
git stash list

# removes a stashed change
git stash drop
git stash drop stash@{0}

# restores stashed change to working directory and drops it from stash list
git stash pop stash@{0}

# only restores stashed change to working directory, but keeps the stash in the stash list
git stash apply stash@{0}
```

# revert
reset - takes you back to specific commit and discards all existing commit after that point.
revert - removes the effects of previous commit **by creating a new commit**; this means fixing a commit mistake without removing the faulty commit or overwriting the history

```
git log --online

git revert <commit-id>
```

note:
- after running the command, you'll see a prompt asking for a commit message, you can write a commit message 
- exit by pressing `WQ` (write and quit)


# rebase

situation: you work on a feature on a feature branch, meanwhile, there's an update on main branch
task: you want to bring updates from main branch to the feature branch

before rebase:
![](https://i.imgur.com/Ah0vbbr.png)

after rebase:
![](https://i.imgur.com/urSzlqr.png)

```
# always start rebasing on the branch you want to merge into
git checkout feature

# rebase command
git rebase main
```

what happens in the backend:
![](https://i.imgur.com/VMTNtxM.png)

note: 
- **do not** use git rebase on publish repositories (reason: rebase rewrites commit history; changing commit ids)


# pull request

**pull request** is a request you make to merge your changes to another branch

a pull request basically says: "I've made some changes in my branch; please review them, and if everything looks good, merge them into the main branch"




