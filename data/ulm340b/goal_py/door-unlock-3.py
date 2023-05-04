
    # Steps:
    #  1. Put gripper right of door knob
    #  2. Twist gripper to open door
    #  3. Push door closed
    # First, line up the gripper right of the door knob
    if check("the robot's gripper is not right of door knob"):
        robot.move_gripper("right of the door knob")
    # Now that the gripper is lined up, twist it on the door knob to open
    # the door
    if check("the robot's gripper is right of door knob"):
        robot.move_gripper("left of the door knob")

# peg-insert-vertical: grab the peg and insert it into the hole from the top
def peg_insert_vertical(robot):
    # Steps:
    #  1. Line up the gripper as seen from above
    #  2. Move gripper down towards the top of the peg
    #  3. Grab the peg with the gripper
    #  4. Line the peg up with the hole
    #  5. Drop the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not almost vertically aligned with the peg"):
        robot.move_gripper("almost vertically aligned with the peg", close_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    if check("peg is left of the robot's gripper and peg is not vertically aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # As long the gripper is still lined up with the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("peg is vertically aligned with hole"):
        robot.move_gripper("almost vertically aligned with the peg", close_gripper=True)
    # If the peg is lined up with the hole above the peg, drop it.
    if check("the robot's gripper is forward aligned with the peg and the peg is not almost horizontally aligned with hole"):
        robot.move_gripper("above the peg")

# door-close: push the door closed
def door_close(robot):