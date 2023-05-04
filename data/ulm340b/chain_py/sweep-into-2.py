
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move the cube to the goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.place("gripper above cube")
    # If the cube isn't around the gripper, put it there.
    if check("cube is not near the robot's gripper"):
        robot.drop("gripper around cube")
    # If the gripper is around the cube and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube at goal")

# sweep-into-goal: grab the cube and sweep it to the target location
def sweep_into_goal(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Move gripper around the cube
    #  3. Slide the cube to the goal
    # If the cube isn't below the gripper as seen from above, move the gripper
    # above the cube.
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.place("the gripper above the cube")
    # If the gripper is aligned with the cube but not near it, move the gripper
    # down to the cube to slide it.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near cube"):
        robot.move("the gripper around the cube")
    # If the gripper is near the cube, we've probably trapped the