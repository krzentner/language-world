# hand-insert: pick up the small object and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper above the object
    #  2. Grab the object with the gripper
    #  3. Move the object to the target location
    # First, put the gripper above the object.
    if check("the gripper is not above the object"):
        robot.place("gripper above object")
    # If the gripper is not around the object, put it around the object.
    if check("the gripper is not around object and the gripper is open"):
        robot.drop("gripper around object")
    # If the gripper is near the object and open, maybe we can grab it by closing
    # the gripper.
    if check("the gripper is near object and the gripper is open"):
        robot.close("gripper around object")
    # We closed the gripper, and the object is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the object to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the gripper is above object and the gripper is closed"):
        robot.place("object at target location")