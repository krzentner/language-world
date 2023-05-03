# Steps:
    #  1. Put the gripper in front of the button
    #  2. Lift the gripper over the wall
    #  3. Push the button down
    # First, put the gripper roughly in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.place("gripper in front of button")
    # If there is a wall between the gripper and button, lift the gripper over
    # the wall before pushing the button.
    if check("there is a wall between the gripper and the button"):
        robot.lift("gripper over the wall")
    # Once the gripper is in front of the button and over the wall, push down on the button.
    if check("the robot's gripper is in front of the button and over the wall"):
        robot.push("down on button")