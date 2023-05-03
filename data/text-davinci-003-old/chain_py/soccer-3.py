
    # Steps:
    #  1. Put gripper above the soccer ball
    #  2. Push the soccer into the goal
    # The robot needs to place its gripper right over the soccer ball so it can
    # trap it.
    if check("the robot's gripper is not above soccer ball"):
        robot.put("gripper above ball")
    # Once the robot's gripper is over the soccer ball, it can push it towards
    # the target location.
    if check("the robot's gripper is above soccer ball"):
        robot.push("ball to goal")