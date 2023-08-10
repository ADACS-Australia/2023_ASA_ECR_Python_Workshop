---
title: "Git workflows"
teaching: 20
exercises: 0
questions:
- "How should I work with Git branches?"
objectives:
- "Understand git workflows"
keypoints:
- "Choose a workflow that suits your project"
---
## [Git workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)

Git is the most commonly used version control system today.
A Git workflow is a recipe or recommendation for how to use Git to accomplish work in a consistent and productive manner.
Git workflows encourage developers and DevOps teams to leverage Git effectively and consistently.
Git offers a lot of flexibility in how users manage changes.
Given Git's focus on flexibility, *there is no standardized process on how to interact with Git*.
When working with a team on a Git-managed project, it’s important to make sure the team is all in agreement on how the flow of changes will be applied.
To ensure the team is on the same page, an agreed-upon Git workflow should be developed or selected.
There are several publicized Git workflows that may be a good fit for your team.
Here, we will discuss some of these Git workflow options.
In this section we'll discuss a few different ways to use git.
We refer to these as a process or workflow which you incorporate into your existing work habits.


> ## What makes a workflow successful?
> When evaluating a workflow for your team, it's most important that you consider your team’s culture.
> You want the workflow to enhance the effectiveness of your team and not be a burden that limits productivity.
> Some things to consider when evaluating a Git workflow are:
> 
> - Does this workflow scale with team size?
> - Is it easy to undo mistakes and errors with this workflow?
> - Does this workflow impose any new unnecessary cognitive overhead to the team?
{: .callout}


### Centralized workflow
In this workflow there is a single repository (usually the one on GitHub) is designated as the central repository.
When people want to make changes to the repo they pull the current version, make their changes and then push back to the central repo.
This style works well if you have only a few developers who do not work on similar parts of the code at the same time, so the expectation for conflicts is very low.
This method is simple to understand and easy to work with.
If you are the sole developer/user of your repository then this is probably how you will work.

Atlassian have a [deeper discussion](https://www.atlassian.com/git/tutorials/comparing-workflows) about the pro/con of working in this way.
![CentralizedWorkflow](https://wac-cdn.atlassian.com/dam/jcr:0869c664-5bc1-4bf2-bef0-12f3814b3187/01.svg?cdnVersion=714)

### Feature branching workflow
Similar to the centralized workflow except that when changes are going to be made to the repo a developer will create a branch to work on those changes.
As a feature is being developed changes will often break the functionality of the software so keeping all these changes in a branch separate from `main` will mean that there is always a 'known working' version of the code that people can use.
You could consider the local copies of a repo in the centralized workflow to have a similar purpose to the branches in the feature branching workflow.
However, a key difference is that by having the branches stored in the repository, you can have multiple people seeing and working on these branches.
Another difference is that you can make a different branch for each feature, and have multiple features being developed at the same time.

Consider the case where you are working on a new feature for your code.
You pull the main branch from the centralized workflow and start developing that feature.
As you are part way through you find a bug that needs to be fixed in the code.
You now either have to make that bug fix part of the feature development, meaning that you cant push it back to the main repository until your development is complete, or you have to discard your development in order to fix the bug, before retuning.
Now consider how this would work if you used a feature branching workflow.
You make a new branch from `main` for `feature-1` and start working on it.
You notice a bug in the main code so you create a new branch from `main` called `bugfix-1`.
You fix the bug in `bugfix-1` and then merge it back to `main` and then also to `feature-1` (possibly using a `merge rebase main`).
You can now return to developing on `feature-1` without having to backtrack.

![FeatureBranching](https://wac-cdn.atlassian.com/dam/jcr:09308632-38a3-4637-bba2-af2110629d56/07.svg?cdnVersion=745)

Another advantage to the feature branching workflow is that by having the branches exist in the central repo, you can have multiple people working on (testing/reviewing) them at the same time.
The feature branching workflow includes a new operation that isn't used in the centralized workflow: a pull (or merge) request.
A pull request (or PR) is initiated on the central repository (eg, GitHub), and is a request to pull changes from one branch into another.
The idea is that developer A will make a bunch of changes in their feature branch, and then when they are happy with the changes, they will create a PR to merge these into another branch (usually main).
Good practice is to then have a different developer act as a reviewer for these changes.
Developer B will look at what the feature branch is trying to address, what has changed, and check that tests are still passing, new tests have been created, and documentation has been created/updated.
Once the reviewer is happy they approve the PR and the feature branch is merged.
For solo developers the PR is not always required, but is still sometimes used as it can cause automated testing to be run (see CI/CD later).
Even in small teams, it can be very beneficial to require all changes to the main branch to be done via pull requests from a feature branch, with some code review and discussion before the PR is accepted.
Again, Atlassian have a [more detailed description](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) of the feature branching workflow.


### GitFlow
GitFlow takes the feature branching workflow and adds some additional structure.
The features are:
- A main branch that is changed only by pull requests from a development branch
- Tagging of the main branch with versions corresponding to updates to the branch
- A pull request onto the main branch is considered a "release"
- A persistent development branch from which all features are branched and then merged back onto
  - Feature branches are deleted once merged back into the development branch
  - Critical bugs in the main branch can be fixed and merged into both main and development branch. We call this a "hotfix" and it's considered to be messy.
- Tracking of issues is done via GitHub issues, and to work on an issue you will create a branch with that issue name or number (eg. `114-https-bugfix`)

![GitFlow](https://wac-cdn.atlassian.com/dam/jcr:34c86360-8dea-4be4-92f7-6597d4d5bfae/02%20Feature%20branches.svg?cdnVersion=714)

When an issue is resolved, a pull request is made.
Linking the issue to the pull request will cause the issue to be closed when the PR is accepted and merged.
GitHub will automatically prompt you to delete the branch once it is merged.

This workflow is very good for working in teams as it will allow you to more easily incorporate project management into your development workflow.
When working in a team, rules or guides for branch names, testing and documentation requirements, and coding style, should all be agreed on and ideally documented within the repository itself.


## Conflicts
As soon as people can work in parallel, or on different branches, they'll likely step on each other's toes.
This will even happen with a single person: if we are working on a piece of software on both our laptop and a server in the lab, we could make different changes to each copy.
Version control helps us manage these conflicts by giving us tools to resolve overlapping changes.

![Merging Conflicts](https://swcarpentry.github.io/git-novice/fig/conflict.svg)

The process of joining different branches together is called merging.
Just like the typical Perth driver, git doesn't always know how to handle a merge.

To see how we can resolve conflicts, we must first create one!
The most reliable way to create a conflict is to edit overlapping parts of a file in two locations.
Either in two branches, or in two instances of your repository.


> ## Create a conflict
> Make sure your remote repository is up to date by having a clean local repository and running `git push origin main`.
>
> Go to your GitHub repo and choose the `sky_sim.py` file.
> Open this file and edit it using the GitHub online editor.
> Change the `ra` and `dec` values for our galaxy.
> Save the file and make a note about the commit like "updating ra/dec from GitHub".
>
> On your local repo, edit the same file, and change the `ra` and `dec` to a **different** value.
> Save the file and make a commit with a comment like "updating the ra/dec from local".
>
> Don't push/pull your repo (yet).
{: .challenge}

> ## Note
> In the above we have explicitly avoided doing a `git push` or `git pull` between working in different locations because we intentially want a conflict to occur.
> Of course in our daily work we would always ensure that we pull before we start work and push when we are done.
{: .callout}

Now if we try to pull the remote changes we have a conflict:

~~~
git pull origin main
~~~
{: .language-bash}

~~~
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), 754 bytes | 754.00 KiB/s, done.
From github.com:PaulHancock/symmetrical-octo-parakeet
   91ba8c2..4a180ae  main     -> origin/main
Auto-merging mymodule/sky_sim.py
CONFLICT (content): Merge conflict in mymodule/sky_sim.py
Automatic merge failed; fix conflicts and then commit the result.
~~~
{: .output}

The `git pull` command updates the local repository to include those changes already included in the remote repository.
After the changes from the remote branch have been fetched, Git detects that changes made to the local copy overlap with those made to the remote repository, and therefore refuses to merge the two versions to stop us from trampling on our previous work.

The status of our repository is now broken as can be seen from `git status`:
~~~
git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   sky_sim.py
~~~
{: .output}


The conflict is marked in in the affected file:

~~~
# Determine Andromeda location in ra/dec degrees

# from wikipedia
<<<<<<< HEAD
ra = '00:42:44.2'
dec = '41:16:08'
=======
ra = '00:42:44.4'
dec = '41:16:10'
>>>>>>> 4a180aeb4955e4af97cfef3a2831ad8029ceae1d

# convert to decimal degrees
from math import *
~~~
{: .language-python}

Our change is preceded by `<<<<<<< HEAD`.
Git has then inserted `=======` as a separator between the conflicting changes and marked the end of the content downloaded from GitLab with `>>>>>>>`.
(The string of letters and digits after that marker identifies the commit we've just downloaded.)

It is now up to us to edit this file to remove these markers and reconcile the changes.
We can do anything we want: keep the change made in the local repository, keep the change made in the remote repository, write something new to replace both, or get rid of the change entirely.

> ## Resolve the conflict
> For now, choose one of the two edits to be correct and fix the file accordingly.
>
> Don't forget to remove the `<<<` `==` and `>>` lines!
>
> When you have saved the merged version of the file you'll have to add the changes using `git add sky_sim.py`.
>
{: .challenge}

If we now run `git status` we should see:
~~~
git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
	modified:   sky_sim.py
~~~
{: .output}

And typing `git commit` will finish our merge with a default message:
~~~
git commit
[main c526818] Merge branch 'main' of github.com:PaulHancock/symmetrical-octo-parakeet
~~~
{: .output}

Now we can push our changes to GitHub with `git push origin main` and we will have fixed the conflict and synchronized both instances of the repository.
