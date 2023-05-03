# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.put("gripper above mug")
    # Once the gripper is aligned with the mug from above, grab the mug.
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around the mug"):
        robot.grab("mug")
    # Once the mug is grabbed, move it to the target location.
    if check("the robot's gripper is around the mug"):
        robot.slide("mug to goal")