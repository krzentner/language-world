

Your program must move the robot's gripper to the specified `target location`, without grasping the puck.
It should use the function `robot.move_gripper()` to move the robot's gripper, and `robot.step()` to step the simulation forward.
"""

# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

    robot.step()
    if check("the puck is not around the target location"):
        robot.move_gripper("around the target location", close_gripper=True)
    if check("the puck is not around the target location"):
        robot.move_gripper("left of the target location", close_gripper=True)
    if check("the puck is not around the target location"):
        robot.move_gripper("below the target location", close_gripper=True)

    robot.step()
    if check("the puck is not around the target location"):
        robot.move_gripper("right of the target location", close_gripper=True)
    if check("the puck is not around the target location"):
        robot.move_gripper("right of the target location", close_gripper=True)
    if check("the puck is not around the target location"):
        robot.move_gripper("in front of the target location", close_gripper=