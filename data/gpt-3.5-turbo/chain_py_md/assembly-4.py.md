# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    # 1. Put gripper above wrench
    # 2. Drop gripper around wrench
    # 3. Close gripper around wrench
    # 4. Put gripper above peg
    # 5. Move gripper down and around peg
    # 6. Slide wrench onto peg
    # First, put the gripper roughly above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If the gripper is near the wrench and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    # We closed the gripper, and the wrench is still near the gripper, so maybe we
    # grabbed it.
    # Now put the gripper roughly above the peg.
    if check("the robot's gripper is above wrench and the robot's gripper is closed and the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    # Move the gripper down and around the peg.
    if check("the robot's gripper is above peg and the robot's gripper is closed and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    # Slide the wrench onto the peg.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.slide("wrench onto peg")