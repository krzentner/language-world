

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper to the target location
    #  4. Lower the puck to the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Once the gripper is above the puck, we just need to grab it.
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper has the puck, we can move it to the target location.
    if check("the robot has the puck"):
        robot.move_gripper("near the target location")
    # Once the gripper is at the target location, lower the puck.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location")