"""

test class  Rover_direction library used in the
MarsRover Challenge program.

It used to show positive testing of module

In this instance we make use of unittest from Python 3.9.

"""

# We import the python  math module to make use of Pi
import math as mt

# Import python unittest for testing
import unittest
# Import library to be tested
from MarsRover import Rover_Direction

"""Test Rover direction class consists of the following functions :


    1) test_rover_rotate : Function that tests rotations

    2) test_rover_move : Function that  tests the rover movement

    3) test_rover_operation : Function that tests rover rotations and
                           displacements"""


class TestRoverDirection(unittest.TestCase):

    def test_rover_rotate(self):
        """ Function that tests rotations movements """

        # Recall that class is created by setting lower left
        # and upper right coordinates of grid:lower left --> (0,0,0),upper right ---> (5,5,0)
        # Dependency for this class are  to follow: Rover_Direction.py
        # it is solved by the following problem
        test_rover_rotate = Rover_Direction.Rover_controller(((0, 0, 0), (5, 5, 0)))

        # we set up the rover at a position and its direction solved by
        # this statement
        test_rover_rotate.add_rover('id_1', (2, 1, 0), (mt.pi / 2, mt.pi / 2))

        # We test the rover 90 degrees clockwise
        test_rover_rotate.rotate('id_1', -mt.pi / 2, 0)

        # test it to check it rotates
        self.assertEquals(test_rover_rotate.get_rover('id_1').direction, (0., mt.pi / 2))

        # We test it 90 degrees  anticlockwise
        test_rover_rotate.rotate('id_1', mt.pi / 2, 0)

        # test if it rotates again
        self.assertEquals(test_rover_rotate.get_rover('id_1').direction, (mt.pi / 2, mt.pi / 2))

    def test_rover_move(self):
        """Function that  tests the rover movement """

        # we set up the rover at a position and its direction solved by
        # this statement
        test_rover_move = Rover_Direction.Rover_controller(((0, 0, 0), (5, 5, 0)))

        # we add a rover to test its movement direction with the following
        # statement of the problem
        test_rover_move.add_rover('id_2', (2, 1, 0), (mt.pi / 2, mt.pi / 2))

        # test one unit on each grid displacements
        test_rover_move.move('id_2', 1)

        # put it on test
        self.assertEqual(test_rover_move.get_rover('id_2').position, (2, 2, 0))

        # test it on a no movement displacements
        test_rover_move.move('id_2', 0)

        # put it on a test
        self.assertEqual(test_rover_move.get_rover('id_2').position, (2, 2, 0))

        # test one unit on each grid displacements
        test_rover_move.move('id_2', 1)

        # test final rover position
        self.assertEqual(test_rover_move.get_rover('id_2').position, (2, 3, 0))

    def test_rover_operation(self):
        """ Function that tests rover rotations and
                           displacements """

        # for the rover to operate is we set up lower left
        # and upper right coordinates of grid:lower left --> (0,0,0),upper right ---> (5,5,0)
        # Dependency for this class are  to follow: Rover_Direction.py
        # the operation solution is solved as follows
        test_rotate_move = Rover_Direction.Rover_controller(((0, 0, 0), (5, 5, 0)))

        # we add a rover to test its movement direction with the following
        # statement of the problem
        test_rotate_move.add_rover('id_3', (2, 1, 0), (mt.pi / 2, mt.pi / 2))

        # We test one unit on each grid displacements
        test_rotate_move.move('id_3', 1)

        # put it on a test
        self.assertEqual(test_rotate_move.get_rover('id_3').position, (2, 2, 0))

        # ...followed by a rotation 90 degrees clockwise
        test_rotate_move.rotate('id_3', -mt.pi / 2, 0)

        # put it on a test
        self.assertEqual(test_rotate_move.get_rover('id_3').direction, (0., mt.pi / 2))

        # test it on a one unit grid displacements
        test_rotate_move.move('id_3', 1)

        # put on a test again test it again
        self.assertEqual(test_rotate_move.get_rover('id_3').position, (3, 2, 0))


if __name__ == '__main__':
    unittest.main()
