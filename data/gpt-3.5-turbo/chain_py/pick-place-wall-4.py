# Steps:
    #  1. Line up gripper with puck, with wall in between
    #  2. Move gripper towards puck
    #  3. Lift puck over wall
    #  4. Move gripper to target
    #  5. Lower the puck onto the target
    # First, line up the gripper with the puck, with the wall in the way.
    if check("the robot's gripper is not aligned with the puck and the wall"):
        robot.align("gripper with puck and wall")
    # Move the gripper towards the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move("gripper towards puck")
    # Lift the puck over the wall.
    if check("the puck is below the top of the wall"):
        robot.lift("puck over the wall")
    # Move the gripper to the target location.
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to the target location")
    # Lower the puck onto the target.
    if check("the puck is over the target and the robot's gripper is not open"):
        robot.lower("puck onto the target")