---
title: "Group project setup"
teaching: 30
exercises: 60
questions:
- "What is this project?"
objectives:
- "Form project groups"
- "Decide on a topic for your group"
keypoints:
- "Group work is where you'll do the most practice"
- "A diverse group is a good group"
---

## Group projects
Throughout this week, we'll spend the mornings learning different aspects of software development in python.
During the lessons there will be opportunities to practices the lessons learned, but often these will involve simple or contrived examples.
We have decided to use mini group projects to allow you all to really dig into the lessons learned and practice them in a more real world situation.



### Group project topic ideas
Some suggestions for projects:
- a command line tool that will take an ra/dec and tell you which constellation it lies in,
- a tool to identify which satellites will be in your field of view during an observation,
- an anti-transient checker that will tell you if your transient is actually just the Moon/Jupiter/etc
- a pedantic radio astronomer's spell checker that wil identify incorrect uses of flux vs flux density,
- a single player version of [Set!](https://en.wikipedia.org/wiki/Set_%28card_game%29) to keep you sharp during long observing runs,
- 

> ## Pitch your ideas
> Use the [etherpad]({{site.ether_pad}}) to pitch additional ideas for projects.
>
{: .challenge}

### Forming groups

Coding on your own may be more typical for your research work, but it does limit the dissemination of coding best practice and your opportunities to learn new skills.
Working in a group does mean that you'll have to spend more time explaining what you are doing, planning and agreeing on plans, and reviewing the work of others, but ultimately all these tasks will result in fewer bad choices, and more brains available to fix problems as they arise.
With this in mind, you will get the most benefit out of this task if you:

- work with people that you haven't worked with before,
- work with people that work on different science projects,
- work with people who have a different view of the world,
- accept that the way you do things may not be the best solution for all situations,
- be open to learn from others on any topic, even the ones where you feel you are an expert.

Therefore, we will be forming groups, but we will be forming as diverse groups as possible.

> ## Let's play set!
> Form groups of 3-4 people such that at most 2 people have:
> - Published a paper together,
> - An overlapping PhD supervisor,
> - The same operating system on their laptop,
> - Met socially outside of work,
> - The same gender.
>
> If you find yourself in a room full of clones then group work is more important than solo work so form a group anyway.
>
> If there are online participants we strongly encourage hybrid groups to form!
{: .challenge}

> ## Choose group names and roles
> Assign the following roles to people in your group:
> - a speaker who will answer questions on behalf of the group,
> - a presenter who will run a short presentation on Friday afternoon,
> - a convenor who will keep discussions on topic and on time
> 
> You cannot have one person doing two roles.
>
> Additionally assign someone to be the keeper of the github repo, ideally someone who doesn't already have a role.
>
> Choose your group name by having the github repo owner selecting whatever default name github comes up with when you create a new repository.
{: .challenge}

> ## Make a repo and report back
> Make a new github repo with your team name, add all your team members as collaborators with at least write access to the repo.
>
> Record your team name, team members, and repo link in the [etherpad]({{site.ether_pad}}).
{: .challenge}

### Project activities
The goal of the group projects is for you to practice skills that you are learning in the workshop, and to engage in collaborative software development.

1. Choose a project topic (see suggestions below)
2. Develop a MVP python project for this idea
3. Use git and github throughout
    - Use a feature branching workflow
    - Create at least one pull request, have it reviewed, and then merge
4. Structure your python project as a python module
5. At least one of the following:
   1. Create a user friendly experience
    - Include a CLI that includes `--help`
    - Write user documentation in a README.md file
    - Make your package easy to cite by including a `--cite` option and instructions in your READEME.md
   2. Create Documentation
    - Write docstrings for all functions classes
    - Write user documentation in a README.md file
    - Generate basic documentation with pandoc or sphynx
    - Create a user help page or FAQ on github wiki, or using pandoc/sphynx
   3. Create tests
    - Write at least one test for each function
    - Use pytest to automate testing
    - Create a coverage report for your code and identify untested code
    - Have tests run on push to github dev branch and PR into main
   4. Profiling
    - Benchmark your code
    - Profile your code and identify lines/functions which could benefit from optimization (CPU or RAM)
    - Make a github issue with the above information
    - Attempt to improve your code based on the profiling

Within your group, identify the activities that you have the *least* experience with and make them a focus for this week.

> ## Choose a project and set priorities
> Within your group choose a project from the ideas previously listed.
> Doubling up on projects is not a problem!
>
> Come up with a name for the python module that you'll be developing and write a short problem statement for the project as well as some learning objectives from the above list.
>
{: .challenge}

## Main engine start
In the remaining time, begin planning and working on your projects.