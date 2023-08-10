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
