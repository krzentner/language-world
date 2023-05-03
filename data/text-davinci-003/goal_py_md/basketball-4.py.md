

Solutions:

# basketball: put the ball into into the hoop
def basketball(robot):
  # Steps: 
  #  1. Put the gripper directly below the ball
  #  2. Push the ball with the gripper towards the hoop
  #  3. Move the ball closer to the hoop
  #  4. Release the ball
  # First, put the gripper directly below the ball so that it can catch it.
  if check("the robot's gripper is not above the ball"):
      robot.move_gripper("below the ball")
  # Once the gripper is above the ball, drop it around the ball and close the
  # gripper.
  if check("the robot's gripper is not around the ball and the robot's gripper is open"):
      robot.move_gripper("near the ball", close_gripper=True)
  # Now that the gripper has the ball, we can move the ball closer to the hoop.
  if check("the robot's gripper is around the ball"):
      robot.move_gripper("tilted towards the hoop")
  # If the ball is close to the hoop, we can release it.
  if check("the ball is close to the hoop"):
      robot.move_gripper("left of the hoop", open_gripper=True)