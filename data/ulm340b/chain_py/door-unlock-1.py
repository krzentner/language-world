
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the dial forward
    #  3. Line up the gripper as viewed from above
    #  4. Push the dial right
    #  5. Line up the gripper as viewed from above
    #  6. Pull the dial left
    # If the robot's gripper is not aligned with the dial, move it to above the
    # dial.
    if check("the robot's gripper is not vertically aligned with door dial"):
        robot.move("gripper above door dial")
    # If the gripper is above the dial and left of it, we should be able to push
    # the dial forward.
    if check("the robot's gripper is vertically aligned with door dial and the robot's gripper is left of door dial"):
        robot.push("door dial forward")
    # If the dial is roughly right of the gripper, try to move the gripper above
    # it.
    if check("the robot's gripper is vertically aligned with door dial and the robot's gripper is right of door dial"):
        robot.align("gripper above door dial")
    # If the robot's gripper is above the dial and left of it, we should be able
    # to push the dial right.
    if check("the robot's gripper is vertically aligned with door dial and the robot's gripper is left of door dial"):
        robot.push("door dial right")
    # If the dial is roughly left of the gripper, try to move the gripper above
    # it.
    if check("the robot's gripper is vertically aligned with door dial and the robot's gripper is left of door dial"):
        robot.align("gripper above door dial")
    # If the robot's gripper is above the dial and right of it, we should be
    # able to pull the dial left.
    if check("the robot's gripper is vertically aligned with door dial and the robot's gripper is right of door dial"):
        robot.pull("door dial left")

# drawer-close-topdown: push the drawer closed from above
def drawer_close_topdown(robot):
    # Steps:
    #  1. Put gripper above the drawer handle
