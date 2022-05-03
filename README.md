# Function Plotter

## Overview
A GUI program that plots arbitrary user-entered function built with Python and Tkinter.

![Screenshots of working examples and errors](https://i.ibb.co/4mx5yqN/fun-plot.png)

## Requirements
- [x] Take a function of x from the user, e.g., 5*x^3 + 2*x.
- [x] Take min and max values of x from the user.
- [x] The following operators must be supported: + - / * ^.
- [x] The GUI should be simple and beautiful (well organized).
- [x] Apply appropriate input validation to the user input.
- [x] Display messages to the user to explain any wrong input.
- [x] You must test your program. Include the testing codes in your repository.
- [x] Your code should be well organized and well documented.


## The Arithmetic Interpreter
- The biggest challenge for me was to take a function expression as a string, parse it, and get back the result.
- The first solution that came to my mind was to use the `eval()` built-in function in Python, but I knew that it is not an efficient or a secure way to approach this problem. (as the user can easily inject harmful code into the program)
- After doing some research I got to know about *lexers* and *parsers*.
  - Lexer: Piece of software responsible for parsing string characters in a given expression into *tokens*
  - Token: Lower-level representation of what a given expression consists of.
  - Parser: Piece of software that parses a given set of tokens into a tree that represents the hierarchy of operations in the given expression. The tree consists of operator nodes.
  - Nodes: The basic unit of the tree. It represents a single operation.
- Lexers and parsers are usually used for **building compilers and interpreters** (programming languages) as they are handy tools to better understand what a given expression (code or arithmetic) means.

### References
- [Lexical analysis - Wikipedia](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Simple Math Interpreter in Python - CodePulse](https://youtube.com/playlist?list=PLZQftyCk7_Sdu5BFaXB_jLeJ9C78si5_3)


## The Graphical User Interface
- The GUI of the application is simple but intuitive. I used the Tkinter package for building the basic widgets of the UI, and the matplotlib package for embedding the graph. The inputs ensure that the user inserts the appropriate values and display an error message if not.
- Please keep in mind that the GUI (and the whole app) was developed and tested on a macOS machine so pardon any inconsistency (if any) from the Tkinter package while running the app in a different environment.

### References
- [Embedding in Tk - Matplotlib](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html)

## Testing 
- I used the unittest testing package for Python for creating and running unit tests that heavily tests the operations of the arithmetic interpreter.

## Installation
- Open the terminal and navigate to the desired location for cloning the repository
- Run the following commands
```commandline
    git clone https://github.com/amirhesham65/function-plotter.git
    cd cd function-plotter/
    pip install virtualenv
    virtualenv mypython
    source mypython/bin/activate
    pip install matplotlib
    python3 main.py
```
- if you are using windows, you can access the virtualenv by
```commandline
    mypthon\Scripts\activate
```