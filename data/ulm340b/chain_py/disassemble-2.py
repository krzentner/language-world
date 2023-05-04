
    # Steps:
    #  1. Put gripper above wrench
    #  2. Put gripper around wrench
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # Once the gripper is above the wrench, we should be able to grab it.
    if check("the robot's gripper is not around wrench and the robot's gripper is above wrench"):
        robot.put("gripper around wrench")
    # Once the wrench is held, we can pull it off the peg.
    if check("the robot's gripper is around wrench"):
        robot.pull("wrench off the peg")

# BUTTON-PRESS-SIDE: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper from the side
    #  2. Push the button from the side
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper next to button")
    # Now that the gripper is lined up, just push the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")

# disassemble-topdown: pull the wrench off the peg from the top-down
def disassemble_topdown(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Put gripper around wrench
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # Once the gripper is above the wrench, we should be able to grab it.
    if check("the robot's gripper is not around wrench and the robot's gripper is above wrench"):
        robot.put("gripper around wrench")
    # Once the wrench is held, we can pull it off the peg.