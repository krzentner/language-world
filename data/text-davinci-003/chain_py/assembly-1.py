
    # Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench
    #  3. Pull wrench to peg
    #  4. Wrap wrench around peg
    # First, put the gripper roughly above the wrench so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above wrench"):
        robot.move("gripper above wrench")
    # If the gripper isn't around the wrench, drop it around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If the gripper is near the wrench, try to grab it by closing the gripper.
    if check("the robot's gripper is near wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    # We closed the gripper, and the wrench is still near the gripper, so maybe
    # we grabbed it.
    # Try to pull the wrench to the peg.
    if check("the robot's gripper is forward aligned with wrench and the robot's gripper is closed"):
        robot.pull("wrench to peg")
    # If the wrench is near the peg, we can wrap it around the peg.
    if check("the wrench is near peg"):
        robot.rotate("wrench around peg")

# fan-on: rotate the fan so it's on
def fan_on(robot):
    # Steps:
    #  1. Put gripper above fan handle
    #  2. Drop gripper around fan handle
    #  3. Rotate fan handle to turn fan on
    # First, put the gripper above the fan handle.
    if check("the robot's gripper is not above fan handle"):
        robot.put("gripper above fan handle")
    # As long as the gripper is still above the fan handle, try to grab the
    # handle.
    # We don't need to be precise for grabbing, since the handle is big.
    if check("the robot's gripper is above fan handle and the robot's gripper is open"):
        robot.drop("gripper around fan handle")
    # If the gripper is around the fan handle, try to rotate it
    if check("the robot's gripper is around fan handle"):
        robot.rotate("fan handle on")