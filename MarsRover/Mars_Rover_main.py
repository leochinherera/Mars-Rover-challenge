"""

Introducing  the execution class for the Mars Rover Challenge
this class contains:
-class Mars_Rover_main_ as object
-main() function  for execution of the rovers
*************************************************************
"""
# We do import os for the  basic interaction with command line
import os
# import library that handles all moves and rotations of the rover
from pip._vendor.distlib.compat import raw_input
# Import Rover_Direction class.
import Rover_Direction
# import the math for the use of pi
import math as mt


# Initialising  class Mars_Rover_main as an object
class Mars_Rover_main(object):
    """
 In this class we created typical dictionary of directions
 so that  the rover rotation values will be on  Z-axis as opposed
 to set a simple list or strings such as 'NSEW'
 -the set of dictionary for the  direction  of the rover are as follows

  N = North, associated with theta = 90 degrees
  S = North, associated with theta = 270 degrees
  E = North, associated with theta = 0 degrees
  W = North, associated with theta = 180 degrees

"""
    # Direction is associated with the dictionary
    Direction = {'S': 3 * mt.pi / 2, 'N': mt.pi / 2, 'E': 0, 'W': mt.pi}
    # set user input which is allowed in the commands
    # L = Left
    # R = Right
    # M = Move
    Commands = ['L', 'R', 'M']

    # initialization function
    def __init__(self):
        # Initialize rover controller
        self.commander = None

        # Initialize  Array that holds instructions
        self.Commands = []

        # Initialize Array for the rovers
        self.rovers = []

    def rover_welcome_message(self):
        """ Function to display welcome screen and  instruction for the user """
        # We display the instructions for the user
        print('   ')
        print('*                                      *')
        print('*   WELCOME TO THE MARS ROVER CHALLENGE            *')
        print('*                                      *')
        print('   ')
        print('You will prompted to enter: ')
        print(' I) Upper-Right coordinates of grid ')
        print(' ii) Rovers position and direction ')
        print('III) Sequence of direction  commands ')
        print('*****************************************************************   ')
        print('Please enter the information for one or more  rover.')
        print('Once you  finished providing rovers and information')
        print('please hit enter when you are asked again Enter (x y) Direction.:')
        print('******************************************************************   ')
        print(' Continue')
        print('   ')
        print('******************************************************************')
        print('   ')

    def fmove(self, rover_id):

        """ This function moves rovers to a forward one grid position Argument:
        rover_id is label that identifies rover and  to keep track of it """

        # The rover is only allowed to move one unit forward
        self.commander.fmove(rover_id, 1)

    def L_rotate(self, rover_id):

        """ Function allows rover only to rotate 90 degrees counterclockwise
         rover_id is label that identifies rover and  to keep track of it
        """

        # Function to rotate rover 90 degrees counterclockwise
        self.commander.rotate(rover_id, mt.pi / 2, 0)

    def R_rotate(self, rover_id):

        """ Function that  allows rover only to rotate 90 degrees clockwise:
        rover_id is label that identifies rover and to keep track of it
         """

        # Function to rotate rover 90 clockwise
        self.commander.rotate(rover_id, -mt.pi / 2, 0)

    # Function that parses input strings Argument received from user on the  command line
    def input_parser(self, input):
        # We split the user input with a new line"\n"
        input = input.split('\n')
        # We initialize coordinates for the user input
        coordinates = self.coordinates_parser(input[0])
        # Also the controller on the same instance
        self.commander = Rover_Direction.Rover_controller(((0, 0, 0), coordinates))

        # User first line input from the command line
        for line in input[1::2]:
            # The input parsed to get information about rover  location and direction
            self.parse_add_rover(line)
        # User second line input from the command line
        for line in input[2::2]:
            # The input parsed to get information about rover  location and direction
            # Instructions for the corresponding rover
            self.User_instruction_parser(line)

    # Function that parses and adds string instructions Argument
    # input.- Instructions received by user from command line
    def User_instruction_parser(self, input):

        # This appends instructions from the command line to the Commands array[]
        self.Commands.append([strg for strg in input.strip()])

    def coordinates_parser(self, coordinates):

        """ Function responsible for parsing the upper coordinates (x,y) coordinates from the user
       provided coordinates.- Coordinates (x,y)  provided by user from the command line
        """

        # We use try to feed the tuple for the coordinates to prevent  unexpected format error
        try:
            # We return the desired tuple with integers
            return tuple([int(upper_corner) for upper_corner in coordinates.strip().split(' ')] + [0])
        # ...exception with a message
        except ValueError as e:

            print('   ')
            print(' =' * 30)
            print('   ')
            print('      Please  specify coordinates correctly ')
            print('   ')
            print(' =' * 30)
            print('   ')
            raise ValueError('Coordinates must be a (int , int)  please try again!')

    def controller_rover_direction(self, direction_val):

        """ It checks correct direction  of rover Argument """
        # direction_val.- its the Value of angle within allowed directions returns:
        if not direction_val in self.Direction.values():
            print('   ')
            print(' >' * 10)
            print('   ')
            print('      SORRY THERE SEEMS TO BE AN ISSUE WITH ROVERS DIRECTION! ')
            print('   ')
            print(' >' * 10)
            raise Exception('Controller direction unknown error %s'
                            % str(direction_val))
        else:
            # direction_key.- Coordinates point associated with value provided in direction_val
            for direction_key in self.Direction.keys():
                if self.Direction[direction_key] == direction_val:
                    return direction_key

    def Direction_checker(self, direction):

        """ Function that checks the  direction coordinates  given are within the  allowed Scope:
        direction.- Value of coordinates provided by user  """

        # If a direction given is NOT in the valid set (N,S,E,W)....
        if not direction in self.Direction.keys():
            # ... we display a message of warning and raise exception
            print('   ')
            print(' >' * 15)
            print('   ')
            print('   Invalid  Coordinates have been  PROVIDED! ')
            print('   ')
            print(' >' * 15)
            print('   ')
            raise Exception('User provided a invalid coordinates  %s'
                            % str(direction))

        # ... we proceed with the given coordinates
        else:
            return self.Direction[direction]

    def parse_add_rover(self, input):

        """ Function that parses one or more rovers to the argument given by the user:
        userinput.- String representing a rover given by user coordinates (x,y)
        """

        # In this instance we strip and split line by line so we  can feed to the rover.
        rover = input.strip().split(' ')
        # Here making  sure the coordinates is capitalized to have valid matching
        # ..with dictionary keys
        rover[2] = rover[2].upper()
        # Here we are expecting an input length that consists of three elements (e.g 5 6 N)
        if len(rover) == 3:
            # our expectation is the user to  enter a tuple according to the  Coordinates (x y)
            # and facing direction  (W or N or E or S)...
            try:
                position = tuple([int(v) for v in rover[0:2]] + [0])
            #
            # ... if we don't get our expectation we raise an error
            # which the error  message is ...

            # except ValueError, e:
            except ValueError:
                print('   ')
                print(' >' * 20)
                print('   ')
                print('      ROVER POSITION WAS NOT CORRECTLY SPECIFIED!  ')
                print('   ')
                print(' >' * 20)
                print('   ')
                raise ValueError('ERROR rover position  not been correctly specified!')

            direction = (self.Direction_checker(rover[-1]), mt.pi / 2)
            self.commander.add_rover(input, position, direction)
            self.rovers.append(input)  # rover id starting position and heading
        # ... in case the line given has no three elements, we raise an exception
        elif len(rover) != 3:
            print('   ')
            print(' =' * 20)
            print('   ')
            print('      ROVER INCORRECTLY UNSPECIFIED')
            print('   ')
            print(' =' * 20)
            print('   ')
            raise Exception('Please check coordinates and direction given!')

    def dispatch_input(self):

        """ Function which  dispatches rover input to the Controller """
        # For rover and commands in given set of instructions...
        for rover, Commands in zip(self.rovers, self.Commands):
            # ... we iterate over instructions in the given Command
            # to Validate Left, Right, or Move
            for user_instruction in Commands:
                # If Left then we use L_rotate function..
                if user_instruction == 'L':
                    self.L_rotate(rover)
                # If Right then we use the R_rotate function..
                elif user_instruction == 'R':
                    self.R_rotate(rover)
                # If Move then  the rover move with the move function
                elif user_instruction == 'M':
                    self.fmove(rover)
                # If none then we raise exception
                else:
                    print('   ')
                    print(' =' * 20)
                    print('   ')
                    print('      ERROR INVALID INSTRUCTION HAS BEEN GIVEN!')
                    print('   ')
                    print(' =' * 20)
                    print('   ')
                    raise Exception('Invalid  instruction given %s' % str(user_instruction))

    def display_output(self):

        """ Function that provides current rover position:
        output.- The final position of rover to displayed on the screen for  user's information
        """
        # output to be displayed as a string
        output: str = ""

        # For every rover in the collection...
        for rover in self.rovers:
            r = self.commander.get_rover(rover)
            direction: str = self.controller_rover_direction(r.direction[0])
            output += '%d %d %s\n' % (r.position[0], r.position[1], direction)

        return output


# Main function for execution
def main():
    """ To  excecute main just run python Mars_Rover_main.py """

    # clean screen for the user
    os.system('')

    # lets Create a dispatcher from our main class
    dispatcher = Mars_Rover_main()

    # Welcome message for the user
    dispatcher.rover_welcome_message()

    # After welcome screen has  been displayed we pause the code
    # until enter is hit by the user..
    raw_input("To continue please press enter to begin the mission of the rover on mars...")

    # clear the screen for the user once again..
    os.system('')

    # We make a blank input be set
    input = ''
    # Instructions for user
    print('Please provide Coordinates of grid as a pair')
    print('E.g. 7 3')
    # We receive coordinates as a raw input from line command
    coodinates = raw_input('Enter upper-right coordinates of grid  (X Y): ')
    # We add upper coordinates provided to command line input
    input += coodinates + '\n'
    # while User keeps entering rovers
    while True:
        # Request position and direction...
        print(' ')
        print('Please enter rover coordinates,')
        print('E.g. 4 3 W OR 5 1 E OR ...')
        print(' ')
        print('If you are satisfied by entering at least one set')
        print('of rover position and coordinates you can press enter to')
        print('continue to see final position of rovers.If not satisfied')
        print('you have privilege to  add more rovers.')
        print(' ')
        # instructing user to enter coordinates
        r = raw_input('Please Enter (xCoord yCoord):')
        # If no info is received
        if r == '':
            # ... we break..
            break
        # ... or else keep adding more input.
        else:
            input += r + '\n'

        # User sequence of commands....
        print('You can  enter sequence of commands ')
        print('E.g. MMLRLMLRM OR MRLMLRMRRL OR ...')
        print(' ')
        # ... we get them as raw input the upper case them
        # for a pure matching we compare with [L,R,M]
        Commands = raw_input('You can enter commands for this rover:').upper()
        # ... Keep adding more.
        input += Commands + '\n'

    # We strip input
    # In case the provided last element of user input is a wrong, we use else to handle it
    if input[-1] == '\n':
        input = input[:-1]
    # ... in other ways leave input without change
    else:
        input = input

    # parsing  the  input
    dispatcher.input_parser(input)
    # Dispatching  the instructions received e.g. LRMlMLRMR
    dispatcher.dispatch_input()
    # clear the screen for the user once again..
    os.system('')
    # ...Displaying a message announcing rovers final positions..
    print('   ')
    print('*' * 20)
    print('*                                      *')
    print('*   FINAL POSITION(S) OF ROVER(S)      *')
    print('*                                      *')
    print('*' * 20)
    print('   ')
    # ...Rovers positions
    print(dispatcher.display_output())


if __name__ == '__main__':
    main()
