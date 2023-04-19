# Steps:
#   1. Put gripper above cube
#   2. Drop gripper to grab cube
#   3. Lift cube off surface
#   4. Move gripper to target location
#   5. Lower cube onto target location
# First, position the gripper above the cube.
if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
# If the gripper is above the cube, drop it to grab the cube.
if check("the robot's gripper is above the cube and the robot's gripper is open"):
    robot.drop("gripper onto cube")
# Once the gripper has the cube, lift it off the surface.
if check("the robot's gripper is holding the cube and the cube is on the surface"):
    robot.lift("cube off surface")
# Move the gripper to the target location.
if check("the robot's gripper is holding the cube"):
    robot.move("gripper to goal location")
# Lower the cube onto the target location.
if check("the cube is above the goal location"):
    robot.put("cube onto goal location")