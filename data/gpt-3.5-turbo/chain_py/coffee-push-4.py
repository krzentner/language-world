# Steps:
#  1. Put gripper above mug
#  2. Grab mug with gripper
#  3. Lift mug off surface
#  4. Move gripper to target location
#  5. Lower mug onto surface at target location
# First, move the gripper above the mug.
if check("the robot's gripper is not above the mug"):
    robot.move("gripper to above mug")
# If the gripper is not closed, grab the mug with it.
if check("the robot's gripper is open and near the mug"):
    robot.grab("mug")
# Once the mug is in the gripper, lift it off the surface.
if check("the mug is in the gripper"):
    robot.lift("mug off surface")
# Move the gripper to the target location.
if check("the gripper is holding the mug and not at the target location"):
    robot.move("gripper to target location")
# Lower the mug onto the surface at the target location.
if check("the gripper is holding the mug and at the target location"):
    robot.lower("mug onto surface at target location")