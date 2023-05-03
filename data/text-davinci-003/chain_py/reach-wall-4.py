
    # Steps:
    #  1. Reach above the wall
    #  2. Reach down to the goal
    #  We can't reach directly through the wall, so we'll need to reach to either side of the wall.
    #  First, move the gripper to the top of the wall.
    if check("the robot's gripper is not above wall"):
        robot.put("gripper above wall")
    # Now that the gripper is above the wall, move straight down to the goal.
    if check("the robot's gripper is above wall"):
        robot.reach("down to goal")