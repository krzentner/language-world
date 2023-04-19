# Steps:
#  1. Scan bin for cube
#  2. Put gripper above cube
#  3. Grab the cube with the gripper
#  4. Move the cube to the target bin
#  5. Release the cube into the bin
# We'll start by scanning the bin to find the cube.
if check("the cube is not in sight"):
    robot.scan("the bin")
# If the gripper isn't above the cube, move it into position.
if check("the robot's gripper is not above the cube"):
    robot.move("gripper above cube")
# If the gripper is open and above the cube, grab the cube.
if check("the robot's gripper is open and above the cube"):
    robot.grab("the cube")
# If the gripper is closed and not above the target bin, move the cube to the
# target bin.
if check("the robot's gripper is closed and the cube is not above the target bin"):
    robot.move("cube to target bin")
# If the gripper is closed and above the target bin, release the cube into it.
if check("the robot's gripper is closed and the cube is above the target bin"):
    robot.release("the cube into the target bin")