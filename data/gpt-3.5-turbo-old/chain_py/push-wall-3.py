# Steps:
    # 1. Put gripper above puck
    # 2. Push gripper into top of puck
    # 3. If there's a wall in the way, move the gripper to the side of the wall
    # 4. Slide puck to goal
    # Same as the push function, but with an extra step for the wall.
    # If the wall is in the way, move the gripper to the side of the wall.
    if check("there's a wall in the way and the robot's gripper is not beside the wall"):
        robot.move("gripper beside wall")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    elif check("the robot's gripper is verticaly aligned with puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    elif check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")