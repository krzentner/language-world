

# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the handle of the mug
    #  2. Drop gripper around the handle of the mug 
    #  3. Close gripper around the handle of the mug
    #  4. Move the mug to the target location
    # First, put the gripper above the handle of the mug.
    if check("the robot's gripper is not above the handle of the mug"):
        robot.put("gripper above the handle of the mug")
    # If the gripper isn't around the handle of the mug, put it around the handle.
    if check("the robot's gripper is not around the handle of the mug and the robot's gripper is open"):
        robot.drop("gripper around the handle of the mug")
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the handle of the mug and the robot's gripper is open"):
        robot.close("gripper around the handle of the mug")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the mug to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above the handle of the mug and the robot's gripper is closed"):
        robot.slide("mug to target")