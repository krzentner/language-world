
    # Steps: 
    #  1. Put gripper above wall
    #  2. Reach over wall
    # We can reach over a short wall by putting the gripper above the wall and
    # then reach over the wall.
    if check("the robot's gripper is not above wall"):
        robot.put("gripper above wall")
    # Once the gripper is above the wall, we can reach over it.
    if check("the robot's gripper is above wall"):
        robot.reach("over wall")