# Steps:
    #  1. Check if the wall is blocking our way to the target
    #  2. If the wall is not blocking us, reach to the target
    #  3. If the wall is blocking us, move to the side to get around it,
    #     then reach to the target
    # Check if the wall is blocking our way to the target.
    if check("there is a wall blocking the path to the target"):
        # Move the robot to the side to get around the wall.
        robot.move("to the side of the wall")
    # Once we're past the wall, we can just reach to the target normally.
    robot.reach("to goal")