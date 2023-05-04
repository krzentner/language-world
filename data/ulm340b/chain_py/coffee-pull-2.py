
    # Steps:
    #  1. Put gripper near the front of the handle
    #  2. Move gripper near the back of the handle
    #  3. Grab handle by closing the gripper
    #  4. Move the mug towards the goal
    # First, put the gripper roughly near the front of the handle, so that we
    # don't bump it while trying to grab it.
    if check("the robot's gripper is not near handle"):
        robot.put("gripper near the handle")
    # Next, move the robot's gripper towards the back of the handle to line up
    # to grab it.
    # If the gripper is not lined up with the handle, move it closer.
    # Otherwise, continue to the next step.
    if check("the robot's gripper is not near handle"):
        robot.grab("the handle")
    # If the gripper is around the handle, we can pull it towards the goal.
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("handle towards goal")

# coffee-push: grab the mug and push it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper near the back of the handle
    #  2. Move gripper near the front of the handle
    #  3. Grab handle by closing the gripper
    #  4. Move the mug towards the goal
    # First, put the gripper roughly near the back of the handle, so that we
    # don't bump it while trying to grab it.
    if check("the robot's gripper is not near handle"):
        robot.put("gripper near handle")
    # Next, move the robot's gripper towards the front of the handle to line up
    # to grab it.
    # If the gripper is not lined up with the handle, move it closer.
    # Otherwise, continue to the next step.
    if check("the robot's gripper is not near handle"):
        robot.grab("the handle")
    # If the gripper is around the handle, we can push it towards the goal.
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("handle towards