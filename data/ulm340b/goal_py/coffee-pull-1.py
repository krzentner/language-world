
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Pull mug to target location
    # First, put the gripper roughly above mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near mug", close_gripper=True)
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# coffee-push: push the mug to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper left of mug
    #  2. Push against mug
    #  3. Push mug to target location
    # If the robot's gripper is not left of the mug, move it left of the mug.
    if check("the robot's gripper is not left of mug"):
        robot.move_gripper("left of mug")
    # The mug is large enough that once we're pushing on it we should just push
    # harder if possible.
    if check("the robot's gripper is left of mug and the robot's gripper is not forward aligned with mug"):
        robot.move_gripper("near mug")

# door-pull: pull the door open
def door_pull(robot):
    # Steps:
    #  1. Put gripper near door handle
    #  2. Grab door handle with gripper
    #  3. Pull open door
    # Put the gripper near the door handle
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle", close_gripper=True)
  