
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target bin
    # First, put the gripper above the cube so we can pick it up.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # The gripper should be around the cube to pick it up.
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("near the cube")
    # Now that the gripper is around the cube, close it and lift the cube up.
    if check("the robot's gripper is open"):
        robot.move_gripper("above the cube", close_gripper=True)
    # Now, the robot has grabbed the cube and can move it to the target bin.
    if check("the robot's gripper is closed"):
        robot.move_gripper("above the target bin")

# peg-insert-topdown: drop the peg into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Pick the peg up
    #  3. Move the peg above the hole
    #  4. Drop the peg into the hole
    # First, put the gripper above the peg so we can pick it up.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # Move the gripper down around the peg to pick it up.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Close the gripper to lift the peg off the table.
    if check("the robot's gripper is not closed"):
        robot.move_gripper("above the peg", close_gripper=True)
    # Once the peg is lifted up, we can move the peg above the hole.
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.move_gripper("