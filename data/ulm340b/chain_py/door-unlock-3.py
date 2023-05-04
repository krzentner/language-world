
    # Steps:
    #  1. Put the robot's gripper above the door handle
    #  2. Rotate the robot's gripper around the door handle
    # Since the door's handle is vertical, we can rotate it by just putting the
    # robot's gripper above the door handle and rotating it.
    if check("the robot's gripper is not above door handle and the robot's gripper is open"):
        robot.put("gripper above door handle")
    # Once the gripper is vertically aligned with the door handle, just spin it
    # until the door is unlocked.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.spin("around door handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Push door closed
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.push("door closed")

# peg-insert-side-start: grab the peg and insert it into the hole from the side, starting above the hole
def peg_insert_side_start(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
