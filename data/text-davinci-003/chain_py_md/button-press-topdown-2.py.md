

The code should then be:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper down onto the button
    #  3. Push the button down 
    # We need to put the gripper above the button before we can push it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Once the gripper is lined up above the button, we should be able to push 
    # the button down by moving the gripper down onto it.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.push("gripper down onto button")
    # Once the gripper is around the button, we can just push the button down.
    if check("the robot's gripper is near button"):
        robot.push("button down")
``