
    # Steps:
    #  1. Put gripper slightly above the short wall
    #  2. Push the short wall to the side
    #  3. Put gripper above the button and push it
    # To start, put the gripper slightly above the short wall so that it can
    # push it safely.
    if check("the robot's gripper is not slightly above short wall"):
        robot.move_gripper("slightly above short wall")
    # Once the gripper is slightly above, start pushing the short wall to the
    # side.
    if check("the robot's gripper is slightly above the short wall"):
        robot.move_gripper("right of the short wall")  
    # Once we've pushed the wall to the side, the button should be visible. Line
    # up the gripper above the button and push it.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("vertically aligned with the button")