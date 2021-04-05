"""

Module to test rover position library used in the
MarsRover Challenge program.

We make use of unittest from Python.


"""

# We import the math module to make use of Pi
import math as mt

# Import unittest for testing
import unittest

# We import sys Pyhton library to be sure ...

# import class  to be tested
from MarsRover import Rover_position

"""This test module test contains Test Rover position class
with following functions test

  -test_allocate_position :  this Function tests rotations function
                              allocates rover of free available positions 

    - test_rover_inside_grid :Test rover if its within required grid

   -test_add_rovers : it test the adding of rover on the mars"""


class TestRoverPosition(unittest.TestCase):

    def test_allocate_position(self):
        """
            Function tests rotations function allocates rover of free available positions
        """

        # here we set grid providing lower left and upper right coordinates
        test_rover_postion = Rover_position.Manager(((0, 0, 0), (5, 5, 0)))

        # we add a rover with a specific given id to a position with given direction
        test_rover_postion.add_rover('id_1', (3, 3, 0), (0, mt.pi / 2))

        # We now test if the position is already taken up by the following example coordinates
        [self.assertFalse(test_rover_postion.available_position((x, y, 0))) if (x, y, 0) == (3, 3, 0)
         # if the position is not taken we  assert True
         else self.assertTrue(test_rover_postion.available_position((x, y, 0)))
         # it is done for values of x and y in the square [0,5] X [0,5]
         for x in range(6) for y in range(6)]

    def test_rover_inside_grid(self):
        """ Test rover if its within required grid """

        # We firstly set  grid with lower left and upper right coordinates
        test_manager = Rover_position.Manager(((0, 0, 0), (5, 5, 0)))

        # Test actual points inside a grid
        self.assertTrue(test_manager.rover_inside_grid((0, 0, 0)))
        self.assertTrue(test_manager.rover_inside_grid((5, 5, 0)))

        # and test points which are not
        self.assertFalse(test_manager.rover_inside_grid((0, 6, 0)))
        self.assertFalse(test_manager.rover_inside_grid((-1, 0, 0)))

        # Let's remove a rover from the (x.y)grid points
        self.assertFalse(test_manager.rover_inside_grid((3, 3, 1)))

    def test_add_rovers(self):
        """ Function that tests adding of rover """

        #  We firstly set  grid with lower left and upper right coordinates
        test_manager = Rover_position.Manager(((0, 0, 0), (5, 5, 0)))

        # We  add a rover with its specific  id, position and direction
        test_manager.add_rover('id_1', (3, 4, 0), (mt.pi / 2, 0))

        # Then check if its successfully added
        self.assertTrue('id_1' in test_manager.rovers.keys())


if __name__ == '__main__':
    unittest.main()
