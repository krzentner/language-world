
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop the gripper around the cube
    #  3. Close the gripper around the cube
    #  4. Pull the cube up out of the bin
    #  5. Slide the cube above the target bin
    #  6. Move the gripper above the target bin
    #  7. Open the gripper above the target bin
    # We should start by putting the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # Then we should put the gripper around the cube.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is roughly around the cube, we can probably pick it up by
    # closing the gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.move_gripper("horizontally aligned with the cube")
    # Once the cube is held in the gripper, we can move it towards the target
    # bin.
    if check("the robot's gripper is horizontally aligned with the cube"):
        robot.move_gripper("above the target bin")
    # Now, if we're above the target bin, we can open the gripper.
    if check("the robot's gripper is above the target bin"):
        robot.move_gripper("vertically aligned with the target bin", open_gripper=True)

# place-red-in-green: place the red cube in the green bin
def place_red_in_green(robot):
    # Steps:
    #  1. Line up the gripper with the red cube
    #  2. Drop the gripper around the cube
    #  3. Close the gripper around the cube
    #  4. Move the gripper above the target bin
    #  5. Open the gripper above the target bin
    # We should start by putting the gripper above the cube.
    if check("the robot's gripper is not above the red cube"):
        robot.