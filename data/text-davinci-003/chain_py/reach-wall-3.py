
    # Steps:
    #  1. Put gripper above wall
    #  2. Reach gripper over wall to reach target
    # Move the gripper above the wall so that the gripper has enought height to
    # reach over the wall.
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above the wall")
    # Reach the gripper over the wall.
    if check("the robot's gripper is above the wall"):
        robot.reach("gripper over the wall to goal")