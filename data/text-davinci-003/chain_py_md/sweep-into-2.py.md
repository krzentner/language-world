

The `sweep-into` task requires the robot to grab a cube and move it to a target location.

# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put the gripper above the cube
    #  2. Drop the gripper around the sides of the cube
    #  3. Close the gripper around the cube
    #  4. Move the cube to the goal
    # 
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper is above the cube, but not near it, move the gripper down
    # around the sides of the cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not near the cube"):
        robot.drop("gripper around sides of cube")
    # If the gripper is near the cube, we can probably grab it by closing the
    # gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, so maybe we grabbed it.
    # Try moving the cube to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube at goal")