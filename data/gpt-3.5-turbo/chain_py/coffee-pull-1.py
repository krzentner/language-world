# Steps:
#  1. Put gripper around the handle of the mug
#  2. Pull the mug towards the target location
# To grab the mug, we need to put the gripper around the handle. 
if check("the robot's gripper is not around mug handle"):
    robot.grab("mug handle")
# Once the gripper is around the handle, we can pull the mug towards the target location.
if check("the robot's gripper is around mug handle and the robot's gripper is not near target location"):
    robot.pull("mug towards target location")
# If the mug is near the target location, we can release the gripper to place the mug.
if check("the robot's gripper is near target location"):
    robot.release("mug")