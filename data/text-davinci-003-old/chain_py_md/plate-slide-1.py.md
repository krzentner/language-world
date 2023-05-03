

Steps:
1. Put gripper above plate
2. Push gripper into plate
3. Slide plate to goal

If the robot's gripper is not above the plate, we should move it to the plate in order to start sliding it.

if check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
    
Once the gripper is over the plate, we can start pushing down to get control of it.

if check("the robot's gripper is above the plate and the robot's gripper is not in the plate"):
    robot.push("gripper into plate")
    
Once the gripper is trapping the plate, we can start sliding it to the goal.

if check("the robot's gripper is in the plate"):
    robot.slide("plate to the goal")