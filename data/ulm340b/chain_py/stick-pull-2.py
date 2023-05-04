
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the stick to pull the thermos to the goal
    # First, line up the robot's gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the gripper is roughly above the stick, put the gripper down around
    # the stick.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not near stick and the robot's gripper is open"):
        robot.grab("stick")
    # Now that we've grabbed the stick, we can move the thermos by moving the
    # stick.
    # Because we're using the stick as a handle, move the gripper so the stick
    # is aligned with the gripper from the front.
    if check("the robot's gripper is near stick and the robot's gripper is vertically aligned with stick"):
        robot.align("stick to pull thermos to goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the stick to push the thermos to the goal
    # First, line up the robot's gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the gripper is roughly above the stick, put the gripper down around
    # the stick.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not near stick and the robot's gripper is open"):
        robot.grab("stick")
    # Now that we've grabbed the stick, we can move the thermos by moving the
    # stick.
    # Because we're using the stick as a handle, move the gripper so the stick
    # is aligned with the gripper from the front.
    if check("the robot's gripper is