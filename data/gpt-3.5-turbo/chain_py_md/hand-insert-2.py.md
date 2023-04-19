# hand-insert: pick up the object and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper above object
    #  2. Drop gripper around object
    #  3. Close gripper around object
    #  4. Move object to goal
    # First, put the gripper roughly above the object so we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    # If the gripper isn't around the object, put it around the object.
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    # If the gripper is near the object and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near object and the robot's gripper is open"):
        robot.close("gripper around object")
    # We closed the gripper, and the object is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the object to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        robot.place("object at goal")