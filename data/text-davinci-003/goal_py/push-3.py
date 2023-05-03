
    # Steps:
    #  1. Put gripper near puck
    #  2. Slide puck to goal
    # To start the task, find the puck and get the gripper near it so that the
    # task can be completed.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # Once the gripper is near the puck, push the puck to the target location.
    if check("the robot's gripper is forward aligned with the puck and the puck is not near target location"):
        robot.move_gripper("around the puck")