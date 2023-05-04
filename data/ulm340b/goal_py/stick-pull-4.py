
    # Steps:
    #  1. Put gripper above stick handle
    #  2. Put gripper above the stick
    #  3. Drop gripper down around the stick
    #  4. Put gripper in front of the thermos
    #  5. Pull the stick and the thermos to the target location
    # First, we need to put the gripper above the stick handle.
    if check("the robot's gripper is not vertically aligned with the stick handle"):
        robot.move_gripper("vertically aligned with the stick handle")
    # If the stick handle is vertically aligned with the gripper, we should move
    # the gripper down above the stick.
    if check("the robot's gripper is above the stick handle and the robot's gripper is not above the stick"):
        robot.move_gripper("in front of the stick", close_gripper=True)
    # Once the gripper is above the stick, we can put it around the stick.
    if check("the robot's gripper is above the stick"):
        robot.move_gripper("around the stick")
    # If the gripper is around the stick, we can move the stick in front of the
    # thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("in front of the thermos")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above stick handle
    #  2. Put gripper above the stick
    #  3. Drop gripper down around the stick
    #  4. Put gripper behind the thermos
    #  5. Push the stick and the thermos to the target location
    # First, we need to put the gripper above the stick handle.
    if check("the robot's gripper is not vertically aligned with the stick handle"):
        robot.move_gripper("vertically aligned with the stick handle")
    # If the stick handle is vertically aligned with the gripper, we should move
    # the gripper down above the stick.
    if check("the robot's gripper is above the stick handle and the robot's gripper is not above the stick"):