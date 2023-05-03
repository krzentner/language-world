

Steps:
  1. Put gripper above mug
  2. Drop gripper around mug
  3. Pick up mug
  4. Pull mug away from starting location
  5. Slide mug towards target location

if check("the robot's gripper is not above the mug"):
    robot.put("gripper above mug")
if check("the robot's gripper is not around mug and the robot's gripper is open"):
    robot.drop("gripper around mug")
if check("the robot's gripper is near mug and the robot's gripper is open"):
    robot.pick("up mug")
if check("the robot's gripper is above mug and the robot's gripper is closed"):
    robot.pull("mug away from start")
if check("the robot's gripper is near mug and the robot's gripper is closed"):
    robot.slide("mug towards the goal")