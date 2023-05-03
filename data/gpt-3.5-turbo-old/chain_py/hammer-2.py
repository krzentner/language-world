# Steps:
#   1. Grab the hammer
#   2. Position the hammer above the nail
#   3. Swing the hammer down to hit the nail
# To begin, the robot needs to grab the hammer.
if check("the robot's gripper is not holding the hammer"):
    robot.grab("the hammer")
# Next, the robot needs to position the hammer above the nail.
if check("the robot's gripper is not vertically aligned with the nail and holding the hammer"):
    robot.put("the hammer directly above the nail")
# Finally, the robot can swing the hammer down to hit the nail.
if check("the robot's gripper is vertically aligned with the nail and holding the hammer"):
    robot.swing("the hammer down to hit the nail")