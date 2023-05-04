
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Move gripper towards door hinge
    #  3. Move gripper harder towards door hinge
    # If the gripper is right of the door handle as seen from in front, go back to
    # grabbing the handle again.
    if check("the robot's gripper is right of the door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # If the gripper is in front of the door handle as seen from in front, move
    # it to the left.
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("left of the door handle")
    # If the gripper is left of the door handle as seen from in front, start
    # closing the door by moving the gripper in the direction of the hinge.
    if check("the robot's gripper is left of the door handle"):
        robot.move_gripper("vertically aligned with the door handle")

# drawer-close-topdown: push the drawer closed from above
def drawer_close_topdown(robot):
    # Steps: