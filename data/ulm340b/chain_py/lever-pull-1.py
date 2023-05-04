
    # Steps:
    #  1. Move gripper close to lever and around lever
    #  2. Close gripper around lever
    #  3. Pull the lever up
    # The easiest way to grab the lever is just to move the gripper close to it,
    # as the gripper will probably end up around it.
    if check("the robot's gripper is not around lever and the robot's gripper is not near lever"):
        robot.grab("lever")
    # Once the gripper is around the lever, we can close it to get a good grasp
    # of the lever.
    if check("the robot's gripper is around lever"):
        robot.close("gripper around lever")
    # Once the gripper is closed, the robot should be able to just pull the
    # lever up without thinking about it.
    if check("the robot's gripper is closed and the robot's gripper is around lever"):
        robot.pull("lever up")

# slide: slide puck towards goal
def slide(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck by pushing gripper into puck
    #  3. Slide the puck to the target location
    # First, put the gripper above puck, so that we don't bump it while trying to
    # grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is above puck"):
        robot.push("puck with gripper")
    # If the gripper is near the puck, we've probably grabbed it and can slide
    # it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck"):
        robot.slide("the puck to the goal")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
 