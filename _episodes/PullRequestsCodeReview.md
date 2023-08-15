---
title: "Pull requests and reviewing code"
teaching: 25
exercises: 30
questions:
- "What is a pull request?"
- "When and how do I accept a pull request?"
objectives:
- "Understand github pull requests"
- "Understand code peer review"
keypoints:
- "Pull requests are a natural way to discuss new code before accepting it into your project"
- "Establish a set of criteria for acceptance before starting a code review"
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
> We will be merging our previously created feature branch (called `feature-1` here) with the `dev` branch so press the "New pull request" button.
>
> By default GitHub will think we want to merge this feature in to the main branch.
> Click the button "base: main" and change it to be "base: dev".
> Hopefully you should see the following:
> ![GitHubBranchesView]({{page.root}}{% link fig/GitHubPRHeader.png%})
>
> Leave the title of the PR to be the default value (the branch name), but fill in a short description of what this pull request involves.
> Once done, press the green "Create pull request" button. 
{: .challenge}

We now have a bare-bones pull request, which consists of probably only 1-2 commits.

### Structure of a pull request (PR)
Here is a screen shot for a pull request merging branch `feature-1` into `dev`.

![GitHubPRInitial]({{page.root}}{%link fig/GitHubPRInitial.png%})

- **Description** Once created, the pull request will look  a bit like a conversation starting with your description of what is going to be merged.
- **Commits** Following this description, you'll see a list of the commits that are going to be applied if the merge takes place.
- **Reviewers** You can assign collaborators to act as reviewers for your pull request. You are essentially asking these people for approval to merge the changes.
- **Assignees** You can select one or more assignees for the PR, which are essentially the people responsible for making whatever changes are being requested by the reviewers. You will see that there is a "assign yourself" link since it is most common that the person making the PR is going to be working on it.
- **Labels**, **Projects**, **Milestones** We will ignore these attributes.
- **Development** If you have linked issues to this pull request (using #ID) then merging this PR will close the related issues.


> ## Fill out your PR
> 1. Assign yourself as the assignee for this PR.
> 1. Select the "bug" label for this PR.
> 1. If there are not issues linked in the "Development" section, choose the issue that we created earlier.
>
> Normally we would also assign someone as the reviewer but you cannot review to a PR that you created.
{: .challenge}

The next step in our process is to have someone review the changes that were made to the code before merging them.
This is the code review process.

### Code reviews
Code reviews are widely recognized as the best way to enhance code quality.
Additionally, a code review offers a natural point for you and your reviewer(s) to learn from each other.

A good code review requires:
1. a knowledgeable reviewer with time and capacity for the review,
2. an agreed upon set of standards against which the code will be judged, and
3. a focus on constructive and meaningful feedback.

You can of course create a PR and then accept it imedately without review (and GitHub awards a [Quickdraw achievement](https://github.com/drknzz/GitHub-Achievements) for this) but that is not really in the spirit of the process.
Whilst part (2) above suggests that there is a check list of requirements (there is!) the review process is more than just ticking boxes.
The review process is an iteration of code reviewing and code updating.

![Review Process](https://images.ctfassets.net/zsv3d0ugroxu/Z8dtCNdftgdcNAFQEnyYy/bc728a50ec535ed7ff5f062ef532efbd/PR_review_process)

If you find that your pull request is stuck in an endless loop of review/update then this could be because:
1. you have tried to take on too much at once, 
   - consider submitting smaller PRs which tackle a smaller amount of work each
2. you and your reviewer have a different set of standards or goals, 
   - consider developing a set of standards for acceptance before starting the PR.
3. you have submitted rushed or poor quality code that is just hard to review effectively,
   - consider incorporating automation into your review process

As part of the pull request, there are places for you to view changes, make requests, and discuss the PR before it is accepted.
In the "Files Changed" tab, you can see the cumulative result of all the commits that would be merged.
From this tab you see a diff of each file, and have the ability to either give overall comments in the "Review changes" button, or by higlighting a line/lines and commenting.

![GitHub PR Review Page]({{page.root}}{%link fig/GitHubPRReviewPage.png%})

Even if you were not requested as a reviewer, you can provide your 2c.


> ## Review your PR
> 1. Navigate to the "Files Changed" tab of your pull request.
> 1. Locate the line in your code which calculates the distance between each data point and the reference location.
> 1. Highlight these lines and make a comment "Euclidean distance metric isn't appropriate here".
> 1. Choose "start a review" from the options provided.
> 1. Locate the line where you apply the `crop_to_circle` function.
> 1. Highlight the line and make a comment "This cropping will result in fewer sources, so that less than nsrc sources are returned".
> 1. Choose "Add review comment".
> 1. Click the "Viewed" check-box on the top right of the `sky_sim.py` file
> 1. Press "finish your review" and submit it as a comment.
> 1. Navigate back to the "Conversation tab"
> 
{: .challenge}

> ## Expected result
> ![GitHub PR Conversation]({{page.root}}{%link fig/GitHubPRConversation.png%})
{: .solution}

You should be able to see the comments that you made in the main conversation.
If you push additional changes that modify these lines of code, then these comments get marked as "Outdated".
You can have a threaded conversation about each comment, and then resolve it when you are done.
Resolved comments are folded in the history of the PR, but you can unfold them as needed.

> ## Accept your PR
> 1. Resolve all the conversations in the PR
> 1. Press the big green "Merge pull request" button to complete and close the PR.
> 1. Delete the feature branch related to this PR.
> 1. Navigate to your "Issues" tab and confirm that the linked issue was closed (close it if not).
>
{: .challenge}