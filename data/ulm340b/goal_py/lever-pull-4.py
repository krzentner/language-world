
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Pull the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not above lever"):
        robot.move_gripper("above lever")
    # If the gripper is above lever, and the lever is left of the robot's
    # gripper, maybe we can grab the lever by moving the gripper around the
    # lever.
    if check("the robot's gripper is vertically aligned with lever and lever is left of the robot's gripper"):
        robot.move_gripper("forward aligned with lever", close_gripper=True)
    # As long the gripper is still mostly around the lever, pull the lever up
    # with the gripper.
    if check("the robot's gripper is forward aligned with lever"):
        robot.move_gripper("above lever", close_gripper=False)

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("around door handle")

# push-slide: slide the puck to the target location
def push_slide(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If