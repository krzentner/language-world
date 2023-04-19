# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    
    # First, check if the robot's gripper is not above the puck and not
    # vertically aligned with the puck.
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        # If not, move the gripper to be above the puck.
        robot.move_gripper("above the puck")
    
    # Check if the gripper is not near the puck, but is vertically aligned
    # with the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        # If so, move the gripper down to grab the puck.
        robot.move_gripper("near the puck", close_gripper=True)
    
    # Check if the gripper is near the puck and if the puck is below the
    # gripper.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        # If so, move the gripper to the target location.
        robot.move_gripper("above the target location")