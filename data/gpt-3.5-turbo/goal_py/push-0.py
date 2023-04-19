I'm sorry, it looks like there was a duplicate of the 'push' function. Here's the next function:

# peg-insert-topdown: insert the peg into the hole from the top
# def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push the peg down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is not inside the gripper, open the gripper and put the gripper
    # around the peg.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("above the peg", close_gripper=False)
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is not lined up with the hole from above, move it over the
    # peg until it is.
    if check("the robot's gripper is not almost vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # Push down on the peg to insert it into the hole.
    if check("the robot's gripper is vertically aligned with the hole"):
        robot.move_gripper("above the peg")