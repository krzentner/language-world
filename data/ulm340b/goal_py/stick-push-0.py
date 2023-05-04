
    # Steps:
    #  1. Put gripper above the stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Line stick up with thermos
    #  5. Push the thermos to the target location
    # First, put the gripper roughly above the stick, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick")
    # Once we have the stick, make sure we line it up to push the thermos to the
    # target location.
    if check("the robot's gripper is forward aligned with the stick"):
        robot.move_gripper("above the thermos")

# rope-pull: grab the rope and pull the thermos to the target location
def rope_pull(robot):
    # Steps:
    #  1. Put gripper above the rope
    #  2. Drop gripper around rope
    #  3. Close gripper around rope
    #  4. Pull thermos to target location
    # First, put the gripper roughly above the rope, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not vertically aligned with rope"):
        robot.move_gripper("above the rope")
    # If the gripper isn't around the rope, put it around the rope.
    if check("the robot's gripper is not around rope and the robot's gripper is open"):
        robot.move_gripper("near the rope", close_gripper=True)
    # Once we have the rope, make sure we line it up to pull the thermos to the
    # target location.
    if check("the robot's gripper is forward aligned with the rope"):
        robot.move_gripper("horizontally aligned with the thermos", open_gripper=True)
[eod]