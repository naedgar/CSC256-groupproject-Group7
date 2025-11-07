# Common Instructions in Labs

This is provided so that Project Sprint Labs can be streamlined with only the primary uniqueness of that respective lab.  Most labs have common instructions and rather than put in each lab this document is referenced for you to review for additional instructions

## **Before You Start...**

### Make sure you’re ready to hit the ground running! 
* ✅ Know how to **use GitHub Issues and Projects** to keep track of your sprint work.
* ✅ Be comfortable using **GitHub Flow**, including:
  * Creating branches
  * Making and committing changes
  * Opening a pull request (PR)
  * Merging your work after review

### Before Starting the Project Lab

>[!IMPORTANT] **ALWAYS BE IN A WORKING BRANCH** and *NEVER* the `main` branch.  The only time `main` sees your code is after a *Pull Request and  Merge Confirm* OR after your local `main` has been updated with a `Fetch Origin`. Thats it!!!

1. Make sure your local repository `main` has been **updated** and reflects the `PR's` and `Merges` you did in the previous weeks Sprint/Lab.
2. Ensure you are still in your `virtual environment` and the dependencies `flask`, `pytest` and `pytest-cov` are installed. Install other dependencies when the Lab requires. 

3. Each time you install a new dependency make sure you update `requirements.txt`
```bash
 pip freeze > requirements.txt
```
## Things You Can Do When Its Not Working!

#### 🔥 Keep Working It and/or Continue to the Next Phase
* If you are unsuccessful in completing a phase of the lab, make a detailed **bug issue** on GitHub to address it. 
* Then push it (*this is one reason why important to be on `working branch` and not `main`*) with comments and a link to the Issue addressing the bug, DO NOT MERGE! 
* See below **How to Handle Unsuccessful Code While Others are Good** for more strategies
* Create a new branch to continue with the lab or move to the next phase which may have a new branch already designated. Rinse and Repeat. 
🔴🔴ALWAYS BE IN A WORKING BRANCH THAT IS **NOT** MAIN!!!
* By following this process you may improve your final grade for that lab; dependent on the accuracy and clarity of the bug report and the process you used (GitHub Flow)

* See Syllabus
>	•	GitHub Classroom Individual Project Labs/Sprints — All Individual project assignments are expected to be your work. Collaboration and problem solving are permitted, but you must submit your own lab assignments to your respective individual repository (this includes each expected branch push and  required images from your codebase i.e. follow EACH instruction no shortcuts!!)
>
#### How to Handle Unsuccessful Code While Others are Good

1. **Split Your Work Into Separate Commits**
>[!NOTE] The project labs do not require this but it is good strategy which you can easily implement

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

#### ⚠️ Ask the Instructor for Starter Code

The labs builds on your previous week/lab/sprint codebase. If you encounter major issues or cannot continue, **ask your instructor** for help. They can provide a working `sX-starter` version by pushing it directly to your GitHub repository but **only after the due date** for the lab. 

With an instructor push, your version history is still intact and grading will occur on the work you actually did (to include the CI result from your work) but you will now be able to continue the project and take the next steps. Only the codebase will be in the starter version, you are still expected to make sure your agile documentation is updated in your repository.

Once the `sX-starter` code is pushed, you should:

1. **Review the changes** on GitHub to understand what was corrected.
2. Compare your previous work with the updated code.

> 💡 To view the differences:
>
> * Visit your repository on GitHub.
> * Go to the **"Commits"** tab.
> * Click on the commit that says **“Pushed Sprint X starter code”**.
> * Use the **"Browse files"** or **"Compare changes"** view to see what was added or modified.

## 📄 Agile Documentation Template (Instructor-Provided)

A recommended template for each of your Agile documents has been provided. This includes sample wording and structure to help you get started. You may use the suggested content as-is or enhance/add to what is there for your clarification needs.

>[!NOTE] For your Group Project, your group will be responsible for the creation of the required Agile Documentation. There will not be a template.

* 🔍 **Where to Find It:** You can find the template on **Blackboard** under the respective Project Assignment for that week

>[!NOTE]  Templates are provided to guide in completing agile documentation for your individual project.

## Create and Activate a Virtual Environment, Install Dependencies (Repeat/Reference)

1. Set up an isolated Python environment for the project and install required packages:
  
  [!NOTE] You can do this using the command/terminal line or VS Code to create a virtual environment, but for either you will need to use the command line/terminal to install dependencies.
  
  ```bash
  # Create a virtual environment (named .venv)
  python -m venv .venv
  # Activate the virtual environment (use .venv\Scripts\activate on Windows)
  source .venv/bin/activate
  
  # Install Flask, pytest and pytest-cov in the venv
  pip install flask pytest pytest-cov
  # Creates a requirements.txt document
  pip freeze > requirements.txt
  ```

## ✅ Set Up Issue Tracking

Now that we have defined the work for Sprint #, we will use GitHub **Issues** to track progress:

1. Review the **ISSUE Guidance** (`s#_template.md`)
2. Create *Parent* **Sprint # Completion** Issue
3. Create *Sub-Issues*

> [!NOTE] When all sub-tasks for a parent ISSUE are completed and the code is merged, the parent issue (user story) should be closed. (Notice each Issue has an assigned #Number. Including “Closes #123” in a commit or PR will automatically close issue #123 when the PR is merged.)

## Set Up Your Project Board on GitHub

1. **Set Up the Kanban Board**

   * Create a **Sprint # Project Board** in GitHub (Respective Sprint).
   * Use the following columns:

     * `Backlog` → `Ready` → `In Progress` → `In Review` → `Done`
   * These represent the typical Agile flow from planned to completed work.

2. **Populate with Issues**

   * Add all sprint-related issues to the board.
   * Issues should begin in the **Backlog** column.
   * As work progresses, move each issue forward through the workflow:

     * `Backlog`: Not yet prioritized
     * `Ready`: Selected for sprint and ready to start
     * `In Progress`: Currently being worked on
     * `In Review`: Work is completed and undergoing review or testing
     * `Done`: Task is complete and merged/deployed

> ✅ Tip: Link the project board to your repository so you can easily track progress within pull requests and issues.




