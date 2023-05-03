# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Slide soccer ball to goal
    # The robot can slide the soccer ball by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the soccer ball isn't below the gripper as seen from above, move the gripper
    # above the soccer ball.
    if check("the robot's gripper is not above soccer ball and the robot's gripper is not vertically aligned with the soccer ball"):
        robot.put("gripper above soccer ball")
    # If the gripper is aligned with the soccer ball but not near it, move the gripper
    # down to the soccer ball to slide it.
    if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near soccer ball"):
        robot.push("gripper into soccer ball")
    # If the gripper is near the soccer ball, we've probably trapped the soccer ball and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the soccer ball.
    if check("the robot's gripper is near soccer ball and the soccer ball is below the robot's gripper"):
        robot.slide("soccer ball to goal")