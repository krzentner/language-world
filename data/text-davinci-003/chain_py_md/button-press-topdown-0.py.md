

 
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper over the button
    #  2. Push the button 
    # First, put the gripper over the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper is above the button, we can try to push it down.
    if check("the robot's gripper is above the button"):
        robot.push("button down")