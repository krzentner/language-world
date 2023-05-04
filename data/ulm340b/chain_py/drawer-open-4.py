
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper above the drawer handle.
    # Since the drawer handle is large, we just need to be roughly above it.
    if check("the robot's gripper is not almost above drawer handle"):
        robot.put("gripper above drawer handle")
    # As long as the gripper is mostly above the drawer handle, drop the gripper
    # around the drawer handle.
    # Since the drawer handle is large, we just need to roughly put the gripper
    # around it.
    if check("the robot's gripper is above drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    # As long as the gripper is mostly lined up with the drawer, pull the drawer
    # open.
    # Since the drawer handle is large, we just need to roughly pull forward.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# button-press-topside: push the button down from the side
def button_press_topside(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Move the gripper into the button until the button moves
    # Because this is "topside", we just need to line up the gripper from the
    # side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.align("gripper to button")
    # Now that the gripper is lined up, just push the button sideways.
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.move("the gripper into the button until the button moves")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
 