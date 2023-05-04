
    # Steps:
    #  1. Put gripper above door handle
    #  2. Close gripper around door handle
    #  3. Pull door closed
    # If the door is left of the robot's gripper and not aligned with the door
    # handle from the front, move to gripper above the door handle.
    if check("door is not left of the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the door handle")
    # Now that the gripper is lined up above the door handle, we can try to grab
    # it by closing the gripper.
    if check("the robot's gripper is almost vertically aligned with door handle"):
        robot.move_gripper("in front of the door handle", close_gripper=True)
    # If the gripper is around the door handle and the door is left of the
    # robot, we can pull the door closed.
    if check("the door handle is in front of the robot's gripper"):
        robot.move_gripper("behind the door handle")

# slide-back: slide the puck to the left, back to the target location
def slide_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # Slide back is the same as slide, except the puck starts in front of the
    # target.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make