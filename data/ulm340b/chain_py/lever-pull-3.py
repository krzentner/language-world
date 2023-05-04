
    # Steps:
    #  1. Put gripper above lever
    #  2. Grab the lever
    #  3. Pull lever up
    # First, put the gripper roughly above the lever.
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    # Once the gripper is above the lever, try to grab it.
    if check("the robot's gripper is above the lever"):
        robot.grab("lever")
    # Once the gripper is around the lever, it's safe to pull it up.
    if check("the robot's gripper is around lever"):
        robot.pull("lever up")

# switch-on: push the switch on
def switch_on(robot):
    # Steps:
    #  1. Put gripper vertically aligned with switch
    #  2. Push the switch on
    # First, put the gripper vertically aligned with switch.
    if check("the robot's gripper is not vertically aligned with the switch"):
        robot.put("gripper above switch")
    # Once the gripper is above the switch, push it on.
    # This is not a long object, so don't check if the gripper is around the
    # object, just whether it's above.
    if check("the robot's gripper is vertically aligned with the switch"):
        robot.push("switch on")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push the peg down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if