
## Set up a folder with 2 repos
##### /Main
https://github.com/DeliSauce/Git-Commit-Script/commits/main/
- Run the script in the Main folder:
```console
user:~$ python git_date_commmit_script.py]
```

##### /Dummy
https://github.com/DeliSauce/Dummy-Commit-Log/commits/main/
- Contains the file that is committed.

## Commit with specific date
GIT_COMMITTER_DATE="Tue 28 Jan 2025 10:19:19 BST" git commit --date "Tue 28 Jan 2025 10:19:19 BST"

## Amend commit with specific date
GIT_COMMITTER_DATE="Mon 27 Jan 2025 10:19:19 BST" git commit --amend --no-edit --date "Mon 27 Jan 2025 10:19:19 BST"