# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    
    # Check if the gripper is not above the puck and not vertically aligned with it, 
    # then move the gripper to be vertically aligned with the puck.
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    
    # Check if the gripper is not near the puck, then move the gripper down above the puck to begin pushing it.
    if check("the robot's gripper is above the puck and the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    
    # Check if the gripper is near the puck and the puck is below the gripper,
    # then move the gripper to the target location while keeping the puck trapped.
    if check("the robot's gripper is near the puck and the puck is below robot's gripper"):
        robot.move_gripper("above the target location", close_gripper=True)