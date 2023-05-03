# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper near the end of the lever, above it
    #  2. Grab the lever
    #  3. Rotate the lever upwards
    # Lever is a long and thin object, so we need to make sure the gripper is
    # aligned correctly.
    # We initially put the gripper roughly near the end of the lever.
    if check("the robot's gripper is not near the end of the lever"):
        robot.place("gripper near end of lever")
    # If gripper is not around the lever, put the gripper around it.
    if check("the robot's gripper is not around the lever and the robot's gripper is open"):
        robot.drop("gripper around the lever")
    # If the gripper is around the lever, rotate the lever upwards by moving the
    # gripper up.
    # We don't need to be very precise in the direction when rotating the lever
    # up, because of the shape of the lever.
    if check("the robot's gripper is around the lever and the lever is not rotated upwards"):
        robot.move("gripper up to rotate lever")