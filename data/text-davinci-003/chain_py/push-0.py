
    # Steps:
    #  1. Put gripper in front of puck
    #  2. Press down on the puck
    #  3. Push the puck forward
    # If the puck is not in front of the robot's gripper, put the gripper in
    # front of the puck.
    if check("the robot's gripper is not in front of puck"):
        robot.place("gripper in front of puck")
    # If the puck is in front of the gripper, press down gently to give ourselves
    # some traction
    if check("the robot's gripper is in front of puck"):
        robot.push("down on puck")
    # If the gripper is still firmly on the puck, push the puck forward.
    if check("the robot's gripper is pressing down on the puck"):
        robot.push("puck forward")