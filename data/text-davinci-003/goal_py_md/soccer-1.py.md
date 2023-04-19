 

Steps:
1. Put gripper above soccer ball
2. Push gripper into top of soccer ball
3. Push soccer ball to goal

# soccer: push the soccer ball into the target location
# def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Push soccer ball to goal
    # First, get the gripper above the soccer ball.
    if check("the robot's gripper is not above soccer ball"):
        robot.move_gripper("above the soccer ball")
    # Then, move the gripper into the top of the soccer ball to trap it.
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # Once the gripper is trapping the soccer ball, move it towards the target
    # location.
    if check("the robot's gripper is around soccer ball"):
        robot.move_gripper("above the target location")