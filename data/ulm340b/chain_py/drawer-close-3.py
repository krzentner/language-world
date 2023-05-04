
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Push the drawer closed
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    # Once the gripper is around the drawer handle, we can just push the drawer
    # closed.
    if check("the robot's gripper is around drawer handle"):
        robot.push("toward drawer")

# pick-place-topdown: pick up the object and place it in the target location
def pick_place_topdown(robot):
    # Steps:
    #  1. Put gripper above object
    #  2. Drop gripper around object
    #  3. Close gripper around object
    #  4. Move object to goal
    # First, put the gripper above object, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above object"):
        robot.place("gripper above object")
    # If the gripper isn't around the object, put it around the object.
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    # If the gripper is near the object and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near object and the robot's gripper is open"):
        robot.close("gripper around object")
    # We closed the gripper, and the object is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the object to the goal.
 