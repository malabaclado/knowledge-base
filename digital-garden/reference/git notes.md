---
title: git
---
# Related notes
- [[Git is a version control system]]
- [[Git and GitHub Crash Course for Beginners]]

> [!info]
> The sections are arranged in order of recently added.

# Useful Aliases

Add these to your `~/.gitconfig` under `[alias]`:

```
[alias]
    s = status -sb
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate --all
    last = log -1 HEAD --stat
    unstage = restore --staged
    undo = reset --soft HEAD~1
    amend = commit --amend --no-edit
    wip = !git add -A && git commit -m 'WIP'
    pushf = push --force-with-lease
    prune-merged = !git branch --merged | grep -v main | xargs git branch -d
```

To edit the config file, use the command:
```
git config --global --edit
```

**How I set up an alias to quickly update my knowledge base**
```
git config --global alias.publish "!f() { git add -A && git commit -m \"\${1:-update}\" && git push; }; f"


-- to update my knowledge base
git publish
```


| Alias                | What it does                         |
| -------------------- | ------------------------------------ |
| `git s`              | Short status                         |
| `git lg`             | Pretty log graph                     |
| `git last`           | Show last commit                     |
| `git unstage <file>` | Unstage a file                       |
| `git undo`           | Undo last commit (keep changes)      |
| `git amend`          | Amend last commit silently           |
| `git wip`            | Quick work-in-progress commit        |
| `git pushf`          | Safe force push                      |
| `git prune-merged`   | Delete local branches already merged |
# Clean & Maintenance

|Command|Description|
|---|---|
|`git clean -fd`|Remove untracked files and directories|
|`git clean -fdn`|Dry run — show what would be deleted|
|`git gc`|Garbage collect (optimize repo)|
|`git fsck`|Check integrity|
|`git archive --format=zip HEAD -o repo.zip`|Export repo as zip|
# Diff & Inspect

|Command|Description|
|---|---|
|`git diff`|Unstaged changes|
|`git diff --staged`|Staged changes (about to commit)|
|`git diff <branch1>..<branch2>`|Diff between branches|
|`git diff HEAD~3..HEAD`|Changes in last 3 commits|
|`git diff --name-only`|List changed file names only|
|`git diff --stat`|Summary of changes|
|`git show <commit>`|Show a specific commit|
|`git show <commit>:<file>`|Show file at a specific commit|

# Remote Push & Pull

|Command|Description|
|---|---|
|`git remote -v`|Show remotes with URLs|
|`git remote add origin <url>`|Add a remote|
|`git remote set-url origin <url>`|Change remote URL|
|`git remote remove <name>`|Remove a remote|
|`git push`|Push current branch|
|`git push -u origin main`|Push + set upstream tracking|
|`git push --force-with-lease`|Force push (safe — checks for remote changes)|
|`git push --force`|Force push (**dangerous** — overwrites remote)|
|`git pull`|Fetch + merge|
|`git pull --rebase`|Fetch + rebase (cleaner)|
|`git fetch`|Download remote changes (don't merge)|
|`git fetch --all --prune`|Fetch all remotes + delete stale branches|
# Merge & Rebase

|Command|Description|
|---|---|
|`git merge <branch>`|Merge branch into current branch|
|`git merge --no-ff <branch>`|Merge with a merge commit (no fast-forward)|
|`git merge --squash <branch>`|Squash all commits into one before merging|
|`git merge --abort`|Abort a conflicted merge|
|`git rebase <branch>`|Rebase current branch onto another|
|`git rebase -i HEAD~3`|Interactive rebase last 3 commits|
|`git rebase --abort`|Abort a rebase|
|`git rebase --continue`|Continue after resolving conflicts|

Interactive rebase actions

|Action|What it does|
|---|---|
|`pick`|Keep the commit as-is|
|`reword`|Keep commit, edit message|
|`squash`|Merge into previous commit (keep message)|
|`fixup`|Merge into previous commit (discard message)|
|`drop`|Remove the commit|
|`edit`|Pause to amend the commit|

# Stash

| Command                           | Description                        |
| --------------------------------- | ---------------------------------- |
| `git stash`                       | Stash current changes              |
| `git stash push -m "description"` | Stash with a message               |
| `git stash list`                  | List all stashes                   |
| `git stash pop`                   | Apply last stash + remove it       |
| `git stash apply`                 | Apply last stash (keep it in list) |
| `git stash apply stash@{2}`       | Apply a specific stash             |
| `git stash drop stash@{0}`        | Delete a specific stash            |
| `git stash clear`                 | Delete all stashes                 |
| `git stash show -p`               | Show stash diff                    |
| `git stash push -u`               | Stash including untracked files    |

# Undo & Reset
| Command                        | Description                              |
| ------------------------------ | ---------------------------------------- |
| `git restore <file>`           | Discard changes in working directory     |
| `git restore --staged <file>`  | Unstage a file (keep changes)            |
| `git reset HEAD~1`             | Undo last commit (keep changes staged)   |
| `git reset --soft HEAD~1`      | Undo last commit (keep changes staged)   |
| `git reset --mixed HEAD~1`     | Undo last commit (keep changes unstaged) |
| `git reset --hard HEAD~1`      | Undo last commit (**discard changes**)   |
| `git reset --hard origin/main` | Reset to match remote exactly            |
| `git revert <commit>`          | Create a new commit that undoes a commit |
| `git checkout -- <file>`       | Discard changes (older syntax)           |

# Stage and Commit
|Command|Description|
|---|---|
|`git status`|Show working tree status|
|`git add <file>`|Stage a specific file|
|`git add .`|Stage all changes|
|`git add -p`|Stage interactively (hunk by hunk)|
|`git commit -m "message"`|Commit with message|
|`git commit -am "message"`|Stage tracked files + commit|
|`git commit --amend`|Edit last commit message|
|`git commit --amend --no-edit`|Add staged changes to last commit|
|`git commit --allow-empty -m "msg"`|Empty commit (trigger CI, etc.)|

# Branches

|Command|Description|
|---|---|
|`git branch`|List local branches|
|`git branch -a`|List all branches (local + remote)|
|`git branch <name>`|Create a new branch|
|`git checkout <name>`|Switch to branch|
|`git checkout -b <name>`|Create + switch in one step|
|`git switch <name>`|Switch to branch (modern)|
|`git switch -c <name>`|Create + switch (modern)|
|`git branch -d <name>`|Delete branch (safe — only if merged)|
|`git branch -D <name>`|Force delete branch|
|`git branch -m <old> <new>`|Rename branch|
|`git branch -M main`|Rename current branch to `main`|
|`git push origin --delete <name>`|Delete remote branch|
# Create & Clone

|Command|Description|
|---|---|
|`git init`|Initialize new repo in current directory|
|`git init my-project`|Initialize new repo in `my-project/`|
|`git clone <url>`|Clone a remote repo|
|`git clone <url> my-folder`|Clone into a specific folder|
|`git clone --depth 1 <url>`|Shallow clone (latest commit only)|
|`git clone --branch <name> <url>`|Clone a specific branch|

# Setup

|Command|Description|
|---|---|
|`git config --global user.name "Your Name"`|Set your name|
|`git config --global user.email "you@example.com"`|Set your email|
|`git config --global init.defaultBranch main`|Default branch = main|
|`git config --global core.autocrlf true`|Fix line endings (Windows)|
|`git config --global core.autocrlf input`|Fix line endings (macOS/Linux)|
|`git config --global pull.rebase true`|Rebase on pull (cleaner history)|
|`git config --global push.autoSetupRemote true`|Auto-track remote branches|
|`git config --list`|Show all config|
|`git config user.name`|Show a specific setting|


# External References
- [atryx/git-cheatsheet: Git commands cheat sheet — branches, merges, rebases, stashes, undos, and aliases every developer needs (2026)](https://github.com/atryx/git-cheatsheet)