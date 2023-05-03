

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper just left of the stick
    #  2. Drop gripper around the stick
    #  3. Close gripper around stick
    #  4. Pull thermos toward the target location
    # First, put the gripper just left of the stick.
    if check("the robot's gripper is not left of the stick"):
        robot.move_gripper("left of the stick")
    # As long as the stick is not at the bottom of the gripper, move the gripper
    # around the stick.
    if check("the robot's gripper is not around stick"):
        robot.move_gripper("around the stick")
    # If the stick is at the bottom of the gripper, close the gripper to pick up
    # the stick.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("ahead of the thermos", close_gripper=True)
    # If the gripper is holding the stick, pull the thermos toward the target
    # location.
    if check("the robot's gripper is around the stick and the robot's gripper is closed"):
        robot.move_gripper("near the target location with the stick")