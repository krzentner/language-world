
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper down against soccer ball
    #  3. Slide soccer ball to goal
    # The robot can slide the soccer ball by trapping it by pushing down on it
    # from above and moving the gripper.
    # If the soccer ball is not below the gripper as seen from above, move the
    # gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball and the robot's gripper is not vertically aligned with the soccer ball"):
        robot.move_gripper("vertically aligned with the soccer ball")
    # If the gripper is lined up with the soccer ball but not near it, move the
    # gripper down to the soccer ball to slide it.
    if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.move_gripper("above the soccer ball", close_gripper=True)
    # If the gripper is near the soccer ball, we've probably trapped the soccer
    # ball and can slide it to the target location.
    # Close the gripper to make sure we keep control of the soccer ball.
    if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
        robot.move_gripper("above the target location")

# hammer-tap: hammer the peg into the hole using repeated tapping motions
def hammer_tap(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Line the peg up with the hole
    #  3. Tap the peg into the hole
    # We can put the gripper above the peg to start off with.
    if check("the robot's gripper is not above the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is lined up with the hole, tap it.
    if check("the peg is not horizontally aligned with hole"):
        robot.move_gripper("above the peg", close_gripper=True)
    # If the peg isn't lined up with the hole from above, we'll probably have to
  