# Euler
## Eclipse projects for Project Euler
Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems. See http://projecteuler.net for more info.

I am using Python to explore these problems, partly because Python has built-in support for large numbers (thousands of digits) and because it has a rich numerical library. This repo contains the Eclipse PyDev projects for my exploration of Project Euler.  Each problem typically has multiple implementations that all return the same answer - they are explorations is implementing different approaches to solving the provided problem in Python.  Each implementation includes an "assert" to confirm the solution gives the answer that was provided in the problem statement, along with code that returns the answer to the problem statement.  Each implementation then finishes with timing information - a tabular output of some simple test times, followed by a pyplot graph showing the performance as the problem scales up.

NOTE : Several files require extra Python modules to be installed in order to run - they will need to be installed in PyDev (which uses pip) or via the command line using "pip install MODULE_NAME"

- matplotlib : Used to display timing plot at end of each run.
- math : This is a standard library, but "math.prod()" was introduced in Python 3.8.  The "utils" project includes an implementation of "prod()" for pre-3.8 versions.
- sympy : Used for symbolic math operations in some projects.  Note that using it with PyDev requires Java 11 or later (I'm using Java 17) and a recent Eclipse.
- pyprimesieve : Fast C/C++ implementation of prime sieve functions, used in some projects.
### Wiki
This repo includes a Wiki with detailed documentation - to explore the Wiki, select the "Wiki" tab in the repo or follow this link : https://github.com/maccergit/Euler/wiki
