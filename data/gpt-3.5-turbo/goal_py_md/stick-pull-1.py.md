# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos handle
    #  4. Slide the stick through the thermos handle
    #  5. Drag the thermos to the target location
    # First, put the gripper roughly above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Once the gripper is around the stick, line up the stick with the thermos
    # handle.
    if check("the robot's gripper is around the stick and the thermos handle is not aligned with the stick"):
        robot.move_gripper("forward aligned with the thermos handle")
    # Once the stick is lined up with the thermos handle, slide the stick
    # through the thermos handle.
    if check("the robot's gripper is forward aligned with the thermos handle and the stick is not through the thermos handle"):
        robot.move_gripper("around the thermos handle")
    # Once the stick is through the thermos handle, drag the thermos to the
    # target location.
    if check("the robot's gripper is around the thermos handle"):
        robot.move_gripper("near the target location")