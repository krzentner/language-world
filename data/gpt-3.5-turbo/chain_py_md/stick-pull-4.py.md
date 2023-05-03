# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper near the stick
    #  2. Grab the stick
    #  3. Move the stick towards the thermos
    #  4. Slide the stick under the thermos
    #  5. Pull the stick towards the target location
    # First, put the gripper near the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move("gripper to stick")
    # Then, grab the stick.
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.grab("stick")
    # Once the stick is grabbed, move it towards the thermos.
    if check("the robot's gripper is around the stick and the stick is not near the thermos"):
        robot.move("stick to thermos")
    # Once the stick is near the thermos, slide it under.
    if check("the stick is near the thermos and the thermos is not on the stick"):
        robot.slide("stick under thermos")
    # Once the stick is under the thermos, pull it towards the target location.
    if check("the thermos is on the stick and the stick is not at the target location"):
        robot.pull("stick towards target location")