# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move gripper to the target location
    #  4. Release the puck at the target location
    
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to pick it up.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck and has picked it up, move the gripper to the target location.
    # Open the gripper to release the puck at the target location.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("near the target location", close_gripper=False)