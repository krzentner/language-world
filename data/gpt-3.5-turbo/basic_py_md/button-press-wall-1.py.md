# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not in front of button"):
        robot.move("gripper in front of button")
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not open"):
        robot.open()
    if check("the robot's gripper is open and there's a wall blocking the button"):
        robot.move("gripper to the left of the wall")
        robot.slide("gripper against the wall")
        robot.move("gripper to the right of the wall")
        robot.slide("gripper towards the button")
    if check("the gripper's fingers are around the button"):
        robot.close()
    if check("the gripper has hold of the button and is in front of the button"):
        robot.push("button")
    if check("the button has been pushed and the gripper is in its initial position"):
        robot.move("gripper to its initial position")