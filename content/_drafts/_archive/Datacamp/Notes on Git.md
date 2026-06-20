![[git-transport.png]]

Initializing a repository
```
git init
```

Staging files to commit
```
git add
```

Committing files to local repository
```
git commit -m "your message"
```

View history of commits
```
git log
```

Reverting back to a commit
```
git checkout "hash"
```

List all branches
```
git branch
```

Creating and switching to a new branch
```
git branch "new branch name"
git checkout "new branch name"
```


Merge branches
```
git merge "branch name"
```

Viewing all remote repositories
```
git remove -v
```

Connecting to a remote (online) repository
```
git remote add origin "github link"
```

Saving to a remote repository
```
git push "repository name" "branch name"
```

Note: Use `git push -u "repository name" "branch name"` to set as default repository - so that you wont need to specify the repository and branch for future push.	