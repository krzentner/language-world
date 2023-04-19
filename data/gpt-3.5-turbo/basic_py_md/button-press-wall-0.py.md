# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    if check("the robot's gripper is not near the button on the wall"):
        robot.move("gripper closer to button on the wall")
    if check("the robot's gripper is near the button on the wall and the robot's gripper is not around the button"):
        robot.drop("gripper around the button on the wall")
    if check("the robot's gripper is around the button on the wall and there is a short wall blocking the robot's gripper"):
        robot.move("gripper up to avoid the wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not directly above the button"):
        robot.move("gripper to center over the button")
    if check("the robot's gripper is directly above the button"):
        robot.push("down on the button")