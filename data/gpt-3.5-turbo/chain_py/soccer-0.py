# Steps:
    #  1. Put the gripper above the soccer ball
    #  2. Close the gripper around the ball
    #  3. Move the ball towards the goal
    #  4. Release the ball
    # To start, put the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    # Once the gripper is above the ball, close it around the ball.
    if check("the robot's gripper is above the soccer ball and the gripper is open"):
        robot.close("gripper around soccer ball")
    # Now that the ball is in the gripper, move it towards the goal.
    if check("the ball is in the gripper and the gripper is vertically aligned with the goal"):
        robot.move("ball towards goal")
    # Once the ball is near the goal, release it by opening the gripper.
    if check("the ball is near the goal"):
        robot.open("gripper to release soccer ball")