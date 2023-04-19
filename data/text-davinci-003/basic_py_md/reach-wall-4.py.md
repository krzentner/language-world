

The program should check for the below conditions and take the corresponding action accordingly:

1. If the robot’s gripper is not above the wall
    - robot.put("gripper above wall")

2. If the robot's gripper is above the wall and is not near the target location
    - robot.reach("to goal")

3. If the robot's gripper is near the target location and the wall is blocking the gripper from reaching the target
    - robot.slide("side-ways to go around wall")