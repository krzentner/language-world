# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Position the gripper above the stick
    #  2. Grab the stick
    #  3. Position the stick above the thermos, touching it
    #  4. Push the thermos to the target location using the stick
    # First, position the gripper above the stick
    if check("the gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Once the gripper is lined up with the stick, grab the stick
    if check("the gripper is vertically aligned with the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Once the stick is grabbed, position it above the thermos, touching it
    if check("the stick is not above the thermos"):
        robot.move_gripper("above the thermos")
    # Once the stick is above the thermos, push the thermos to the target location
    if check("the stick is above the thermos"):
        robot.move_gripper("above the target location")