
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("forward aligned with door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is in front of door handle"):
        robot.move_gripper("left of the door handle")

# slide-back: slide the object back
def slide_back(robot):
    # Steps:
    #  1. Push the object to the left with the gripper
    # Slide the object back by just pushing it with the gripper.
    # Since we don't have to worry about grabbing anything, we can just move
    # the gripper where we want the object to end up and close the gripper to
    # push the object there.
    if check("the robot's gripper is not forward aligned with the object"):
        robot.move_gripper("forward aligned with the object")
    # If the robot's gripper is in front of the object, we should slide the
    # object left.
    if check("the robot's gripper is in front of the object"):
        robot.move_gripper("vertically aligned with the object", close_gripper=True)

# slide-back-v2: slide the object back
def slide_back_v2(robot):
    # Steps:
    #  1. Push the object to the left with the gripper
    # Slide the object back by just pushing it with the gripper.
    # Since we don't have to worry about grabbing anything, we can just move
    # the gripper where we want the object to end up and close the gripper to
    # push the object there.
    if check("the robot's gripper is not vertically aligned with the object"):
        robot.move_gripper("vertically aligned with the object")
    # If the