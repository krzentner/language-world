

Then,

# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Slide soccer ball to goal 
    # First, the robot needs to put the gripper above the soccer ball.
    if check("the robot's gripper is not above soccer ball and the robot's gripper is not vertically aligned with soccer ball"):
        robot.put("gripper above soccer ball")
    # If the gripper is lined up with the soccer ball, but not near it, move the
    # gripper to the soccer ball.
    if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not near soccer ball"):
        robot.push("gripper into soccer ball")
   # When the gripper is near the soccer ball, the robot should be able to slide
    # the soccer ball to the target location.
    if check("the robot's gripper is near soccer ball and the soccer ball is below the robot's gripper"):
        robot.slide("soccer ball to goal")