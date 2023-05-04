
    # Steps:
    #  1. Put gripper around stick
    #  2. Grab stick with gripper
    #  3. Move the stick in front of the thermos
    #  4. Push the thermos to the target location
    # If the robot's gripper isn't around the stick, move it there.
    # Because the gripper is horizontal, we don't have to move it above the stick
    # first.
    if check("the robot's gripper is not around stick"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the gripper is around the stick, pick it up by closing the gripper.
    if check("the robot's gripper is around stick and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the stick")
    # If the robot's gripper has grabbed the stick, line up the gripper with the
    # thermos to push it.
    if check("the robot's gripper is below stick"):
        robot.move_gripper("forward aligned with thermos")

# thermos-pick-place: pick up the thermos and hold it at the target location
def thermos_pick_place(robot):
    # Steps:
    #  1. Put gripper around thermos
    #  2. Grab thermos with gripper
    #  3. Move the thermos to the target location
    # If the robot's gripper isn't around the thermos, move it there.
    # Because the gripper is horizontal, we don't have to move it above the
    # thermos first.
    if check("the robot's gripper is not around thermos"):
        robot.move_gripper("around the thermos", close_gripper=True)
    # If the gripper is around the thermos, pick it up by closing the gripper.
    if check("the robot's gripper is around thermos and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the thermos")
    # If the robot's gripper has grabbed the thermos, move the gripper to the
    # target location to hold it there.
    if check("the robot's gripper is below thermo