
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the wrench around the peg
    # First, put the gripper above wrench.
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    # If the wrench is not in front of the gripper, grab it by moving the gripper
    # down.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is not forward aligned with wrench"):
        robot.grab("wrench")
    # As long the gripper is still mostly around the wrench, we can wrap the
    # wrench around the peg by moving the gripper forward
    # If we move the gripper enough, the wrench will fall and be wrapped around
    # the peg.
    if check("the robot's gripper is forward aligned with wrench"):
        robot.place("wrench around peg")

# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Move the gripper into the button
    #  3. Keep pushing down harder
    # First, put the gripper roughly above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # As long as the button is roughly above the gripper and not pushed in,
    # push down harder.
    if check("the robot's gripper is vertically aligned with button and button is not pressed"):
        robot.push("down on button")
    # As long as the button is pushed in, keep pushing harder.
    if check("button is pressed"):
        robot.push("down on button harder")

# assembly-v1: grab the wrench and wrap it around the peg
def assembly_v1(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Put gripper around wrench
    #  3. Move