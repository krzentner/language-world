# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
        
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    
    if check("the robot's gripper is not close to the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
        
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("above the target location")