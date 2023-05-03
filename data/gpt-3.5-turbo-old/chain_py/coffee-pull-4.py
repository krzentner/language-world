# Steps:
#  1. Put the gripper above the handle of the mug
#  2. Drop the gripper around the handle
#  3. Grab the handle
#  4. Pull the mug towards the target location
#  5. Release the handle
# First, put the gripper above the handle of the mug.
if check("the robot's gripper is not vertically aligned with the mug handle"):
    robot.place("gripper above the mug handle")
# Once the gripper is above the handle, we should drop it around the handle.
if check("the robot's gripper is above the mug handle and the gripper is open"):
    robot.drop("gripper around the mug handle")
# If the gripper is around the handle, we can probably grab the handle.
if check("the robot's gripper is around the mug handle"):
    robot.grab("handle of the mug")
# Now that we have a hold on the handle, we can pull the mug towards the target
# location.
if check("the robot's gripper is holding the mug and the mug is not near the target location"):
    robot.pull("mug towards the target location")
# Once the mug has reached the target location, we can release the handle.
if check("the mug is at the target location and the robot's gripper is holding the mug"):
    robot.release("handle of the mug")