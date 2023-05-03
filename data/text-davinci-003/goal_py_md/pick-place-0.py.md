

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    #  4. Place the puck at the target location
    # First, move the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck", close_gripper=True)
    # Once the gripper is lined up above the puck, grab it by moving the
    # gripper down around the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Now that the puck is secured, move it to the target location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("above the target location")
    # Finally, release the puck at the target location.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("above the target location", open_gripper=True)