# Day 1 - Git Basics
**Date:** 1 July 2026 / 3 July 2026
**Topic:** Git, Version Control, Commit History, Working Directory, Staging Area, DVCS, git config, git diff

---

## What is Git?

> Git is a **distributed version control system**.

---

## 1) Local Version Control

Creating locally in the system. Creating (or) having the version control locally in the system is called **local version control**.

> Problem: Because when your PC is not working then you can't access the data, because it is in locally in your system. To overcome this we are having a **CVCS** (Centralized Version Control System).

---

## 2) CVCS (Centralized Version Control System)

- Here we will be having a centralized repository.
- Everyone gets a copy from it and uses it locally.

**Advantages:**
1. Others can see the commits done to the code.
2. All the project history will be in that server only.

```
                Central Server
               Project Repository
              /         |         \
        Developer A  Developer B  Developer C
```

> If server crashes, then all the data will be gone, unless there is a local copy.

---

## 3) DVCS (Distributed Version Control System)

Every developer has their own complete copy of the repository.

```
              Server Repository
             /        |        \
       Repository  Repository  Repository
           |            |           |
      Working copy  Working copy  Working copy
       Developer 1  Developer 2  Developer 3
```

**Advantages:**
1. **Offline work** — commits, branches, merge can be done in offline.
2. **Complete backup** — every developer has a complete repository.

---

## Commit History

All the commits that have been done to the repository. All are stored in an order in the server.

The commit history has:
1. Commit ID (Hash)
2. Author
3. Date & Time
4. Commit message

---

## Working Directory

The project folder that we are working in is called **working directory**.

---

## Git Repository

- `.git` folder stores the complete project history.
- `.git` folder is called **git repository**.

---

## To Create Git in Local Repository

```bash
1) git status           # check status
2) git init             # create empty git repository
```

> By default it gives `master`, but if we need `main` then:
> `git init -b main`

```
Project Directory : First Project
+------------------+---------------------------+
| Working Directory|  Local Repository (.git)  |
|                  |  +----------+----------+  |
|  FirstCode.txt   |  | Staging  | Commit   |  |
|                  |  |  Area    | History  |  |
+------------------+---------------------------+
```

---

## git config

```bash
git config --global --list
# It will give username and user email.
```

If we need to config name and email:
```bash
git config --global user.name "vishnu"
git config --global user.email "@gmail.com"
```

---

## Staging Area

We will place the files that are going to be committed. Only the files that are in the staging area are going to be committed.

```bash
# To add files into the staging area:
git add FirstCode.txt

# To add all files at once:
git add .

# To delete from git:
git rm --cached creds.txt
# After that we can delete in working directory
```

---

## To See All the Commit History

```bash
git log
```

---

## To Commit the Files That Are in Staging Area

```bash
git commit

# To pass message along with commit:
git commit -m "my first commit"

# To skip the staging area we can do something like:
git commit -a -m "my third commit"
# use "-a" — directly stages and commits
```

---

## git diff

To check the old one and new code changes. Shows the difference between two versions — before changing how it is and after changing how it is.

- If the file is in **working directory** and we need to check differences then use:
```bash
git diff
```

- If the file is in **staging area** then we need to use:
```bash
git diff --staged
```

---

## Remote Repository

Remote Repository means an online server like GitHub.

```bash
# To create a folder through Command Prompt:
mkdir git-course
```

---

## git remote add origin

```bash
git remote add origin https://github.com/vishnu
```

1. `git remote` — used to manage remote repositories.
2. `add` — telling to create a new remote repository.
3. `origin` — taking as alias for the URL, so that when we push, we will only use `git push origin main`, whose `origin` is our git URL `https://github.com/vishnu`.

**Complete meaning:** Connect my local repository to the GitHub repository.

---

## -u (set-upstream)

Telling to git that our local branch (main) to connect to remote branch (origin/main).

```bash
git push -u origin main
```

> By using `-u` we don't need to tell every time `git push origin main`. Instead we can use just `git push`.

---

## git log --pretty=oneline

Shows all the information in one line — commits and push.

```bash
git log --pretty=oneline
```

---

## git remote -v

It will give the origin names. Fetch and push.

```bash
git remote -v
```

---

## git push --tags

Push all tags to remote.

```bash
git push origin --tags    # push all tags to remote
git push origin v1.0      # push specific tag to remote
```

`git push -u origin main` will be used.

---

## git push -u origin main

Connects the local main branch to the remote origin/main. Also sets origin/main as the upstream, allowing future `git pull` and `git push` commands to work without specifying branch names.

---

## Git Branch

```bash
# To create a git branch:
git branch use                # git switch -b featured

# To know how many branches are there:
git branch

# To switch to different branches:
git switch main               # (branch name)

# To see all branches in remote also then:
git branch --all

# To switch into previous branch:
git branch-                   # git switch -

# To delete a branch:
git branch -d branchname
```

---

## To Push Branch from Local to Remote Repo

```bash
git push origin branchname
```

---

## Merge

```bash
git merge
# First go to main branch then:
git pull origin main
git merge feature
git push origin main
```

---

## Tagging

Tagging means — allowing future git push and git pull commands to work without specifying the branch names.

There are two types of tagging:
1. **Lightweight Tagging**
2. **Annotated Tagging**

For annotated use:

```bash
git tag -a v1.0 -m "1st release"
# to see the tags:
git tag 3 to see the tag under these
git show v1.0
```

---

## git tag

A **git tag** is a named reference that points to a specific commit (or) version.

> Commonly used to mark important milestones (e.g. v1.0, v2.0) so they can be easily identified and restored.

**Creating tag:**
```bash
git tag -a v1.0 -m "1st release"
```

**List all tags:**
```bash
git tag
```

**View a specific tag:**
```bash
git show v1.0
```
