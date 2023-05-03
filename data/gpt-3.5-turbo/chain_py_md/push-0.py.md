# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper around puck
    #  2. Slide the puck to the target location
    # First, put the gripper around the puck.
    if check("the robot's gripper is not around the puck"):
        robot.drop("gripper around puck")
    # Once the gripper is around the puck, slide the puck to the target location.
    if check("the robot's gripper is around the puck"):
        robot.slide("puck to goal")