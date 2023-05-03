# Steps:
#  1. Put gripper around lever
#  2. Rotate gripper upwards to pull lever
# We need to put the gripper around the lever before we can pull it, so first
# check if it's lined up.
if check("the robot's gripper is not around the lever"):
    robot.drop("gripper around lever")
# If the gripper is around the lever, we can just rotate it upwards to pull the
# lever up.
if check("the robot's gripper is around lever"):
    robot.rotate("gripper upwards to pull lever")