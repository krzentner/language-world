# push: slide the puck to the target location
# def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal

    # If the gripper is not above the puck, move it above the puck
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
        
    # If the gripper is not touching the top of the puck, move it into the top of the puck
    if check("the robot's gripper is not touching the top of the puck"):
        robot.push("gripper into top of puck")
        
    # Slide the puck to the target location
    robot.slide("puck to goal")