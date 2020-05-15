# Modified-N-Puzzle-A-Solver

This is a simple A* search algorithm for solving a modified N-Puzzle

### Programming Language Used - Python 3.7.4

### In the implementation we have 3 .py files namely,

•	constant.py
•	state.py
•	main.py

In the constant.py we hold the all the constants that we need in the implementation like the symbol of the empty string and number of empty of strings (Even though the problem asks only to solve two empty locations configurations I have generalized the implementation to solve for any number of empty locations, 
we only have to change the value of NumberOfBlanks to the number of empty locations).

In the state.py we create the State class where it holds the values like parent state, heuristic type, heuristic cost etc. 
In this class we also have functions like, expand() which will expand the current state, 
getBlanksPos() to get the postions of the empty locations etc.

In main.py (figure 5) we have the function to do the A* search. In this file we also handling the inputs and outputs as well.
