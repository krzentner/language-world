# Steps:
#  1. Use camera to locate cube and determine its orientation
#  2. Put the gripper above the cube
#  3. Close the gripper around the cube
#  4. Move the gripper above the target bin
#  5. Drop the cube into the bin

# First, use the camera to locate the cube and figure out its orientation.
if check("cube is not located and orientation is not determined"):
    robot.locate_cube()
# Once we know where the cube is and its orientation, move the gripper above it.
if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
# If the gripper isn't around the cube, put it around the cube.
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
# If the gripper is near the cube and open, maybe we can grab it by closing
# the gripper.
if check("the robot's gripper is near cube and the robot's gripper is open"):
    robot.close("gripper around cube")
# We closed the gripper, and the cube is still near the gripper, so maybe we
# grabbed it.
# Move the gripper above the target bin.
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.move("gripper above target bin")
# Once the gripper is above the target bin, we can drop the cube into the bin.
if check("the robot's gripper is above target bin and the robot's gripper is closed"):
    robot.drop("cube into bin")