
## Set up a folder with 2 repos
/Main
https://github.com/DeliSauce/Git-Commit-Script/commits/main/
/Dummy
https://github.com/DeliSauce/Dummy-Commit-Log/commits/main/

## Commit with specific date
GIT_COMMITTER_DATE="Tue 28 Jan 2025 10:19:19 BST" git commit --date "Tue 28 Jan 2025 10:19:19 BST"

## Amend commit with specific date
GIT_COMMITTER_DATE="Mon 27 Jan 2025 10:19:19 BST" git commit --amend --no-edit --date "Mon 27 Jan 2025 10:19:19 BST"