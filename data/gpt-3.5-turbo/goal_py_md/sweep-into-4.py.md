# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Locate the cube
    #  2. Put the gripper above the cube
    #  3. Drop the gripper around the cube
    #  4. Close the gripper around the cube
    #  5. Move the cube towards the target location
    #  6. Release the cube at the target location
    # First, locate the cube.
    if check("the cube is not visible"):
        robot.move_head("look for the cube")
    # Once the cube is located, put the gripper above it.
    if check("the cube is visible and the robot's gripper is not above the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # After the gripper is positioned, drop it around the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube")
    # Then, close the gripper around the cube.
    if check("the robot's gripper is around the cube and the robot's gripper is not closed"):
        robot.move_gripper("above the target location", close_gripper=True)
    # Move the cube towards the target location.
    if check("the robot's gripper is closed and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Release the cube at the target location.
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.move_gripper("above the target location", close_gripper=False)