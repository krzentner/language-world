

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above the puck 
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    #  4. Release the puck at the target location
    
    # First, put the gripper above the puck
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Now the gripper is lined up, close it to grab the puck
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # Once the puck is in the gripper we can move it to the target location
    if check("the robot's gripper is above the puck"):
        robot.move_gripper("above the target location")
    # Lastly, release the puck at the target location. 
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("closed")