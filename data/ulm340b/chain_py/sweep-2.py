
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube at goal")

# push-sweep: slide the cube to the target location
def push_sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Push gripper into side of cube
    #  3. Slide cube to goal
    # The robot can slide the cube by pushing down on it from above and moving
    # the gripper.
    # If the gripper isn't above the cube as seen from above, move the gripper
    # above the cube.
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with cube"):
        robot.put("the gripper above cube")
    # If the gripper is aligned with the cube but not near it, move the gripper
    # down to the cube to slide it.
    if check("the robot's gripper is vertically aligned with cube and the robot'