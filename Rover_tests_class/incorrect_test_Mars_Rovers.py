"""

test class  Rover_direction library used in the
MarsRover Challenge program.

It used to show nagative testing of module





"""

# Import unittest for testing
import unittest

# We import sys Pyhton library to be sure ...
# ... and we do so
# Import main module; to be tested end-to-end
from MarsRover import Mars_Rover_main

"""This test module test contains MarsRoverTest class
with the following functions:
   
    test_MarsRover_main : function that does 
                        the end-to-end testing
"""


class TestMarsRover(unittest.TestCase):

    def test_MarsRover_main(self):
        """
            The function is to test the whole mars rover mission
        """

        # we provide input as a user would probably do.
        # This input will consists two rovers.
        input = '5 5\n1 2 N\nLMRMLMLRM\n3 3 E\nMMRMMRMRRM'

        # this a purposely put to produce wrong output
        output = '1 3 N\n5 1 S\n'

        # Lets create dispatcher, as we did in the main program,
        dispatcher = Mars_Rover_main.Mars_Rover_main()

        # We parse input provided...
        dispatcher.input_parser(input)

        # Parse the input
        dispatcher.dispatch_input()

        # The output to be displayed will be found in MarsRoverMain class
        # display_output function
        display_output = dispatcher.display_output()

        # Finally do the test
        self.assertEquals(display_output, output)


if __name__ == '__main__':
    # Doing the test...
    unittest.main()
