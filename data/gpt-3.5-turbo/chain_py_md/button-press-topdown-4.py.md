# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    # 1. Put gripper above the button
    # 2. Push gripper down onto button
    # 3. Push button down
    # 4. Release gripper and retract it
    # Put the gripper above the button
    if check("the robot's gripper is not above the button"):
        robot.place("gripper above button")
    # Push the gripper down onto the button
    if check("the robot's gripper is above the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper onto button")
    # Push the button down
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("button down")
    # Release the gripper and retract it
    if check("the robot's gripper is gripping the button"):
        robot.release("gripper")
        robot.retract("gripper")