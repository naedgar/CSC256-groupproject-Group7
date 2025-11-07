# GitHub & Git Workflow Guide

## 1. GitHub Fundamentals

**Git is a distributed Version Control System (VCS) that helps track changes as you work on new software development projects.** Git tracks the changes you make so you always have a record of what you’ve worked on and you can easily revert back to an older version of your code if need be. It also makes working with others easier—groups of people can work together on the same project and merge their changes into one final source! 

## 2. 💻 GitHub features 

### Repositories 

A repository is where your project work happens. It contains all of your project’s files and revision history. You can work within a repository alone or invite others to collaborate with you on those files. As you work more on GitHub you will have many repositories. Use your GitHub dashboard to easily navigate to them. 

Repositories also contain README’s. You can add a README file to your repository to tell other people why your project is useful, what they can do with your project, and how they can use it. We are using this README to communicate how to learn Git and GitHub with you. :smile: 

Read more about repositories [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories) and repository README’s [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes). 

### Pull requests

Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add more changes if need be. 

Adding someone as a reviewer on your pull request is a signal to them that you want help or would like them to review the content. 

Read more about pull requests [here](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). 

### Issues

Use issues to track enhancements, tasks, or bugs for your work on GitHub. Issues are a great way to keep track of all the tasks you want to work on for your project and let others know what you plan to work on. For larger projects, you can keep track of many issues on a project board. GitHub Projects help you organize and prioritize your work and you can read more about them [here](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards). 

Pull requests and issues can also be linked together! You can link a pull request to an issue to show that a fix is in progress and to automatically close the issue when someone merges the pull request. 

Read more about issues and linking them to your pull requests [here](https://docs.github.com/en/github/managing-your-work-on-github/about-issues). 

### Using markdown on GitHub 

You can minimally style your issues, pull requests, and files (as long as they are .md format!). Using Markdown in your issues, pull requests, and files helps organize your information and make it easier for others to read. You can also drop in gifs and images to convey your point!

Read more about using GitHub’s flavor of markdown [here](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax). 

## 3. Understanding the GitHub flow 

The GitHub flow is a lightweight workflow that allows you to experiment with new ideas safely, without fear of compromising a project.

### Branching 

You can use branches on GitHub to isolate work that you do not want merged into your final project. Branches allow you to develop features, fix bugs, or safely experiment with new ideas in a contained area of your repository. You always create a branch from an existing branch. Typically, you might create a new branch from the default branch of your repository—`main`. 

Once your new changes have been reviewed by a teammate, or you are satisfied with them, you can merge your changes into the default branch of your repository.

Read more about branching [here](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches). 

### Cloning and forking 

When you create a repository it exists remotely outside of your local machine. You can clone a repository to create a local copy on your computer and then use Git to sync the two. 

You can clone a repository from GitHub to your local computer to make it easier to fix issues, add or remove files, and push larger commits. You can also use an IDE or editing tool of your choice as opposed to the GitHub UI. When you clone a repository, you copy the repository from GitHub to your local machine.

Cloning a repository pulls down a full copy of all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project.

A fork is another way to copy a repository, but is most commonly used when contributing to someone else’s project. Forking a repository allows you to freely experiment with changes without affecting the original project and is very popular when contributing to open source software projects.

This guide explains how to **stage**, **commit**, **push**, **Pull Request** and **Merge** for collaboration using GitHub. It includes steps for both **GitHub Desktop** and **Command Line** workflows, with CI considerations.

## 4. 🔁 Core Concepts

| Step                         | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| 🌿 **Create Branch**         | Start a new feature/fix branch from `main`                   |
| 🔧 **Make Code/Doc Changes** | Modify code or documentation as needed                       |
| 💾 **Stage + Commit**        | Save snapshots of work (can do multiple commits before push) |
| ⬆️ **Push**                  | Send your commits to GitHub remote                           |
| 📋 **Pull Request**          | Open PR with clear description on GitHub Remote              |
| 🔍 **Review + CI**           | Wait for test results and team approval                      |
| 🔀 **Merge**                 | Merge PR into `main`                                         |
| 🔄 **Update Local `main`**   | Pull latest changes locally after merge                      |

In Git/GitHub, **you cannot partially merge only "successful parts" of a commit or PR**—Git operates on a **commit-by-commit** or **file-by-file** basis, not on "which parts of code passed tests." However, here are realistic, professional **strategies you can follow** in your scenario:

## 5. How these fit together

Your Project Lab will contain instructions for each required `branch` telling you which Workflow to use.

- **Workflow A (Direct to `main`)**: Only for early setup (Week 1–2).  
- **Workflow B (Feature Branch → PR)**: Standard teamwork flow (Weeks 2–3).  
- **Workflow C (Feature Branch → PR → CI checks → Merge)**: **Required from Week 3 onward**.
 [!NOTE] Your Project Labs do not require you to do multiple `commits` but it is a good habit to get into.  The Project Labs **DO** require multiple `branch` ***stage, commit, push, Pull Request and Merge***.
---

### Workflow A — Commit directly to `main` (early setup only)

**Use when:** Initial scaffolding files only (e.g., `.gitignore`, `requirements.txt`, project skeleton). Not for features or tests.

#### Steps (GitHub Desktop)
1. Open your cloned repo in **GitHub Desktop**.
2. Make your changes in your editor (setup files only).
3. In Desktop, select changed files → write a short commit message → **Commit to main**.
4. Click **Push origin**.

#### Steps (GitHub.com)
1. Open the file in the repo → **Edit**.
2. Make small changes → write a commit message → **Commit directly to main**.

**Why:** Fast bootstrap. After setup, switch to B/C.

---

### Workflow B — Feature branch → Pull Request → Merge → Sync(standard teamwork)

**Use when:** Building features/tests/docs that don’t yet require CI to pass (earlier sprints or exploratory work).

#### Steps (GitHub Desktop)
1. **Create a branch**  
   - Top bar → **Current Branch** → **New Branch…**  
   - Name it: `feature/US###-short-title` (e.g., `feature/US002-add-task-api`)
2. **Make changes** in your editor (code, tests, docs).
3. **Stage & Commit**  
   - Desktop → select files → meaningful message → **Commit to branch**.  
   - Repeat small, logical commits.
4. **Publish branch** (first time only) → **Push origin**.
5. **Open PR**  
   - Desktop shows a banner → **Create Pull Request** (opens GitHub), or go to GitHub → **Pull requests → New**.  
   - Base = `main`, Compare = your branch.  
   - Title + Description (what/why).  
   - **Request a review** (for the Individual Project that would be you).
6. **Merge** after review.
7. **Sync**  
   - Switch to `main` in Desktop → **Fetch origin** → **Pull origin**.

#### Steps (GitHub or Git CLI)

1. **Create a Branch**

   ```bash
   git checkout -b feature/US###-short-title
   ```

   Example:

   ```bash
   git checkout -b feature/US002-add-task-api
   ```

2. **Make Changes** in your editor

   * Edit code, tests, or documentation as needed.

3. **Stage & Commit**

   ```bash
   git add .
   git commit -m "Meaningful commit message"
   ```

   *(Make small, logical commits — repeat as needed.)*

4. **Push the Branch** (first time only)

   ```bash
   git push -u origin feature/US###-short-title
   ```

   *(For later pushes, just use `git push`.)*

5. **Open a Pull Request (PR)**

   * From CLI:

     ```bash
     gh pr create --base main --head feature/US###-short-title --title "PR Title" --body "Description of changes"
     ```
   * Or from GitHub.com:

     * Go to **Pull requests → New pull request**
     * Base = `main`, Compare = your branch
     * Add a title + description (what/why)
     * **Request a review** from a teammate

6. **Merge After Review**

   * Once approved, merge via GitHub.com or CLI:

     ```bash
     gh pr merge <PR-number>
     ```

7. **Sync Your Local Main Branch**

   ```bash
   git checkout main
   git fetch origin
   git pull origin main
   ```
**Why:** Safe collaboration with review before changes hit `main`.

---

### Workflow C — Feature branch → PR → CI checks → Merge → Sync

**PRs must pass *CI* before merging.**

### Steps (GitHub Desktop)
1. **Create a branch**  
   - **Current Branch** → **New Branch…**  
   - Name: `feature/US###-short-title`
2. **Make changes** (write tests first if practicing TDD):
   - Unit/integration tests (pytest)
   - Acceptance tests (Robot Framework, where applicable)
3. **Stage & Commit**  
   - Desktop → select changed files → clear message → **Commit**.  
   - **Push origin** (or **Publish branch** then push).
4. **Open PR** (Desktop banner → Create Pull Request, or on GitHub):
   - Base = `main`, Compare = your feature branch
   - **PR description:** What changed, why, how tested  
     ```
     ## What’s new
     - Implemented POST /api/tasks with title validation
     - Added pytest for valid/invalid requests

     ## Why
     - Core CRUD endpoint for tasks

     ## Tests
     - Pytest: tests/api/test_tasks.py (green locally)
     - Robot: tests/robot/tasks.robot (added)
     ```
5. **Wait for CI**  
   - On PR → **Checks** tab or **Actions**  
   - CI must be green for: **pytest** (and **Robot** if present)  
   - Fix failures locally → commit → push → CI reruns automatically.
6. **Review & Merge**  
   - At least **1 approval** (for the Individual Project that would be you) + **All checks passing** → **Merge pull request**.
7. **Sync**  
   - Switch to `main` in Desktop → **Fetch origin** → **Pull origin**.

#### Steps (CLI)

1. **Create a Branch**

   ```bash
   git checkout -b feature/US###-short-title
   ```

   Example:

   ```bash
   git checkout -b feature/US002-add-task-api
   ```

2. **Make Changes** (write tests first if practicing TDD)

      * Unit/integration tests (pytest)
      * Acceptance tests (Robot Framework, if applicable)
      * Edit code, tests, or documentation as needed

3. **Stage & Commit**

      ```bash
      git add .
      git commit -m "Meaningful commit message"
      ```

      *(Make small, logical commits — repeat as needed.)*

4. **Push the Branch** (first time only)

   ```bash
   git push -u origin feature/US###-short-title
   ```

   *(For later pushes, just use `git push`.)*

5. **Open a Pull Request (PR)**

   * From CLI:

     ```bash
     gh pr create --base main --head feature/US###-short-title --title "PR Title" --body "## What’s new
     - Implemented POST /api/tasks with title validation
     - Added pytest for valid/invalid requests

     ## Why
     - Core CRUD endpoint for tasks

     ## Tests
     - Pytest: tests/api/test_tasks.py (green locally)
     - Robot: tests/robot/tasks.robot (added)"
     ```
6. **Wait for CI to Pass**

   * On the PR page → **Checks** tab or **Actions** tab
   * CI must be green for **pytest** (and **Robot Framework** if present)
   * If a check fails, fix locally → commit → push → CI reruns automatically

7. **Merge After Review** (for the Individual Project that would be you)

   * Once approved, merge via GitHub.com or CLI:

     ```bash
     gh pr merge <PR-number>
     ```

8. **Sync Your Local Main Branch**

   ```bash
   git checkout main
   git fetch origin
   git pull origin main
   ```

**Why:** Protects `main` with automated tests and review — this is the professional standard.

## 6. Quick reference (Desktop vs GitHub.com)

| Action                | GitHub Desktop                                       | GitHub CLI (Terminal)                                                                 |
|-----------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------|
| Create branch         | Current Branch → New Branch                           | `git checkout -b feature/US###-short-title`                                           |
| Stage & commit        | Changes tab → select files → Commit                   | `git add .` → `git commit -m "Meaningful commit message"`                             |
| Push                  | Push origin / Publish branch                          | `git push -u origin feature/US###-short-title` (first push) / `git push` (later)      |
| Open PR               | Desktop banner → Create PR (opens browser)            | `gh pr create --base main --head feature/US###-short-title --title "PR Title" --body "Description"` |
| See CI results        | PR → Checks (or Actions tab)                          | `gh pr view --web` (opens PR page in browser) or check Actions tab via `gh run list`  |
| Merge PR              | PR page → Merge after green checks + review           | `gh pr merge <PR-number>`                                                             |
| Sync main locally     | Switch to `main` → Fetch → Pull                       | `git checkout main` → `git fetch origin` → `git pull origin main`                     |

---

## 7. When to use which?

- **Workflow A**: Day 1–2 setup only.  
- **Workflow B**: Early sprints for non-CI items (or instructor says OK).  
- **Workflow C**: **From Week 3 onward** and for **Group Project** (required).

---

## 8. Branch naming, commit messages, and PRs

### Branch naming
- Use the required `branch` name in the Labs but if need to create more follow this convention:
   - `feature/US###-short-title`  
   e.g., `feature/US003-list-tasks`
   - `fix/bug-brief-fix`  
   - `chore/docs-update-readme`

### Commit messages
- One logical change per commit  
- Present-tense, short summary  
  `Add POST /api/tasks with title validation`

### PR titles & descriptions
- **Title:** short & clear  
- **Description:** what changed, why, tests, any notes  
- Reference issues: `Closes #12`

---
## 9. ✅ Git Workflow `Commits/PRs for Help` 

### How to Handle Unsuccessful Code While Others are Good

1. **Split Your Work Into Separate Commits**

* Ensure that the code that passes tests is in **one or more clean commits**, separate from the code that fails.
* Use `git add -p` or GitHub Desktop/VS Code to **stage only files or code chunks that are passing**.
* Commit these working changes separately.
* Additional Guidance `how_to_move_commit_new_branch.md`

2. **Open a PR With the Passing Commits Only**

* Push the branch containing **only passing commits** to GitHub.
* Open a PR to merge them into `main` or the target branch.
* ✅ This PR will **pass CI** and can be merged.

 3. **Handle the Failing Code in a Separate Branch**

* Create a new branch for the part that **doesn’t pass tests yet**.
* Push that branch and open a **separate PR** for collaboration and review.
* **Link an issue** to this PR and explain what's broken or needs help.
* See `how_to_move_commit_new_branch.md`
---

### 🛠 Example Workflow

```bash
git checkout -b split-working-code
# Stage only passing files
git add src/utils.py tests/test_utils.py
git commit -m "Add tested utility functions"

# Create PR #1 → ✅ Fully tested, can be merged

git checkout -b partial-broken-feature
# Stage the untested or broken feature
git add src/feature_incomplete.py
git commit -m "WIP: Partial implementation of feature X (needs help)"

# Create PR #2 → ❌ Test failing, but useful for team to review and fix
# Link it to GitHub Issue #123
```