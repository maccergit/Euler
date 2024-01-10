# Euler
Eclipse projects for Project Euler

Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems. See http://projecteuler.net for more info.

I am using Python to explore these problems, partly because Python has built-in support for large numbers (thousands of digits) and because it has a rich numerical library. This repo contains the Eclipse PyDev projects for my exploration of Project Euler.  Each problem typically has multiple implementations that all return the same answer - they are explorations is implementing different approaches to solving the provided problem in Python.  Each implementation includes an "assert" to confirm the solution gives the answer that was provided in the problem statement, along with code that returns the answer to the problem statement.  Each implementation then finishes with timing information - a tabular output of some simple test times, followed by a pyplot graph showing the performance as the problem scales up.

NOTE : Several files require extra Python modules to be installed in order to run - they will need to be installed in PyDev (which uses pip), or on the command line using
"pip install MODULE_NAME"

- utils.timing : "timeit" is a standard Python library that is already installed with Python, but "matplotlib" is not and needs to be installed.
- utils.prod : "operator" and "functools" are both standard Python libraries.  Python 3.8 introduced "math.prod()" which obsoletes rolling your own version of "prod()".
- prob002/04 : "math" is a standard Python library.
- prob002/05 : "sympy" is not standard and needs to be installed.  Note that using it with PyDev requires Java 11 or later (I'm using Java 17) and a recent Eclipse.
