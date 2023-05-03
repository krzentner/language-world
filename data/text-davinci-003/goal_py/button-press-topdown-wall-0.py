
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    #  3. Push the wall and the button down together
    #  4. Push down on the wall to release the button from the wall
    # Just like before, we need to line up the gripper from above, but with a
    # wall in the way.
    if check("the robot's gripper is not vertically aligned with button and wall"):
        robot.move_gripper("vertically aligned with the button and wall", close_gripper=True)
    # Now that the the gripper is lined up, the robot should be able to push
    # down on the button and the wall together.
    if check("the robot's gripper is vertically aligned with button and wall"):
        robot.move_gripper("near the button and wall")
    # To release the button from the wall, we need to push down on the wall.
    if check("the button is stuck in the wall"):
        robot.move_gripper("pushing down on the wall")
    # If the button isn't stuck in the wall, we can move it to the target location.
    if check("the button is not stuck in the wall"):
        robot.move_gripper("near the target location", close_gripper=True)