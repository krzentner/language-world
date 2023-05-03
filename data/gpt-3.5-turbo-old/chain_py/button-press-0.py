# Steps:
#   1. Align gripper with button from the front
#   2. Push the button
# Because we're pressing from the front, we need to align the gripper with the
# button from the front view.
if check("the robot's gripper is not forward aligned with button"):
    robot.move("gripper towards button from front")
# Once the gripper is lined up from the front, just push the button.
if check("the robot's gripper is forward aligned with button"):
    robot.push("button")