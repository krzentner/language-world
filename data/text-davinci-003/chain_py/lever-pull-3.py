
    # Steps:
    #  1. Put gripper above the lever
    #  2. Drop gripper around the lever
    #  3. Rotate the lever up

    # Put the gripper above the lever.
    if check("the robot's gripper is not almost vertically aligned with lever"):
        robot.put("gripper above lever")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the lever and the robot's gripper is open"):
        robot.put("gripper around lever")
    # Rotate the lever up.
    if check("the robot's gripper is vertically aligned with the lever"):
        robot.pull("lever up")

# button-press-side: press the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper forward of button
    #  2. Push button
    # 
    # Put the gripper forward of the button.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.put("gripper forward of button")
    # If the gripper is in front of the button and the gripper is open, push the
    # button.
    if check("the robot's gripper is forward aligned with the button and the robot's gripper is open"):
        robot.push("down on button")