# hand-insert: pick up the puck and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper around the object to hold it
    #  2. Lift the object
    #  3. Move the object to the target location
    #  4. Release the object at the target location
    # We start by putting the gripper around the object.
    if check("the robot's gripper is not around the object and the robot's gripper is open"):
        robot.drop("gripper around object")
    # If the gripper is around the object and the object is lifted, we can move
    # it to the target location.
    if check("the robot's gripper is around the object and the object is lifted and the robot is not near the target location"):
        robot.move("to the target location")
    # If the robot is near the target location and the object is still lifted in
    # the gripper, we release the object at the target location.
    if check("the robot is near the target location and the object is lifted in the gripper"):
        robot.release("the object at the target location")