# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Line up gripper with button from front
    #  2. Move gripper towards button until obstruction is detected
    #  3. Turn gripper to the side to avoid obstruction
    #  4. Move gripper towards button again
    #  5. Push down on the button
    # First, line up the gripper with the button from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper in front of button")
    # Move the gripper towards the button until obstruction is detected.
    # We'll assume the robot has sensors to detect the obstruction.
    while check("obstruction detected"):
        robot.move("gripper towards button")
    # Turn the gripper to the side to avoid the obstruction.
    robot.rotate("gripper to the side")
    # Move the gripper towards the button again.
    if check("the robot's gripper is not near button"):
        robot.move("gripper towards button")
    # Push down on the button.
    robot.push("down on button")