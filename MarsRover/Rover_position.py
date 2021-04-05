"""
This class controls the  rovers and their positions

"""

# We import the math module to make use of Pi
import math as mt


class Rover_position(object):
    """
The rover position class consists of the following

        - __init__ : this is a functional initialisation

        - get_direction: Obtains direction

        - get_rover_position: Obtains the rover position

        - set_direction: Sets which direction  rover moves

        - set_rover_position: Sets position for the rover
    """

    def __init__(self, position, direction):

        """ This is a function that initialize rover

            consists of Arguments:

                position.-  position of rover

                direction.- complies to  movement direction of rover

        """

        # Set position and direction of rover
        self._direction = (direction[0] % (2 * mt.pi), direction[1] % (2 * mt.pi))
        self.position = position
        self.direction = direction

    def get_direction(self):

        """ to get the rovers direction"""

        return self._direction

    def get_rover_position(self):

        """ get the actual rover's position """

        return self._position

    def set_direction(self, direction):

        """ Sets up a rover's direction

            it consists of Arguments as follows :
                direction.- As the  name suggests, direction of rover
        """

        # We validate  if the direction is a tuple and gives  the expected length
        if isinstance(direction, tuple) and len(direction) == 2:
            # if its valid we  proceed to get the corresponding directions through the modulo 2*pi

            pass
        else:
            # If its not valid we raise an exception

            print('   ')
            print(' =' * 32)
            print('   ')
            print('   The direction provided does not have the expected output ')
            print('   ')
            print(' =' * 32)
            print('   ')

            raise ValueError('The direction  provided does not have length 2 that is required')

    def set_rover_position(self, position):

        """ this function Sets up a rover's position

            Arguments:

                position.-  direction of rover position

        """

        # We check This is where we validate the length.
        # ..on this case is as..
        if isinstance(position, tuple) and len(position) == 3:
            # The position is set
            self._position = position
        else:
            # if there is an error we display the following message

            print('   ')
            print(' =' * 32)
            print('   ')
            print('   LOOKS LIKE THE POSITION PROVIDED IS NOT VALID ')
            print('   ')
            print(' =' * 32)
            print('   ')

            raise ValueError('THE POSITION SHOULD HAVE A LENGTH OF 3')

    # We obtain position and direction from property of class
    position = property(get_rover_position, set_rover_position, None)
    heading = property(get_direction, set_direction, None)


class Manager(object):
    """
    The class Manager obtain the given instruction  to be set on a given position
    """

    def __init__(self, coordinates):

        """ this is to  initialise the manager by giving out opposite
            coordinates of the grid of the rover (lower_left and  upper_right)

        """

        # create an empty dictionary  as to keep track of rovers
        self._coordinates = coordinates
        self.rovers = {}
        # Initialise coordinates
        self.coordinates = coordinates

    def get_rover(self, rover_id):

        """ Function that has  object of rover assigned to
            a rover_id

           consists of  Argument:

                rover_id.- A label to identify rover and  keep track of it

        """

        # Validate if a given rover is not in the set of rovers
        # obtained by keys in rovers dictionary...
        if not rover_id in self.rovers.keys():
            # ... if invalid , display an error message and raise an exception

            print('   ')
            print(' =' * 20)
            print('   ')
            print('     It Seems A Rover has been lost!!! ')
            print('      this  ', rover_id, ' is lost?')
            print('   ')
            print(' =' * 20)

            raise Exception('The system cannot find %s rover' % str(rover_id))
        # if the rover is in set of rovers we proceed to place it in a dictionary

        else:
            return self.rovers[rover_id]

    def check_position(self, position):

        """ Function that validate the position of rover if its allowed

            Argument:

                position.- variable suggests position of rover

        """

        if not isinstance(position, tuple) and len(self.coordinates) == 3:
            print('   ')
            print(' =' * 21)
            print('   ')
            print('   THE ROVER POSITION DOES NOT HAVE THE EXPECTED LENGTH ')
            print('   ')
            print(' =' * 21)
            print('   ')

            raise Exception('Rovers position does not  have the right length')
        if not (isinstance(position[0], int) and isinstance(position[1], int)
                and isinstance(position[2], int)):
            print('   ')
            print(' =' * 25)
            print('   ')
            print('   The rover position is not allowed its invalid ')
            print('   ')
            print(' =' * 25)
            print('   ')

            raise Exception('Rovers position is invalid')
        if not self.available_position(position):

            print('   ')
            print(' =' * 25)
            print('   ')
            print('  YOUR ROVER WANTS TO TAKE UP A SPACE OCCUPIED BY OTHER ROVERS')
            print('   ')
            print(' =' * 25)
            print('   ')

            raise Exception('This space is already occupied by another Rover %s' % str(position))
        elif not self.rover_inside_grid(position):

            """
            Note:
            the current requirements of the rover  problem 
            is to only print (x,y) coordinates as the rover is considered 
            to move in a 2D grid 
            """

            pos2D = position[:2]

            print('   ')
            print(' =' * 32)
            print('   ')
            print(' ALERT!! -- ROVER OUT OF BOUND ', pos2D)
            print(' POSITION NOT IN REQUIRED GRID')
            print('   ')
            print(' =' * 32)
            print('   ')

            raise Exception('Rover Position %s is outside  grid ' % str(pos2D))

    def add_rover(self, rover_id, position, direction):

        """this function adds a rover to the manager then it checks if rover being
        added has a unique id and also it is not trying to occupy already occupied space.

        """

        self.check_position(position)
        """first instance is to check position and then after it  proceeds to 
        check whether position has been taken or not by exploiting 
        the keys in dictionary  """
        if not rover_id in self.rovers.keys():
            # If not, we add to rover dictionary...
            self.rovers[rover_id] = Rover_position(position, direction)
        else:
            # ... if occupied we display an error message and raise an exception

            print('   ')
            print(' =' * 25)
            print('   ')
            print('     ERROR AS IT SEEMS YOU TRYING TO DUPLICATE ROVER WITH SAME IDS!!! ')
            print('       THE ROVER ', rover_id, ' ALREADY EXISTS')
            print('   ')
            print(' =' * 25)

            raise Exception('Rover id %s is already occupied' % str(rover_id))

    def rover_inside_grid(self, position):

        """ Function responsible  for checking  if the current position of rover is
            within grid boundaries.It considers the general case of
         3D space (x,y,z) theory

            Argument:

                position.- Position of rover
        """

        # position coordinates
        x, y, z = position

        # Let's get "min" and "max" values of X, Y and Z according
        # to the coordinates given
        # For value x:
        x1 = self.coordinates[0][0]
        x2 = self.coordinates[1][0]
        # For value y:
        y1 = self.coordinates[0][1]
        y2 = self.coordinates[1][1]
        # For value z:
        z1 = self.coordinates[0][2]
        z2 = self.coordinates[1][2]

        return (True if ((x1 <= x <= x2 or x2 <= x <= x1) and
                         (y1 <= y <= y2 or y2 <= y <= y1) and
                         (z1 <= z <= z2 or z2 <= z <= z1))
                else False)

    def available_position(self, position):

        """ Function that validate whether the provided position is open space

            Argument:

                position.- Position of rover

        """

        # The value to be returned  returns True if position is
        # available and False otherwise.
        return (False if position in [r.position for r in self.rovers.values()]
                else True)

    def get_coordinates(self):

        """ Function that obtains coordinates from manager """

        return self._coordinates

    def set_coordinates(self, coordinates):

        """ Function that sets up coordinates from manager
"""
        # We validate if coordinates is a tuple and has two coordinates (X,Y)...
        if isinstance(coordinates, tuple) and len(coordinates) == 2:
            if (isinstance(coordinates[0], tuple) and len(coordinates[0]) == 3 and
                    isinstance(coordinates[1], tuple) and len(coordinates[1]) == 3):
                pass
            else:

                print('   ')
                print(' =' * 25)
                print('   ')
                print('   SEEMS THE SHAPE OF COORDINATES PROVIDED ARE NOT VALID ')
                print('   ')
                print(' =' * 25)
                print('   ')

                raise Exception('The coordinates does not have the proper required  length')
        else:

            print('   ')
            print(' =' * 25)
            print('   ')
            print('   SEEMS THE SHAPE OF CODINATES PROVIDED IS NOT VALID')
            print('   ')
            print(' =' * 25)
            print('   ')

            raise Exception('The coordinates does not have the proper required length')

    # Get coordinates from corresponding class property

    coordinates = property(get_coordinates, set_coordinates, None)
