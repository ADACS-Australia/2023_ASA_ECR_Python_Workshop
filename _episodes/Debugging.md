---
title: "Debugging tactics"
teaching: 90
exercises: 0
questions:
- "What is debugging?"
- "How can I debug a problem?"
- "What tools are available to help me with debugging?"
objectives:
- "Understand python traceback messages"
- "Learn some common debugging techniques"
- "Learn to use a debugging tool"
keypoints:
- "Best practice coding will reduce bugs and their severity"
- "There will always be bugs - don't feel bad"
- "Use debugging tools"
---

## Getting things wrong
Much of academic software development involves writing code that is broken, adjusting it until it works, and then moving on.
This similar to the process of learning anything - getting it wrong until you get it right.
The process of debugging is typically thought of as finding all the errors and fixing them.
Largely this is correct, however there are also strategies that you can use to reduce the number of errors along your path to a final solution.
These techniques are like good study habits - they speed up your learning process.

The first thing to learn when debugging code is that **all** code has bugs.
So the first step in debugging is to embrace this and accept it, and not feel bad about having bugs in your code.
Shame doesn't help anyone.
Even professional software developers don't write bug-free code, they just have strategies and processes in place that will:
- reduce the number of bugs introduced
- make bugs easier to identify
- reduce the severity/impact of existing bugs

We have already learned some strategies that will help [write better code]({{page.root}}{%link _episodes/BestPracticesInComputing.md%}), all of which will result in fewer bugs:
- Clarity of efficiency
- Naming is important
- Don't repeat yourself
- Don't repeat others
- Document
- Test
- Version control

In this lesson we'll explore ways to identify and squash the inevitable bugs that will occur in our python code.

## Understanding the python traceback
The easiest kind of bugs to identify are those that crash your program, because they will generate a traceback of the python call stack that shows you where an error occurred.
An example is given below:
~~~
python3 mymodule/sky_sim.py
Traceback (most recent call last):
  File "mymodule/sky_sim.py", line 119, in <module>
    ras, decs = make_positions(ra, dec)
  File "mymodule/sky_sim.py", line 87, in make_positions
    ras, decs = crop_to_circle(ras, decs)
TypeError: crop_to_circle() missing 3 required positional arguments: 'ref_ra', 'ref_dec', and 'radius'
~~~
{: .output}

The first thing to note about tracebacks is that they are trace**BACK**s meaning that you should read them backwards.
The last line of the trace back will typically be some kind of Error (`TypeError` in the above example).
There are many exceptions built into the python language ([full list](https://docs.python.org/3/library/exceptions.html)), the most common ones that you'll experience are:

| Exception | Cause | Example | 
| --- | --- | --- |
| AssertionError | Raised when an assert statement fails. | `assert value > 0` when `value==0`|
| AttributeError | Raised when attribute assignment or reference fails. | `a.b` when object `a` has no attribute `b` |
| FileNotFoundError | Raised when a file/directory is expected to exist, but doesn't. | `open('test.txt','r')` |
| ImportError | Raised when the imported module is not found. | `import numpy` when `numpy` not installed |
| IndexError | Raised when the index of a sequence is out of range. | `a[5]` when `a` has 5 or fewer elements |
| KeyError | Raised when a key is not found in a dictionary. | `a{"days"}` instead of `a{'Days'}` |
| KeyboardInterrupt | Raised when the user hits the interrupt key (Ctrl+C). | |
| MemoryError | Raised when an operation runs out of memory. | `np.ones( (1_000_000, 1_000_000) )` |
| NameError | Raised when a variable is not found in local or global scope. | `a=b+1` when `b` is not defined |
| OSError | Raised when system operation causes system related error. | |
| OverflowError | Raised when the result of an arithmetic operation is too large to be represented. | `int(1e500)` |
| RuntimeError | Raised when an error does not fall under any other category. | 
| SyntaxError | Raised by parser when syntax error is encountered. | `a + = 1` |
| TypeError | Raised when a function or operation is applied to an object of incorrect type. ** | `1 + 'two'`|
| ValueError | Raised when a function gets an argument of correct type but improper value. ** | `math.asin(-2)` |
| ZeroDivisionError | Raised when the second operand of division or modulo operation is zero. | `1/0` |

** Note: The `TypeError` and `ValueError` are also caused by calling a function with the wrong number of arguments, especially if a function has a mix of required and optional arguments.

Python also allows developers to create their own exceptions by extending the `Exception` class and giving it their own name, so depending on the libraries you are using you may see exceptions not listed above.
Refer to the library documentation to see what they mean and what causes them.

The first thing to do when reading a traceback is look at the kind of exception that is being reported, and the line on which it was generated.
In the above example we have a `TypeError` and it is complaining about `missing 3 required positional arguments`.
The second last line shows the code that caused the problem, and the line above that shows the file and line number of where you can find that error.
In this case it's line 87 in the `make_positions` function within the file `mymodule/sky_sim.py`.
The lines above this show how we got to the offending line.
So line 87 was called within the function `make_positions` which in turn was called from line 119 of `<module>` which means the global scope of the file.
Long tracebacks can occur when you have many layers of functions calling functions, and sometimes you even get what look like loops in the traceback.

For the example shown, python is telling us that we also need to supply three more arguments: `ref_ra`, `ref_dec`, and `radius`.
This should be a simple fix!

Occasionally, you will find yourself in a situation where the traceback is quite misleading and the line that raised the error isn't where your bug is being created.
A common example is when you are passing variables to a function that wants to work on a given data type, but you've given a slightly different data type.
Python is built on the principles of [leap before you look](https://realpython.com/python-lbyl-vs-eafp/), and [duck typing](https://towardsdatascience.com/duck-typing-python-7aeac97e11f8), meaning that functions tend not to inspect the types of all the passed variables, but instead assume they have the correct, or at least compatible, data types and only complain when something goes wrong.
For example this function:
~~~
def add_one(num):
    """Add one to an integer"""
    return num + 1
~~~
{: .language-python}
was written to expect `num` of type `int`.
However, you can pass `float`, `complex`, or even `numpy.ndarray` type objects and this function will still work.
Passing a `str` or `list` or `tuple` will cause and exception to be raised.
If we passed the argument `[a]` to the above function we would cause an exception and the traceback would point to the return statement of this function as the source of the exception.
However, this function isn't the *cause* of the error.
The *cause* of the error is elsewhere in our code where we have failed to unpack the list `[a]` and only pass `a` to the function.
This is why it is useful to have the full traceback available.

There are of course types of bugs that don't generate exceptions and these can be hard to trace because we don't get an execution stack to show us the issue.
An example would be a function `dms_to_degrees` that turns `-00:12:15` into a positive declination instead of a negative one.
There is no exception raised here, because all the code is valid python, but there is an error in the implementation which gives the wrong result.
How can we catch these sorts of errors?
The answer is [testing!]({{page.root}}{%link _episodes/Testing.md%}): we create tests for our functions that raise exceptions when something isn't doing what we intend it to do.

## Getting feedback from your code
lots of `print` statements

logging module with .debug, .info, .error

python debugger and VSCode examples

## Not repeating errors
tests

mocking