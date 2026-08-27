# Lesson Plan for CH381M Guest Lecture on Python

The goal of this lecture is to introduce Python for Analytical Chemistry.

Data analysis has always been an important part of analytical chemistry, but the rise in speed of computerized instrumentation makes it essential.

In the past, you could use Excel for a lot of data anlaysis, but that can get tedious. Scripting your data analysis will save you time,
and it allows you to track your analysis

# Setting up the Environment

## Setting up Python

Our first goal is to have everyone set up Python on their computers. There are several ways to do this.

My personal favorite is to install Python to a known location (C:\Python3XX for me, where the XX is the version number). I then use pip terminal commands to install the libraries I want, like `pip install numpy`.

Another approach is that you can install Anaconda, a large Python distribution that bundles a lot of libraries with it.

Finally, you may have Python already installed on your computer. You can figure this out by opening a terminal and typing `python`. If this is the case, make sure you can use pip to install packages (see below). Sometimes, it will lock down the Python on your machine, and you would need to install another if that is the case.

*TODO: Whichever of these three you pick, install Python.*

## Setting up an Integrated Development Environment

You can run Python directly from the command line and use text editors to write scripts. However, it is very helpful to set up an Integrated Development Environment (IDE). An IDE is a text editor written to help you write and run code. Personally, I use PyCharm and love it: https://www.jetbrains.com/pycharm/. PyCharm is free, and you can even get the full Pro version if you apply for an educational license. But, you don't need that. There are many others, such as Visual Studio Code, that you can use. 

*TODO: Pick whatever IDE you are most comfortable with and install it.*

## Setting up Git

The final piece of the development toolkit is Git. Git is a tool for tracking changes to your code. Think of it like an early version of Dropbox but where you have more control. You can "clone" a project from a repository, like GitHub. You can then make changes and commit them. Each commit is a snapshot of the project such that you can go back and undo changes that you make. There is a lot more to it, but today we will use git to clone this project.

To install git, follow the instructions in this link: https://github.com/git-guides/install-git. You can either install it as a commandline tool or install GitHub Desktop, which gives you a user interface to clone things. You can test that it is set up properly by opening a terminal and typing `git -v`.

*TODO: After setting it up, clone the project by typing `git clone https:\\github.com\michaelmarty\AnalChem.git`. You can also do this on GitHub Desktop.*

Note, there are other projects for other classes in this Git repository. You can ignore them and focus on the CH381M folder.

## Final Setup

After you have Python, git, and the IDE set up, you can make sure they all connect to each other. Your IDE should be able to run Python files and also likely commit to git for you.

# How to Use Python

## The Python Console

There are several different ways to run Python. The simplest and least effective way is to open a terminal, type `python` to start up the Python console, and then start typing commands. Try this! It works fine, and you can use it to do things if you want. However, it is very tedious to type everything every time, and it can be easy to mix up and overwrite variables. 

## Scripts: The Best Way

The best way to use Python is to write Python scripts. Scripts are simply text files (with a .py ending) that list all of the commands you would normally otherwise enter in the terminal. The script works by starting at the top and executing each line down until the end. It enables direct tracking and a clear workflow.

## Notebooks: Another Good Way

Another way to use Python is with a Notebook. A notebook has a mixture of cells. Some cells are code, others are results of code, others are just text content like notes and figures. The limitation of notebooks is mixing up variables, like with the console. In other words, if you set y, reference it to set z, change y, and then reference it again in a different, it will be changed. But, z will not be changed. 

One way to improve this is with a Marimo notebook, which automatically resets things: https://marimo.io. We are going to try using a Marimo notebook today. 

*TODO: To install marimo, you will need to do `pip install marimo` in the terminal. You may also want to install a Marimo plugin for your IDE, which will help them work together.* 

## Installing the Necessary Libraries

*TODO: While you are at it, do `pip install numpy matplotlib` to install the other libraries that we will use in our tutorial.*

# Final Setup

To check that everything is setup, open the eic_notebook.py and see if it is working for you. You can open it in PyCharm with the Marimo plugin. You can also open a terminal and type: `marimo edit eic_notebook.py` to open it in a browser. 

# A note on AI programming agents

At UT, you have access to Codex from OpenAI. You can log in with your UT EID and connect it to your notebook and IDE. It's very helpful as you learn more. We won't cover it explicitly, but you can use it to help you. 
