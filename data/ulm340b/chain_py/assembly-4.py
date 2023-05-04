
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up with the peg
    #  4. Slide the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the wrench is not left of the robot's gripper and the wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    # As long the gripper is still mostly around the wrench and the wrench isn't
    # lined up with the peg, line up the wrench with the peg.
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not horizontally aligned with peg"):
        robot.align("wrench to peg")
    # If the wrench is lined up with the peg to the side, rotate it to wrap it
    # around the peg.
    if check("the wrench is horizontally aligned with peg"):
        robot.insert("wrench around peg")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button from the side
    # Put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    # Push down on the button from the side.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on the button from the side")

# button-press-top: push the button from above
def button_press_top(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button from above
    # Put the gripper above