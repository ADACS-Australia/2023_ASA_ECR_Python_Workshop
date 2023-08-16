---
title: "Automation with GitHub"
teaching: 15
exercises: 30
questions:
- "What can I automate?"
- "How can GitHub help with automation?"
objectives:
- "Learn about GitHub actions"
- "Create a github action to run your tests automatically"
keypoints:
- "Automated testing helps you find errors faster"
- "Testing on GitHub avoids local issues"
- "GitHub actions can automate more than just testing"
---

## CI/CD in GitHub

In this lesson we will introduce what automation is possible for continuous integration/development/deployment/delivery within GitHub.

**Continuous Integration** is the practice of integrating code into a shared repository and building/testing each change automatically.
Continuous integration is able to:
- Detect errors as they are introduced
  - Fix while fresh in your mind
- Reduce integration problems
  - Smaller problems are easier to digest
  - Don’t compound problems
- Allow teams to develop faster, with more confidence

**Continuous Delivery** extends the above by deploying all changes to a test or production environment.
Continuous delivery allows you to:
- See the effects of all changes in the final product immediately
- Easily perform user based testing and acceptance
- Approve and deploy changes to production more often

**Continuous Deployment** goes even further, and automates the above so that changes that pass automated quality control are automatically rolled out into the production environment.

### GitHub CI/CD features

1. **Multi-platform:** you can execute builds on Unix, Windows, and OSX.
1. **Multi-language:** build scripts are command line driven and work with Java, PHP, Ruby, C, and any other language.
1. **Parallel builds:** GitHub CI splits builds over multiple machines, for fast execution.
1. **Realtime logging:** a link in the pull request takes you to the current build log that updates dynamically.
1. **Pipeline:** define multiple jobs per stage and even trigger other pipelines.
1. **Versioned workflows:** Workflows are described in `.yml` files within your repo so you can track changes like with any other files.
1. **Build artifacts:** upload binaries and other build artifacts to GitHub and browse and download them.
1. **Run locally:** reproduce workflows locally using [act](https://github.com/nektos/act).
1. **Self hosted workflows:** use your [own infrastructure](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners) instead of that provided by GitHub, whilst still using the GitHub actions to initiate work.
1. **Docker support and container registry:** use custom Docker images, run on Kubernetes, built-in container registry to store, share, and use container images.

## Creating a GitHub action
In this lesson we will focusing on using GitHub actions to build our code and run our tests.
You can write custom actions from scratch but there are a large number of templates that cover most of the common use cases.

> ## Use a template action
> - On your GitHub repo, navigate to the actions tab.
> - Search for "python package"
> - Select the following template by pressing "configure"
> ![Package Template]({{page.root}}{%link fig/GitHubActionPythonPackageTemplate.png%})
> - Change the filename to be `python-build-test.yml`
> - Change the `name` on line 4 to be "Python build and test"
> - Change line 8 to be `["main","dev"]`
> - Change line 10 to be `[ "main", "dev" ]`
> - Change line 19 by removing "3.11"
> - Add `pip install .` before line 32 so that we install our module
> - Comment out lines 33-38 which perform Linting with flake8
> - Save your file by pressing "commit changes"
{: .challenge}

> ## Resulting file
> ~~~
> # This workflow will install Python dependencies, run tests and lint with a variety of Python versions
> # For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
> 
> name: Python build and test
> 
> on:
>   push:
>     branches: [ "main", "dev" ]
>   pull_request:
>     branches: [ "main", "dev" ]
> 
> jobs:
>   build:
> 
>     runs-on: ubuntu-latest
>     strategy:
>       fail-fast: false
>       matrix:
>         python-version: ["3.9", "3.10"]
> 
>     steps:
>     - uses: actions/checkout@v3
>     - name: Set up Python ${{ matrix.python-version }}
>       uses: actions/setup-python@v3
>       with:
>         python-version: ${{ matrix.python-version }}
>     - name: Install dependencies
>       run: |
>         python -m pip install --upgrade pip
>         python -m pip install flake8 pytest
>         if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
>         pip install .
>     # - name: Lint with flake8
>     #   run: |
>     #     # stop the build if there are Python syntax errors or undefined names
>     #     flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
>     #     # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
>     #     flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
>     - name: Test with pytest
>       run: |
>         pytest
> ~~~
> {: .output}
>
{: .solution}


> ## Watch your action
> Once you have finished the above you should navigate to the "actions" tab and you'll see your action running.
> It's running because you pushed a change to the main branch!
> 
> Running actions have a yellow dot next to their name.
> Failed actions have a red cross, while successful actions have a green check mark.
> 
> ![Actions completed]({{page.root}}{%link fig/GitHubActionsCompleted.png%})
> You can click on one of the actions to see the jobs that are part of that action, and then on each job to see the output from the run.
>
> Take some time to explore this now.
{: .challenge}

If your action contains multiple jobs (usually because you have a matrix set up) then if one job fails, the entire action will be marked as a failure.
The repo owner will be notified every time an action fails, and again when an action is successful after a failure.
Subsequent successes don't send emails.

GitHub actions are run either when you make a push to the repo (or selected branch) or when you create a pull request into a selected branch.
We set this up in the following lines of our job file:
~~~
on:
  push:
    branches: [ "main", "dev" ]
  pull_request:
    branches: [ "main", "dev" ]
~~~
{: .output}

The action that we ran previously was triggered by us pushing to the main branch.
Let's now make a pull request from the `dev` to `main` branch to see how actions work with pull requests.

> ## Make a PR to merge `dev` with `main`
> 1. Create a new pull request to merge our `dev` branch into the `main` branch.
> 1. Observe our build/test action starting, running, and then completing from the PR page.
> 1. Once complete, click on the "checks" tab and see the jobs that were run and their status.
{: .challenge}

You should see something like the following:
![Action Startup]({{page.root}}{%link fig/GitHubPRActionStartup.png%})
![Action Complete]({{page.root}}{%link fig/GitHubPRActionComplete.png%})
Once the jobs complete successfully they will be folded up so you don't see them.
If any of the checks pass then you'll see a red label and a link to the failed job.
If a job fails then you can update your code/documentation/job to remedy the situation and make another commit to the branch you are trying to merge.
Each push to the branch being merged will cause the jobs to be re-run.

GitHub will let you merge a PR with failed checks, but the normal life cycle of development includes having working tests before your accept the pull request.

## What else can we use GitHub actions for?
There are a large number of templates in the actions gallery which you can explore.
Here are some use cases that might be relevant to you:
- compile documentation
- build your code an push it to pypi.org
- create a website for your repository (eg, [the pages for this workshop](https://github.com/ADACS-Australia/2023_ASA_ECR_Python_Workshop/blob/gh-pages/.github/workflows/website.yml))
- deploy your app to cloud infrastructure
- run security checks against your code or web-app.