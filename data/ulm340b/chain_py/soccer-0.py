
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Drop gripper around soccer ball
    #  3. Close gripper around soccer ball
    #  4. Move soccer ball to goal
    # If the soccer ball is not below the gripper, line it up with the gripper
    # as seen from above, so that we don't bump it when trying to grab it.
    if check("the robot's gripper is not vertically aligned with soccer ball"):
        robot.put("gripper above soccer ball")
    # If the gripper is lined up above the soccer ball, put the gripper down
    # around it.
    if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    # Once the gripper is lined up with the soccer ball as seen from the front,
    # close the gripper.
    # If we got the ball, we'll move the ball to the goal later.
    # If we didn't get the ball, we'll go back to the earlier steps to keep
    # trying to get it.
    if check("the robot's gripper is forward aligned with soccer ball"):
        robot.close("gripper around soccer ball")
    # If the gripper is around the soccer ball, let's try moving the soccer ball
    # to the goal.
    if check("the robot's gripper is around soccer ball"):
        robot.move("soccer ball to goal")

# pick: pick up the object by moving the gripper down around it
def pick(robot):
    # Steps:
    #  1. Put gripper above object
    #  2. Drop gripper around object
    #  3. Close gripper around object
    #  4. Move object above table
    # If the object is not below the gripper, line it up with the gripper as
    # seen from above, so that we don't bump it when trying to grab it.
    if check("the robot's gripper is not vertically aligned with object"):
        robot.put("gripper above object")
    # If the gripper is lined up above the object, put the gripper down around