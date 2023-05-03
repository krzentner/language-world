# Steps:
#  1. Put the gripper above the cube
#  2. Lower the gripper onto the cube
#  3. Push the cube towards the target location while keeping the gripper closed
#  4. Release the cube once it's at the target location
# First, put the gripper above the cube.
if check("the robot's gripper is not vertically aligned with the cube"):
    robot.place("gripper above the cube")
# Once the gripper is above the cube, we try to grab it by lowering the gripper
# and closing it.
if check("the robot's gripper is above the cube and the gripper is open"):
    robot.grab("the cube")
# If we have a good grasp on the cube, we push it towards the target location.
# We keep the gripper closed to maintain control.
if check("the robot's gripper is around the cube and the robot is not near the target location"):
    robot.slide("the cube towards the target location")
# Once we reach the target location, we release the cube by opening the gripper.
if check("the robot is near the target location and the gripper is closed around the cube"):
    robot.release("the cube")