# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not in front of the button"):
        robot.move("gripper to front of button")
        robot.move("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not behind the wall"):
        robot.push("the gripper into the wall")
    if check("the robot's gripper is behind the wall and the wall is above the robot's gripper and the robot's gripper is vertical"):
        robot.move("gripper to top of wall")
        robot.push("down on button")