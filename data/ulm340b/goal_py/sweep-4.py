
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Pull the cube to the side
    # We can try to pick up the cube as long as the robot's gripper is above the
    # cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper is not around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube and open, try to grab it by closing the
    # gripper.
    # The cube can be grabbed even from the top with this gripper, as long as
    # the gripper is mostly above the cube.
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# stack: pick up the cube and hold it on top of the other cube
def stack(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Lift cube into the air
    #  5. Lower cube down onto other cube
    # First, put the gripper roughly above the cube.
    # Because the cube is very large, we don't have to be too precise about
    # this.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("above the cube", close_gripper=True)
    # If the gripper is around the cube, try to grab it by closing the gripper.
    if check("the robot's gripper is around the cube and the robot