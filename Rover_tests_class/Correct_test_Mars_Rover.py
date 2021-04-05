"""

test class  Rover_direction library used in the
MarsRover Challenge program.

It used to show positive testing of module

In this instance we make use of unittest from Python 3.9.



"""

# Import unittest for testing
import unittest

# ... and we do so
# Import main module; it is going to be tested end-to-end
from MarsRover import Mars_Rover_main

"""This test module test contains TestMarsRover class
with following function:

     test_MarsRover_main : function that does 
                             the end-to-end testing"""


class TestMarsRover(unittest.TestCase):

    def test_MarsRover_main(self):
        """
          The function is to test the whole mars rover mission
        """

        # we provide input as a user would probably do.
        # This input will consists two rovers.
        input = '5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM'

        # Lets set our expected output
        output = '1 3 N\n5 1 E\n'

        # Lets create dispatcher, as we did in the main program,
        dispatcher = Mars_Rover_main.main()

        # Parse the input
        dispatcher.input_parser(input)

        # we dispatch input once it has been parsed
        dispatcher.dispatch_input()

        # The output to be displayed will be found in MarsRoverMain class
        # display_output function
        display_output = dispatcher.display_output()

        # Finally do the test
        self.assertEqual(display_output, output)


if __name__ == '__main__':
    # Doing the test...
    unittest.main()
