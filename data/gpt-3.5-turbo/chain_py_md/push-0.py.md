# push: slide the puck to the target location
# def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal

    # Checking if the gripper is not above the puck
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    
    # Checking if the gripper is not on top of the puck
    if check("the robot's gripper is not on top of puck"):
        robot.push("gripper into top of puck")
        
    # Checking if the gripper is not near the goal
    if check("the robot's gripper is not near the goal"):
        robot.slide("puck to goal")