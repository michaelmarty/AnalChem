import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Overall Goal of this Project

    Let's start by talking about the science. Here, I have collected a set of data. The goal is to quantify the percentage of cholesterol in a background of phosphatidyl-choline (PC). We have run MS analysis with D7 internal standards of both. Extracted ion chromatograms (EICs) are available for each of the samples and each of the 4 species. Our goal is to quantify the percentage of cholesterol. Assume that our standards are added at a 1:10 D7-chol:D7-PC ratio.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Learning Some Python Basics

    Now, let's do some basic Python execution. In the next block of code, I have defined the variable x and given it a number. Define y and print the sum of the outputs. Use "shift+enter" to execute the code block or click the play icon.
    """)
    return


@app.cell
def _():
    x = 10
    print(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's learn about for loops. For loops iterate over a list and then do something. Here's an example.
    """)
    return


@app.cell
def _():
    l = [2, 4, 6, 8]
    for i, l in enumerate(l):
        print(i, l)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Doing Science with Python

    Ok, now that we have our feet wet, let's start doing some science. First, we need to load our data. We can do that with basic Python functions, but there are better ways to do it using libaries. Libraries are Python packages that you need to install. You've already installed Marimo, which is a library. Hopefully, you have already installed numpy and matplotlib. If not, revisit the GettingStarted.md file and use `pip install numpy matplotlib` to install them. After installing the libraries, we next need to import them.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This last command imports numpy and renames it to np for easy calling. Now, we can call numpy commands using np.[command]. Let's take a look.
    """)
    return


@app.cell
def _(np):
    print(np.arange(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This prints a numpy array of length 10. An array is similar to a list of numbers. It's technically a "class", which means a programming object that has both variables and functions attached to it. Let's see some examples.
    """)
    return


@app.cell
def _(np):
    array = np.arange(10)
    print(array.shape)
    print(array.max())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here, array.shape is a varaible that tells what the shape of the data is, here a single dimension with 10 elements. You can tell it is a variable because it has no parentheses after it. array.max() is actually calling a function that is attached to the array object. That function calculates the maximum and returns it. Here, we did not give an arguments to the function, but we could have put things in the parentheses to give it more direction.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Loading Our Data

    Now, let's load our data. To do this, we will first need to tell it where our data is. We will use the os library here and a function called chdir ("change directory") to set the working path to the EIC Dataset folder. If your computer struggles here, you might need to give it a more exact path for the EIC Dataset folder. Finally, we will use os.listdir() to list the current working directory, which is now the EIC Dataset folder. You should see a list of text files.
    """)
    return


@app.cell
def _():
    import os
    os.chdir("EIC Dataset")
    os.listdir()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's load one of those data files using numpy. Here, we use the np.loadtxt() command but include an argument with the file name. We need to use quotation marks to indicate that the file name is a string (text). Otherwise, it trys to interpret text as numbers or variables.
    """)
    return


@app.cell
def _(np):
    data = np.loadtxt("popc_2-1_test.txt")
    print(data.shape)
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I also had it print the shape of the data. Here, there are 1035 data points in two columns. The first column is retention time in minutes. The second colum is intensity. To access these, we use array slicing, with [] markers. In array slicing, the values are 0 indexed, meaning the first value is the 0 position. A ":" means take all. Negative values mean start at the end. Dimensions are offset with a ",".
    """)
    return


@app.cell
def _(data):
    print("First data pair:", data[0])
    print("Last data pair:", data[-1])
    print("Retention Time column:", data[:,0])
    print("Intensity column:", data[:,1])
    print("Retention Time Range:", data[:,0].min(), data[:,0].max())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Play around with this and see how you can slice things differently.

    # Plotting the Data

    To plot the data, we will use matplotlib as a library and specifically the pyplot module. We need to feed it the x and y data.
    """)
    return


@app.cell
def _(data):
    import matplotlib.pyplot as plt

    plt.plot(data[:,0], data[:,1], color="red")
    plt.xlabel("Retention Time (min)")
    plt.ylabel("Intensity")
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, it's your turn. Try adjusting the file names above and looking at some of the data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Normalization and Background Subtraction

    Now let's do some normalization and background subtraction. Normalization divides by the maximum, and background subtraction subtracts the minimum. I'll show you how to do background subtraction, and you can then add in normalization. Here, we make use of the fact that math can be done directly on numpy arrays, and it propagates through every element.
    """)
    return


@app.cell
def _(data, np, plt):
    processed_data = data.copy()
    processed_data[:,1] = processed_data[:,1] - np.amin(processed_data[:,1])

    plt.plot(processed_data[:,0], processed_data[:,1])
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your turn, got back to the code and normalize the data now.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Plotting Multiple Things
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's plot an example of each chromtogram together. Import data from each molecule from the the 2-1_test data. Plot them all together. You can do this by simply adding multiple plt.plot() lines.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Functions and Peak Integration

    Ok! We're able to plot our data. It's time to integrate our peaks and start to do quantitation. Here, we will write a function to help us do the integration. Functions are defined like this in Python.
    """)
    return


@app.cell
def _(np):
    def integrate(x, y, min=3, max=20):
        mask = (x >= min) & (x <= max)
        area = np.trapezoid(y[mask], x[mask])
        return area

    return (integrate,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are a few key elements here. "def" tells it that you are defining a function. "integrate" is the function name. "x" and "y" are required arguments. These are only defined inside the function. You call them as x and y in the function block. However, they may be named something else outside the function! Because they don't have a keyword associated with them, you just supply them in the function in those positions when you call it. "min" and "max" are optional keyward arguments. They can be supplied if you want by either saying "min=2" or something like that when calling the function. They can also be supplied without the keywork, in which case it assumes the order is the same as here. If you don't supply them, the default is used.

    Now, let's try using the function.
    """)
    return


@app.cell
def _(data, integrate):
    integral = integrate(data[:,0], data[:,1], min=4, max=18)
    print(integral)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    0
    """)
    return


if __name__ == "__main__":
    app.run()
