

Then, describe steps for performing this task:

1. Put gripper above puck
2. Push gripper into top of puck
3. Slide back puck to target location

# Steps:
1. Put gripper above the puck 
2. Push the gripper into the top of the puck
3. Slide the puck backwards to the target location 

if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")

if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)

if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")