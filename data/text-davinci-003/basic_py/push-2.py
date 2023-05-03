
    if check("the robot's gripper is not vertically aligned with puck and the robot's gripper is above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near the puck"):
        robot.slide("puck to goal")

# button-press-sideways: press the button sideways
def button_press_sideways(robot):
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper to the side of button")
    if check("the robot's gripper is not around button and the robot's gripper is open"):
        robot.open("gripper around button")
    if check("the robot's gripper is near the button"):
        robot.push("sideways on the button")