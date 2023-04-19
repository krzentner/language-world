# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    if check("the robot's gripper is not facing towards the button and the robot's gripper is not close to the wall"):
        robot.move("the gripper towards the wall until it is close to the wall")
    if check("the robot's gripper is close to the wall but not facing towards the button"):
        robot.turn("the gripper to face towards the button")
    if check("the robot's gripper is facing towards the button but not vertically aligned with the button"):
        robot.move("the gripper up and down until it is vertically aligned with the button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("the button")