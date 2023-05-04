
    # Steps:
    #  1. Line up the gripper from above, slightly in front of the button
    #  2. Push down on the button from above
    # First, line up the robot's gripper from above, since this is a "topdown"
    # task.
    if check("the robot's gripper is not almost vertically aligned with button and the robot's gripper is not forward aligned with button"):
        robot.put("gripper above button")
    # As long as the gripper is lined up from above, push down on the button.
    if check("the robot's gripper is almost vertically aligned with button"):
        robot.push("down on button")

# drawer-close-topdown: push the drawer closed from above
def drawer_close_topdown(robot):
    # Steps:
    #  1. Line up gripper vertically with drawer handle
    #  2. Put gripper near drawer handle
    #  3. Push drawer closed
    # First, line up gripper vertically with drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # If the gripper is above the drawer handle, we can just push it straight
    # down.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not near drawer handle"):
        robot.push("gripper into drawer handle")
    # If the gripper is near the drawer handle and vertically aligned with it,
    # we can push the drawer handle straight down.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is near drawer handle"):
        robot.push("drawer closed")

# peg-unstack: pick up the top of the stack of two pegs and place it somewhere else
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab the top peg
    #  3. Lift top peg
    #  4. Place peg at goal
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # As