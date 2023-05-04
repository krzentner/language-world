

Your program will be evaluated on a number of tests, which are not shown here.

'''

# Code from lesson 4.
def door_unlock(robot):
    '''Unlock the door by turning the door handle.'''
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.twist("clockwise")
    if check("the dial is not fully turned clockwise"):
        robot.twist("clockwise")


# Test code, not shown to students.
tests = '''\
>>> def robot_checks():
...     yield check, "the robot's gripper is not near the drawer handle"
...     yield check, "the robot's gripper is forward aligned with drawer handle"
...     yield check, "the robot's gripper is not near reach target"
...     yield check, "the robot's gripper is not vertically aligned with the peg"
...     yield check, "peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"
...     yield check, "the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"
...     yield check, "peg is horizontally aligned with hole"
...     yield check, "the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"
...     yield check, "the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"
...     yield check, "the robot's gripper is near the puck and the puck is below the robot's gripper"
...     yield check, "the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"
...     yield check, "the robot's gripper is near the window handle"
...     yield check, "the robot's gripper is in front of the window handle"
...     yield check, "the robot's gripper is not vertically aligned with button"
...     yield check, "the robot's gripper is vertically aligned with button"
...     yield check, "the robot's gripper is not above the puck"
...     yield check, "the robot's gripper