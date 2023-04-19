

The robot should slide the puck backwards to the target location.

Steps:

1. Put gripper above puck
2. Push gripper into the bottom of puck
3. Slide puck backwards to the target location

if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
    robot.move_gripper("vertically aligned with the puck")

if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
    robot.move_gripper("below the puck", close_gripper=True)

if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
    robot.move_gripper("below the target location")