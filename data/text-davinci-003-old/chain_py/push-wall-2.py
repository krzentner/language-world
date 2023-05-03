
    # Steps:
    #  1. Put the gripper in front of the puck and the wall
    #  2. Move the gripper against the wall 
    #  3. Push the puck to the goal
    # First, depending on the obstacle, check if the obstacle is blocking the
    # way.
    # If yes, put the gripper in front of the puck and the wall.
    if check("the obstacle is blocking the puck and the robot's gripper is not left of the wall and the robot's gripper is not forward aligned with the wall and the robot's gripper is not forward aligned with the puck and the robot's gripper is not around the puck"):
        robot.put("gripper in front of the puck and the wall")
    # Then, we need to move the gripper against the wall 
    if check("the robot's gripper is left of the wall and the robot's gripper is not forward aligned with the wall"):
        robot.move("gripper against the wall")
    # Lastly, once the wall is out of the way, push the puck until it reaches the
    # goal.
    if check("the robot's gripper is forward aligned with the wall and the robot's gripper is not around the puck and the obstacle is not blocking anything"):
        robot.push("puck to the goal")