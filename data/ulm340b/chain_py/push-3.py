
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Line the puck up with the goal
    #  4. Slide the puck to the goal
    # We need to put the gripper above the puck before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # As long the gripper is still roughly above the puck, move it down.
    if check("the robot's gripper is above the puck"):
        robot.place("gripper around puck")
    # If the gripper is now below the puck, we should be able to grab it by
    # closing the gripper.
    if check("the robot's gripper is below the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # If the gripper is roughly around the puck, we can line it up towards the
    # target by moving the gripper towards the target.
    if check("the robot's gripper is roughly aligned with puck"):
        robot.slide("puck towards target")
    # Now that the puck is aligned towards the target, we can slide it there.
    if check("the robot's gripper is aligned with puck"):
        robot.slide("puck to target")

# lift: lift the puck up to the target height
def lift(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Lift the puck above a target height
    # We need to put the gripper above the puck before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # As long the gripper is still roughly above the puck, move it down.
    if check("the robot's gripper is above the puck"):
        robot.place("gripper around puck")
    # If the gripper is now below the puck, we should be able to grab it by
    #