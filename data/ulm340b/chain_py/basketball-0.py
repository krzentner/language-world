
    # Steps:
    #  1. Move the gripper above the ball
    #  2. Drop gripper to grab the ball
    #  3. Move the ball below the hoop
    #  4. Pull the ball out of the gripper and into the hoop
    # If the gripper is not above the ball, move it above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper above the ball")
    # If the gripper is above the ball and it is not grabbing it yet, move it
    # down to grab the ball.
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.grab("the ball")
    # Now that the ball is in the gripper, move the gripper below the hoop.
    if check("the robot's gripper is holding the ball"):
        robot.put("the ball below the hoop")
    # To let go of the ball, we just release the gripper.
    if check("the robot's gripper is holding the ball"):
        robot.let_go("the ball")

# peg-insert-topdown: grab the peg and insert it into the hole from the top
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the peg to be above the hole
    #  4. Push the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg is left of the gripper, go back to putting the gripper above the
    # peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long as the peg is still mostly lined up with the gripper and is not
    # directly above the hole, move the peg above the