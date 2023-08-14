---
title: "Pull requests and reviewing code"
teaching: 20
exercises: 0
questions:
- "What is a pull request?"
- "When and how do I accept a pull request?"
objectives:
- "Understand github pull requests"
- "Understand code peer review"
keypoints:
- "Pull requests are a natural way to discuss new code before accepting it into your project"
---

## Merging branches via pull requests
In previously lessons we have seen how we can merge branches locally, however it is often good practice to involve your collaborators in the merge process.
GitHub allows you to merge branches via the web using a pull request.
Once a pull requests is initiated (opened), you will have the opportunity to name and describe the request, and to invite others to evaluate the changes.
If there are any conflicts between the branches being merged they will be highlighted you'll be blocked from performing the merge.
To resolve the merge conflicts you'll have to create new commits to your branch.
Once all the conflicts have been resolve you'll be allowed to press the big green "Merge" button.

Let us firstly go through the pull request process from a practical point of view.

> ## Create a pull request
> Head to your GitHub repo and press this button:
> ![GitHubBranchesButton]({{page.root}}{% link fig/GitHubBranchesButton.png%})
> From the drop-down menu press the "view all branches" link.
>
> You should see a page similar to this:
> ![GitHubBranchesView]({{page.root}}{% link fig/GitHubBranchesView.png%})
>
> We will be merging the `feature-1` branch with the `dev` branch so press the "New pull request" button.
>
> By default GitHub will think we want to merge this feature in to the main branch.
> Click the button "base: main" and change it to be "base: dev".
> Hopefully you should see the following:
> ![GitHubBranchesView]({{page.root}}{% link fig/GitHubPRHeader.png%})
>
> Leave the title of the PR to be "Feature 1", but fill in a short description of what this pull request involves.
> Once done, press the green "Create pull request" button. 
{: .challenge}

We now have a bare-bones pull request, which consists of probably only 1-2 commits.

### Structure of a pull request (PR)
- **Description** Once created, the pull request will look  a bit like a conversation starting with your description of what is going to be merged.
- **Commits** Following this description, you'll see a list of the commits that are going to be applied if the merge takes place.
- **Reviewers** You can assign collaborators to act as reviewers for your pull request. You are essentially asking these people for approval to merge the changes.
- **Assignees** You can select one or more assignees for the PR, which are essentially the people responsible for making whatever changes are being requested by the reviewers. You will see that there is a "assign yourself" link since it is most common that the person making the PR is going to be working on it.
- **Labels**, **Projects**, **Milestones** We will ignore these attributes.
- **Development** If you have linked issues to this pull request (using #ID) then merging this PR will close the related issues.

![GitHubPRInitial]({{page.root}}{%link fig/GitHubPRInitial.png%})



### Code reviews

![Review Process](https://images.ctfassets.net/zsv3d0ugroxu/Z8dtCNdftgdcNAFQEnyYy/bc728a50ec535ed7ff5f062ef532efbd/PR_review_process)