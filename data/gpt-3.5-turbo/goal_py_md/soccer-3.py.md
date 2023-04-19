# soccer: push the soccer ball into the target location
# def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into side of soccer ball
    #  3. Turn gripper to face target location
    #  4. Slide soccer ball to goal
    # The robot can slide the soccer ball by trapping it by pushing into its side
    # from above and moving the gripper.
    
    # If the soccer ball isn't below the gripper as seen from above, move the
    # gripper above the ball.
    if check("the robot's gripper is not above soccer ball"):
        robot.move_gripper("above the soccer ball")

    # If the gripper is above the soccer ball but not near it, move the gripper
    # down to the ball to slide it.
    if check("the robot's gripper is above soccer ball and the robot's gripper is not near soccer ball"):
        robot.move_gripper("near the soccer ball", close_gripper=True)

    # If the gripper is near the soccer ball and the soccer ball is trapped between
    # gripper, turn the gripper to face the target location.
    # We can randomly decide the direction to face.
    if check("the robot's gripper is near soccer ball and the soccer ball is not between gripper"):
        if random.choice([True, False]):
            robot.move_gripper("around the soccer ball", theta=90)
        else:
            robot.move_gripper("around the soccer ball", theta=-90)

    # Once the gripper is facing the target location, we can slide the soccer ball
    # to the goal.
    # Close the gripper to make sure we keep control of the soccer ball.
    if check("the robot's gripper is facing the target location"):
        robot.move_gripper("above the target location")