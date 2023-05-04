
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper around the button
    #  3. Close gripper around the button
    #  4. Press down on the button
    # First, put the gripper roughly above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("the gripper above the button")
    # If the gripper is above the button but not around it, close the gripper
    # around it.
    if check("the robot's gripper is above the button and the robot's gripper is open"):
        robot.put("the gripper around the button")
    # If the button is near the gripper, close it to try to grab it.
    # (This step is separate because we might have grabbed it from a distance.)
    if check("the robot's gripper is near the button and the robot's gripper is open"):
        robot.close("the gripper around the button")
    # If we've grabbed the button, push down on the button.
    if check("the robot's gripper is above the button and the robot's gripper is closed"):
        robot.push("down on the button")

# button-press-side: push the button sideways
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper around the button
    #  3. Close gripper around the button
    #  4. Push the button sideways
    # First, put the gripper roughly above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("the gripper above the button")
    # If the gripper is above the button but not around it, close the gripper
    # around it.
    if check("the robot's gripper is above the button and the robot's gripper is open"):
        robot.put("the gripper around the button")
    # If the button is near the gripper, close it to try to grab it.
    # (This step is separate because we might have grabbed it from a distance.)
    if check("the robot's gripper is near the button and the robot'