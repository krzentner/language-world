# Steps:
#  1. Put the gripper above the cube
#  2. Grab the cube with the gripper
#  3. Move the cube to the target location while aligning it with the gripper
# First, put the gripper above the cube
if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
# If the gripper is not around the cube, we should grab it with the gripper
if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
# If the gripper is around the cube, we can start moving it to the target location
if check("the robot's gripper is around the cube"):
    # Align the cube with the gripper if necessary
    if check("the cube is not aligned with the gripper"):
        robot.align("cube with gripper")
    # Move the gripper and the cube to the target location
    robot.slide("gripper and the cube to the goal")