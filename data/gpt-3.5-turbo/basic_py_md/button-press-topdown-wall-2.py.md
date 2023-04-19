# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    if check("the robot's gripper is not on the same side of the wall as the button"):
        robot.move("to the other side of the wall")
    if check("the robot's gripper is not vertically aligned with the button and the wall is blocking the gripper's movement"):
        robot.move("to right above the button")
    if check("the robot's gripper is right above the button but the wall is still blocking the gripper's downward movement"):
        robot.move("gripper around the wall")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")