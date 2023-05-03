# Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Move gripper to target location
    #  4. Release the puck at the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Once the gripper is above the puck, we should be able to grab the puck by
    # moving the gripper down around it.
    # Close the gripper to hold on to the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.grab("puck")
    # Once we have the puck, move the gripper to the target location.
    if check("the robot's gripper is around puck"):
        robot.go_to("the goal")
    # Once the gripper is at the target location, release the puck.
    if check("the robot's gripper is at the goal location"):
        robot.release("puck")