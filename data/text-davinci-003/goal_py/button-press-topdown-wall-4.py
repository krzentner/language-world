
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top while pushing against the wall
    #  3. Push down harder
    # First, we need to line up the gripper with the button as viewed from above.
    # We can do this by lining up the gripper with the bottom of the wall,
    # since that is where the button is behind.
    # Put the gripper slightly above the wall.
    if check("the robot's gripper is below the wall"):
        robot.move_gripper("above the wall")
    # If the gripper is above the wall and aligned with the button, we can push
    # down and start pushing against the wall.
    if check("the robot's gripper is above wall and the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")
    # Once we start pushing against the wall, push harder.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("above the button")

# twist: twist the peg clockwise
def twist(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg
    #  3. Line up the robot with the peg
    #  4. Twist the peg clockwise
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the peg isn't left of the gripper, move the gripper to the peg.
    # We don't have to be careful about the direction, since we're just grabbing
    # onto it.
    if check("the peg is not left of the gripper and the gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # Before twisting, align the robot's gripper with the peg.
    if check("the robot's gripper is horizontally aligned with the peg"):
        robot.move_gripper("right of the peg")
    # Now that the robot is lined up with the peg, twist the peg clockwise.
    if check("the robot's gripper is right of the peg"):
        robot.rotate_gripper("clockwise")