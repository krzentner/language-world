# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put the gripper close to the puck
    #  2. Move the puck to the goal location
    # For pushing, we don't need to grab the puck. We can simply place the gripper close to the puck.
    if check("the robot's gripper is not near the puck"):
        robot.place("gripper near puck")
    # Once the gripper is near the puck, move the puck to the goal.
    if check("the robot's gripper is near the puck"):
        robot.slide("puck to goal")