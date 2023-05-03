# Steps:
#  1. Put the gripper above the stick
#  2. Open the gripper and grab the stick
#  3. Place the gripper near the thermos
#  4. Push the thermos with the stick towards the target
# First, put the gripper above the stick.
if check("the robot's gripper is not vertically aligned with the stick"):
    robot.put("gripper above stick")
# If the gripper is above the stick, open it and grab the stick.
if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is open"):
    robot.grab("stick")
# Once we have the stick, place the gripper near the thermos
if check("the stick is in the robot's gripper and the robot's gripper is not near the thermos"):
    robot.place("gripper near thermos")
# If we are close to the thermos with the stick, start pushing it towards the target
if check("the stick is close to the thermos and the thermos is not at the target location"):
    robot.push("thermos towards target")