# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper around button
    #  2. Close gripper around button
    #  3. Push button
    # We need to put the gripper around the button before we can push it.
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Then, drop the gripper around the button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is open"):
        robot.drop("gripper around button")
    # Close the gripper around the button.
    if check("the robot's gripper is around button and the robot's gripper is open"):
        robot.close("gripper around button")
    # Finally, push the button.
    if check("the robot's gripper is around button and the robot's gripper is closed"):
        robot.push("button")