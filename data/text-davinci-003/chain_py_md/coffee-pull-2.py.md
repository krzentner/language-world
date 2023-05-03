

# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Grab the handle with the gripper
    #  3. Pull the mug to the goal 
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # If the mug handle is now left of the gripper as viewed from the front, go
    # ahead and grab it.
    # If it is not yet close enough, move the gripper to the mug handle.
    if check("the mug handle is not left of the robot's gripper and the robot's gripper is not near the mug handle"):
        robot.move("gripper to the mug handle")
    # Once the gripper is near the mug handle and the mug is below the gripper,
    # grab the mug.
    if check("the robot's gripper is near the mug handle and the mug is below the robot's gripper"):
        robot.grab("mug handle")
    # Now that the mug is grabbed, pull it to the goal.
    if check("the robot's gripper is above the mug handle and the mug is below the robot's gripper"):
        robot.pull("mug to goal")