# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos
    #  4. Use the stick to pull the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the gripper is above the stick, grab it.
    if check("the robot's gripper is vertically aligned with the stick and the gripper is not around the stick"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the robot's gripper is around the stick, line up the stick with the thermos.
    if check("the robot's gripper is around the stick and the stick is not horizontally aligned with the thermos"):
        robot.move_gripper("horizontally aligned with the thermos")
    # If the stick is lined up with the thermos, pull the thermos to the target location.
    if check("the robot's gripper is horizontally aligned with the thermos and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")