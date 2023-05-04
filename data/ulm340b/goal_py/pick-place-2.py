
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck by pushing down with the gripper
    #  3. Bring the puck up
    #  4. Place the puck at the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the puck becomes below the gripper, go back to putting the gripper
    # above the puck.
    if check("the puck is not below the robot's gripper"):
        robot.move_gripper("above the puck", close_gripper=True)
    # Now that the puck is trapped, lift the gripper up.
    if check("the puck is below the robot's gripper"):
        robot.move_gripper("forward aligned with the robot's gripper")
    # Now that the puck is above the gripper, we can just put the gripper to the
    # target location.
    # We don't need to worry about pushing the puck out, because it's above the
    # gripper.
    if check("the puck is above the robot's gripper"):
        robot.move_gripper("to the target location")

# pick-place-wall: pick up the puck and hold it against the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck by pushing down with the gripper
    #  3. Bring the puck up
    #  4. Slide the puck against the wall
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the puck becomes below the gripper, go back to putting the gripper
    # above the puck.
    if check("the puck is not below the robot's gripper"):
        robot.move_gripper("above the puck", close_gripper=True)
    # Now that the puck is trapped, lift the gripper up.
    if check("the puck is below the robot's gripper