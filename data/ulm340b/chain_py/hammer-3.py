
    # Steps:
    #  1. Put gripper near nail
    #  2. Push the nail to the left
    # First, put the gripper near the nail so that we can hit it with the
    # hammer.
    if check("the robot's gripper is not near the nail"):
        robot.move("gripper near nail")
    # If the robot's gripper is near the nail, push the nail.
    if check("the robot's gripper is near the nail"):
        robot.slide("nail to left")

# drawer-pull: pull the drawer open
def drawer_pull(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull open the drawer
    # We need to put the gripper roughly around the drawer handle before we can
    # pull it open.
    # We need to check that we are above the drawer handle from in front instead
    # of above because we don't want to grab the drawer handle from the wrong
    # side.
    if check("the robot's gripper is not forward aligned with drawer handle"):
        robot.move("gripper near drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # pull the drawer open.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# peg-unplug-side: hold the peg and pull it out of the hole from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper near the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg sideways out of the hole
    # First, put the gripper near the peg, so that we don't bump it while
    # grabbing it.
    if check("the robot's gripper is not near the peg"):
        robot.put("gripper near the peg")
    # If the peg becomes right of the gripper, go back to putting the gripper
    # near the peg.
    # Because the peg is a long object, check if the gripper is forward lined
    # up with it instead of around it.
    if check("