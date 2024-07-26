# Lesson Introduction: Working with Others Using Version Control

Though you should already be comfortable with using version control for your own projects, this lesson will prepare you to use version control with a team. First, there will be a short review of key commands for working with git and Github on your own:

1. `git add`
2. `git commit`
3. `git push`

Next, you will learn how to

1. `Create branches`
2. `Use git and Github for different workflows`
3. `Perform code reviews`

Be sure to practice each of these areas using the quizzes and exercises. The best way to ensure you are taking away the key concepts is to practice! If you get stuck, there are solutions and walkthroughs for you to follow along with or check your solution. Each of these areas is key to performing machine learning tasks in the workplace.


# Working Independently
## Creating a new GitHub repository
In the above video, you saw how to create a new Github repository. Next, let's take a look at a common workflow for adding new files or updates.

A common flow for making these changes means using three common git commands including:

1. `git add`
2. `git commit`
3. `git push`

This lesson provides some specifics of working with version control in a team, production setting. The tasks will be relatively specific. If you are looking for a more general course on git, please check out the course linked below.

git & Github course(opens in a new tab)
This course may also be useful if any of these foundations could use more information before continuing.


# Working with Teams

## Scenario 1: Creating a Branch

Let's walk through the Git commands that go along with each step in the scenario you just observed in the video.

Step 1: You have a local version of this repository on your laptop, and to get the latest stable version, you pull from the develop branch.

Switch to the develop branch
`git checkout develop`

Pull the latest changes in the develop branch
`git pull`


Step 2: When you start working on this demographic feature, you create a new branch called demographic, and start working on your code in this branch.

Create and switch to a new branch called demographic from the develop branch
`git checkout -b demographic`

Work on this new feature and commit as you go
`git commit -m 'added gender recommendations'`
`git commit -m 'added location specific recommendations'`
...


Step 3: However, in the middle of your work, you need to work on another feature. So you commit your changes on this demographic branch, and switch back to the develop branch.

Commit your changes before switching
`git commit -m 'refactored demographic gender and location recommendations '`

Switch to the develop branch
`git checkout develop`


Step 4: From this stable develop branch, you create another branch for a new feature called friend_groups.

Create and switch to a new branch called friend_groups from the develop branch
`git checkout -b friend_groups`

Step 5: After you finish your work on the friend_groups branch, you commit your changes, switch back to the development branch, merge it back to the develop branch, and push this to the remote repository’s develop branch.

Commit your changes before switching
`git commit -m 'finalized friend_groups recommendations '`

Switch to the develop branch
`git checkout develop`

Merge the friend_groups branch into the develop branch
`git merge --no-ff friends_groups`

Push to the remote repository
`git push origin develop`


Step 6: Now, you can switch back to the demographic branch to continue your progress on that feature.
Switch to the demographic branch
`git checkout demographic`

### Branching
In the above video, the following commands were introduced:

* `git branch` which shows all the branches you have available
* `git checkout -b` which both creates a branch as well as moves you onto it

Though it wasn't introduced, the git checkout command allows you to move from one branch to another when you are not also looking to create the branch. You also learned that branches cannot have spaces in their names.

In this second video, you were able to see the `git checkout` command in action to move between branches. You were also introduced to the `git branch -d command`, which allows you to delete branches. Note this second command requires that you are not currently on the branch you would like to delete.


## Scenario 2: Creating a Branch

Let's walk through the Git commands that go along with each step in the scenario you just observed in the video.

Step 1: Andrew commits his changes to the documentation branch, switches to the development branch, and pulls down the latest changes from the cloud on this development branch, including the change I merged previously for the friends group feature.
Commit the changes on the documentation branch
`git commit -m "standardized all docstrings in process.py"`

Switch to the develop branch
`git checkout develop`

Pull the latest changes on the develop branch down
`git pull`

Step 2: Andrew merges his documentation branch into the develop branch on his local repository, and then pushes his changes up to update the develop branch on the remote repository.
Merge the documentation branch into the develop branch
`git merge --no-ff documentation`

Push the changes up to the remote repository
`git push origin develop`

Step 3: After the team reviews your work and Andrew's work, they merge the updates from the development branch into the master branch. Then, they push the changes to the master branch on the remote repository. These changes are now in production.
Merge the develop branch into the master branch
`git merge --no-ff develop`

Push the changes up to the remote repository
`git push origin master`

Resources
Read this great article(opens in a new tab) on a successful Git branching strategy.

Note on merge conflicts
For the most part, Git makes merging changes between branches really simple. However, there are some cases where Git can become confused about how to combine two changes, and asks you for help. This is called a merge conflict.

Mostly commonly, this happens when two branches modify the same file.

For example, in this situation, let’s say you deleted a line that Andrew modified on his branch. Git wouldn’t know whether to delete the line or modify it. You need to tell Git which change to take, and some tools even allow you to edit the change manually. If it isn’t straightforward, you may have to consult with the developer of the other branch to handle a merge conflict.

To learn more about merge conflicts and methods to handle them, see About merge conflicts(opens in a new tab).

### Version Control Workflow
In the two videos on this page, we will add to the flow already introduced with branching earlier. This means:

* Pushing our branches to Github
* Opening pull requests
* Introducing code reviews

In the previous video, you notice that pushing a branch to Github follows essentially the same steps as pushing code from main or master to Github. That is, you use the flow of:

* `git add`
* `git commit -m`
* `git push`

However, when pushing a branch, you will get an error that will let you know the exact command needed to push that branch. This is because, the basic `git push` command is intended to be used only when pushing from your main branch up to Github.

One final step not addressed in the above video that is often done in practice is to do a `git pull` on your local to pull the newest version on the Github master branch into your local codebase. Notice this practice will work even if you were not the person to make the newest changes to the master branch.

Otherwise, the above flow shows a great workflow to follow including:

* Creating a new branch
* Adding new features and code
* `add`, `commit`, and `push` your changes to the remote
* Open a pull request
* Have another team member review your changes and merge them in
* Delete the remote branch
* Delete the local branch
* Pull the new code on the remote master to your local machine