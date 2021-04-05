"""
This class controls the movement of rovers and rotation of the rover around z axis
Point to note: In general a rover can be actually allowed to face any direction in spherical
                    3D given by any two angles
"""

# import the math for the use of pi
import math as mt
# import Rover_position class to keep track of the rovers
from MarsRover import Rover_position


# rover_position initialised for the rover rotations and position setting
class Rover_controller(Rover_position.Manager):

    def rotate(self, rover_id, Anglongtude, theta):

        """ The function rotate consists of the following arguments:

                rover_id.- label that keeps track of rover

                Anglongtude- label which carries Angular value which provides  longitude of rover.it is the angle
                that allows rotations around the Z axis (longitude)
                Note:  rotations are a multiple of Pi/2 only

                theta.- Angular value which provides latitude of rover.
               it is the angle measured from the Z axis (latitude)
               Also Note:theta = 0

        """
        # Only rotations by 90 degrees are only allowed around the Z axis
        # (theta = 0) remains constant
        if (theta == 0.) and (Anglongtude % (mt.pi / 2)) == 0.:
            # If the result is consistent, the rover id is set
            r = self.get_rover(rover_id)
            # we set longitude and latitude values for the direction of the rover
            lon, lat = r.direction
            lat += theta
            lon += Anglongtude
            # the direction is obtained by longitude and latitude
            r.direction = (lon, lat)
        # ... otherwise an exception is raised
        else:

            print('   ')
            print(' =' * 33)
            print('   ')
            print('  Sorry there is an issue with the rover rotation! ')
            print('   ')
            print(' =' * 33)
            print('   ')

            raise Exception('Invalid rover rotation')

    def move(self, rover_id, displacement):

        """Rover displacement function with Arguments as follows

                 rover_id- label that keeps track of rover

                displacement- it is the magnitude of displacement
                               the rover will experiment through the transition"""

        # The first issue is to  make sure the displacement is positive and also an integer
        if isinstance(displacement, int) and displacement > 0:
            # If valid continues to get rover id
            r = self.get_rover(rover_id)
            # initialise rover coordinates
            x, y, z = r.position
            # we get direction spherial locational information
            phi, theta = r.direction
            # we get the actual cartesian coordinates from the spherical ones
            x += int(mt.sin(theta) * mt.cos(phi))
            # here we are enforcing the actual  coordinates of rover to be integer
            y += int(mt.sin(theta) * mt.sin(phi))
            z += int(mt.cos(theta))

            # validate is the position is completely allowed
            self.check_position((x, y, z))
            r.position = (x, y, z)
            # we update displacement
            self.move(rover_id, displacement - 1)

        # if the displacement is invalid an exception is raised
        elif displacement < 0:

            print('   ')
            print(' =' * 33)
            print('   ')
            print('  OOPS LOOKS LIKE YOU ARE ATTEMPTING TO MOVE THE ROVER BACKWARDS! WHICH IS NOT ALLOWED ')
            print('   ')
            print(' =' * 33)
            print('   ')

            raise Exception('THE ROVER ONLY MOVES FORWARD')

        # if the displacement is not integer we raise another  exception
        elif not isinstance(displacement, int):

            print('   ')
            print(' =' * 33)
            print('   ')
            print('   OOPS  YOU ARE ATTEMPTING TO MOVE ROVER BY A QUARTER LESS MOVEMENT!')
            print('   ')
            print(' =' * 33)
            print('   ')

            raise Exception('ONLY INTEGER VALUES ARE ALLOWED FOR DISPLACEMENTS')
