
    # Steps:
    #  1. Put gripper vertically above the button
    #  2. Drop gripper down to push the button
    # If the gripper is not lined up with the button as seen from the side, move
    # it to be.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is lined up with the button, drop it down to push the
    # button.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("above the button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the the door handle is right of the robot's gripper, we should move the
    # gripper near the door handle to start pushing
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("right of the door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # door close now by moving the gripper right.
    if check("the door handle is right of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")
    # If the robot's gripper is starting to be in front of the door handle, push
    # harder.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with the door handle")

# pick-orient: pick up the peg, point it towards the hole and insert it
def pick_orient(robot):
    # Steps:
    #  1. Put gripper around the peg
    #  2. Close gripper to grip the peg
    #  3. Move the peg towards the goal
    #  4. Rotate the peg to point at the hole
    #  5. Move the peg into the hole
    # Pick up