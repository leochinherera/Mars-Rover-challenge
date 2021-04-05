MARS ROVER CHALLENGE

1.    PROBLEM DESCRIPTION

a)     Input:

The problem requires input from the user which is then fed into the solution. The input consists of upper-coordinates of the plateauand lower coordinates that holds (x,y)(0,0)

In this problem each rover has two lines of input as follows:

 I.            First line gives the rover’s position

II.            Second line consists of instructions telling the rover to exploit the plateau

The rover position is prescribed by two integers and letters which are separated by white spaces of (x,y) coordinates rovers rotation. Therovers cannot move in a pair they move sequentially meaning one rover cannot move when the other is in motion.

b)    Output

The final coordinates of the rover is the output of the problem and can be illustrated by the following example

Test Input:

`47`

`1 3 N`

`LMRMLMRMM`

`41 E`

`LMRMMRMLRM`

Expected Output:

`61 N`

`5 2 E`

2.    How to run the code and tests

a)      Running of the code

From the Mars Rover challenge master project there is a subfolder Mars rover, then we execute the class Mars_Rover_main.py using the python command line or using any IDE for python, e.g. PyCharm

After execution it will display instructions on the screen for user to follow

b)      Running the test

The test modules are found in the project subfolder Rover tests class. There are two scripts for testing, ‘correct’ to check that all tests set are passed and wrong one set purposely wrong to show that the tester shows mistakes.

3.    CREATIVE EXTRAS

a)      Think about the interface to your problem, should it run on a command line? How does it receive input? Can I connect it through TCP using Telnet?

Solution basis:

Basically, my interface to the problem requires a command line this is because it will be easier to get a TCP connection using telnet. Telnet uses bidirectional interactive text-oriented communications facility using a virtual terminal connection.Telnet uses command line to send and receive responses.

To receive input, we use telnet because it is a text-only protocol, you cannot see any graphics, nor can you transfer files and it is a two-way protocol it can send and receive responses. For instance we can input (x,y)coordinates and receive output response on the current position of the rover.

b)      Think about visualisation of the conceptual model. Can I view the rover’s position in a grid at the start or end of a program run?

 

Answer:

You cannot view rovers inside the grid squares instead they are at the intersections. This problem can be solved by hand using visual conceptual model will let you catch errors that would otherwise cause problems if you encountered them for the first time in the build itself.

