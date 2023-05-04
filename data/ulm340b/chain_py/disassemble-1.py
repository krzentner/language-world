
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Grab the wrench
    #  3. Slide wrench left to get it off the peg
    # First put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    # If the wrench is still below the gripper, drop the gripper around it.
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is open"):
        robot.put("gripper around wrench")
    # If the gripper is around the wrench, pull the wrench to the left to get it
    # off of the peg.
    if check("the robot's gripper is around wrench"):
        robot.slide("wrench to the left")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Grab the door handle
    #  3. Push the door closed
    # First put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # If the door handle is still below the gripper, move the gripper down to
    # grab it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # If the gripper is around the door handle, push the door handle towards the
    # door.
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# latch-close: press the latch down from above to close it
def latch_close(robot):
    # Steps:
    #  1. Put gripper above latch
    #  2. Push gripper into top of latch
    # First, put the gripper above the latch.
    if check("the robot's gripper is not vertically aligned with latch"):
        robot.put("gripper above latch")
    # If the latch is still below the gripper, move the gripper down to push
