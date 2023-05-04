
    # Steps:
    #  1. Put gripper above door knob
    #  2. Drop gripper around door knob
    #  3. Pull the door open
    # We need to put the gripper above the door knob before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door knob"):
        robot.put("gripper above door knob")
    # Once the gripper is lined up above the door knob, we should be able to grab
    # the door knob by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door knob and the robot's gripper is not around door knob"):
        robot.put("gripper around door knob")
    # Once the gripper is around the door knob, we can just pull the door open.
    if check("the robot's gripper is around door knob"):
        robot.pull("door open")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around door knob
    #  2. Push the door closed
    # If the gripper is not near the door knob, move it to the door knob.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near door knob"):
        robot.grab("door knob")
    # If the door is aligned with the gripper as seen from in front, we can push
    # the door closed.
    if check("the robot's gripper is forward aligned with door knob"):
        robot.push("door closed")

# peg-unstack: grab the top peg and move it to the table
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the top peg
    #  2. Grab top peg with the gripper
    #  3. Line the top peg up with the table
    #  4. Move the top peg to the table
    # First, put the gripper above the top peg.
    if check("the robot's gripper is not vertically aligned