
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # As long the gripper is mostly above the handle, move the gripper down
    # around the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    # If the gripper is around the handle, pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")

# handle-pull: pull up the handle from the front
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # As long the gripper is vertically above the handle, put the gripper around
    # the handle.
    # Because the handle is a long object, check if the gripper is lined up
    # with it from the front instead of around it.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not forward aligned with the handle"):
        robot.put("gripper around handle")
    # As long the gripper is around the handle, pull it up.
    # Because the handle is a long object, check if the gripper is lined up
    # with it from the front instead of around it.
    if check("the robot's gripper is forward aligned with the handle"):
        robot.pull("handle up")

# peg-unstack-side: remove the top peg from the stack
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above the top peg
    #  2. Grab the top peg
   