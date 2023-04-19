# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Move the gripper close to the button from the front
    #  2. Align the gripper with the button 
    #  3. Move the gripper as close to the button as possible
    #  4. Push down on the button
    # First, move the gripper close to the button from the front.
    if check("the robot's gripper is not close to the button and cannot move forward"):
        robot.move("gripper to button from the front")
    # Once the gripper is close, align it with the button.
    if check("the robot's gripper is not aligned with the button"):
        robot.align("gripper with button")
    # Move the gripper as close to the button as possible.
    if check("the robot's gripper is not very close to the button"):
        robot.move("gripper closer to button")
    # Push down on the button.
    if check("the robot's gripper is above the button"):
        robot.push("button down")