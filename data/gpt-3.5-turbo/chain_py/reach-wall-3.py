# Steps:
    #  1. Check if there is a wall blocking the robot's path to the target
    #  2. If there is a wall, move the gripper above the wall
    #  3. Reach to the target location
    # Check if there is a wall blocking the robot's path to the target
    if check("there is a wall blocking the robot's path to the target"):
        # Move the gripper above the wall
        robot.move("gripper above the wall")
    # Reach to the target location
    robot.reach("to goal")