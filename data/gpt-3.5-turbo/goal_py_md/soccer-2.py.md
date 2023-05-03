# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put the gripper above the soccer ball
    #  2. Grip the soccer ball by dropping the gripper around it
    #  3. Move the ball towards the target while keeping it trapped in the gripper
    #  4. Release the ball at the target location
    # First, put the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # Next, grip the soccer ball by dropping the gripper around it.
    if check("the robot's gripper is above the soccer ball and the robot's gripper is open"):
        robot.move_gripper("around the soccer ball", close_gripper=True)
    # Once the ball is safely trapped in the gripper, move the ball towards the target while also keeping it trapped in the gripper.
    if check("the robot's gripper is around the soccer ball and the robot's gripper is not above the target location"):
        robot.move_gripper("near the target location")
    # Finally, release the ball at the target location.
    if check("the robot's gripper is around the soccer ball and the robot's gripper is near the target location"):
        robot.move_gripper("above the target location", close_gripper=False)