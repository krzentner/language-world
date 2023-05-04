
    # Steps:
    #  1. Move gripper next to the lever handle
    #  2. Grab the lever handle
    #  3. Pull the lever up
    # If the gripper is not near the lever, move it near the lever.
    if check("the robot's gripper is not near the lever handle"):
        robot.grab("lever handle")
    # As long as the gripper is lined up with the lever handle from in front,
    # move it down to grab the lever handle.
    if check("the robot's gripper is forward aligned with lever handle and the robot's gripper is not around lever handle"):
        robot.put("gripper around lever handle")
    # If the gripper is around the lever handle, pull it up to rotate the lever.
    if check("the robot's gripper is around lever handle"):
        robot.pull("lever up")

# peg-unstack: slide the upper peg off the lower peg
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper near upper peg
    #  2. Move gripper below upper peg
    #  3. Close gripper on upper peg
    #  4. Move upper peg to the goal
    # If the upper peg isn't near the gripper, move the gripper near the upper
    # peg.
    if check("the robot's gripper is not near upper peg"):
        robot.move("gripper to upper peg")
    # If the gripper is near the upper peg but not below it, slide the gripper
    # below the upper peg.
    if check("the robot's gripper is near upper peg and the robot's gripper is above upper peg"):
        robot.move("gripper below upper peg")
    # If the gripper is below the upper peg, move the gripper around the peg
    # and close it to lift the peg.
    if check("the robot's gripper is below upper peg"):
        robot.close("gripper around upper peg")
    # If the gripper is around the upper peg, it's probably lifted, so move the
    # peg to the goal.
    if check("the robot's gripper is around upper peg"):
        robot.move("upper peg to goal")

# dial-turn-