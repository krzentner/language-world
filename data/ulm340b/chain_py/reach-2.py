
    # Steps:
    #  1. Move gripper to goal
    # Just move the gripper to the target location.
    robot.place("gripper at goal")

# scoop: scoop the puck into the box
def scoop(robot):
    # Steps:
    #  1. Put gripper left of the puck
    #  2. Start pushing against the puck to scoop it
    #  3. Push the puck harder
    # First, move the gripper left of the puck.
    if check("the robot's gripper is not left of the puck"):
        robot.place("the gripper left of the puck")
    # If the gripper is right of the puck, we can start scooping it by pushing
    # into the side of the puck.
    if check("the robot's gripper is right of the puck and the robot's gripper is not in front of the puck"):
        robot.push("the puck to the right")
    # If the gripper is forward aligned with the puck, we can really start
    # pushing to move the puck to the target location.
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is right of the puck"):
        robot.slide("the puck to the goal")

# window-close-v2: slide the window closed to the right
def window_close_v2(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be in front of the window handle,
    # push