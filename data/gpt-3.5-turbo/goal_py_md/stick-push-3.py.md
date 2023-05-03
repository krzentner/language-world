# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos
    #  4. Move the stick towards the thermos until it touches it
    #  5. Push the thermos to the target location with the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Once we have the stick, position it close to the thermos.
    if check("the robot's gripper is not near the thermos"):
        robot.move_gripper("near the thermos")
    # If the stick is not lined up with the thermos, move the gripper to line up
    # the stick.
    if check("the robot's gripper is not aligned with the thermos"):
        robot.move_gripper("aligned with the thermos")
    # If the stick is lined up with the thermos, move it towards the thermos
    # until it touches.
    if check("the robot's gripper is aligned with the thermos and the stick is not touching the thermos"):
        robot.move_gripper("touching the thermos")
    # Once the stick is touching the thermos, use it to push the thermos towards
    # the target location.
    if check("the stick is touching the thermos and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")