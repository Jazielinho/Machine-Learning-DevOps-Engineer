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

