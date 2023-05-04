
    # Steps:
    #  1. Put gripper above handle
    #  2. Push down on the handle
    # If the gripper is not aligned with the handle, put it above the handle
    # first.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the gripper is aligned with the handle, push the handle down.
    if check("the robot's gripper is above the handle"):
        robot.push("handle down")

# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Pull up on the handle
    # If the gripper is not aligned with the handle, put it above the handle
    # first.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the gripper is aligned with the handle, pull the handle up.
    if check("the robot's gripper is above the handle"):
        robot.pull("handle up")

# pick-insert-topdown: grab the peg and insert it into the hole from the top
def pick_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Line the peg up with the hole
    #  4. Insert the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the peg is not lined up with the gripper as seen from in front, line it
    # up first.
    if check("the robot's gripper is not forward aligned with peg"):
        robot.align("peg to gripper")
    # If the gripper is open and forward aligned with the peg, put the gripper
    # around the peg.
    if check("the robot's gripper is forward aligned with peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is closed and around the peg, we