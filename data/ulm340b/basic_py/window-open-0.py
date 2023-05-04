
    if check("the robot's gripper is not above window handle"):
        robot.put("gripper above window handle")
    if check("the robot's gripper is vertically aligned with window handle"):
        robot.push("gripper towards window handle")
    if check("the robot's gripper is in front of window handle and window handle is not left of gripper"):
        robot.slide("window left")
    if check("the robot's gripper is near window handle"):
        robot.push("window left harder")

# toggle-switch-side-on: push the switch to turn it on
def toggle_switch_side_on(robot):
    if check("the robot's gripper is not horizontally aligned with the toggle switch handle and the robot's gripper is not vertically aligned with the toggle switch handle"):
        robot.place("gripper above toggle switch handle")
    if check("the robot's gripper is not near toggle switch handle"):
        robot.grab("toggle switch handle")
    if check("the robot's gripper is near toggle switch handle and the robot's gripper is left of toggle switch handle"):
        robot.push("toggle switch handle to the right")
    if check("toggle switch handle is not near robot's gripper and the robot's gripper is right of toggle switch handle"):
        robot.pull("toggle switch handle to the left")
    if check("the robot's gripper is left of toggle switch handle and the robot's gripper is forward aligned with toggle switch handle"):
        robot.push("toggle switch handle harder to the right")
    if check("the robot's gripper is right of toggle switch handle and the robot's gripper is forward aligned with toggle switch handle"):
        robot.push("toggle switch handle harder to the left")

# toggle-switch-side-off: push the switch to turn it off
def toggle_switch_side_off(robot):
    if check("the robot's gripper is not horizontally aligned with the toggle switch handle and the robot's gripper is not vertically aligned with the toggle switch handle"):
        robot.place("gripper above toggle switch handle")
    if check("the robot's gripper is not near toggle switch handle"):
        robot.grab("toggle switch handle")
    if check("the robot's gripper is left of toggle switch handle and the robot's gripper is forward aligned with toggle switch handle"):
        robot.pull("toggle switch handle to the left")
