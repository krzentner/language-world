

The robot should grab the small object and move it up, line it up with the target location and then insert it into the target.

# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above object
    #  2. Drop gripper around object
    #  3. Close gripper around object
    #  4. Move object to target location
    #  5. Line up object with target location
    #  6. Insert object into target location
    # First, put the gripper roughly above the object, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the object"):
        robot.put("gripper above object")
    # If the gripper isn't around the object, put it around the object.
    if check("the robot's gripper is not around the object and the robot's gripper is open"):
        robot.drop("gripper around object")
    # If the gripper is near the object and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the object and the robot's gripper is open"):
        robot.close("gripper around object")
    # We closed the gripper, and the object is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the object to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        robot.move("object to target location")
        # Once the object is roughly aligned with the target location, we need to
        # line up the object before we can insert it into the target.
        if check("robot's gripper is near target location and the object is not horizontally aligned with target location"):
            robot.align("object to target location")
        # If the object is lined up with the target, we can insert the object
        # into the target.
        if check("robot's gripper is near target location and the object is horizontally aligned with target location"):
            robot.insert("object into target location")