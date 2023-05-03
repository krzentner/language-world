

Steps:
1. Put gripper behind puck
2. Push gripper into the back of puck
3. Slide puck backwards to goal

If the robot's gripper is not behind the puck, move the gripper to behind the puck.
if check("the robot's gripper is not behind puck"):
    robot.move_gripper("behind the puck")

# Push the gripper into the back of the puck to trap it.
if check("the robot's gripper is behind the puck"):
    robot.move_gripper("near the puck", close_gripper=True)

# Once the puck is trapped, slide it backwards to the target location.
if check("the robot's gripper is near the puck and the puck is behind the robot's gripper"):
    robot.move_gripper("behind the target location")