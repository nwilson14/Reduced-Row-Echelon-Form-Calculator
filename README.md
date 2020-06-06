# Reduced-Row-Echelon-Form-Calculator
A calculator to find the Row Echelon and/or Reduced Row Echelon Form of a Matrix. The inspiration behind this program comes from this website: http://www.math.odu.edu/~bogacki/cgi-bin/lat.cgi?c=rref 
I referenced this website many times to check my work in the Linear Algebra course I took my sophomore year of college. Eventually, I figured I understood the algorithm to finding the RRE form of a Matrix that I could write my own program, so I would not need to reference the website over and over again.

## Overview of Algorithm
(Simplified terms)
1) First get a 1 in the first position of the Matrix
2) Get 0's below the first one
3) Get a leading 1 in the next row
4) Get 0's below that 1
5) Repeat steps 2 and 3 until bottom of matrix
6) Once in upper triangular form, eliminate all numbers above all leading 1's
7) NOTE: Anything done to one number in a row must be done to the entire row

## Notes
Algorithm can be improved!
When finding Reduced Row Echelon Form, the algorithm finds all the leading 1's in the matrix by using nested for loops and traversing the entire matrix again. However finding the 1's is not needed because previously, when creating normal Row Echelon Form, the position of all the leading 1's are found. Therefore, to increase efficiency of this program, i.e. improve it, simply create a list/array to hold the positions of all the leading 1's and reference that list with a single for loop when finding reduced row echelon form, instead of
using two for loops to locate each leading 1 again.

Furthermore, the algorithm cannot handle rows of 0's yet. This still needs to be implemented in the program.

To make the program nicer to look at and use, a UI will be created using pygame. For now, the program outputs each step and how the matrix changes. It is outputted onto the terminal.

I am aware that in Python the library "sympy" has a built-in function that can find the reduced row echelon form of a Matrix, Matrix.rref(). I did this project as a fun way to test myself and my understanding of the process to reduce a Matrix to reduced row echelon form and to get some practice coding :D.
