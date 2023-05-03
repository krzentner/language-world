# Steps:
#  1. Line up the gripper with the hammer
#  2. Grab the hammer with the gripper
#  3. Line up the gripper with the nail
#  4. Hit the nail with the hammer
# First, line up the gripper with the hammer.
if check("the robot's gripper is not vertically aligned with the hammer"):
    robot.put("gripper above hammer")
# If the gripper is lined up with the hammer from the top view, grab the hammer.
if check("the robot's gripper is vertically aligned with the hammer"):
    robot.grab("hammer handle")
# Once the gripper has the hammer, line up with the nail.
if check("the robot's gripper is holding the hammer and the gripper is not vertically aligned with the nail"):
    robot.put("gripper above nail")
# Finally, hit the nail with the hammer.
if check("the robot's gripper is vertically aligned with the nail and the hammer head is above the nail"):
    robot.hit("nail with hammer")