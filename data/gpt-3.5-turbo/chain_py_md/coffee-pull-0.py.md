# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper around the handle
    #  2. Raise the gripper to lift the mug
    #  3. Move the gripper to the target location
    #  4. Lower the gripper to place the mug
    # If the gripper is not around the mug handle, move it there.
    if check("the robot's gripper is not around the mug handle"):
        robot.grab("mug handle")
    # If the gripper is closed around the handle, raise the mug
    if check("the robot's gripper is closed around the mug handle"):
        robot.move("gripper up")
    # If the mug is lifted, move the gripper to the target location
    if check("the mug is lifted"):
        robot.slide("mug to goal")
    # If the mug is at the target location, lower the gripper to place it
    if check("the mug is at the goal location"):
        robot.move("gripper down")