
    # Steps:
    #  1. Put the gripper in front of the wall
    #  2. Put the gripper to the side of the wall
    #  3. Push the button
    # The first step is to put the gripper in front of the wall, so that the wall
    # is between the gripper and the button.
    if check("the robot's gripper is not forward aligned with the wall"):
        robot.move_gripper("near the wall") 
    # Then, move the gripper near the wall and to the side to push the button.
    if check("the robot's gripper is not side aligned with the wall and the robot's gripper is not near the wall"):
        robot.move_gripper("side aligned with the wall")
    # Once the gripper is to the side of the wall, we can push the button first
    # by getting it almost up against the wall. 
    if check("the robot's gripper is side aligned with the wall and the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    # If the gripper is near the button and the wall is between them, push the
    # button.
    if check("the robot's gripper is facing the button and there is a wall between the robot's gripper and the button"):
        robot.move_gripper("forward aligned with the button")