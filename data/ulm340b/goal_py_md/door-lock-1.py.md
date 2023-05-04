

and write a definition for the function `door_lock` that performs the `door-lock` task.
"""

# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Turn the dial left (anticlockwise)
    #  2. Drop gripper around dial
    #  3. Pull the door open
    #  4. Lock the door by turning the dial
    # First, turn the dial left (anticlockwise).
    if check("the robot's gripper is above door handle"):
        robot.move_gripper("above door handle")
    # Then grab it and pull the door open
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with door handle", close_gripper=True)
    # Once the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.move_gripper("left of the door handle")
    # As long as the gripper is around the dial, we can turn the dial right
    # (clockwise).
    if check("the robot's gripper is near the dial"):
        robot.move_gripper("vertically aligned with the dial")
# I added some steps
# First, put the gripper above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.move_gripper("left of the door handle")
    # As long as the gripper is around the dial, we can turn the dial right
    # (clockwise).
    if check("the robot's gripper is near the dial"):
        robot.move_gripper("vertically aligned with the dial")[eod] [code]"""
WSGI config for django_test_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0