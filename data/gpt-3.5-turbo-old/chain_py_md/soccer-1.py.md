# soccer: push the soccer ball into the target location
# def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Push soccer ball to goal
    # First, we need to move the robot's gripper to above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    # If the gripper is not around the soccer ball and open, move the gripper down
    # onto the soccer ball.
    if check("the robot's gripper is above soccer ball and the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    # If the gripper is near the soccer ball and open, maybe we can grab it by
    # closing the gripper.
    if check("the gripper is near soccer ball and the robot's gripper is open"):
        robot.close("gripper around soccer ball")
    # We closed the gripper, and the soccer ball is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the soccer ball toward the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above soccer ball and the robot's gripper is closed"):
        robot.push("the soccer ball to the goal")