# Steps:
#  1. Put the gripper above the coffee mug
#  2. Grab the handle of the coffee mug
#  3. Lift the coffee mug up
#  4. Move the coffee mug to the target location
#  5. Lower the coffee mug to the target height
# First, put the gripper above the coffee mug.
if check("the robot's gripper is not above the coffee mug"):
    robot.reach("to coffee mug")
    robot.put("gripper above coffee mug")
# If the coffee mug's handle is not inside the gripper, grab the handle.
if check("the handle of the coffee mug is not inside the gripper"):
    robot.move("gripper to coffee mug handle")
    robot.grab("coffee mug handle")
# If the gripper is holding the coffee mug, lift it up.
if check("the gripper is holding the coffee mug"):
    robot.lift("coffee mug")
# If the coffee mug is not at the target location, move it to the target location.
if check("the coffee mug is not at the target location"):
    robot.move("coffee mug to the target location")
# If the coffee mug is not at the target height, lower it to the target height.
if check("the coffee mug is not at the target height"):
    robot.lower("coffee mug to target height")