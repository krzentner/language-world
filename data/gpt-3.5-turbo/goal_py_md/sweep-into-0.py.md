# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the target location
    # First, put the gripper above the cube so we don't accidentally hit it
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube, put it around the cube
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("over the cube", close_gripper=True)
    # Once we have the cube, move it to the target location
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("near the target location")